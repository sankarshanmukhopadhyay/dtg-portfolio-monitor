import tempfile
import unittest
from dtg_monitor.report import _clean

class ReportTests(unittest.TestCase):
    def test_markdown_table_escaping(self):
        self.assertEqual("a \\| b", _clean("a | b"))

if __name__ == "__main__":
    unittest.main()
