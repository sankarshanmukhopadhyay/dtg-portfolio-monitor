from __future__ import annotations
from .config import repositories, rules, report_settings, portfolio_model, cross_spec_pressure_tests

VALID_WEIGHTS = {"critical", "high", "medium", "low"}
VALID_LIFECYCLES = {"active", "transitional", "dormant", "archived"}


def validate() -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    repo_items = repositories()
    for index, item in enumerate(repo_items):
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

    model = portfolio_model()
    capabilities = model.get("capabilities", [])
    if not isinstance(capabilities, list) or not capabilities:
        errors.append("portfolio-model capabilities must be a non-empty list")
        return errors
    capability_ids = {item.get("id") for item in capabilities if isinstance(item, dict)}
    if None in capability_ids or len(capability_ids) != len(capabilities):
        errors.append("portfolio-model capability ids must be present and unique")
    model_workstreams: set[str] = set()
    for item in capabilities:
        if not isinstance(item, dict):
            errors.append("portfolio-model capabilities must be mappings")
            continue
        streams = item.get("workstreams", [])
        if not isinstance(streams, list) or not streams:
            errors.append(f"capability {item.get('id', '<unknown>')} must declare workstreams")
            continue
        for stream in streams:
            if stream in model_workstreams:
                errors.append(f"workstream mapped to multiple capabilities: {stream}")
            model_workstreams.add(stream)
    configured_workstreams = {item.get("workstream") for item in repo_items}
    for stream in sorted(configured_workstreams - model_workstreams):
        errors.append(f"portfolio-model does not map workstream: {stream}")
    for relation in model.get("relationships", []):
        if relation.get("from") not in capability_ids or relation.get("to") not in capability_ids:
            errors.append("portfolio-model relationship references an unknown capability")

    known_repositories = {item["repo"] for item in repo_items}
    for link in model.get("implementation_links", []):
        if link.get("specification_repository") not in known_repositories:
            errors.append("portfolio-model implementation link references an unknown specification repository")
        for repo in link.get("implementation_repositories", []):
            if repo not in known_repositories:
                errors.append(f"portfolio-model implementation link references unknown repository: {repo}")
        if link.get("capability") not in capability_ids:
            errors.append("portfolio-model implementation link references an unknown capability")

    xsp = cross_spec_pressure_tests()
    xsp_ids: set[str] = set()
    for index, item in enumerate(xsp.get("compositions", [])):
        cid = item.get("id")
        if not cid or cid in xsp_ids:
            errors.append(f"cross-spec composition id must be present and unique at index {index}")
        xsp_ids.add(cid)
        repos = item.get("repositories", [])
        if not isinstance(repos, list) or len(repos) != 2:
            errors.append(f"cross-spec composition {cid} must reference exactly two repositories")
        for repo in repos:
            if repo not in known_repositories:
                errors.append(f"cross-spec composition {cid} references unknown repository: {repo}")
        if item.get("readiness") not in {"runnable", "candidate"}:
            errors.append(f"cross-spec composition {cid} has invalid readiness")
        if item.get("readiness") == "runnable":
            for field in ("issue_mode", "evidence_grade", "corpus_id", "assessment"):
                if not item.get(field):
                    errors.append(f"runnable cross-spec composition {cid} requires {field}")
    return errors
