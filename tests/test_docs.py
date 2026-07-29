import unittest
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class DocumentationTests(unittest.TestCase):
    def test_no_public_markdown_links(self):
        root = ROOT / "docs"
        bad = []
        for path in root.glob("*.md"):
            if path.name.startswith("legacy-"):
                continue
            for line in path.read_text(encoding="utf-8").splitlines():
                if "](" in line and ".md)" in line:
                    bad.append(f"{path.name}: {line}")
        self.assertEqual([], bad)

    def test_stable_permalink_frontmatter(self):
        root = ROOT / "docs"
        expected = {
            "repositories.md": "/repositories/",
            "portfolio-status.md": "/portfolio-status/",
            "reports.md": "/reports/",
            "dashboard.md": "/dashboard/",
        }
        for name, route in expected.items():
            text = (root / name).read_text(encoding="utf-8")
            self.assertIn(f"permalink: {route}", text)

    def test_legacy_redirect_routes(self):
        expected = {
            "legacy-repositories.md": ("/repositories.md", "/repositories/"),
            "legacy-portfolio-status.md": ("/portfolio-status.md", "/portfolio-status/"),
        }
        for name, (legacy, target) in expected.items():
            text = (ROOT / "docs" / name).read_text(encoding="utf-8")
            self.assertIn(f"permalink: {legacy}", text)
            self.assertIn(target, text)

    def test_just_the_docs_theme_configured(self):
        config = (ROOT / "_config.yml").read_text(encoding="utf-8")
        gemfile = (ROOT / "Gemfile").read_text(encoding="utf-8")
        self.assertIn("theme: just-the-docs", config)
        self.assertIn('gem "just-the-docs"', gemfile)

    def test_just_the_docs_default_layout_is_configured(self):
        config = yaml.safe_load((ROOT / "_config.yml").read_text(encoding="utf-8"))
        defaults = config.get("defaults", [])
        self.assertTrue(
            any(
                item.get("scope", {}).get("type") == "pages"
                and item.get("values", {}).get("layout") == "default"
                for item in defaults
            ),
            "Normal documentation pages must receive the Just the Docs default layout",
        )

    def test_legacy_redirects_override_default_layout(self):
        for name in ("legacy-repositories.md", "legacy-portfolio-status.md"):
            text = (ROOT / "docs" / name).read_text(encoding="utf-8")
            self.assertRegex(text, r"(?m)^layout:\s*null\s*$")

if __name__ == "__main__":
    unittest.main()
