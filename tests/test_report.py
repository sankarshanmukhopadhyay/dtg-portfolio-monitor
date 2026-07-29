import tempfile
import unittest
from dtg_monitor.report import _clean

class ReportTests(unittest.TestCase):
    def test_markdown_table_escaping(self):
        self.assertEqual("a \\| b", _clean("a | b"))

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
