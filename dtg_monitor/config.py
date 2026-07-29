from __future__ import annotations
from pathlib import Path
from typing import Any
import yaml

ROOT = Path(__file__).resolve().parents[1]

def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a YAML mapping")
    return data

def repositories() -> list[dict[str, Any]]:
    data = load_yaml(ROOT / "config" / "repositories.yaml")
    repos = data.get("repositories")
    if not isinstance(repos, list):
        raise ValueError("repositories must be a list")
    return repos

def rules() -> dict[str, Any]:
    return load_yaml(ROOT / "config" / "significance-rules.yaml")

def report_settings() -> dict[str, Any]:
    return load_yaml(ROOT / "config" / "report-settings.yaml")
