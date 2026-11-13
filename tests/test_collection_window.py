import tempfile
import unittest
from datetime import date
from pathlib import Path

from scripts.collection_window import required_lookback


class CollectionWindowTests(unittest.TestCase):
    def test_new_monitor_uses_requested_window(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual((7, None), required_lookback(Path(tmp), date(2026, 11, 13)))

    def test_missed_publication_interval_is_replayed(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "2026/10/21.json"
            path.parent.mkdir(parents=True)
            path.write_text("[]")
            self.assertEqual(
                (24, date(2026, 10, 21)),
                required_lookback(Path(tmp), date(2026, 11, 13)),
            )

    def test_recent_snapshot_respects_requested_minimum(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "2026/11/12.json"
            path.parent.mkdir(parents=True)
            path.write_text("[]")
            self.assertEqual((7, date(2026, 11, 12)),
                             required_lookback(Path(tmp), date(2026, 11, 13)))

    def test_old_snapshot_does_not_silently_truncate(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "2026/09/01.json"
            path.parent.mkdir(parents=True)
            path.write_text("[]")
            with self.assertRaisesRegex(ValueError, "safety cap"):
                required_lookback(Path(tmp), date(2026, 11, 13))

    def test_future_snapshot_does_not_hide_gap(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "2026/11/14.json"
            path.parent.mkdir(parents=True)
            path.write_text("[]")
            self.assertEqual((7, None), required_lookback(Path(tmp), date(2026, 11, 13)))

    def test_invalid_limits_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                required_lookback(Path(tmp), date(2026, 11, 13), requested_days=0)
