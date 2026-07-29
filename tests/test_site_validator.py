import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class SiteValidatorTests(unittest.TestCase):
    def _build_site(self, themed=True):
        temporary = tempfile.TemporaryDirectory()
        site = Path(temporary.name)
        for route in ("repositories", "portfolio-status", "reports", "dashboard"):
            target = site / route / "index.html"
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("<html><body>page</body></html>", encoding="utf-8")
        for name, target in (("repositories.md", "/repositories/"), ("portfolio-status.md", "/portfolio-status/")):
            (site / name).write_text(f'<meta http-equiv="refresh" content="0; url={target}">', encoding="utf-8")
        css = site / "assets" / "css" / "just-the-docs-light.css"
        css.parent.mkdir(parents=True, exist_ok=True)
        css.write_text(".side-bar{display:block}", encoding="utf-8")
        classes = '<div class="side-bar"></div><header class="site-header"></header><main class="main"></main>' if themed else "<main></main>"
        (site / "index.html").write_text(
            f'<html><head><link rel="stylesheet" href="/dtg-portfolio-monitor/assets/css/just-the-docs-light.css"></head><body>{classes}</body></html>',
            encoding="utf-8",
        )
        return temporary, site

    def test_accepts_just_the_docs_custom_stylesheet_name(self):
        temporary, site = self._build_site(themed=True)
        self.addCleanup(temporary.cleanup)
        result = subprocess.run(
            [sys.executable, "scripts/validate_site.py", str(site)],
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn("Just the Docs layout", result.stdout)

    def test_rejects_missing_theme_layout(self):
        temporary, site = self._build_site(themed=False)
        self.addCleanup(temporary.cleanup)
        result = subprocess.run(
            [sys.executable, "scripts/validate_site.py", str(site)],
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(0, result.returncode)
        self.assertIn("expected Just the Docs layout", result.stderr)


if __name__ == "__main__":
    unittest.main()
