import unittest

from dtg_monitor.awareness import analyse
from dtg_monitor.config import portfolio_model, repositories


def event(repo, significance="high", title="credential proof protocol"):
    return {
        "repository": repo,
        "event_type": "pull_request",
        "title": title,
        "body": "",
        "url": f"https://example.test/{repo}",
        "significance": significance,
    }


class AwarenessTests(unittest.TestCase):
    def test_capability_pulse_aggregates_repositories(self):
        events = [event("trustoverip/dtgwg-cred-spec") for _ in range(3)]
        snapshot = analyse(events, generated_at="2026-08-11T00:00:00Z")
        state = snapshot["capabilities"]["credentials-and-evidence"]
        self.assertEqual("advancing", state["pulse"])
        self.assertEqual(3, state["material_change_units"])

    def test_related_material_activity_produces_convergence(self):
        events = [
            event("trustoverip/dtgwg-cred-spec", title="credential proof protocol"),
            event("trustoverip/dtgwg-trust-tasks-tf", title="credential proof protocol binding"),
        ]
        snapshot = analyse(events, generated_at="2026-08-11T00:00:00Z")
        pairs = {(item["from"], item["to"]) for item in snapshot["convergences"]}
        self.assertIn(("credentials-and-evidence", "governed-action"), pairs)

    def test_specification_and_implementation_alignment(self):
        events = [
            event("trustoverip/dtgwg-cred-spec"),
            event("OpenVTC/dtg-credentials"),
        ]
        snapshot = analyse(events, generated_at="2026-08-11T00:00:00Z")
        states = {item["capability"]: item["state"] for item in snapshot["implementation_alignment"]}
        self.assertEqual("moving-together", states["credentials-and-evidence"])

    def test_quiet_is_not_treated_as_failure(self):
        snapshot = analyse([], generated_at="2026-08-11T00:00:00Z")
        self.assertTrue(all(item["pulse"] == "quiet" for item in snapshot["capabilities"].values()))
        self.assertEqual([], snapshot["attention_signals"])

    def test_all_configured_repositories_map_to_a_capability(self):
        model = portfolio_model()
        stream_to_cap = {
            stream: capability["id"]
            for capability in model["capabilities"]
            for stream in capability["workstreams"]
        }
        self.assertTrue(all(item["workstream"] in stream_to_cap for item in repositories()))


if __name__ == "__main__":
    unittest.main()
