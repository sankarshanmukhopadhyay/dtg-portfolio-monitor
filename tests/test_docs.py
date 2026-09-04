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
            "domain-brief.md": "/domain-brief/",
            "domain-model.md": "/domain-model/",
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

    def test_mermaid_rendering_is_enabled_when_diagrams_exist(self):
        config = yaml.safe_load((ROOT / "_config.yml").read_text(encoding="utf-8"))
        mermaid = config.get("mermaid", {})
        self.assertTrue(mermaid.get("version"), "Mermaid must be enabled in Just the Docs")

        diagram_pages = []
        for path in (ROOT / "docs").glob("*.md"):
            if "```mermaid" in path.read_text(encoding="utf-8"):
                diagram_pages.append(path.name)
        self.assertTrue(diagram_pages, "Expected at least one Mermaid diagram page")

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

    def test_custom_sass_is_inside_jekyll_source(self):
        custom = ROOT / "docs" / "_sass" / "custom" / "custom.scss"
        self.assertTrue(custom.is_file(), "Custom Sass must live inside the docs/ Jekyll source tree")
        self.assertIn(".portfolio-event-table", custom.read_text(encoding="utf-8"))
        self.assertFalse(
            (ROOT / "_sass" / "custom" / "custom.scss").exists(),
            "Root-level custom Sass is outside the Pages --source docs boundary",
        )

    def test_pages_push_covers_publication_inputs(self):
        pages = (ROOT / ".github/workflows/pages.yml").read_text(encoding="utf-8")
        for expected in (
            '- "docs/**"',
            '- "_config.yml"',
            '- "Gemfile"',
            '- "scripts/validate_site.py"',
            '- ".github/workflows/pages.yml"',
        ):
            self.assertIn(expected, pages)

    def test_collection_explicitly_deploys_persisted_revision(self):
        collect = (ROOT / ".github/workflows/collect.yml").read_text(encoding="utf-8")
        pages = (ROOT / ".github/workflows/pages.yml").read_text(encoding="utf-8")

        self.assertIn("deployment_ref: ${{ steps.persist.outputs.deployment_ref }}", collect)
        self.assertIn("uses: ./.github/workflows/pages.yml", collect)
        self.assertIn("ref: ${{ needs.collect.outputs.deployment_ref }}", collect)
        self.assertIn("docs/domain-brief.md", collect)
        self.assertIn("data", collect)
        self.assertNotIn("persist_changes:", collect)
        self.assertIn("workflow_call:", pages)
        self.assertIn("Exact commit to build and deploy", pages)
        self.assertIn("ref: ${{ inputs.ref != '' && inputs.ref || github.sha }}", pages)

if __name__ == "__main__":
    unittest.main()
