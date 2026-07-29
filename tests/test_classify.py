import unittest
from dtg_monitor.classify import classify
from dtg_monitor.config import rules

class ClassificationTests(unittest.TestCase):
    def test_authority_and_interoperability_score(self):
        event = {
            "event_type": "pull_request",
            "title": "Define revocation authority and canonicalization",
            "body": "This changes protocol conformance.",
            "changed_files": ["specs/example/spec.md"],
        }
        level, score, reasons = classify(event, rules(), "critical")
        self.assertIn(level, {"critical", "high"})
        self.assertGreaterEqual(score, 55)
        self.assertTrue(reasons)

if __name__ == "__main__":
    unittest.main()
