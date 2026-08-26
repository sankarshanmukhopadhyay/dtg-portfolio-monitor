from dtg_monitor.discovery import run
from dtg_monitor.github import GitHubClient


if __name__ == "__main__":
    snapshot = run(GitHubClient.from_environment())
    admitted = sum(1 for item in snapshot["decisions"] if item["admitted"])
    rejected = len(snapshot["decisions"]) - admitted
    print(f"Repository discovery complete: {admitted} admitted, {rejected} rejected")
