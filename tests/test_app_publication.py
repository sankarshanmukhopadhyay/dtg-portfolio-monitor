"""Fail-closed native-check publication credential contract for collection."""
from pathlib import Path
import unittest

WORKFLOW = (Path(__file__).resolve().parents[1]
            / ".github/workflows/collect.yml")


class AppPublicationTests(unittest.TestCase):
    def test_app_preflight_before_observation_and_publication(self):
        text = WORKFLOW.read_text()
        required = (
            "vars.DTG_MONITOR_APP_ID",
            "secrets.DTG_MONITOR_APP_PRIVATE_KEY",
            "actions/create-github-app-token@64ab729a6294000f5aa4a4bc0b73d1f32bc45510",
            "repositories: dtg-portfolio-monitor",
            "permission-contents: write",
            "permission-pull-requests: write",
            "persist-credentials: false",
            "GH_TOKEN: ${{ steps.publisher-app.outputs.token }}",
            "APP_SLUG: ${{ steps.publisher-app.outputs.app-slug }}",
            "token: ${{ steps.publisher-app.outputs.token }}",
            "committer: ${{ steps.bot.outputs.signature }}",
            "author: ${{ steps.bot.outputs.signature }}",
            "signoff: true",
        )
        for assertion in required:
            with self.subTest(assertion=assertion):
                self.assertIn(assertion, text)
        self.assertLess(text.index("Require repository-scoped portfolio publication App"),
                        text.index("Collect activity"))
        self.assertLess(text.index("Authenticate repository-scoped publication App"),
                        text.index("Collect activity"))

    def test_no_default_token_or_unqualified_automerge(self):
        text = WORKFLOW.read_text()
        self.assertNotIn("secrets.MONITOR_AUTOMATION_TOKEN || github.token", text)
        self.assertNotIn("AUTO_TOKEN_PRESENT", text)
        self.assertIn('if: steps.publication.outputs.pull-request-number != \'\'', text)
        self.assertIn('gh pr checks "$PR_NUMBER" --watch', text)
        self.assertIn('gh pr merge "$PR_NUMBER" --squash --delete-branch', text)
        self.assertIn('gh pr checks "$PR_NUMBER" --json name', text)
        for expected in ("DCO", "validate", "pages-build"):
            with self.subTest(check=expected):
                self.assertIn(expected, text)
        self.assertIn("Native PR checks were not registered", text)
        self.assertIn("timeout 900 gh pr checks", text)
        self.assertLess(text.index('gh pr checks "$PR_NUMBER" --json name'),
                        text.index('gh pr checks "$PR_NUMBER" --watch'))
        self.assertLess(text.index('gh pr checks "$PR_NUMBER" --watch'),
                        text.index('gh pr merge "$PR_NUMBER" --squash --delete-branch'))
        self.assertIn("concurrency:\n  group: dtg-portfolio-collection", text)


if __name__ == "__main__":
    unittest.main()
