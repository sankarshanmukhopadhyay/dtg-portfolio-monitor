#!/usr/bin/env python3
"""Prune generated daily evidence outside the configured calendar-month window.

The monitor preserves recent reproducible snapshots in Git while preventing the
repository from becoming an unbounded data warehouse. Weekly reports remain as
longer-lived summaries; source GitHub URLs remain the external evidence of record.
"""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import re
import sys

# GitHub Actions invokes this file directly (`python scripts/prune_evidence.py`).
# In that mode Python places `scripts/` rather than the repository root on
# sys.path. Bootstrap the repository root explicitly so local package imports
# behave the same way as `python -m ...` invocations.
REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from dtg_monitor.config import ROOT, report_settings

DATE_PATH = re.compile(r"^(\d{4})/(\d{2})/(\d{2})\.json$")


def month_index(year: int, month: int) -> int:
    return year * 12 + month


def prune_tree(root: Path, retain_months: int, now: datetime) -> list[Path]:
    removed: list[Path] = []
    current = month_index(now.year, now.month)
    if not root.exists() or retain_months < 1:
        return removed
    for path in root.glob("????/??/??.json"):
        rel = path.relative_to(root).as_posix()
        match = DATE_PATH.match(rel)
        if not match:
            continue
        year, month, _day = map(int, match.groups())
        if current - month_index(year, month) >= retain_months:
            path.unlink()
            removed.append(path)
    for directory in sorted((p for p in root.glob("**/*") if p.is_dir()), reverse=True):
        try:
            directory.rmdir()
        except OSError:
            pass
    return removed


def main() -> int:
    settings = report_settings()
    retain_months = int(settings.get("evidence_snapshot_retention_months", 3))
    now = datetime.now(timezone.utc)
    removed: list[Path] = []
    for relative in ("data/events", "data/findings", "data/awareness"):
        removed.extend(prune_tree(ROOT / relative, retain_months, now))
    print(f"Pruned {len(removed)} generated evidence snapshot(s); retention={retain_months} calendar month(s).")
    for path in removed:
        print(path.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
