#!/usr/bin/env python3

import argparse
import csv
import hashlib
import html
import json
import re
import shutil
import tempfile
from collections.abc import Iterable, Sequence
from datetime import date, timedelta
from pathlib import Path

Row = tuple[str, ...]
REPOSITORY_NAME = re.compile(r"^(beta|unstable|gear)-(\d+)$")


class SnapshotError(RuntimeError):
    pass


def read_tsv(path: Path, columns: int) -> list[Row]:
    if not path.is_file():
        raise SnapshotError(f"Missing repository inventory: {path}")
    rows: list[Row] = []
    with path.open(encoding="utf-8", newline="") as stream:
        for line_number, row in enumerate(csv.reader(stream, dialect="excel-tab"), 1):
            if not row or row == [""]:
                continue
            if len(row) != columns:
                raise SnapshotError(
                    f"{path}:{line_number}: expected {columns} fields, found {len(row)}"
                )
            rows.append(tuple(row))
    return rows


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", dir=path.parent, delete=False
    ) as stream:
        temporary = Path(stream.name)
        stream.write(content)
    temporary.replace(path)


def write_tsv(path: Path, rows: Iterable[Sequence[str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", newline="", dir=path.parent, delete=False
    ) as stream:
        temporary = Path(stream.name)
        writer = csv.writer(stream, dialect="excel-tab", lineterminator="\n")
        writer.writerows(sorted({tuple(row) for row in rows}))
    temporary.replace(path)


def file_digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def repository_sources(repo_root: Path, state_root: Path) -> list[tuple[str, str, str]]:
    sources: list[tuple[str, str, str]] = []
    for directory in sorted(repo_root.iterdir()):
        match = REPOSITORY_NAME.fullmatch(directory.name)
        if match is None:
            continue
        debug = repo_root / f"{directory.name}-debuginfo"
        inventory = state_root / directory.name / "inventory.tsv"
        required = (
            directory / "repodata/repomd.xml",
            debug / "repodata/repomd.xml",
            directory / "packages.txt",
            inventory,
        )
        missing = [str(path) for path in required if not path.is_file()]
        if missing:
            raise SnapshotError("Incomplete repository state: " + ", ".join(missing))
        sources.append((directory.name, match.group(1), match.group(2)))
    if not sources:
        raise SnapshotError("No published repositories are available to snapshot")
    return sources


def source_manifest(repo_root: Path, state_root: Path) -> dict[str, dict[str, str]]:
    manifest: dict[str, dict[str, str]] = {}
    for repository, _profile, _releasever in repository_sources(repo_root, state_root):
        manifest[repository] = {
            "debug_repodata": file_digest(
                repo_root / f"{repository}-debuginfo/repodata/repomd.xml"
            ),
            "inventory": file_digest(state_root / repository / "inventory.tsv"),
            "repodata": file_digest(repo_root / repository / "repodata/repomd.xml"),
        }
    return manifest


def repository_config(
    owner: str,
    project: str,
    profile: str,
    snapshot_date: str,
) -> str:
    prefix = f"{project}-github:{profile}-snapshot-{snapshot_date}"
    root = f"https://{owner}.github.io/{project}/snapshots/{snapshot_date}"
    return f"""[{prefix}]
name={owner}/{project} (GitHub) - {profile.title()} snapshot {snapshot_date} for Fedora $releasever
baseurl={root}/{profile}-$releasever/
type=rpm-md
skip_if_unavailable=True
gpgcheck=1
gpgkey=https://raw.githubusercontent.com/solopasha/kde6-copr/refs/heads/unstable/RPM-GPG-KEY-solopasha
repo_gpgcheck=0
enabled=1
enabled_metadata=1
metadata_expire=never

[{prefix}-debuginfo]
name={owner}/{project} (GitHub) - {profile.title()} snapshot {snapshot_date} for Fedora $releasever - debuginfo
baseurl={root}/{profile}-$releasever-debuginfo/
type=rpm-md
skip_if_unavailable=True
gpgcheck=1
gpgkey=https://raw.githubusercontent.com/solopasha/kde6-copr/refs/heads/unstable/RPM-GPG-KEY-solopasha
repo_gpgcheck=0
enabled=0
enabled_metadata=0
metadata_expire=never

"""


def render_index(
    repo_root: Path,
    owner: str,
    project: str,
) -> None:
    cards: list[str] = []
    snapshots_root = repo_root / "snapshots"
    for date_directory in sorted(snapshots_root.iterdir(), reverse=True):
        if not date_directory.is_dir():
            continue
        for repository in sorted(date_directory.iterdir()):
            match = REPOSITORY_NAME.fullmatch(repository.name)
            if match is None or not (repository / "packages.txt").is_file():
                continue
            profile, releasever = match.groups()
            package_count = len(
                [
                    line
                    for line in (repository / "packages.txt")
                    .read_text(encoding="utf-8")
                    .splitlines()
                    if line
                ]
            )
            config_name = f"{project}-{profile}-snapshot-{date_directory.name}.repo"
            config_url = (
                f"https://{owner}.github.io/{project}/snapshots/"
                f"{date_directory.name}/{repository.name}/{config_name}"
            )
            command = f"sudo dnf config-manager addrepo --from-repofile={config_url}"
            cards.append(
                f"""      <article class="card">
        <div class="card-heading"><h2>{html.escape(profile.title())} · Fedora {html.escape(releasever)}</h2></div>
        <p class="description">Snapshot from {html.escape(date_directory.name)}.</p>
        <div class="facts"><span>{package_count} source packages</span></div>
        <pre><code>{html.escape(command)}</code></pre>
      </article>"""
            )
    rendered = "\n".join(cards) or "      <p>No repository snapshots exist.</p>"
    content = f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{html.escape(project)} · Repository snapshots</title>
    <link rel="stylesheet" href="../style.css">
  </head>
  <body>
    <header class="shell">
      <p class="eyebrow">Dated repository snapshots</p>
      <h1>Install a dated repository state.</h1>
      <p class="lede">Snapshot metadata reuses the original GitHub Release RPM assets.</p>
    </header>
    <main class="shell"><section class="grid" aria-label="Repository snapshots">
{rendered}
    </section></main>
  </body>
</html>
"""
    write_text(snapshots_root / "index.html", content)


def dated_directories(root: Path) -> dict[date, Path]:
    if not root.exists():
        return {}
    directories: dict[date, Path] = {}
    for directory in root.iterdir():
        if not directory.is_dir() or directory.name.startswith("."):
            continue
        try:
            parsed = date.fromisoformat(directory.name)
        except ValueError as error:
            raise SnapshotError(f"Invalid snapshot directory: {directory}") from error
        if parsed.isoformat() != directory.name:
            raise SnapshotError(f"Invalid snapshot directory: {directory}")
        directories[parsed] = directory
    return directories


def apply_retention(
    repo_root: Path,
    state_root: Path,
    current_date: date,
    retention_days: int,
) -> list[str]:
    if retention_days < 1:
        raise SnapshotError("Snapshot retention days must be positive")
    repo_snapshots = dated_directories(repo_root / "snapshots")
    state_snapshots = dated_directories(state_root / "snapshots")
    if repo_snapshots.keys() != state_snapshots.keys():
        raise SnapshotError("Repository and state snapshot dates do not match")
    cutoff = current_date - timedelta(days=retention_days - 1)
    expired = sorted(snapshot for snapshot in repo_snapshots if snapshot < cutoff)
    for snapshot in expired:
        shutil.rmtree(repo_snapshots[snapshot])
        shutil.rmtree(state_snapshots[snapshot])
    return [snapshot.isoformat() for snapshot in expired]


def create_snapshot(
    repo_root: Path,
    state_root: Path,
    snapshot_date: str,
    owner: str,
    project: str,
    retention_days: int = 7,
) -> None:
    try:
        parsed_date = date.fromisoformat(snapshot_date)
    except ValueError as error:
        raise SnapshotError("Snapshot date must use YYYY-MM-DD format") from error
    destination = repo_root / "snapshots" / snapshot_date
    snapshot_state = state_root / "snapshots" / snapshot_date
    descriptor_path = snapshot_state / "snapshot.json"
    manifest = source_manifest(repo_root, state_root)
    descriptor = {"date": snapshot_date, "repositories": manifest, "schema": 1}
    if descriptor_path.is_file():
        existing = json.loads(descriptor_path.read_text(encoding="utf-8"))
        if existing == descriptor and destination.is_dir():
            apply_retention(repo_root, state_root, parsed_date, retention_days)
            render_index(repo_root, owner, project)
            return

    destination.parent.mkdir(parents=True, exist_ok=True)
    snapshot_state.parent.mkdir(parents=True, exist_ok=True)
    with (
        tempfile.TemporaryDirectory(
            prefix=f".{snapshot_date}-", dir=destination.parent
        ) as temporary_repo,
        tempfile.TemporaryDirectory(
            prefix=f".{snapshot_date}-", dir=snapshot_state.parent
        ) as temporary_state,
    ):
        staged_destination = Path(temporary_repo)
        staged_state = Path(temporary_state)
        for repository, profile, _releasever in repository_sources(
            repo_root, state_root
        ):
            for name in (repository, f"{repository}-debuginfo"):
                shutil.copytree(repo_root / name, staged_destination / name)
                for config in (staged_destination / name).glob("*.repo"):
                    config.unlink()
            config_name = f"{project}-{profile}-snapshot-{snapshot_date}.repo"
            write_text(
                staged_destination / repository / config_name,
                repository_config(owner, project, profile, snapshot_date),
            )
            inventory = read_tsv(state_root / repository / "inventory.tsv", 5)
            write_tsv(staged_state / repository / "inventory.tsv", inventory)
            write_tsv(staged_state / repository / "retired.tsv", ())

        write_text(
            staged_state / "snapshot.json",
            json.dumps(descriptor, indent=2, sort_keys=True) + "\n",
        )
        if destination.exists():
            shutil.rmtree(destination)
        if snapshot_state.exists():
            shutil.rmtree(snapshot_state)
        staged_destination.rename(destination)
        staged_state.rename(snapshot_state)
    apply_retention(repo_root, state_root, parsed_date, retention_days)
    render_index(repo_root, owner, project)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True)
    parser.add_argument("--owner", required=True)
    parser.add_argument("--project", required=True)
    parser.add_argument("--retention-days", type=int, default=7)
    parser.add_argument("--repo", type=Path, default=Path("repo"))
    parser.add_argument("--state", type=Path, default=Path("state"))
    arguments = parser.parse_args(argv)
    create_snapshot(
        arguments.repo,
        arguments.state,
        arguments.date,
        arguments.owner,
        arguments.project,
        arguments.retention_days,
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, SnapshotError, json.JSONDecodeError) as error:
        raise SystemExit(f"error: {error}") from error
