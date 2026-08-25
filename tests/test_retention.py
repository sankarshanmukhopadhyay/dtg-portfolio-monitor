import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

from scripts.prune_evidence import prune_tree


class RetentionTests(unittest.TestCase):
    def test_prunes_snapshots_older_than_calendar_window(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            old = root / "2026/04/30.json"
            recent = root / "2026/07/31.json"
            current = root / "2026/08/25.json"
            for path in (old, recent, current):
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("{}\n", encoding="utf-8")

            removed = prune_tree(root, retain_months=3, now=datetime(2026, 8, 25, tzinfo=timezone.utc))

            self.assertIn(old, removed)
            self.assertFalse(old.exists())
            self.assertTrue(recent.exists())
            self.assertTrue(current.exists())

    def test_zero_or_negative_retention_does_not_delete(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "2025/01/01.json"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("{}\n", encoding="utf-8")
            self.assertEqual([], prune_tree(root, 0, datetime(2026, 8, 25, tzinfo=timezone.utc)))
            self.assertTrue(path.exists())


if __name__ == "__main__":
    unittest.main()
