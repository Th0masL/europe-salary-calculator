"""Structural regression tests for the formula calculators and data pipeline."""

import importlib
import math
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CALC_DIR = ROOT / "tools" / "calc"
sys.path.insert(0, str(CALC_DIR))
sys.path.insert(0, str(ROOT / "tools"))

from build_consensus import enforce_monotonic  # noqa: E402
from engine import progressive  # noqa: E402
from validate_data import DATASETS, validate_dataset  # noqa: E402


class EngineTests(unittest.TestCase):
    def test_progressive_brackets(self):
        brackets = [(10_000, 0.10), (20_000, 0.20), (float("inf"), 0.30)]
        self.assertEqual(progressive(5_000, brackets), 500)
        self.assertEqual(progressive(15_000, brackets), 2_000)
        self.assertEqual(progressive(30_000, brackets), 6_000)

    def test_isotonic_pooling_is_minimal_and_monotonic(self):
        points = [{"net": 10}, {"net": 20}, {"net": 16}, {"net": 30}]
        self.assertTrue(enforce_monotonic(points, "net"))
        self.assertEqual([point["net"] for point in points], [10, 18, 18, 30])
        self.assertFalse(enforce_monotonic(points, "net"))


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
    def test_all_generated_datasets(self):
        errors = []
        for dataset in DATASETS:
            errors.extend(validate_dataset(dataset))
        self.assertEqual(errors, [], "\n".join(errors))


if __name__ == "__main__":
    unittest.main()
