import unittest
from dtg_monitor.config import repositories
from dtg_monitor.validate import validate

class ConfigTests(unittest.TestCase):
    def test_repository_count(self):
        self.assertEqual(13, len(repositories()))

    def test_required_openvtc_repositories(self):
        names = {item["repo"] for item in repositories()}
        self.assertIn("OpenVTC/dtg-credentials", names)
        self.assertIn("OpenVTC/openvtc", names)
        self.assertIn("OpenVTC/verifiable-trust-infrastructure", names)

    def test_configuration_valid(self):
        self.assertEqual([], validate())

if __name__ == "__main__":
    unittest.main()
