#!/usr/bin/env python3
"""Publish and maintain the project's RPM repositories."""

from __future__ import annotations

import argparse
import bz2
import csv
import filecmp
import fnmatch
import gzip
import hashlib
import html
import json
import logging
import lzma
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import xml.etree.ElementTree as ET
from collections import defaultdict
from collections.abc import Callable, Iterable, Mapping, Sequence
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from pathlib import Path
from threading import Lock
from types import MappingProxyType
from typing import TypeAlias, TypeVar
from urllib.parse import unquote, urlparse

LOGGER = logging.getLogger("publish-repo")
PathArgument: TypeAlias = str | os.PathLike[str]
Row: TypeAlias = tuple[str, ...]
Input = TypeVar("Input")
Output = TypeVar("Output")
PACKAGE_KINDS = ("packages", "debuginfo")
DEBUG_PACKAGE_SUFFIXES = ("-debuginfo", "-debugsource")
MAX_REMOTE_ATTEMPTS = 5
LOCAL_COMMAND_TIMEOUT = 30 * 60
REMOTE_COMMAND_TIMEOUT = 5 * 60
PACKAGE_SNAPSHOT = Path("packages-before.tsv")
RELEASE_METADATA_CACHE = Path("incoming/release-metadata.json")
RPM_NAMESPACE = "http://linux.duke.edu/metadata/rpm"
DEFAULT_EXCLUDED_SOURCES = (
    "python-ytmusicapi",
    "ktextaddons",
    "kirigami-app-components",
)
SAFE_COMPONENT = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")
SAFE_GITHUB_REPOSITORY = re.compile(
    r"^[A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?/[A-Za-z0-9._-]+$"
)


class PublishError(RuntimeError):
    """An expected publishing failure with a user-facing message."""


@dataclass(frozen=True, slots=True)
class RetentionPolicy:
    max_age: timedelta
    default_versions: int
    source_version_overrides: Mapping[str, int]
    always_keep_newest: bool


@dataclass(frozen=True, slots=True)
class RepositoryProfile:
    name: str
    display_name: str
    source_branch: str
    retention: RetentionPolicy
    dependency_repositories: tuple[str, ...] = ()
    default_excluded_sources: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class ReleaseMetadata:
    body: str
    assets: tuple[dict[str, object], ...]


DEFAULT_RETENTION_POLICY = RetentionPolicy(
    max_age=timedelta(days=7),
    default_versions=3,
    source_version_overrides=MappingProxyType(
        {
            "kwin": 5,
            "plasma-desktop": 5,
            "plasma-workspace": 5,
            "plasma-workspace-wallpapers": 1,
        }
    ),
    always_keep_newest=True,
)
REPOSITORY_PROFILES: dict[str, RepositoryProfile] = {
    name: RepositoryProfile(
        name=name,
        display_name=name.title(),
        source_branch=name,
        retention=DEFAULT_RETENTION_POLICY,
        default_excluded_sources=DEFAULT_EXCLUDED_SOURCES,
    )
    for name in ("beta", "unstable")
}
REPOSITORY_PROFILES["gear"] = RepositoryProfile(
    name="gear",
    display_name="KDE Gear",
    source_branch="unstable",
    retention=DEFAULT_RETENTION_POLICY,
    dependency_repositories=("unstable",),
)

_release_metadata: dict[str, ReleaseMetadata] = {}
_release_metadata_repository: str | None = None
_release_metadata_lock = Lock()


def repository_profile(name: str) -> RepositoryProfile:
    try:
        return REPOSITORY_PROFILES[name]
    except KeyError as error:
        supported = ", ".join(sorted(REPOSITORY_PROFILES))
        raise PublishError(
            f"Unknown repository profile {name!r}; expected one of: {supported}"
        ) from error


@dataclass(frozen=True, order=True, slots=True)
class SourcePackage:
    name: str
    epoch: str
    version: str
    release: str

    @classmethod
    def from_row(cls, row: Row, source: Path) -> SourcePackage:
        name, epoch, version, release = row
        if not all(row):
            raise PublishError(f"Empty source package field in {source}: {row!r}")
        if epoch == "(none)":
            epoch = "0"
        if not epoch.isdigit():
            raise PublishError(f"Invalid package epoch in {source}: {epoch!r}")
        return cls(name, epoch, version, release)

    @property
    def evr(self) -> str:
        epoch = "" if self.epoch == "0" else f"{self.epoch}:"
        return f"{epoch}{self.version}-{self.release}"

    @property
    def nvr(self) -> str:
        return f"{self.name}-{self.version}-{self.release}"

    @property
    def nevr(self) -> str:
        return f"{self.name}-{self.evr}"

    def as_row(self) -> Row:
        return self.name, self.epoch, self.version, self.release


@dataclass(frozen=True, slots=True)
class Config:
    branch: str
    releasever: str
    testing: bool
    logical_repository: str
    debug_repository: str
    normal_repository: str
    github_repository: str
    repository: str
    repository_owner: str
    max_assets_per_release: int
    max_parallel_transfers: int
    excluded_sources: tuple[str, ...]
    batch_id: str
    commit_sha: str

    @property
    def profile(self) -> RepositoryProfile:
        return repository_profile(self.branch)

    @property
    def inventory(self) -> Path:
        return Path("state") / self.logical_repository / "inventory.tsv"

    @property
    def retired_inventory(self) -> Path:
        return self.inventory.with_name("retired.tsv")

    @property
    def pending_inventory(self) -> Path:
        return self.inventory.with_suffix(".tsv.next")

    @property
    def applied_batches(self) -> Path:
        return self.inventory.with_name("applied-batches.tsv")

    @property
    def applied_deletions(self) -> Path:
        return self.inventory.with_name("applied-deletions.tsv")

    @property
    def package_list(self) -> Path:
        return Path("repo") / self.logical_repository / "packages.txt"

    @property
    def published_repositories(self) -> tuple[str, ...]:
        if self.testing:
            return (self.logical_repository,)
        return (self.logical_repository, f"{self.normal_repository}-testing")

    def repository_for_kind(self, kind: str) -> str:
        if kind == "packages":
            return self.logical_repository
        if kind == "debuginfo":
            return self.debug_repository
        raise PublishError(f"Unknown package kind: {kind!r}")

    @classmethod
    def from_environment(cls) -> Config:
        names = (
            "branch",
            "releasever",
            "testing",
            "logical_repository",
            "debug_repository",
            "normal_repository",
            "GITHUB_REPOSITORY",
            "REPOSITORY",
            "REPOSITORY_OWNER",
            "MAX_ASSETS_PER_RELEASE",
            "MAX_PARALLEL_TRANSFERS",
            "BATCH_ID",
            "COMMIT_SHA",
        )
        values = {name: require_environment(name) for name in names}
        testing = values["testing"].lower()
        if testing not in {"true", "false"}:
            raise PublishError("testing must be either 'true' or 'false'")
        maximum = positive_integer(
            "MAX_ASSETS_PER_RELEASE", values["MAX_ASSETS_PER_RELEASE"]
        )
        parallel_transfers = positive_integer(
            "MAX_PARALLEL_TRANSFERS", values["MAX_PARALLEL_TRANSFERS"]
        )
        if not values["releasever"].isdigit():
            raise PublishError("releasever must be numeric")
        if not values["BATCH_ID"].isdigit() or int(values["BATCH_ID"]) < 1:
            raise PublishError("BATCH_ID must be a positive integer")
        if not re.fullmatch(r"[0-9a-fA-F]{7,64}", values["COMMIT_SHA"]):
            raise PublishError("COMMIT_SHA must be a Git commit SHA")
        for name in (
            "branch",
            "logical_repository",
            "debug_repository",
            "normal_repository",
            "REPOSITORY",
            "REPOSITORY_OWNER",
        ):
            if not SAFE_COMPONENT.fullmatch(values[name]):
                raise PublishError(f"{name} contains unsafe characters")
        if not SAFE_GITHUB_REPOSITORY.fullmatch(values["GITHUB_REPOSITORY"]):
            raise PublishError("GITHUB_REPOSITORY must have the form owner/repository")
        profile = repository_profile(values["branch"])
        configured_exclusions = os.environ.get("EXCLUDE_SOURCES")
        excluded_sources = tuple(
            pattern
            for pattern in re.split(
                r"[\s,]+",
                configured_exclusions
                if configured_exclusions is not None
                else ",".join(profile.default_excluded_sources),
            )
            if pattern
        )
        for pattern in excluded_sources:
            if (
                "/" in pattern
                or "\\" in pattern
                or any(character in pattern for character in "\x00\n\r\t")
            ):
                raise PublishError(f"Invalid excluded source pattern: {pattern!r}")
        return cls(
            branch=values["branch"],
            releasever=values["releasever"],
            testing=testing == "true",
            logical_repository=values["logical_repository"],
            debug_repository=values["debug_repository"],
            normal_repository=values["normal_repository"],
            github_repository=values["GITHUB_REPOSITORY"],
            repository=values["REPOSITORY"],
            repository_owner=values["REPOSITORY_OWNER"],
            max_assets_per_release=maximum,
            max_parallel_transfers=parallel_transfers,
            excluded_sources=excluded_sources,
            batch_id=values["BATCH_ID"],
            commit_sha=values["COMMIT_SHA"].lower(),
        )


def require_environment(name: str) -> str:
    value = os.environ.get(name)
    if value is None or not value.strip():
        raise PublishError(f"{name} is required")
    return value


def positive_integer(name: str, value: str) -> int:
    try:
        parsed = int(value)
    except ValueError as error:
        raise PublishError(f"{name} must be an integer") from error
    if parsed < 1:
        raise PublishError(f"{name} must be greater than zero")
    return parsed


def command(
    *arguments: PathArgument,
    capture_output: bool = False,
    timeout: int = LOCAL_COMMAND_TIMEOUT,
) -> str:
    args = [os.fspath(argument) for argument in arguments]
    LOGGER.debug("Running command: %s", " ".join(args))
    result = subprocess.run(
        args,
        check=True,
        encoding="utf-8",
        stdout=subprocess.PIPE if capture_output else None,
        timeout=timeout,
    )
    return result.stdout if capture_output else ""


def retry_operation(
    operation: Callable[[], Output],
    description: str,
    attempts: int = MAX_REMOTE_ATTEMPTS,
) -> Output:
    for attempt in range(1, attempts + 1):
        try:
            return operation()
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
            if attempt == attempts:
                raise
            delay = 2 ** (attempt - 1)
            LOGGER.warning(
                "%s failed (attempt %d/%d); retrying in %d seconds",
                description,
                attempt,
                attempts,
                delay,
            )
            time.sleep(delay)
    raise AssertionError("retry loop exited unexpectedly")


def remote_command(
    *arguments: PathArgument,
    capture_output: bool = False,
    attempts: int = MAX_REMOTE_ATTEMPTS,
) -> str:
    return retry_operation(
        lambda: command(
            *arguments,
            capture_output=capture_output,
            timeout=REMOTE_COMMAND_TIMEOUT,
        ),
        f"Remote command {' '.join(os.fspath(argument) for argument in arguments[:4])}",
        attempts,
    )


def parallel_map(
    function: Callable[[Input], Output],
    items: Iterable[Input],
    max_workers: int,
) -> list[Output]:
    with ThreadPoolExecutor(
        max_workers=max_workers, thread_name_prefix="package-transfer"
    ) as executor:
        return list(executor.map(function, items))


def load_mapping(output: str, description: str) -> dict[str, object]:
    try:
        value = json.loads(output)
    except json.JSONDecodeError as error:
        raise PublishError(
            f"Invalid JSON returned for {description}: {error}"
        ) from error
    if not isinstance(value, dict):
        raise PublishError(f"Expected a JSON object for {description}")
    return value


def read_tsv(path: Path, columns: int) -> list[Row]:
    if not path.exists():
        return []
    rows: list[Row] = []
    with path.open(encoding="utf-8", newline="") as stream:
        for line_number, row in enumerate(csv.reader(stream, dialect="excel-tab"), 1):
            if not row or row == [""]:
                continue
            if len(row) != columns:
                raise PublishError(
                    f"{path}:{line_number}: expected {columns} fields, found {len(row)}"
                )
            if any(
                any(character in field for character in "\x00\n\r") for field in row
            ):
                raise PublishError(f"{path}:{line_number}: invalid control character")
            rows.append(tuple(row))
    return rows


def write_tsv(
    path: Path, rows: Iterable[Sequence[str]], *, unique: bool = False
) -> None:
    normalized = [tuple(row) for row in rows]
    if unique:
        normalized = sorted(set(normalized))
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            newline="",
            dir=path.parent,
            prefix=f".{path.name}.",
            delete=False,
        ) as stream:
            temporary = Path(stream.name)
            csv.writer(stream, dialect="excel-tab", lineterminator="\n").writerows(
                normalized
            )
            stream.flush()
            os.fsync(stream.fileno())
        temporary.replace(path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def atomic_write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=path.parent,
            prefix=f".{path.name}.",
            delete=False,
        ) as stream:
            temporary = Path(stream.name)
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        temporary.replace(path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def atomic_write_bytes(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb", dir=path.parent, prefix=f".{path.name}.", delete=False
        ) as stream:
            temporary = Path(stream.name)
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        temporary.replace(path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def serialize_xml(root: ET.Element) -> bytes:
    if root.tag.startswith("{"):
        namespace = root.tag[1:].partition("}")[0]
        ET.register_namespace("", namespace)
    ET.register_namespace("rpm", RPM_NAMESPACE)
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def safe_rpm_name(name: str) -> str:
    safe_name = name.replace("~", "_").replace("^", "_")
    if Path(safe_name).name != safe_name or not safe_name.endswith(".rpm"):
        raise PublishError(f"Unsafe RPM filename: {name!r}")
    return safe_name


def rpm_name_and_release(path: Path) -> tuple[str, str]:
    output = command(
        "rpm", "-qp", "--qf", "%{NAME}\t%{RELEASE}", path, capture_output=True
    ).strip()
    fields = output.split("\t")
    if len(fields) != 2 or any(
        not field or any(character in field for character in "\n\r") for field in fields
    ):
        raise PublishError(f"Unable to determine package name and release for {path}")
    return fields[0], fields[1]


def release_matches_releasever(release: str, releasever: str) -> bool:
    return re.search(rf"\.fc{re.escape(releasever)}(?:[._]|$)", release) is not None


def rpm_source_name(path: Path) -> str:
    source_name = command(
        "dnf", "-q", "rq", "--qf", "%{source_name}", path, capture_output=True
    ).strip()
    if not source_name or "\n" in source_name:
        raise PublishError(f"Unable to determine a unique source name for {path}")
    return source_name


def package_kind(package_name: str) -> str:
    if package_name.endswith(DEBUG_PACKAGE_SUFFIXES):
        return "debuginfo"
    return "packages"


def package_is_excluded(name: str, patterns: Sequence[str]) -> bool:
    return any(fnmatch.fnmatchcase(name, pattern) for pattern in patterns)


def parse_bucket(row: Row, config: Config, source: Path) -> int:
    name, kind, bucket_value, tag, _ = row
    if kind not in PACKAGE_KINDS:
        raise PublishError(f"Unknown package kind in {source}: {kind!r}")
    try:
        bucket = int(bucket_value)
    except ValueError as error:
        raise PublishError(
            f"Invalid bucket number in {source}: {bucket_value!r}"
        ) from error
    if bucket < 1:
        raise PublishError(f"Invalid bucket number in {source}: {bucket}")
    repository = config.repository_for_kind(kind)
    expected_tag = f"{repository}-rpm-{bucket:04d}"
    if tag != expected_tag:
        raise PublishError(
            f"Invalid release tag in {source} for {name}: expected {expected_tag}, found {tag}"
        )
    return bucket


def select_bucket(bucket_counts: dict[int, int], maximum: int) -> int:
    available = [bucket for bucket, count in bucket_counts.items() if count < maximum]
    return min(available) if available else max(bucket_counts, default=0) + 1


def pull_manifest(item: tuple[Path, str, str]) -> tuple[str, Path]:
    manifests_directory, reference, digest = item
    destination = manifests_directory / digest.removeprefix("sha256:")
    destination.mkdir(parents=True, exist_ok=True)
    LOGGER.info("Downloading package manifest %s", reference)
    remote_command("oras", "pull", reference, "-o", destination)
    return reference, destination


def resolve_manifest(item: tuple[str, str, str]) -> Row:
    package_name, image, tag = item
    descriptor = load_mapping(
        remote_command(
            "oras",
            "manifest",
            "fetch",
            "--descriptor",
            f"{image}:{tag}",
            capture_output=True,
        ),
        f"descriptor for {image}:{tag}",
    )
    digest = descriptor.get("digest")
    if not isinstance(digest, str) or not re.fullmatch(r"sha256:[0-9a-f]{64}", digest):
        raise PublishError(f"Invalid digest returned for {image}:{tag}")
    return package_name, f"{image}@{digest}", digest


def batch(config: Config) -> None:
    """Resolve only immutable artifact references declared by this batch."""
    config.applied_batches.parent.mkdir(parents=True, exist_ok=True)
    config.applied_batches.touch()
    applied = read_tsv(config.applied_batches, 2)
    if (config.batch_id, config.commit_sha) in applied:
        Path("batch-noop").touch()
        write_tsv(Path("new-manifests.tsv"), ())
        LOGGER.info("Batch %s was already committed; nothing to do", config.batch_id)
        return

    descriptor_root = Path("batch-descriptors")
    descriptor_paths = sorted(descriptor_root.rglob("*.json"))
    if not descriptor_paths:
        raise PublishError(f"No descriptors found for batch {config.batch_id}")
    by_build: dict[int, tuple[str, str, str]] = {}
    for path in descriptor_paths:
        document = load_mapping(path.read_text(encoding="utf-8"), str(path))
        try:
            schema = document["schema"]
            batch_id = str(document["batch_id"])
            build_id = int(document["build_id"])
            commit_sha = str(document["commit_sha"]).lower()
            branch = str(document["branch"])
            profile = str(document["profile"])
            releasever = str(document["releasever"])
            package = str(document["package"])
            reference = str(document["oci_reference"])
        except (KeyError, TypeError, ValueError) as error:
            raise PublishError(f"Invalid batch descriptor {path}: {error}") from error
        if (
            schema != 1
            or batch_id != config.batch_id
            or commit_sha != config.commit_sha
        ):
            raise PublishError(
                f"Descriptor {path} does not belong to the requested batch"
            )
        if build_id < 1 or not SAFE_COMPONENT.fullmatch(package):
            raise PublishError(
                f"Descriptor {path} contains an invalid build or package"
            )
        expected_prefix = f"ghcr.io/{config.github_repository}/{package.lower()}:"
        if not reference.startswith(expected_prefix) or not SAFE_COMPONENT.fullmatch(
            reference.removeprefix(expected_prefix)
        ):
            raise PublishError(f"Descriptor {path} contains an unsafe OCI reference")
        if profile != config.branch or releasever != config.releasever:
            continue
        if branch != config.profile.source_branch:
            raise PublishError(f"Descriptor {path} has the wrong source branch")
        row = (package, reference.rsplit(":", 1)[0], reference.rsplit(":", 1)[1])
        previous = by_build.get(build_id)
        if previous is not None and previous != row:
            raise PublishError(f"Conflicting descriptors for build {build_id}")
        by_build[build_id] = row

    resolved = parallel_map(
        resolve_manifest, sorted(set(by_build.values())), config.max_parallel_transfers
    )
    known = {
        row[4]
        for path in (config.inventory, config.retired_inventory)
        for row in read_tsv(path, 5)
    }
    write_tsv(
        Path("new-manifests.tsv"),
        (row for row in resolved if row[2] not in known),
        unique=True,
    )


def download(config: Config) -> None:
    manifests = Path("incoming/manifests")
    rpms = Path("incoming/rpms")
    manifests.mkdir(parents=True, exist_ok=True)
    rpms.mkdir(parents=True, exist_ok=True)
    references_by_digest: dict[str, set[str]] = defaultdict(set)
    for _, reference, digest in read_tsv(Path("new-manifests.tsv"), 3):
        if not re.fullmatch(r"sha256:[0-9a-f]{64}", digest):
            raise PublishError(f"Invalid manifest digest: {digest!r}")
        references_by_digest[digest].add(reference)

    transfers = [
        (manifests, min(references), digest)
        for digest, references in sorted(references_by_digest.items())
    ]
    downloads = parallel_map(
        pull_manifest,
        transfers,
        config.max_parallel_transfers,
    )
    candidates_by_name: dict[str, Row] = {}
    for reference, destination in downloads:
        digest = f"sha256:{destination.name}"
        for rpm_file in destination.rglob("*.rpm"):
            name = safe_rpm_name(rpm_file.name)
            target = rpms / name
            if target.exists() and not filecmp.cmp(rpm_file, target, shallow=False):
                raise PublishError(f"Conflicting RPM assets have the same name: {name}")
            if not target.exists():
                shutil.copy2(rpm_file, target)
            candidate = (name, reference, digest)
            previous = candidates_by_name.get(name)
            if previous is None or candidate < previous:
                candidates_by_name[name] = candidate
    candidates = list(candidates_by_name.values())
    write_tsv(Path("incoming/candidates.tsv"), candidates, unique=True)
    known = {
        row[0]
        for path in (config.inventory, config.retired_inventory)
        for row in read_tsv(path, 5)
    }
    stable_names: set[str] = set()
    if config.testing:
        for repository_name in (
            config.normal_repository,
            f"{config.normal_repository}-debuginfo",
        ):
            stable_names.update(
                repository_package_names(Path("repo") / repository_name)
            )
    new_rpms: list[Row] = []
    for name, reference, digest in sorted(set(candidates)):
        rpm_path = rpms / name
        source_name = rpm_source_name(rpm_path)
        if package_is_excluded(source_name, config.excluded_sources):
            LOGGER.info("Skipping %s: source package %s is excluded", name, source_name)
            continue
        package_name, release = rpm_name_and_release(rpm_path)
        if not release_matches_releasever(release, config.releasever):
            LOGGER.info("Skipping %s: not built for Fedora %s", name, config.releasever)
        elif name in stable_names:
            LOGGER.info("Skipping %s: already present in the stable repository", name)
        elif name not in known:
            kind = package_kind(package_name)
            new_rpms.append((name, kind, reference, digest))
    write_tsv(Path("incoming/new-rpms.tsv"), new_rpms, unique=True)


def assign(config: Config) -> None:
    inventory = read_tsv(config.inventory, 5)
    retired = read_tsv(config.retired_inventory, 5)
    bucket_history = [
        (row, parse_bucket(row, config, source))
        for source, rows in (
            (config.inventory, inventory),
            (config.retired_inventory, retired),
        )
        for row in rows
    ]
    assignments: list[Row] = []
    new_rpms = read_tsv(Path("incoming/new-rpms.tsv"), 4)
    for _, kind, _, _ in new_rpms:
        if kind not in PACKAGE_KINDS:
            raise PublishError(f"Unknown package kind: {kind!r}")
    for kind in PACKAGE_KINDS:
        repository_name = config.repository_for_kind(kind)
        kind_rows = [row for row in new_rpms if row[1] == kind]
        if not kind_rows:
            continue
        known_buckets = {bucket for row, bucket in bucket_history if row[1] == kind}

        bucket_counts: dict[int, int] = {}
        for bucket in sorted(known_buckets):
            tag = f"{repository_name}-rpm-{bucket:04d}"
            bucket_counts[bucket] = len(release_assets(config, tag))
            LOGGER.info(
                "Release bucket %s contains %d/%d assets",
                tag,
                bucket_counts[bucket],
                config.max_assets_per_release,
            )
        if not bucket_counts:
            bucket_counts[1] = 0

        for name, _, reference, digest in kind_rows:
            bucket = select_bucket(bucket_counts, config.max_assets_per_release)
            if bucket not in bucket_counts:
                bucket_counts[bucket] = 0
            tag = f"{repository_name}-rpm-{bucket:04d}"
            inventory.append((name, kind, str(bucket), tag, digest))
            assignments.append((name, kind, str(bucket), tag, reference))
            bucket_counts[bucket] += 1
    write_tsv(config.pending_inventory, inventory, unique=True)
    write_tsv(Path("incoming/assignments.tsv"), assignments)


def load_release_metadata_cache(config: Config) -> None:
    global _release_metadata_repository
    if _release_metadata_repository == config.github_repository:
        return
    _release_metadata.clear()
    _release_metadata_repository = config.github_repository
    if not RELEASE_METADATA_CACHE.is_file():
        return
    try:
        cache = load_mapping(
            RELEASE_METADATA_CACHE.read_text(encoding="utf-8"),
            str(RELEASE_METADATA_CACHE),
        )
    except OSError as error:
        raise PublishError(
            f"Unable to read release metadata cache {RELEASE_METADATA_CACHE}: {error}"
        ) from error
    if cache.get("repository") != config.github_repository:
        LOGGER.info("Ignoring release metadata cache for another repository")
        return
    releases = cache.get("releases")
    if not isinstance(releases, dict):
        raise PublishError(f"Invalid release map in {RELEASE_METADATA_CACHE}")
    for tag, value in releases.items():
        if not isinstance(tag, str) or not isinstance(value, dict):
            raise PublishError(f"Invalid release entry in {RELEASE_METADATA_CACHE}")
        body = value.get("body")
        assets = value.get("assets")
        if not isinstance(body, str) or not isinstance(assets, list):
            raise PublishError(
                f"Invalid metadata for release {tag} in {RELEASE_METADATA_CACHE}"
            )
        _release_metadata[tag] = ReleaseMetadata(
            body,
            tuple(asset for asset in assets if isinstance(asset, dict)),
        )


def save_release_metadata_cache(config: Config) -> None:
    content = {
        "repository": config.github_repository,
        "releases": {
            tag: {"assets": metadata.assets, "body": metadata.body}
            for tag, metadata in sorted(_release_metadata.items())
        },
    }
    atomic_write_text(
        RELEASE_METADATA_CACHE,
        json.dumps(content, indent=2, sort_keys=True) + "\n",
    )


def cache_release_metadata(config: Config, tag: str, metadata: ReleaseMetadata) -> None:
    with _release_metadata_lock:
        load_release_metadata_cache(config)
        _release_metadata[tag] = metadata
        save_release_metadata_cache(config)


def release_metadata(
    config: Config,
    tag: str,
    *,
    missing_ok: bool = False,
    refresh: bool = False,
) -> ReleaseMetadata | None:
    with _release_metadata_lock:
        load_release_metadata_cache(config)
        if not refresh and tag in _release_metadata:
            return _release_metadata[tag]
        try:
            release = load_mapping(
                remote_command(
                    "gh",
                    "release",
                    "view",
                    tag,
                    "-R",
                    config.github_repository,
                    "--json",
                    "assets,body",
                    capture_output=True,
                    attempts=1 if missing_ok else MAX_REMOTE_ATTEMPTS,
                ),
                f"release {tag}",
            )
        except subprocess.CalledProcessError:
            if missing_ok:
                _release_metadata.pop(tag, None)
                save_release_metadata_cache(config)
                return None
            raise
        body = release.get("body")
        assets = release.get("assets")
        if not isinstance(body, str):
            raise PublishError(f"Invalid body returned for release {tag}")
        if not isinstance(assets, list):
            raise PublishError(f"Invalid asset list returned for release {tag}")
        metadata = ReleaseMetadata(
            body,
            tuple(asset for asset in assets if isinstance(asset, dict)),
        )
        _release_metadata[tag] = metadata
        save_release_metadata_cache(config)
        return metadata


def release_asset_records(config: Config, tag: str) -> tuple[dict[str, object], ...]:
    metadata = release_metadata(config, tag)
    if metadata is None:
        raise PublishError(f"Release {tag} does not exist")
    return metadata.assets


def release_assets(config: Config, tag: str) -> set[str]:
    return {
        asset["name"]
        for asset in release_asset_records(config, tag)
        if isinstance(asset.get("name"), str)
    }


def parse_github_timestamp(value: object, description: str) -> datetime:
    if not isinstance(value, str):
        raise PublishError(f"Missing creation time for {description}")
    try:
        timestamp = datetime.fromisoformat(value)
    except ValueError as error:
        raise PublishError(
            f"Invalid creation time for {description}: {value!r}"
        ) from error
    if timestamp.tzinfo is None:
        raise PublishError(
            f"Creation time lacks a timezone for {description}: {value!r}"
        )
    return timestamp


def release_asset_creation_times(config: Config, tag: str) -> dict[str, datetime]:
    creation_times: dict[str, datetime] = {}
    for asset in release_asset_records(config, tag):
        name = asset.get("name")
        if not isinstance(name, str):
            continue
        creation_times[name] = parse_github_timestamp(
            asset.get("createdAt"),
            f"{name} in release {tag}",
        )
    return creation_times


def upload_asset(item: tuple[Config, str, str]) -> None:
    config, tag, name = item
    LOGGER.info("Uploading package %s to %s", name, tag)
    for attempt in range(1, MAX_REMOTE_ATTEMPTS + 1):
        try:
            command(
                "gh",
                "release",
                "upload",
                tag,
                Path("incoming/rpms") / safe_rpm_name(name),
                "-R",
                config.github_repository,
            )
            return
        except subprocess.CalledProcessError:
            metadata = release_metadata(config, tag, refresh=True)
            if metadata is not None and any(
                asset.get("name") == name for asset in metadata.assets
            ):
                LOGGER.info("Package %s is already present in %s", name, tag)
                return
            if attempt == MAX_REMOTE_ATTEMPTS:
                raise
            delay = 2 ** (attempt - 1)
            LOGGER.warning(
                "Upload of %s failed (attempt %d/%d); retrying in %d seconds",
                name,
                attempt,
                MAX_REMOTE_ATTEMPTS,
                delay,
            )
            time.sleep(delay)


def repofile_url(config: Config, branch: str, repository: str) -> str:
    filename = f"{config.repository}-{branch}-{config.releasever}.repo"
    return (
        f"https://{config.repository_owner}.github.io/"
        f"{config.repository}/{repository}/{filename}"
    )


def pages_repository_url(config: Config, repository: str) -> str:
    return (
        f"https://{config.repository_owner}.github.io/{config.repository}/{repository}/"
    )


def repository_from_release_tag(config: Config, tag: str) -> str:
    for repository in (config.logical_repository, config.debug_repository):
        if re.fullmatch(rf"{re.escape(repository)}-rpm-\d{{4}}", tag):
            return repository
    raise PublishError(f"Invalid release tag for {config.logical_repository}: {tag}")


def release_notes(config: Config, tag: str) -> str:
    repository = repository_from_release_tag(config, tag)
    if repository == config.debug_repository:
        return ""
    profile = config.profile
    display_name = profile.display_name
    variant = " testing" if config.testing else ""
    repository_suffix = repository.removeprefix(config.normal_repository)
    repository_id = (
        f"{config.repository}-github:{config.profile.name}{repository_suffix}"
    )
    commands: list[str] = []
    introduction = "Install the repository configuration with:"
    if profile.dependency_repositories:
        dependencies = [
            repository_profile(name) for name in profile.dependency_repositories
        ]
        dependency_names = ", ".join(
            dependency.display_name for dependency in dependencies
        )
        introduction = (
            f"{display_name} uses packages from {dependency_names}. Install all "
            "repository configurations with:"
        )
        for dependency in dependencies:
            dependency_repository = f"{dependency.name}-{config.releasever}"
            commands.append(
                "sudo dnf config-manager addrepo --from-repofile="
                + repofile_url(
                    config,
                    dependency.name,
                    dependency_repository,
                )
            )
    commands.append(
        "sudo dnf config-manager addrepo --from-repofile="
        + repofile_url(config, profile.name, config.normal_repository)
    )
    if repository != config.normal_repository:
        commands.append(f"sudo dnf config-manager enable '{repository_id}'")
    command_block = "\n".join(commands)
    summary = f"RPM packages from the {display_name} package stream."
    if profile.source_branch != profile.name:
        source = repository_profile(profile.source_branch)
        summary = (
            f"{display_name} packages built from the {source.display_name} "
            "package stream."
        )
    testing_warning = ""
    if config.testing:
        testing_warning = (
            "\n> Testing packages may be unstable and are disabled by default.\n"
        )
    return f"""# {display_name}{variant} repository for Fedora {config.releasever}

{summary}

> This release stores RPM assets used by the repository metadata.
> Install the repository configuration instead of downloading RPMs manually.
{testing_warning}
## Enable the repository

{introduction}

```console
{command_block}
```

Repository ID: `{repository_id}`
"""


def update_release_notes(
    config: Config,
    tag: str,
    notes: str,
    metadata: ReleaseMetadata | None = None,
) -> None:
    if metadata is None:
        metadata = release_metadata(config, tag)
    if metadata is None:
        raise PublishError(f"Release {tag} does not exist")
    if metadata.body == notes:
        LOGGER.debug("Release description for %s is already current", tag)
        return
    LOGGER.info("Updating release description for %s", tag)
    remote_command(
        "gh",
        "release",
        "edit",
        tag,
        "-R",
        config.github_repository,
        "--notes",
        notes,
    )
    cache_release_metadata(config, tag, ReleaseMetadata(notes, metadata.assets))


def update_existing_release(config: Config, tag: str) -> None:
    metadata = release_metadata(config, tag, missing_ok=True)
    if metadata is not None:
        update_release_notes(config, tag, release_notes(config, tag), metadata)


def ensure_release(config: Config, tag: str) -> None:
    notes = release_notes(config, tag)
    metadata = release_metadata(config, tag, missing_ok=True)
    if metadata is not None:
        update_release_notes(config, tag, notes, metadata)
        return
    for attempt in range(1, MAX_REMOTE_ATTEMPTS + 1):
        try:
            command(
                "gh",
                "release",
                "create",
                tag,
                "-R",
                config.github_repository,
                "--title",
                tag,
                "--notes",
                notes,
            )
            cache_release_metadata(config, tag, ReleaseMetadata(notes, ()))
            return
        except subprocess.CalledProcessError:
            metadata = release_metadata(config, tag, missing_ok=True, refresh=True)
            if metadata is not None:
                update_release_notes(config, tag, notes, metadata)
                return
            if attempt == MAX_REMOTE_ATTEMPTS:
                raise
            delay = 2 ** (attempt - 1)
            LOGGER.warning(
                "Creation of %s failed (attempt %d/%d); retrying in %d seconds",
                tag,
                attempt,
                MAX_REMOTE_ATTEMPTS,
                delay,
            )
            time.sleep(delay)


def upload(config: Config) -> None:
    grouped: dict[str, list[Row]] = defaultdict(list)
    for row in read_tsv(Path("incoming/assignments.tsv"), 5):
        grouped[row[3]].append(row)
    active_tags = {row[3] for row in read_tsv(config.pending_inventory, 5)}
    retired_tags = {row[3] for row in read_tsv(config.retired_inventory, 5)}
    for tag in sorted(active_tags - grouped.keys()):
        update_existing_release(config, tag)
    for tag in sorted(retired_tags - active_tags):
        if not release_notes(config, tag):
            update_existing_release(config, tag)
    transfers: list[tuple[Config, str, str]] = []
    for tag, rows in sorted(grouped.items()):
        ensure_release(config, tag)
        existing = release_assets(config, tag)
        for name, _, _, _, _ in rows:
            if name not in existing:
                transfers.append((config, tag, name))
    parallel_map(upload_asset, transfers, config.max_parallel_transfers)
    pending = config.pending_inventory
    if not pending.is_file():
        raise PublishError(f"Missing pending inventory: {pending}")


def seal(config: Config) -> None:
    pending = config.pending_inventory
    if not pending.is_file():
        raise PublishError(f"Missing pending inventory: {pending}")
    generation = require_environment("PUBLISH_GENERATION")
    if not SAFE_COMPONENT.fullmatch(generation):
        raise PublishError("PUBLISH_GENERATION contains unsafe characters")
    write_generation_markers(config, generation)
    pending.replace(config.inventory)
    write_tsv(
        config.applied_batches,
        (*read_tsv(config.applied_batches, 2), (config.batch_id, config.commit_sha)),
        unique=True,
    )


def write_generation_markers(config: Config, generation: str) -> None:
    created_at = datetime.now(UTC).isoformat().replace("+00:00", "Z")
    for repository in config.published_repositories:
        marker = {
            "created_at": created_at,
            "generation": generation,
            "repository": repository,
        }
        atomic_write_text(
            Path("repo") / repository / "generation.json",
            json.dumps(marker, indent=2, sort_keys=True) + "\n",
        )


def generate_repository(config: Config, kind: str, output: str) -> None:
    repository = Path("repo") / output
    repository.mkdir(parents=True, exist_ok=True)
    sources: list[str] = []
    if (repository / "repodata/repomd.xml").is_file():
        sources.extend(("--repo", str(repository)))
    grouped: dict[str, list[Row]] = defaultdict(list)
    for row in read_tsv(Path("incoming/assignments.tsv"), 5):
        if row[1] == kind:
            grouped[row[3]].append(row)
    for tag, rows in sorted(grouped.items()):
        fragment = Path("metadata-fragments") / tag
        shutil.rmtree(fragment, ignore_errors=True)
        fragment.mkdir(parents=True)
        for name, _, _, _, _ in rows:
            source = Path("incoming/rpms") / safe_rpm_name(name)
            if not source.is_file():
                raise PublishError(f"Missing RPM for metadata generation: {source}")
            os.link(source, fragment / name)
        command(
            "createrepo_c",
            "--baseurl",
            f"https://github.com/{config.github_repository}/releases/download/{tag}/",
            fragment,
        )
        sources.extend(("--repo", str(fragment)))
    if not sources:
        command("createrepo_c", repository)
    elif grouped:
        merged = Path(f"merged-{output}")
        shutil.rmtree(merged, ignore_errors=True)
        command("mergerepo_c", "--all", "-o", merged, *sources)
        generated = merged / "repodata"
        if not (generated / "repomd.xml").is_file():
            raise PublishError(f"mergerepo_c did not create metadata for {output}")
        shutil.rmtree(repository / "repodata", ignore_errors=True)
        generated.replace(repository / "repodata")


def repository_packages_by_source(
    repository: Path,
    latest_limit: int | None = None,
    excluded_sources: Sequence[str] = (),
    included_sources: Sequence[str] = (),
) -> dict[str, set[str]]:
    repo_id = f"retention-{repository.name}"
    arguments: list[PathArgument] = [
        "dnf",
        "-q",
        "--refresh",
        f"--repofrompath={repo_id},{repository}",
        f"--repo={repo_id}",
        "rq",
        "--qf",
        "%{source_name}\\t%{location}\\n",
    ]
    if latest_limit is not None:
        arguments.extend(("--latest-limit", str(latest_limit)))
    output = command(*arguments, capture_output=True)
    names: dict[str, set[str]] = defaultdict(set)
    for line in output.splitlines():
        source_name, separator, location = line.partition("\t")
        if not separator:
            source_name, separator, location = line.partition("\\t")
        if not separator:
            raise PublishError(
                f"Invalid package query output for {repository}: {line!r}"
            )
        if package_is_excluded(source_name, excluded_sources):
            continue
        if included_sources and source_name not in included_sources:
            continue
        name = unquote(Path(urlparse(location).path).name)
        if name:
            names[source_name].add(safe_rpm_name(name))
    return names


def repository_package_names(
    repository: Path,
    latest_limit: int | None = None,
    excluded_sources: Sequence[str] = (),
    included_sources: Sequence[str] = (),
) -> set[str]:
    return {
        name
        for names in repository_packages_by_source(
            repository,
            latest_limit,
            excluded_sources,
            included_sources,
        ).values()
        for name in names
    }


def repository_package_names_for_retention(
    repository: Path, policy: RetentionPolicy
) -> set[str]:
    retained = repository_package_names(repository, policy.default_versions)
    sources_by_limit: dict[int, list[str]] = defaultdict(list)
    for source_name, limit in policy.source_version_overrides.items():
        sources_by_limit[limit].append(source_name)
    for limit, source_names in sorted(sources_by_limit.items()):
        retained.update(
            repository_package_names(
                repository,
                latest_limit=limit,
                included_sources=source_names,
            )
        )
    return retained


def local_metadata_path(repository: Path, href: str, source: Path) -> Path:
    candidate = repository / href
    try:
        candidate.resolve(strict=True).relative_to(repository.resolve(strict=True))
    except (FileNotFoundError, ValueError) as error:
        raise PublishError(
            f"Unsafe or missing metadata path in {source}: {href}"
        ) from error
    return candidate


def compress_metadata(path: Path, content: bytes) -> bytes:
    if path.suffix == ".gz":
        return gzip.compress(content, mtime=0)
    if path.suffix == ".bz2":
        return bz2.compress(content)
    if path.suffix == ".xz":
        return lzma.compress(content)
    if path.suffix != ".zst":
        return content
    with tempfile.TemporaryDirectory(prefix="repo-metadata-") as directory:
        source = Path(directory) / "metadata.xml"
        destination = Path(directory) / "metadata.xml.zst"
        source.write_bytes(content)
        command("zstd", "-q", "-f", source, "-o", destination)
        return destination.read_bytes()


def update_repomd_record(
    data: ET.Element, compressed: bytes, uncompressed: bytes
) -> None:
    fields: dict[str, str] = {
        "size": str(len(compressed)),
        "open-size": str(len(uncompressed)),
        "timestamp": str(int(time.time())),
    }
    for field, value in fields.items():
        element = data.find(f"{{*}}{field}")
        if element is not None:
            element.text = value
    for field, payload in (("checksum", compressed), ("open-checksum", uncompressed)):
        element = data.find(f"{{*}}{field}")
        if element is None:
            continue
        algorithm = element.get("type", "sha256")
        try:
            element.text = hashlib.new(algorithm, payload).hexdigest()
        except ValueError as error:
            raise PublishError(
                f"Unsupported repository checksum: {algorithm}"
            ) from error


def retain_repository_packages(repository: Path, retained_names: set[str]) -> None:
    repomd = repository / "repodata/repomd.xml"
    try:
        tree = ET.parse(repomd)
    except (OSError, ET.ParseError) as error:
        raise PublishError(f"Unable to parse {repomd}: {error}") from error
    root = tree.getroot()
    records = {data.get("type"): data for data in root.findall("./{*}data")}
    primary_record = records.get("primary")
    if primary_record is None:
        raise PublishError(f"No primary metadata record in {repomd}")

    retained_package_ids: set[str] = set()
    for metadata_type in ("primary", "filelists", "other"):
        data = records.get(metadata_type)
        if data is None:
            continue
        location = data.find("{*}location")
        href = location.get("href") if location is not None else None
        if not href:
            raise PublishError(f"No location for {metadata_type} metadata in {repomd}")
        path = local_metadata_path(repository, href, repomd)
        content = decompress_metadata(path)
        try:
            metadata_root = ET.fromstring(content)
        except ET.ParseError as error:
            raise PublishError(f"Invalid XML in {path}: {error}") from error
        packages = list(metadata_root.findall("{*}package"))
        for package in packages:
            if metadata_type == "primary":
                rpm_location = package.find("{*}location")
                rpm_href = (
                    rpm_location.get("href") if rpm_location is not None else None
                )
                keep = rpm_href is not None and Path(rpm_href).name in retained_names
                if keep:
                    checksum = package.find("{*}checksum")
                    if checksum is not None and checksum.text:
                        retained_package_ids.add(checksum.text)
            else:
                keep = package.get("pkgid") in retained_package_ids
            if not keep:
                metadata_root.remove(package)
        metadata_root.set("packages", str(len(metadata_root.findall("{*}package"))))
        uncompressed = serialize_xml(metadata_root)
        compressed = compress_metadata(path, uncompressed)
        atomic_write_bytes(path, compressed)
        update_repomd_record(data, compressed, uncompressed)

    for data in list(root.findall("./{*}data")):
        metadata_type = data.get("type", "")
        if not metadata_type.endswith(("_db", "_zck")):
            continue
        location = data.find("{*}location")
        href = location.get("href") if location is not None else None
        if href:
            local_metadata_path(repository, href, repomd).unlink(missing_ok=True)
        root.remove(data)
    revision = root.find("./{*}revision")
    if revision is not None:
        revision.text = str(time.time_ns())
    atomic_write_bytes(repomd, serialize_xml(root))


def packages_within_retention_period(
    config: Config,
    current_time: datetime | None = None,
    eligible_names: set[str] | None = None,
) -> set[str]:
    inventory = read_tsv(config.pending_inventory, 5)
    if eligible_names is None:
        eligible_names = {row[0] for row in inventory}
    new_names = {row[0] for row in read_tsv(Path("incoming/assignments.tsv"), 5)}
    retained = set(new_names)
    cutoff = (current_time or datetime.now(UTC)) - config.profile.retention.max_age
    rows_by_tag: dict[str, list[Row]] = defaultdict(list)
    for row in inventory:
        if row[0] in eligible_names and row[0] not in new_names:
            rows_by_tag[row[3]].append(row)
    for tag, rows in sorted(rows_by_tag.items()):
        creation_times = release_asset_creation_times(config, tag)
        for name, _, _, _, _ in rows:
            created_at = creation_times.get(name)
            if created_at is None:
                LOGGER.warning(
                    "Keeping %s because its creation time is unavailable in %s",
                    name,
                    tag,
                )
                retained.add(name)
            elif created_at >= cutoff:
                retained.add(name)
    return retained


def apply_retention(config: Config) -> None:
    inventory = read_tsv(config.pending_inventory, 5)
    eligible_inventory_names = {row[0] for row in inventory}
    retained_names: set[str] = set()
    policy = config.profile.retention
    recent_names = packages_within_retention_period(
        config, eligible_names=eligible_inventory_names
    )
    repositories = (
        (config.logical_repository, config.normal_repository),
        (config.debug_repository, f"{config.normal_repository}-debuginfo"),
    )
    for repository_name, stable_repository_name in repositories:
        repository = Path("repo") / repository_name
        if config.testing:
            testing_names = repository_package_names(
                repository, excluded_sources=config.excluded_sources
            )
            testing_names.intersection_update(eligible_inventory_names)
            stable_names = repository_package_names(
                Path("repo") / stable_repository_name
            )
            duplicates = testing_names & stable_names
            testing_names.difference_update(duplicates)
            if duplicates:
                LOGGER.info(
                    "Excluded %d RPMs already present in %s",
                    len(duplicates),
                    stable_repository_name,
                )
            retain_repository_packages(repository, testing_names)
        else:
            eligible_names = repository_package_names(
                repository, excluded_sources=config.excluded_sources
            )
            eligible_names.intersection_update(eligible_inventory_names)
            retain_repository_packages(repository, eligible_names)

        current_names = repository_package_names(repository)
        newest_names = (
            repository_package_names(repository, latest_limit=1)
            if policy.always_keep_newest
            else set()
        )
        age_retained_names = (current_names & recent_names) | newest_names
        expired_count = len(current_names - age_retained_names)
        if expired_count:
            LOGGER.info(
                "Retiring %d RPMs older than %d days from %s",
                expired_count,
                policy.max_age.days,
                repository_name,
            )
        retain_repository_packages(repository, age_retained_names)
        retained = repository_package_names_for_retention(repository, policy)
        retain_repository_packages(repository, retained)
        retained_names.update(retained)

    active = [row for row in inventory if row[0] in retained_names]
    newly_retired = [row for row in inventory if row[0] not in retained_names]
    retired = read_tsv(config.retired_inventory, 5)
    write_tsv(config.pending_inventory, active, unique=True)
    write_tsv(config.retired_inventory, (*retired, *newly_retired), unique=True)
    if newly_retired:
        LOGGER.info("Retired %d RPM assets", len(newly_retired))


def metadata(config: Config) -> None:
    generate_repository(config, "packages", config.logical_repository)
    generate_repository(config, "debuginfo", config.debug_repository)
    apply_retention(config)
    packages = repository_source_packages(Path("repo") / config.logical_repository)
    content = "".join(
        f"{nvr}\n" for nvr in sorted({package.nvr for package in packages})
    )
    atomic_write_text(config.package_list, content)


def repository_source_packages(repository: Path) -> set[SourcePackage]:
    if not (repository / "repodata/repomd.xml").is_file():
        return set()
    repo_id = f"summary-{repository.name}"
    output = command(
        "dnf",
        "-q",
        "--refresh",
        f"--repofrompath={repo_id},{repository}",
        f"--repo={repo_id}",
        "rq",
        "--qf",
        "%{source_name}\\t%{epoch}\\t%{version}\\t%{release}\\n",
        capture_output=True,
    )
    packages: set[SourcePackage] = set()
    for line in output.splitlines():
        fields = line.split("\t")
        if len(fields) != 4:
            fields = line.split("\\t")
        if len(fields) != 4:
            raise PublishError(
                f"Invalid source package query output for {repository}: {line!r}"
            )
        packages.add(SourcePackage.from_row(tuple(fields), repository))
    return packages


def snapshot(config: Config) -> None:
    global _release_metadata_repository
    with _release_metadata_lock:
        _release_metadata.clear()
        _release_metadata_repository = None
        RELEASE_METADATA_CACHE.unlink(missing_ok=True)
    repository = Path("repo") / config.logical_repository
    packages = repository_source_packages(repository)
    write_tsv(PACKAGE_SNAPSHOT, (package.as_row() for package in packages), unique=True)


def deletion_request() -> tuple[str, tuple[str, ...]]:
    deletion_id = require_environment("DELETE_ID")
    if not SAFE_COMPONENT.fullmatch(deletion_id):
        raise PublishError("DELETE_ID contains unsafe characters")
    packages = tuple(
        sorted(
            set(
                filter(
                    None,
                    re.split(r"[\s,]+", require_environment("DELETE_PACKAGES")),
                )
            )
        )
    )
    if not packages:
        raise PublishError("DELETE_PACKAGES must contain at least one source package")
    for package in packages:
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9+._-]*", package):
            raise PublishError(f"Invalid source package name: {package!r}")
    return deletion_id, packages


def delete_packages(config: Config) -> None:
    _deletion_id, requested = deletion_request()
    inventory = read_tsv(config.inventory, 5)
    retired = read_tsv(config.retired_inventory, 5)
    previously_deleted = {row[0] for row in read_tsv(config.applied_deletions, 2)}
    repositories = (
        (config.logical_repository, "packages"),
        (config.debug_repository, "debuginfo"),
    )
    names_by_source: dict[str, set[str]] = defaultdict(set)
    for repository_name, _ in repositories:
        repository = Path("repo") / repository_name
        if not (repository / "repodata/repomd.xml").is_file():
            raise PublishError(f"Missing repository metadata: {repository}")
        for source, names in repository_packages_by_source(repository).items():
            names_by_source[source].update(names)

    unknown = sorted(set(requested) - names_by_source.keys() - previously_deleted)
    if unknown:
        raise PublishError(
            "Source packages are not present in the repository: " + ", ".join(unknown)
        )
    deleted_names = {
        name for source in requested for name in names_by_source.get(source, ())
    }
    inventory_names = {row[0] for row in inventory}
    missing_inventory = sorted(deleted_names - inventory_names)
    if missing_inventory:
        raise PublishError(
            "Repository packages are missing from inventory: "
            + ", ".join(missing_inventory)
        )

    active = [row for row in inventory if row[0] not in deleted_names]
    deleted = [row for row in inventory if row[0] in deleted_names]
    write_tsv(config.pending_inventory, active, unique=True)
    write_tsv(config.retired_inventory, (*retired, *deleted), unique=True)
    write_tsv(
        Path("pending-deletions.tsv"),
        ((source,) for source in requested),
        unique=True,
    )
    write_tsv(Path("incoming/assignments.tsv"), ())

    for repository_name, kind in repositories:
        retained = {row[0] for row in active if row[1] == kind}
        retain_repository_packages(Path("repo") / repository_name, retained)
    packages = repository_source_packages(Path("repo") / config.logical_repository)
    atomic_write_text(
        config.package_list,
        "".join(f"{package.nvr}\n" for package in sorted(packages)),
    )
    LOGGER.info(
        "Deleted %d RPMs for source packages %s",
        len(deleted_names),
        ", ".join(requested),
    )


def seal_delete(config: Config) -> None:
    pending = config.pending_inventory
    if not pending.is_file():
        raise PublishError(f"Missing pending inventory: {pending}")
    deletion_id, requested = deletion_request()
    pending_deletions = {row[0] for row in read_tsv(Path("pending-deletions.tsv"), 1)}
    if pending_deletions != set(requested):
        raise PublishError("Pending deletion request does not match workflow inputs")
    generation = require_environment("PUBLISH_GENERATION")
    if not SAFE_COMPONENT.fullmatch(generation):
        raise PublishError("PUBLISH_GENERATION contains unsafe characters")
    write_generation_markers(config, generation)
    pending.replace(config.inventory)
    write_tsv(
        config.applied_deletions,
        (
            *read_tsv(config.applied_deletions, 2),
            *((source, deletion_id) for source in requested),
        ),
        unique=True,
    )


def summary_section(title: str, entries: Sequence[str]) -> str:
    lines = [f"<details><summary>{title} ({len(entries)})</summary>", ""]
    lines.extend(f"- {markdown_code(entry)}" for entry in entries)
    if not entries:
        lines.append("None.")
    lines.extend(("", "</details>"))
    return "\n".join(lines)


def markdown_code(value: str) -> str:
    longest_run = max(
        (len(match.group()) for match in re.finditer(r"`+", value)), default=0
    )
    fence = "`" * (longest_run + 1)
    padding = " " if value.startswith("`") or value.endswith("`") else ""
    return f"{fence}{padding}{value}{padding}{fence}"


def package_version_groups(packages: Iterable[SourcePackage]) -> list[str]:
    versions: dict[str, set[str]] = defaultdict(set)
    for package in packages:
        versions[package.name].add(package.evr)
    return [
        f"{name}: {', '.join(sorted(package_versions))}"
        for name, package_versions in sorted(versions.items())
    ]


def summary(config: Config) -> None:
    if not PACKAGE_SNAPSHOT.is_file():
        raise PublishError(f"Missing package snapshot: {PACKAGE_SNAPSHOT}")
    repository = Path("repo") / config.logical_repository
    if not (repository / "repodata/repomd.xml").is_file():
        raise PublishError(f"Missing repository metadata: {repository}")
    before = {
        SourcePackage.from_row(row, PACKAGE_SNAPSHOT)
        for row in read_tsv(PACKAGE_SNAPSHOT, 4)
    }
    after = repository_source_packages(repository)
    before_names = {package.name for package in before}
    after_names = {package.name for package in after}
    added = package_version_groups(
        package for package in after if package.name not in before_names
    )
    updated = package_version_groups(
        package for package in after - before if package.name in before_names
    )
    removed_versions = sorted(
        package.nevr for package in before - after if package.name in after_names
    )
    removed = sorted(before_names - after_names)
    content = "\n".join(
        (
            f"## Repository update: {config.logical_repository}",
            "",
            "| Change | Count |",
            "| --- | ---: |",
            f"| Added | {len(added)} |",
            f"| Updated | {len(updated)} |",
            f"| Removed versions | {len(removed_versions)} |",
            f"| Removed | {len(removed)} |",
            "",
            summary_section("Added packages", added),
            "",
            summary_section("Updated packages", updated),
            "",
            summary_section("Removed package versions", removed_versions),
            "",
            summary_section("Removed packages", removed),
            "",
        )
    )
    summary_path = Path(require_environment("GITHUB_STEP_SUMMARY"))
    try:
        with summary_path.open("a", encoding="utf-8") as stream:
            stream.write(content)
    except OSError as error:
        raise PublishError(
            f"Unable to write workflow summary {summary_path}: {error}"
        ) from error


def create_empty_repository(directory: Path) -> None:
    temporary = directory.with_name(f".{directory.name}.empty")
    shutil.rmtree(temporary, ignore_errors=True)
    temporary.mkdir(parents=True)
    try:
        command("createrepo_c", temporary)
        shutil.rmtree(directory, ignore_errors=True)
        temporary.replace(directory)
    finally:
        shutil.rmtree(temporary, ignore_errors=True)


def prune(config: Config) -> None:
    if config.testing:
        LOGGER.info("Testing publish; no testing assets will be pruned")
        return
    testing_repository = f"{config.normal_repository}-testing"
    inventory_path = Path("state") / testing_repository / "inventory.tsv"
    retired_path = inventory_path.with_name("retired.tsv")
    applied_batches_path = inventory_path.with_name("applied-batches.tsv")
    inventory = read_tsv(inventory_path, 5)
    create_empty_repository(Path("repo") / testing_repository)
    create_empty_repository(Path("repo") / f"{testing_repository}-debuginfo")
    atomic_write_text(Path("repo") / testing_repository / "packages.txt", "")
    write_tsv(retired_path, (*read_tsv(retired_path, 5), *inventory), unique=True)
    write_tsv(inventory_path, ())
    applied_batches_path.touch()


def repository_entry(
    config: Config,
    repository_id: str,
    repository_path: str,
    description: str,
    enabled: bool,
) -> str:
    value = int(enabled)
    return f"""[{config.repository}-github:{repository_id}]
name={config.github_repository} (GitHub) - {description}
baseurl=https://{config.repository_owner}.github.io/{config.repository}/{repository_path}/
type=rpm-md
skip_if_unavailable=True
gpgcheck=1
gpgkey=https://raw.githubusercontent.com/solopasha/kde6-copr/refs/heads/unstable/RPM-GPG-KEY-solopasha
repo_gpgcheck=0
enabled={value}
enabled_metadata={value}
metadata_expire=6h

"""


def repofile(config: Config) -> None:
    description = config.profile.display_name
    profile = config.profile.name
    repository = f"{profile}-$releasever"
    definitions = (
        (profile, repository, f"{description} Fedora $releasever", True),
        (
            f"{profile}-testing",
            f"{repository}-testing",
            f"{description} Fedora $releasever - testing",
            False,
        ),
        (
            f"{profile}-debuginfo",
            f"{repository}-debuginfo",
            f"{description} Fedora $releasever - debuginfo",
            False,
        ),
        (
            f"{profile}-testing-debuginfo",
            f"{repository}-testing-debuginfo",
            f"{description} Fedora $releasever - testing - debuginfo",
            False,
        ),
    )
    content = "".join(
        repository_entry(config, *definition) for definition in definitions
    )
    destination = (
        Path("repo")
        / config.normal_repository
        / f"{config.repository}-{config.profile.name}-{config.releasever}.repo"
    )
    atomic_write_text(destination, content)


def read_lines(path: Path) -> list[str]:
    if not path.is_file():
        return []
    try:
        return [line for line in path.read_text(encoding="utf-8").splitlines() if line]
    except OSError as error:
        raise PublishError(f"Unable to read {path}: {error}") from error


def site_enable_commands(
    config: Config,
    profile: RepositoryProfile,
    releasever: str,
) -> list[str]:
    commands: list[str] = []
    for dependency_name in profile.dependency_repositories:
        dependency_repository = f"{dependency_name}-{releasever}"
        commands.append(
            "sudo dnf config-manager addrepo --from-repofile="
            f"https://{config.repository_owner}.github.io/{config.repository}/"
            f"{dependency_repository}/{config.repository}-{dependency_name}-"
            f"{releasever}.repo"
        )
    normal_repository = f"{profile.name}-{releasever}"
    commands.append(
        "sudo dnf config-manager addrepo --from-repofile="
        f"https://{config.repository_owner}.github.io/{config.repository}/"
        f"{normal_repository}/{config.repository}-{profile.name}-{releasever}.repo"
    )
    return commands


def site_generation_time(repository: Path) -> str:
    marker = repository / "generation.json"
    if not marker.is_file():
        return "Unknown"
    try:
        generation = load_mapping(marker.read_text(encoding="utf-8"), str(marker))
    except OSError as error:
        raise PublishError(f"Unable to read {marker}: {error}") from error
    timestamp = parse_github_timestamp(
        generation.get("created_at"), f"repository generation {repository.name}"
    )
    return timestamp.astimezone(UTC).strftime("%Y-%m-%d %H:%M UTC")


def site_profile_name(profile: RepositoryProfile) -> str:
    return "KDE Plasma" if profile.name == "unstable" else profile.display_name


def site_card(
    config: Config,
    profile: RepositoryProfile,
    releasever: str,
    repository: str,
) -> str:
    directory = Path("repo") / repository
    packages = read_lines(directory / "packages.txt")
    display_name = site_profile_name(profile)
    if profile.name == "unstable":
        description = "KDE Plasma packages built from the master branch."
    elif profile.name == "gear":
        description = "KDE Gear packages built from the master branch."
    elif profile.source_branch == profile.name:
        description = f"Packages from the {profile.display_name} package stream."
    else:
        source = repository_profile(profile.source_branch)
        description = (
            f"{profile.display_name} packages selected from the "
            f"{site_profile_name(source)} package stream."
        )
    commands = "\n".join(site_enable_commands(config, profile, releasever))
    build_label = "build" if len(packages) == 1 else "builds"
    command_id = f"commands-{repository}"
    return f"""      <article class="card" id="{html.escape(repository)}">
        <div class="card-heading">
          <h2>{html.escape(display_name)} · Fedora {html.escape(releasever)}</h2>
          <button class="copy-button" type="button" data-copy-target="{html.escape(command_id)}" aria-label="Copy commands" title="Copy commands">
            <svg aria-hidden="true" viewBox="0 0 24 24"><path d="M8 7V5a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-2v2a3 3 0 0 1-3 3H5a3 3 0 0 1-3-3v-8a3 3 0 0 1 3-3h3Zm2 0h4a3 3 0 0 1 3 3v4h2V5h-9v2Zm4 2H5a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h9a1 1 0 0 0 1-1v-8a1 1 0 0 0-1-1Z"/></svg>
          </button>
        </div>
        <p class="description">{html.escape(description)}</p>
        <div class="facts">
          <span>{len(packages)} source package {build_label}</span>
          <span>Updated {html.escape(site_generation_time(directory))}</span>
        </div>
        <pre><code id="{html.escape(command_id)}">{html.escape(commands)}</code></pre>
      </article>"""


def site(config: Config) -> None:
    profile_order = {"unstable": 0, "gear": 1, "beta": 2}
    cards: list[tuple[int, int, str]] = []
    for profile in REPOSITORY_PROFILES.values():
        for directory in Path("repo").glob(f"{profile.name}-*"):
            match = re.fullmatch(rf"{re.escape(profile.name)}-(\d+)", directory.name)
            if (
                match is None
                or not (directory / "packages.txt").is_file()
                or not (directory / "repodata/repomd.xml").is_file()
            ):
                continue
            releasever = match.group(1)
            cards.append(
                (
                    profile_order.get(profile.name, len(profile_order)),
                    -int(releasever),
                    site_card(config, profile, releasever, directory.name),
                )
            )
    rendered_cards = "\n".join(card for *_, card in sorted(cards))
    if not rendered_cards:
        rendered_cards = "      <p>No repositories have been published yet.</p>"
    source_url = f"https://github.com/{config.github_repository}"
    snapshot_link = ""
    if (Path("repo") / "snapshots/index.html").is_file():
        snapshot_link = (
            '      <p class="snapshot-link"><a href="snapshots/">'
            "Browse dated repository snapshots</a>.</p>"
        )
    content = f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="KDE RPM repositories for Fedora">
    <title>{html.escape(config.repository)} · KDE RPM repositories</title>
    <link rel="stylesheet" href="style.css">
    <script src="site.js" defer></script>
  </head>
  <body>
    <header class="shell">
      <p class="eyebrow">Fedora RPM repositories</p>
      <h1>Fresh KDE builds, packaged for Fedora.</h1>
      <p class="lede">Browse the available package streams and copy the commands
        for the repository you want to enable. Packages are built automatically
        and served from GitHub Releases.</p>
    </header>
    <main class="shell">
      <aside class="notice"><strong>Use with care.</strong> These repositories
        contain development and pre-release software. Review changes before
        updating production systems.</aside>
{snapshot_link}
      <section class="grid" aria-label="Available repositories">
{rendered_cards}
      </section>
    </main>
    <footer class="shell">Published from
      <a href="{html.escape(source_url)}">{html.escape(config.github_repository)}</a>.
    </footer>
  </body>
</html>
"""
    atomic_write_text(Path("repo/index.html"), content)
    for asset in ("style.css", "site.js"):
        source = Path(".github/site") / asset
        try:
            content = source.read_text(encoding="utf-8")
        except OSError as error:
            raise PublishError(
                f"Unable to read site asset {source}: {error}"
            ) from error
        atomic_write_text(Path("repo") / asset, content)


def primary_metadata_path(repository: Path) -> Path:
    repomd = repository / "repodata/repomd.xml"
    if not repomd.is_file() or repomd.stat().st_size == 0:
        raise PublishError(f"Missing or empty {repomd}")
    try:
        root = ET.parse(repomd).getroot()
    except (OSError, ET.ParseError) as error:
        raise PublishError(f"Invalid XML in {repomd}: {error}") from error
    location = root.find("./{*}data[@type='primary']/{*}location")
    href = location.get("href") if location is not None else None
    if not href:
        raise PublishError(f"No primary metadata location in {repomd}")
    return local_metadata_path(repository, href, repomd)


def decompress_metadata(path: Path) -> bytes:
    try:
        if path.suffix == ".gz":
            with gzip.open(path, "rb") as stream:
                return stream.read()
        if path.suffix == ".bz2":
            with bz2.open(path, "rb") as stream:
                return stream.read()
        if path.suffix == ".xz":
            with lzma.open(path, "rb") as stream:
                return stream.read()
        if path.suffix == ".zst":
            return subprocess.run(
                ["zstd", "-qdc", os.fspath(path)],
                check=True,
                stdout=subprocess.PIPE,
                timeout=LOCAL_COMMAND_TIMEOUT,
            ).stdout
        return path.read_bytes()
    except (OSError, EOFError, lzma.LZMAError) as error:
        raise PublishError(f"Unable to read metadata {path}: {error}") from error


def validate(config: Config) -> None:
    locations: set[str] = set()
    for name in (config.logical_repository, config.debug_repository):
        primary = primary_metadata_path(Path("repo") / name)
        content = decompress_metadata(primary)
        try:
            root = ET.fromstring(content)
        except ET.ParseError as error:
            raise PublishError(f"Invalid XML in {primary}: {error}") from error
        locations.update(
            href
            for element in root.findall(".//{*}location")
            if (href := element.get("href")) is not None
        )
    missing = sorted(
        row[0]
        for row in read_tsv(config.pending_inventory, 5)
        if row[0] not in locations
    )
    if missing:
        raise PublishError(f"Metadata is missing {', '.join(missing)}")


def repoclosure(config: Config) -> None:
    arguments: list[PathArgument] = [
        f"--repofrompath=new,repo/{config.logical_repository}/",
        "--check",
        "new",
        "--newest",
    ]
    if config.testing:
        arguments.append(
            f"--repofrompath=base,{pages_repository_url(config, config.normal_repository)}"
        )
    for dependency_name in config.profile.dependency_repositories:
        dependency = repository_profile(dependency_name)
        repository = f"{dependency.name}-{config.releasever}"
        local_repository = Path("repo") / repository
        if (local_repository / "repodata/repomd.xml").is_file():
            repository_url = f"{local_repository}/"
        else:
            repository_url = pages_repository_url(config, repository)
        arguments.append(f"--repofrompath={dependency.name},{repository_url}")
    for best in (False, True):
        LOGGER.info("Checking repository closure%s", " with --best" if best else "")
        command("dnf", "repoclosure", *arguments, *(("--best",) if best else ()))


Stage: TypeAlias = Callable[[Config], None]
STAGES: dict[str, Stage] = {
    "snapshot": snapshot,
    "batch": batch,
    "delete": delete_packages,
    "download": download,
    "assign": assign,
    "metadata": metadata,
    "prune": prune,
    "repofile": repofile,
    "site": site,
    "repoclosure": repoclosure,
    "validate": validate,
    "summary": summary,
    "upload": upload,
    "seal": seal,
    "seal-delete": seal_delete,
}


def parse_arguments(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=STAGES, help="publishing stage to execute")
    parser.add_argument("--verbose", action="store_true", help="enable debug logging")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    arguments = parse_arguments(argv)
    logging.basicConfig(
        format="%(levelname)s: %(message)s",
        level=logging.DEBUG if arguments.verbose else logging.INFO,
    )
    try:
        config = Config.from_environment()
        Path("incoming/rpms").mkdir(parents=True, exist_ok=True)
        Path("metadata-fragments").mkdir(parents=True, exist_ok=True)
        config.inventory.parent.mkdir(parents=True, exist_ok=True)
        config.inventory.touch()
        config.retired_inventory.touch()
        config.applied_deletions.touch()
        LOGGER.info(
            "Running %s stage for %s", arguments.stage, config.logical_repository
        )
        STAGES[arguments.stage](config)
    except PublishError as error:
        LOGGER.error("%s", error)
        return 1
    except subprocess.CalledProcessError as error:
        LOGGER.error(
            "Command failed with exit status %d: %s", error.returncode, error.cmd
        )
        return error.returncode or 1
    except subprocess.TimeoutExpired as error:
        LOGGER.error("Command timed out after %s seconds: %s", error.timeout, error.cmd)
        return 1
    except OSError as error:
        LOGGER.error("Operating system error: %s", error)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
