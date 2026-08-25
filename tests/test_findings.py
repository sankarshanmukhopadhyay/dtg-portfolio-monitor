import unittest
from dtg_monitor.findings import build_findings


class FindingsTests(unittest.TestCase):
    def test_empty_repository_is_informational(self):
        events = [{
            "repository": "example/empty",
            "event_type": "repository_snapshot",
            "is_empty": True,
            "pushed_at": None,
            "url": "https://github.com/example/empty",
        }]
        findings = build_findings(events, [])
        self.assertEqual("empty_repository", findings[0]["kind"])
        self.assertEqual("informational", findings[0]["severity"])
        self.assertEqual("informational", findings[0]["urgency"])
        self.assertEqual("open", findings[0]["state"])
        self.assertTrue(findings[0]["fingerprint"])

    def test_collection_warning_becomes_action_required_finding(self):
        warnings = [{
            "repository": "example/repo",
            "stream": "issues",
            "message": "API unavailable",
            "url": "https://github.com/example/repo",
        }]
        findings = build_findings([], warnings)
        finding = findings[0]
        self.assertEqual("collection_warning", finding["kind"])
        self.assertEqual("urgent", finding["urgency"])
        self.assertEqual("unknown", finding["assurance_impact"])
        self.assertEqual("action-required", finding["review_status"])

    def test_consolidated_change_produces_one_finding_with_all_evidence(self):
        events = [{
            "repository": "example/repo",
            "event_type": "pull_request",
            "event_id": "pr-7",
            "change_unit_key": "unit-1",
            "title": "feat!: change authority contract",
            "body": "Breaking authority permission change",
            "url": "https://github.com/example/repo/pull/7",
            "significance": "critical",
            "significance_reasons": ["authority-semantics", "normative-language"],
            "linked_repositories": ["example/spec"],
            "correlated_events": [{
                "event_type": "commit",
                "item_id": "abc",
                "url": "https://github.com/example/repo/commit/abc",
            }],
        }]
        findings = build_findings(events, [])
        self.assertEqual(1, len(findings))
        finding = findings[0]
        self.assertEqual("material_cross_reference", finding["kind"])
        self.assertEqual("high", finding["materiality"])
        self.assertEqual("elevated", finding["urgency"])
        self.assertEqual("potentially-breaking", finding["assurance_impact"])
        self.assertEqual(2, len(finding["evidence_urls"]))


if __name__ == "__main__":
    unittest.main()
