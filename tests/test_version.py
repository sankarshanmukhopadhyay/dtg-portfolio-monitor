import tomllib
import unittest
from pathlib import Path

import dtg_monitor


class VersionContractTests(unittest.TestCase):
    def test_version_declarations_match(self):
        root = Path(__file__).resolve().parents[1]
        declared = (root / "VERSION").read_text(encoding="utf-8").strip()
        project = tomllib.loads((root / "pyproject.toml").read_text(encoding="utf-8"))["project"]["version"]
        self.assertEqual("0.5.0", declared)
        self.assertEqual(declared, project)
        self.assertEqual(declared, dtg_monitor.__version__)


if __name__ == "__main__":
    unittest.main()
