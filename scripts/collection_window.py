#!/usr/bin/env python3
"""Choose a bounded collection window that covers unpublished monitor history.

Only snapshots merged into the source checkout establish publication continuity.
Generated PRs, workflow success and local transient data cannot advance it.
"""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


def required_lookback(
    findings_dir: Path, today: date, requested_days: int = 7, max_days: int = 45
) -> tuple[int, date | None]:
    if requested_days < 1 or max_days < requested_days:
        raise ValueError("lookback limits must be positive and max >= requested")
    published: list[date] = []
    for path in findings_dir.glob("*/*/*.json"):
        relative = path.relative_to(findings_dir)
        try:
            candidate = date(int(relative.parts[0]), int(relative.parts[1]), int(path.stem))
        except (ValueError, IndexError):
            continue
        if candidate <= today:
            published.append(candidate)
    latest = max(published, default=None)
    # Overlap one extra day to include time-of-day boundaries and delayed updates.
    needed = max(requested_days, (today - latest).days + 1) if latest else requested_days
    if needed > max_days:
        raise ValueError(
            f"Unpublished collection gap requires {needed} days, exceeding the "
            f"{max_days}-day safety cap. Preserve the gap and plan a deliberate replay."
        )
    return needed, latest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--findings-dir", type=Path, default=Path("data/findings"))
    parser.add_argument("--requested-days", type=int, default=7)
    parser.add_argument("--max-days", type=int, default=45)
    parser.add_argument("--github-output", type=Path)
    args = parser.parse_args()

    window, latest = required_lookback(
        args.findings_dir, date.today(), args.requested_days, args.max_days
    )
    print(
        f"Collector window: {window} day(s); last published snapshot: "
        f"{latest.isoformat() if latest else 'none'}"
    )
    if args.github_output:
        with args.github_output.open("a", encoding="utf-8") as out:
            out.write(f"lookback_days={window}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
