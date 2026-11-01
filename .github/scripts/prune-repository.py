#!/usr/bin/env python3

import argparse
import csv
import os
import tempfile
from collections.abc import Iterable, Sequence
from datetime import UTC, datetime, timedelta
from pathlib import Path

Row = tuple[str, ...]


class PruneError(RuntimeError):
    pass


def read_tsv(path: Path, columns: int) -> list[Row]:
    if not path.exists():
        return []
    rows: list[Row] = []
    with path.open(encoding="utf-8", newline="") as stream:
        for line_number, row in enumerate(csv.reader(stream, dialect="excel-tab"), 1):
            if not row or row == [""]:
                continue
            if len(row) != columns:
                raise PruneError(
                    f"{path}:{line_number}: expected {columns} fields, found {len(row)}"
                )
            rows.append(tuple(row))
    return rows


def write_tsv(path: Path, rows: Iterable[Sequence[str]]) -> None:
    normalized = sorted({tuple(row) for row in rows})
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        newline="",
        dir=path.parent,
        prefix=f".{path.name}.",
        delete=False,
    ) as stream:
        temporary = Path(stream.name)
        writer = csv.writer(stream, dialect="excel-tab", lineterminator="\n")
        writer.writerows(normalized)
    temporary.replace(path)


def parse_timestamp(value: str) -> datetime:
    try:
        timestamp = datetime.fromisoformat(value)
    except ValueError as error:
        raise PruneError(f"Invalid retirement timestamp: {value!r}") from error
    if timestamp.tzinfo is None:
        raise PruneError(f"Retirement timestamp lacks timezone: {value!r}")
    return timestamp.astimezone(UTC)


def timestamp_text(timestamp: datetime) -> str:
    return timestamp.astimezone(UTC).isoformat().replace("+00:00", "Z")


def repository_state_directories(state_root: Path) -> list[Path]:
    return sorted(
        inventory.parent
        for inventory in state_root.rglob("inventory.tsv")
        if "pruning" not in inventory.relative_to(state_root).parts
    )


def current_state(state_root: Path) -> tuple[set[Row], set[tuple[str, str]]]:
    retired: set[Row] = set()
    active_assets: set[tuple[str, str]] = set()
    for directory in repository_state_directories(state_root):
        retired.update(read_tsv(directory / "retired.tsv", 5))
        active_assets.update(
            (row[0], row[3]) for row in read_tsv(directory / "inventory.tsv", 5)
        )
    return retired, active_assets


def plan(
    state_root: Path,
    assets_path: Path,
    retention_days: int,
    now: datetime,
) -> int:
    if retention_days < 0:
        raise PruneError("Retention days cannot be negative")
    ledger_path = state_root / "pruning/retired-assets.tsv"
    recorded: dict[Row, str] = {}
    for row in read_tsv(ledger_path, 6):
        asset = row[:5]
        parse_timestamp(row[5])
        recorded[asset] = row[5]

    retired, active_assets = current_state(state_root)
    now_text = timestamp_text(now)
    ledger = [(*row, recorded.get(row, now_text)) for row in retired]
    write_tsv(ledger_path, ledger)

    cutoff = now.astimezone(UTC) - timedelta(days=retention_days)
    eligible = {
        (row[0], row[3])
        for row in retired
        if (row[0], row[3]) not in active_assets
        and parse_timestamp(recorded.get(row, now_text)) <= cutoff
    }
    write_tsv(assets_path, eligible)
    return len(eligible)


def compact(state_root: Path, assets_path: Path) -> int:
    deleted_assets = set(read_tsv(assets_path, 2))
    if not deleted_assets:
        return 0
    removed = 0
    for directory in repository_state_directories(state_root):
        retired_path = directory / "retired.tsv"
        retired = read_tsv(retired_path, 5)
        retained = [row for row in retired if (row[0], row[3]) not in deleted_assets]
        removed += len(retired) - len(retained)
        write_tsv(retired_path, retained)

    ledger_path = state_root / "pruning/retired-assets.tsv"
    ledger = read_tsv(ledger_path, 6)
    write_tsv(
        ledger_path,
        (row for row in ledger if (row[0], row[3]) not in deleted_assets),
    )
    return removed


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("stage", choices=("plan", "compact"))
    parser.add_argument("--state", type=Path, default=Path("state"))
    parser.add_argument("--assets", type=Path, default=Path("prune-assets.tsv"))
    parser.add_argument("--retention-days", type=int, default=1)
    arguments = parser.parse_args(argv)
    if not arguments.state.is_dir():
        raise PruneError(f"Repository state does not exist: {arguments.state}")
    if arguments.stage == "plan":
        configured_now = os.environ.get("PRUNE_NOW")
        now = parse_timestamp(configured_now) if configured_now else datetime.now(UTC)
        count = plan(
            arguments.state,
            arguments.assets,
            arguments.retention_days,
            now,
        )
        print(f"Planned {count} retired release assets for deletion")
    else:
        count = compact(arguments.state, arguments.assets)
        print(f"Removed {count} retired inventory records")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, PruneError) as error:
        raise SystemExit(f"error: {error}") from error
