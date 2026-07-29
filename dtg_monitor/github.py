from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, timezone
import json
import os
import time
from typing import Any
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from urllib.error import HTTPError

API_ROOT = "https://api.github.com"

@dataclass
class GitHubClient:
    token: str | None = None
    max_retries: int = 3

    @classmethod
    def from_environment(cls) -> "GitHubClient":
        return cls(token=os.getenv("GITHUB_TOKEN") or os.getenv("GH_TOKEN"))

    def get(self, path: str, params: dict[str, Any] | None = None) -> Any:
        query = f"?{urlencode(params)}" if params else ""
        url = f"{API_ROOT}{path}{query}"
        headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": "dtg-portfolio-monitor/0.1.0",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        for attempt in range(self.max_retries):
            request = Request(url, headers=headers)
            try:
                with urlopen(request, timeout=30) as response:
                    return json.loads(response.read().decode("utf-8"))
            except HTTPError as exc:
                if exc.code in {403, 429, 500, 502, 503, 504} and attempt + 1 < self.max_retries:
                    retry_after = int(exc.headers.get("Retry-After", "2"))
                    time.sleep(max(retry_after, 2 ** attempt))
                    continue
                body = exc.read().decode("utf-8", errors="replace")
                raise RuntimeError(f"GitHub API {exc.code} for {url}: {body[:500]}") from exc
        raise RuntimeError(f"GitHub API request failed after retries: {url}")

    def paged(self, path: str, params: dict[str, Any] | None = None, max_pages: int = 10) -> list[Any]:
        params = dict(params or {})
        params["per_page"] = 100
        output: list[Any] = []
        for page in range(1, max_pages + 1):
            params["page"] = page
            batch = self.get(path, params)
            if not isinstance(batch, list):
                raise RuntimeError(f"Expected list from {path}")
            output.extend(batch)
            if len(batch) < 100:
                break
        return output

def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
