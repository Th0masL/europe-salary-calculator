"""Structural regression tests for the formula calculators and data pipeline."""

import importlib
import json
import math
import re
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CALC_DIR = ROOT / "tools" / "calc"
sys.path.insert(0, str(CALC_DIR))
sys.path.insert(0, str(ROOT / "tools"))

from engine import progressive  # noqa: E402
from validate_data import DATASETS, validate_dataset  # noqa: E402


class EngineTests(unittest.TestCase):
    def test_progressive_brackets(self):
        brackets = [(10_000, 0.10), (20_000, 0.20), (float("inf"), 0.30)]
        self.assertEqual(progressive(5_000, brackets), 500)
        self.assertEqual(progressive(15_000, brackets), 2_000)
        self.assertEqual(progressive(30_000, brackets), 6_000)

class CountryModuleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.modules = [
            importlib.import_module(path.stem)
            for path in sorted(CALC_DIR.glob("*.py"))
            if path.stem not in {"engine", "__init__"}
        ]

    def test_expected_country_coverage_and_unique_names(self):
        self.assertEqual(len(self.modules), 36)
        names = [module.NAME for module in self.modules]
        self.assertEqual(len(names), len(set(names)))

    def test_module_contracts_and_financial_invariants(self):
        for module in self.modules:
            with self.subTest(country=module.NAME):
                self.assertIsInstance(module.NAME, str)
                self.assertIsInstance(module.CURRENCY, str)
                self.assertGreaterEqual(module.YEAR, 2025)

                # Non-euro modules use local-currency thresholds and caps, so use
                # representative local amounts rather than pretending these are EUR.
                gross_values = ((20_000, 60_000, 150_000)
                                if module.CURRENCY == "EUR"
                                else (1_000_000, 2_000_000, 3_000_000))
                results = [module.compute(gross) for gross in gross_values]

                for gross, (cost, net) in zip(gross_values, results):
                    self.assertTrue(math.isfinite(cost))
                    self.assertTrue(math.isfinite(net))
                    self.assertGreaterEqual(cost, gross)
                    self.assertGreaterEqual(net, 0)
                    self.assertLessEqual(net, gross)

                costs = [result[0] for result in results]
                nets = [result[1] for result in results]
                self.assertEqual(costs, sorted(costs))
                self.assertEqual(nets, sorted(nets))


class GeneratedDataTests(unittest.TestCase):
    def test_formula_range_and_5k_resolution(self):
        for dataset in ("formula", "us"):
            with self.subTest(dataset=dataset):
                path = ROOT / "data" / f"{dataset}.json"
                doc = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual(doc["meta"]["salaryPoints"], list(range(20_000, 600_001, 5_000)))
                for country in doc["countries"]:
                    self.assertEqual(country["points"][0]["gross"], 20_000)
                    self.assertEqual(country["points"][-1]["gross"], 600_000)

    def test_formula_covers_200k_net_for_every_european_location(self):
        path = ROOT / "data" / "formula.json"
        doc = json.loads(path.read_text(encoding="utf-8"))
        for country in doc["countries"]:
            if country.get("us"):
                continue
            with self.subTest(country=country["name"]):
                nets = [point["net"] for point in country["points"]]
                self.assertLessEqual(nets[0], 200_000)
                self.assertGreaterEqual(nets[-1], 200_000)

    def test_formula_carries_its_own_location_metadata(self):
        path = ROOT / "data" / "formula.json"
        doc = json.loads(path.read_text(encoding="utf-8"))
        european = [country for country in doc["countries"] if not country.get("us")]
        self.assertEqual(len(european), 36)
        self.assertEqual(sum(country.get("eu") is True for country in european), 27)
        for country in doc["countries"]:
            with self.subTest(country=country["name"]):
                self.assertTrue(country.get("flag"))
                if not country.get("us"):
                    self.assertIsInstance(country.get("eu"), bool)

    def test_all_generated_datasets(self):
        errors = []
        for dataset in DATASETS:
            errors.extend(validate_dataset(dataset))
        self.assertEqual(errors, [], "\n".join(errors))


class SiteConfigurationTests(unittest.TestCase):
    def test_live_calculator_loads_formula_only(self):
        index = (ROOT / "index.html").read_text(encoding="utf-8")
        app = (ROOT / "app.js").read_text(encoding="utf-8")
        deploy = (ROOT / ".github" / "workflows" / "deploy.yml").read_text(encoding="utf-8")

        self.assertIn('src="data/formula.js"', index)
        self.assertIn("window.SALARY_DATA_FORMULA", app)
        self.assertIn("cp data/cost_of_living.js data/formula.js _site/data/", deploy)
        self.assertNotIn("cp data/*.js _site/data/", deploy)
        self.assertEqual(
            re.findall(r'<script src="(data/[^"]+\.js)"', index),
            ["data/cost_of_living.js", "data/formula.js"],
        )


if __name__ == "__main__":
    unittest.main()
