from __future__ import annotations
from .config import repositories, rules, report_settings

VALID_WEIGHTS = {"critical", "high", "medium", "low"}
VALID_LIFECYCLES = {"active", "transitional", "dormant", "archived"}

def validate() -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    for index, item in enumerate(repositories()):
        prefix = f"repositories[{index}]"
        repo = item.get("repo", "")
        if "/" not in repo:
            errors.append(f"{prefix}.repo must be owner/name")
        if repo in seen:
            errors.append(f"duplicate repository: {repo}")
        seen.add(repo)
        if item.get("reporting_weight") not in VALID_WEIGHTS:
            errors.append(f"{prefix}.reporting_weight is invalid")
        if item.get("lifecycle") not in VALID_LIFECYCLES:
            errors.append(f"{prefix}.lifecycle is invalid")
    cfg = rules()
    thresholds = cfg.get("thresholds", {})
    if not all(k in thresholds for k in ("critical", "high", "medium", "low")):
        errors.append("all significance thresholds are required")
    report_settings()
    return errors
