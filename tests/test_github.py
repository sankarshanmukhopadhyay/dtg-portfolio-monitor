import unittest
from unittest.mock import patch
from urllib.error import HTTPError
from io import BytesIO

from dtg_monitor.github import GitHubClient

class GitHubClientTests(unittest.TestCase):
    @patch("dtg_monitor.github.urlopen")
    def test_paged_treats_configured_409_as_empty(self, mocked):
        error = HTTPError(
            "https://api.github.com/repos/example/empty/commits",
            409,
            "Conflict",
            {},
            BytesIO(b'{"message":"Git Repository is empty."}'),
        )
        mocked.side_effect = error
        client = GitHubClient(token="test", max_retries=1)
        self.assertEqual(
            [],
            client.paged("/repos/example/empty/commits", empty_on_status={409}),
        )

if __name__ == "__main__":
    unittest.main()
