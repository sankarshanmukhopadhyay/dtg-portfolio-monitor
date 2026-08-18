import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch
from dtg_monitor.report import _clean, _event_table, _prune_daily_reports

class ReportTests(unittest.TestCase):
    def test_markdown_table_escaping(self):
        self.assertEqual("a \\| b", _clean("a | b"))

    def test_event_register_is_dependency_free_and_date_then_repo(self):
        events = [
            {"repository": "z/repo", "updated_at": "2026-08-18T10:00:00Z", "significance": "low", "significance_score": 1, "event_type": "commit", "state": "committed", "title": "z", "url": "https://example.test/z", "significance_reasons": []},
            {"repository": "a/repo", "updated_at": "2026-08-18T11:00:00Z", "significance": "high", "significance_score": 60, "event_type": "release", "state": "published", "title": "a", "url": "https://example.test/a", "significance_reasons": []},
            {"repository": "m/repo", "updated_at": "2026-08-17T11:00:00Z", "significance": "medium", "significance_score": 30, "event_type": "issue", "state": "open", "title": "m", "url": "https://example.test/m", "significance_reasons": []},
        ]
        html = "\n".join(_event_table(events))
        self.assertNotIn("portfolio-table.js", html)
        self.assertLess(html.index("a/repo"), html.index("z/repo"))
        self.assertLess(html.index("z/repo"), html.index("m/repo"))

    def test_daily_report_retention_keeps_current_and_previous_month(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            daily = root / "reports" / "daily"
            daily.mkdir(parents=True)
            old = daily / "2026-06-30.md"
            previous = daily / "2026-07-01.md"
            current = daily / "2026-08-01.md"
            for item in (old, previous, current):
                item.write_text("x")
            with patch("dtg_monitor.report.ROOT", root):
                removed = _prune_daily_reports(datetime(2026, 8, 19, tzinfo=timezone.utc), 2)
            self.assertEqual([old], removed)
            self.assertTrue(previous.exists())
            self.assertTrue(current.exists())

if __name__ == "__main__":
    unittest.main()

from dtg_monitor.report import _is_breaking, _signal_tags, _threshold_legend

class ReportPresentationTests(unittest.TestCase):
    def test_breaking_change_marker_is_detected(self):
        self.assertTrue(_is_breaking({"title": "feat(acl)!: replace legacy grants"}))
        self.assertFalse(_is_breaking({"title": "feat(acl): add grant support"}))

    def test_signal_reasons_are_compacted_to_tags(self):
        event = {"significance_reasons": ["Normative requirement language changed", "Security, privacy, threat, or vulnerability relevance"]}
        self.assertEqual(["NORM", "SEC"], _signal_tags(event))

    def test_threshold_legend_uses_configured_bands(self):
        self.assertEqual("Critical 80+ · High 55–79 · Medium 25–54 · Low <25", _threshold_legend())
