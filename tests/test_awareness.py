import unittest

from dtg_monitor.awareness import analyse
from dtg_monitor.config import portfolio_model, repositories


def event(repo, significance="high", title="credential proof protocol", updated_at="2026-08-11T00:00:00Z"):
    return {
        "repository": repo,
        "event_type": "pull_request",
        "title": title,
        "body": "",
        "url": f"https://example.test/{repo}",
        "updated_at": updated_at,
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
        assertions = [a for a in snapshot["assertions"] if a["kind"] == "cross-capability-convergence"]
        self.assertTrue(assertions)
        self.assertTrue(assertions[0]["assertion_id"].startswith("DTG-A-"))

    def test_specification_and_implementation_alignment(self):
        events = [
            event("trustoverip/dtgwg-cred-spec"),
            event("OpenVTC/dtg-credentials"),
        ]
        snapshot = analyse(events, generated_at="2026-08-11T00:00:00Z")
        states = {item["capability"]: item["state"] for item in snapshot["implementation_alignment"]}
        self.assertEqual("moving-together", states["credentials-and-evidence"])
        assertion = next(a for a in snapshot["assertions"] if a["subject"] == "credentials-and-evidence")
        self.assertEqual("watch", assertion["review_class"])

    def test_implementation_ahead_is_review_required_assertion(self):
        events = [event("OpenVTC/dtg-credentials") for _ in range(3)]
        snapshot = analyse(events, generated_at="2026-08-11T00:00:00Z")
        assertions = [a for a in snapshot["assertions"] if a["kind"] == "specification-implementation-alignment"]
        self.assertTrue(any(a["state"] == "implementation-ahead" and a["review_class"] == "review-required" for a in assertions))
        self.assertGreaterEqual(snapshot["decision_queue"]["review_assertions"], 1)

    def test_provenance_is_persisted(self):
        snapshot = analyse(
            [event("OpenVTC/dtg-credentials")],
            generated_at="2026-08-11T00:00:00Z",
            provenance={"source_revision": "abc123", "collection_run_id": "42", "repository": "owner/repo"},
        )
        self.assertEqual("abc123", snapshot["observation"]["source_revision"])
        self.assertEqual("42", snapshot["observation"]["collection_run_id"])
        self.assertEqual("2026-08-11T00:00:00Z", snapshot["observation"]["evidence_through"])

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
