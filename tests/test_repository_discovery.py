import subprocess
import sys
import unittest
from unittest.mock import patch

from dtg_monitor.discovery import discover, discovery_config, evaluate_candidate, merge_effective, render_repository_page


POLICY = {
    "public_only": True,
    "exclude_archived": True,
    "exclude_forks": True,
    "exclude_repositories": [],
    "allow_forks": [],
    "default_monitor": {"commits": True, "pull_requests": True, "issues": True, "releases": True, "discussions": False},
    "default_material_paths": ["README.md", "docs/**"],
}
SOURCE = {
    "owner": "trustoverip",
    "prefixes": ["dtgwg"],
    "organisation": "toip",
    "default_role": "discovered-dtg-workstream",
    "default_weight": "high",
}


class FakeClient:
    def paged(self, path, params):
        self.path = path
        return [
            {"name": "dtgwg-alpha", "full_name": "trustoverip/dtgwg-alpha", "private": False, "archived": False, "fork": False, "default_branch": "main"},
            {"name": "dtgwg-fork", "full_name": "trustoverip/dtgwg-fork", "private": False, "archived": False, "fork": True, "default_branch": "main"},
            {"name": "dtg-profile", "full_name": "trustoverip/dtg-profile", "private": False, "archived": False, "fork": False, "default_branch": "main"},
        ]


class RepositoryDiscoveryTests(unittest.TestCase):
    def test_repository_discovery_config_is_toip_only(self):
        cfg = discovery_config()
        self.assertEqual(len(cfg["sources"]), 1)
        self.assertEqual(cfg["sources"][0]["owner"], "trustoverip")
        self.assertEqual(cfg["sources"][0]["prefixes"], ["dtgwg"])

    def test_policy_rejects_forks(self):
        fork = {"name": "dtgwg-fork", "full_name": "trustoverip/dtgwg-fork", "private": False, "archived": False, "fork": True}
        self.assertEqual(evaluate_candidate(fork, SOURCE, POLICY), (False, "fork-not-allowlisted"))

    def test_non_dtgwg_name_is_not_admitted(self):
        repo = {"name": "dtg-profile", "full_name": "trustoverip/dtg-profile", "private": False, "archived": False, "fork": False}
        self.assertEqual(evaluate_candidate(repo, SOURCE, POLICY), (False, "name-prefix-mismatch"))

    def test_curated_metadata_overrides_discovered_defaults(self):
        discovered = [{"repo": "trustoverip/dtgwg-alpha", "role": "discovered", "reporting_weight": "medium"}]
        curated = [{"repo": "trustoverip/dtgwg-alpha", "role": "normative", "reporting_weight": "critical"}]
        effective = merge_effective(curated, discovered)
        self.assertEqual(effective[0]["role"], "normative")
        self.assertEqual(effective[0]["reporting_weight"], "critical")

    @patch("dtg_monitor.discovery.discovery_config")
    def test_discovery_emits_admission_and_rejection_evidence(self, config_mock):
        config_mock.return_value = {"policy": POLICY, "sources": [SOURCE]}
        snapshot = discover(FakeClient())
        self.assertEqual([item["repo"] for item in snapshot["admitted"]], ["trustoverip/dtgwg-alpha"])
        decisions = {item["repository"]: item for item in snapshot["decisions"]}
        self.assertTrue(decisions["trustoverip/dtgwg-alpha"]["admitted"])
        self.assertEqual(decisions["trustoverip/dtgwg-fork"]["reason"], "fork-not-allowlisted")
        self.assertNotIn("trustoverip/dtg-profile", decisions)

    def test_personal_dtg_repositories_are_not_discovery_sources(self):
        cfg = discovery_config()
        owners = {source["owner"] for source in cfg["sources"]}
        self.assertNotIn("sankarshanmukhopadhyay", owners)
        self.assertNotIn("OpenVTC", owners)

    def test_repository_page_exposes_admission_source(self):
        effective = [
            {"repo": "OpenVTC/openvtc", "workstream": "community-platform", "role": "implementation", "lifecycle": "active", "reporting_weight": "high"},
            {"repo": "trustoverip/dtgwg-alpha", "workstream": "alpha", "role": "discovered", "lifecycle": "active", "reporting_weight": "high", "discovery": {"admission": "automatic"}},
        ]
        snapshot = {"generated_at": "2026-08-26T00:00:00Z", "policy": "config/repository-discovery.yaml", "admitted": [{}], "decisions": []}
        page = render_repository_page(effective, snapshot)
        self.assertIn("| curated |", page)
        self.assertIn("| dynamic |", page)
        self.assertIn("data/repository-discovery.json", page)

    def test_discovery_script_is_importable_as_direct_entrypoint(self):
        result = subprocess.run(
            [sys.executable, "-c", "import runpy; runpy.run_path('scripts/discover_repositories.py', run_name='not_main')"],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
