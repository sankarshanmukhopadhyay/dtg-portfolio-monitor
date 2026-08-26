import unittest
from unittest.mock import patch

from dtg_monitor.discovery import discover, evaluate_candidate, merge_effective, render_repository_page


POLICY = {
    "public_only": True,
    "exclude_archived": True,
    "exclude_forks": True,
    "exclude_repositories": ["example/dtg-monitor"],
    "allow_forks": ["example/dtg-allowed-fork"],
    "default_monitor": {"commits": True, "pull_requests": True, "issues": True, "releases": True, "discussions": False},
    "default_material_paths": ["README.md", "docs/**"],
}
SOURCE = {
    "owner": "example",
    "prefixes": ["dtg-"],
    "organisation": "independent",
    "default_role": "assurance-or-implementation-profile",
    "default_weight": "high",
}


class FakeClient:
    def paged(self, path, params):
        self.path = path
        return [
            {"name": "dtg-alpha", "full_name": "example/dtg-alpha", "private": False, "archived": False, "fork": False, "default_branch": "main"},
            {"name": "dtg-fork", "full_name": "example/dtg-fork", "private": False, "archived": False, "fork": True, "default_branch": "main"},
            {"name": "other", "full_name": "example/other", "private": False, "archived": False, "fork": False, "default_branch": "main"},
        ]


class RepositoryDiscoveryTests(unittest.TestCase):
    def test_policy_rejects_forks_and_explicit_exclusions(self):
        fork = {"name": "dtg-fork", "full_name": "example/dtg-fork", "private": False, "archived": False, "fork": True}
        excluded = {"name": "dtg-monitor", "full_name": "example/dtg-monitor", "private": False, "archived": False, "fork": False}
        self.assertEqual(evaluate_candidate(fork, SOURCE, POLICY), (False, "fork-not-allowlisted"))
        self.assertEqual(evaluate_candidate(excluded, SOURCE, POLICY), (False, "explicitly-excluded"))

    def test_allowlisted_fork_is_admitted(self):
        repo = {"name": "dtg-allowed-fork", "full_name": "example/dtg-allowed-fork", "private": False, "archived": False, "fork": True}
        self.assertEqual(evaluate_candidate(repo, SOURCE, POLICY), (True, "policy-match"))

    def test_curated_metadata_overrides_discovered_defaults(self):
        discovered = [{"repo": "example/dtg-alpha", "role": "discovered", "reporting_weight": "medium"}]
        curated = [{"repo": "example/dtg-alpha", "role": "normative", "reporting_weight": "critical"}]
        effective = merge_effective(curated, discovered)
        self.assertEqual(effective[0]["role"], "normative")
        self.assertEqual(effective[0]["reporting_weight"], "critical")

    @patch("dtg_monitor.discovery.discovery_config")
    def test_discovery_emits_admission_and_rejection_evidence(self, config_mock):
        config_mock.return_value = {"policy": POLICY, "sources": [SOURCE]}
        snapshot = discover(FakeClient())
        self.assertEqual([item["repo"] for item in snapshot["admitted"]], ["example/dtg-alpha"])
        decisions = {item["repository"]: item for item in snapshot["decisions"]}
        self.assertTrue(decisions["example/dtg-alpha"]["admitted"])
        self.assertEqual(decisions["example/dtg-fork"]["reason"], "fork-not-allowlisted")
        self.assertNotIn("example/other", decisions)

    def test_repository_page_exposes_admission_source(self):
        effective = [
            {"repo": "example/curated", "workstream": "core", "role": "normative", "lifecycle": "active", "reporting_weight": "critical"},
            {"repo": "example/dtg-alpha", "workstream": "alpha", "role": "discovered", "lifecycle": "active", "reporting_weight": "high", "discovery": {"admission": "automatic"}},
        ]
        snapshot = {"generated_at": "2026-08-26T00:00:00Z", "policy": "config/repository-discovery.yaml", "admitted": [{}], "decisions": []}
        page = render_repository_page(effective, snapshot)
        self.assertIn("| curated |", page)
        self.assertIn("| dynamic |", page)
        self.assertIn("data/repository-discovery.json", page)


if __name__ == "__main__":
    unittest.main()
