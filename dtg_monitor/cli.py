from __future__ import annotations
import argparse
import sys
from .collect import collect
from .report import generate
from .validate import validate

def main() -> int:
    parser = argparse.ArgumentParser(prog="dtg-monitor")
    sub = parser.add_subparsers(dest="command", required=True)

    collect_parser = sub.add_parser("collect")
    collect_parser.add_argument("--lookback-days", type=int, default=7)

    report_parser = sub.add_parser("report")
    report_parser.add_argument("--period", choices=["daily", "weekly"], default="daily")

    sub.add_parser("validate")
    args = parser.parse_args()

    if args.command == "collect":
        events = collect(lookback_days=args.lookback_days)
        print(f"Collected {len(events)} events")
    elif args.command == "report":
        path = generate(period=args.period)
        print(path)
    else:
        errors = validate()
        if errors:
            for error in errors:
                print(f"ERROR: {error}", file=sys.stderr)
            return 1
        print("Configuration valid")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
