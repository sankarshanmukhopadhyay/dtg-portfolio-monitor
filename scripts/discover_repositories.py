from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from dtg_monitor.discovery import run
from dtg_monitor.github import GitHubClient


if __name__ == "__main__":
    snapshot = run(GitHubClient.from_environment())
    admitted = sum(1 for item in snapshot["decisions"] if item["admitted"])
    rejected = len(snapshot["decisions"]) - admitted
    print(f"Repository discovery complete: {admitted} admitted, {rejected} rejected")
