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
TOIP_SOURCE = {
    "owner": "trustoverip",
    "prefixes": ["dtgwg"],
    "organisation": "toip",
    "default_role": "discovered-dtg-workstream",
    "default_weight": "high",
}
OPENVTC_SOURCE = {
    "owner": "OpenVTC",
    "match_all": True,
    "organisation": "openvtc",
    "default_role": "discovered-openvtc-repository",
    "default_weight": "high",
}


class FakeClient:
    def paged(self, path, params):
        if path == "/users/trustoverip/repos":
            return [
                {"name": "dtgwg-alpha", "full_name": "trustoverip/dtgwg-alpha", "private": False, "archived": False, "fork": False, "default_branch": "main"},
                {"name": "dtgwg-fork", "full_name": "trustoverip/dtgwg-fork", "private": False, "archived": False, "fork": True, "default_branch": "main"},
                {"name": "dtg-profile", "full_name": "trustoverip/dtg-profile", "private": False, "archived": False, "fork": False, "default_branch": "main"},
            ]
        if path == "/users/OpenVTC/repos":
            return [
                {"name": "openvtc", "full_name": "OpenVTC/openvtc", "private": False, "archived": False, "fork": False, "default_branch": "main"},
                {"name": "vti-setup", "full_name": "OpenVTC/vti-setup", "private": False, "archived": False, "fork": False, "default_branch": "main"},
                {"name": "archived", "full_name": "OpenVTC/archived", "private": False, "archived": True, "fork": False, "default_branch": "main"},
            ]
        return []


class RepositoryDiscoveryTests(unittest.TestCase):
    def test_repository_discovery_config_has_only_trusted_organizations(self):
        cfg = discovery_config()
        owners = {source["owner"] for source in cfg["sources"]}
        self.assertEqual(owners, {"trustoverip", "OpenVTC"})
        self.assertNotIn("sankarshanmukhopadhyay", owners)

    def test_toip_source_is_namespace_bounded(self):
        cfg = discovery_config()
        source = next(item for item in cfg["sources"] if item["owner"] == "trustoverip")
        self.assertEqual(source["prefixes"], ["dtgwg"])
        self.assertFalse(source.get("match_all", False))

    def test_openvtc_source_is_organization_wide(self):
        cfg = discovery_config()
        source = next(item for item in cfg["sources"] if item["owner"] == "OpenVTC")
        self.assertTrue(source["match_all"])

    def test_policy_rejects_forks(self):
        fork = {"name": "dtgwg-fork", "full_name": "trustoverip/dtgwg-fork", "private": False, "archived": False, "fork": True}
        self.assertEqual(evaluate_candidate(fork, TOIP_SOURCE, POLICY), (False, "fork-not-allowlisted"))

    def test_non_dtgwg_toip_name_is_not_admitted(self):
        repo = {"name": "dtg-profile", "full_name": "trustoverip/dtg-profile", "private": False, "archived": False, "fork": False}
        self.assertEqual(evaluate_candidate(repo, TOIP_SOURCE, POLICY), (False, "source-rule-mismatch"))

    def test_openvtc_any_public_non_archived_name_is_admitted(self):
        repo = {"name": "vti-setup", "full_name": "OpenVTC/vti-setup", "private": False, "archived": False, "fork": False}
        self.assertEqual(evaluate_candidate(repo, OPENVTC_SOURCE, POLICY), (True, "policy-match"))

    def test_openvtc_archived_repo_is_rejected(self):
        repo = {"name": "archived", "full_name": "OpenVTC/archived", "private": False, "archived": True, "fork": False}
        self.assertEqual(evaluate_candidate(repo, OPENVTC_SOURCE, POLICY), (False, "archived-repository"))

    def test_curated_metadata_overrides_discovered_defaults(self):
        discovered = [{"repo": "OpenVTC/openvtc", "role": "discovered", "reporting_weight": "medium"}]
        curated = [{"repo": "OpenVTC/openvtc", "role": "implementation", "reporting_weight": "high"}]
        effective = merge_effective(curated, discovered)
        self.assertEqual(effective[0]["role"], "implementation")
        self.assertEqual(effective[0]["reporting_weight"], "high")

    @patch("dtg_monitor.discovery.discovery_config")
    def test_discovery_covers_toip_and_openvtc_with_evidence(self, config_mock):
        config_mock.return_value = {"policy": POLICY, "sources": [TOIP_SOURCE, OPENVTC_SOURCE]}
        snapshot = discover(FakeClient())
        admitted = {item["repo"] for item in snapshot["admitted"]}
        self.assertEqual(admitted, {"trustoverip/dtgwg-alpha", "OpenVTC/openvtc", "OpenVTC/vti-setup"})
        decisions = {item["repository"]: item for item in snapshot["decisions"]}
        self.assertEqual(decisions["trustoverip/dtgwg-fork"]["reason"], "fork-not-allowlisted")
        self.assertEqual(decisions["OpenVTC/archived"]["reason"], "archived-repository")
        self.assertNotIn("trustoverip/dtg-profile", decisions)

    def test_repository_page_exposes_admission_source(self):
        effective = [
            {"repo": "OpenVTC/openvtc", "workstream": "community-platform", "role": "implementation", "lifecycle": "active", "reporting_weight": "high"},
            {"repo": "OpenVTC/vti-setup", "workstream": "vti-setup", "role": "discovered-openvtc-repository", "lifecycle": "active", "reporting_weight": "high", "discovery": {"admission": "automatic"}},
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
