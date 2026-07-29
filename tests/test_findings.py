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

    def test_collection_warning_becomes_finding(self):
        warnings = [{
            "repository": "example/repo",
            "stream": "issues",
            "message": "API unavailable",
            "url": "https://github.com/example/repo",
        }]
        findings = build_findings([], warnings)
        self.assertEqual("collection_warning", findings[0]["kind"])

if __name__ == "__main__":
    unittest.main()
