import unittest
from dtg_monitor.config import repositories, portfolio_model, cross_spec_pressure_tests
from dtg_monitor.validate import validate

class ConfigTests(unittest.TestCase):
    def test_repository_count(self):
        self.assertEqual(15, len(repositories()))

    def test_required_openvtc_repositories(self):
        names = {item["repo"] for item in repositories()}
        self.assertIn("OpenVTC/dtg-credentials", names)
        self.assertIn("OpenVTC/openvtc", names)
        self.assertIn("OpenVTC/verifiable-trust-infrastructure", names)

    def test_required_trust_tasks_spec_repository(self):
        items = {item["repo"]: item for item in repositories()}
        repo = items["trustoverip/dtgwg-trust-tasks-spec"]
        self.assertEqual("normative-specification", repo["role"])
        self.assertEqual("critical", repo["reporting_weight"])
        self.assertIn("spec/**", repo["material_paths"])
        self.assertIn("specs.json", repo["material_paths"])

    def test_required_vds_repository(self):
        names = {item["repo"] for item in repositories()}
        self.assertIn("trustoverip/dtgwg-vds-tf", names)

    def test_portfolio_model_covers_configured_workstreams(self):
        model = portfolio_model()
        mapped = {stream for capability in model["capabilities"] for stream in capability["workstreams"]}
        configured = {item["workstream"] for item in repositories()}
        self.assertEqual(configured, mapped)

    def test_cross_spec_registry_has_runnable_canonical_pair(self):
        registry = cross_spec_pressure_tests()
        items = {x["id"]: x for x in registry["compositions"]}
        self.assertEqual("runnable", items["trust-tasks--credential-spec"]["readiness"])
        self.assertEqual(8, len(items))

    def test_all_cross_spec_compositions_runnable(self):
        registry = cross_spec_pressure_tests()
        self.assertEqual(8, len(registry["compositions"]))
        for item in registry["compositions"]:
            self.assertEqual("runnable", item["readiness"])
            self.assertIn(item["evidence_grade"], {"source-pinned", "source-informed", "scenario-baseline"})
            self.assertTrue(item["corpus_id"])
            self.assertTrue(item["assessment"])
        self.assertEqual("profiles/dtg/cross-spec-tests.yaml", registry["executor"]["registry"])

    def test_configuration_valid(self):
        self.assertEqual([], validate())

if __name__ == "__main__":
    unittest.main()
