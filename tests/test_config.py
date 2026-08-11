import unittest
from dtg_monitor.config import repositories, portfolio_model
from dtg_monitor.validate import validate

class ConfigTests(unittest.TestCase):
    def test_repository_count(self):
        self.assertEqual(14, len(repositories()))

    def test_required_openvtc_repositories(self):
        names = {item["repo"] for item in repositories()}
        self.assertIn("OpenVTC/dtg-credentials", names)
        self.assertIn("OpenVTC/openvtc", names)
        self.assertIn("OpenVTC/verifiable-trust-infrastructure", names)

    def test_required_vds_repository(self):
        names = {item["repo"] for item in repositories()}
        self.assertIn("trustoverip/dtgwg-vds-tf", names)

    def test_portfolio_model_covers_configured_workstreams(self):
        model = portfolio_model()
        mapped = {stream for capability in model["capabilities"] for stream in capability["workstreams"]}
        configured = {item["workstream"] for item in repositories()}
        self.assertEqual(configured, mapped)

    def test_configuration_valid(self):
        self.assertEqual([], validate())

if __name__ == "__main__":
    unittest.main()
