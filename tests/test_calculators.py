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


class CorrectedCountryRegressionTests(unittest.TestCase):
    def assertAmountsAlmostEqual(self, actual, expected):
        self.assertAlmostEqual(actual[0], expected[0], places=2)
        self.assertAlmostEqual(actual[1], expected[1], places=2)

    def test_turkey_unincentivised_employer_rate(self):
        turkey = importlib.import_module("turkey")
        self.assertAmountsAlmostEqual(
            turkey.compute(5_000_000),
            (5_847_219.50, 3_082_633.67),
        )

    def test_ukraine_temporary_2026_usc_cap(self):
        ukraine = importlib.import_module("ukraine")
        self.assertAmountsAlmostEqual(
            ukraine.compute(3_000_000),
            (3_456_561.60, 2_310_000.00),
        )

    def test_bulgaria_split_year_contribution_ceiling(self):
        bulgaria = importlib.import_module("bulgaria")
        expected_base = 7 * 2_111.64 + 5 * 2_300
        cost, net = bulgaria.compute(60_000)
        self.assertAlmostEqual(cost, 60_000 + expected_base * 0.1902, places=2)
        employee = expected_base * 0.1378
        self.assertAlmostEqual(net, 60_000 - employee - 0.10 * (60_000 - employee), places=2)

    def test_portugal_2026_deduction_and_no_double_counted_fgs(self):
        portugal = importlib.import_module("portugal")
        self.assertAlmostEqual(portugal.SPECIFIC_DEDUCTION, 4_587.0902, places=4)
        self.assertAlmostEqual(portugal.compute(60_000)[0], 74_850.00, places=2)

    def test_moldova_employee_side_and_exemption_boundary(self):
        moldova = importlib.import_module("moldova")
        self.assertAmountsAlmostEqual(
            moldova.compute(400_000),
            (496_000.00, 320_320.00),
        )
        gross_at_limit = moldova.ALLOWANCE_CAP / (1 - moldova.EE_HEALTH)
        _, net_below = moldova.compute(gross_at_limit - 0.01)
        _, net_at = moldova.compute(gross_at_limit)
        self.assertLess(net_at - net_below, -3_500)

    def test_malta_total_gross_tax_and_basic_wage_contributions(self):
        malta = importlib.import_module("malta")
        vectors = {
            20_000: (22_007.20, 16_451.04),
            60_000: (62_995.72, 45_491.64),
            100_000: (102_995.72, 71_491.64),
        }
        for gross, expected in vectors.items():
            with self.subTest(gross=gross):
                self.assertAmountsAlmostEqual(malta.compute(gross), expected)

    def test_slovakia_income_dependent_allowance(self):
        slovakia = importlib.import_module("slovakia")
        cost, net = slovakia.compute(20_000)
        self.assertAlmostEqual(cost, 27_239.57, delta=0.05)
        self.assertAlmostEqual(net, 15_001.09, delta=0.02)

    def test_lithuania_npd_and_employer_component_caps(self):
        lithuania = importlib.import_module("lithuania")
        vectors = {
            20_000: (20_354.00, 13_288.74),
            60_000: (61_062.00, 36_300.00),
            200_000: (202_651.59, 118_544.05),
        }
        for gross, expected in vectors.items():
            with self.subTest(gross=gross):
                actual = lithuania.compute(gross)
                self.assertAlmostEqual(actual[0], expected[0], delta=0.05)
                self.assertAlmostEqual(actual[1], expected[1], delta=0.05)

    def test_slovenia_deductible_contributions_and_regresses(self):
        slovenia = importlib.import_module("slovenia")
        vectors = {
            20_000: (25_642.82, 13_414.44),
            60_000: (72_482.82, 35_406.03),
            200_000: (236_422.82, 94_904.78),
        }
        for gross, expected in vectors.items():
            with self.subTest(gross=gross):
                actual = slovenia.compute(gross)
                self.assertAlmostEqual(actual[0], expected[0], places=2)
                self.assertAlmostEqual(actual[1], expected[1], delta=0.01)

    def test_poland_high_income_solidarity_levy(self):
        poland = importlib.import_module("poland")
        # The annual approximation differs from monthly statutory rounding only
        # by grosze; the PLN 75,667 levy must be present at PLN 3 million.
        self.assertAlmostEqual(poland.compute(1_000_000)[1], 585_331.08, delta=0.50)
        self.assertAlmostEqual(poland.compute(3_000_000)[1], 1_660_754.11, delta=0.50)

    def test_montenegro_in_year_payroll_baseline(self):
        montenegro = importlib.import_module("montenegro")
        vectors = {
            20_000: (20_422.60, 16_376.00),
            60_000: (61_710.60, 46_176.00),
            600_000: (619_098.60, 448_476.00),
        }
        for gross, expected in vectors.items():
            with self.subTest(gross=gross):
                self.assertAmountsAlmostEqual(montenegro.compute(gross), expected)

    def test_albania_personal_deduction_and_taxable_bands(self):
        albania = importlib.import_module("albania")
        vectors = {
            2_000_000: (2_334_000.00, 1_562_800.00),
            6_000_000: (6_437_548.80, 4_592_285.76),
            60_000_000: (61_355_548.80, 45_254_285.76),
        }
        for gross, expected in vectors.items():
            with self.subTest(gross=gross):
                self.assertAmountsAlmostEqual(albania.compute(gross), expected)

    def test_latvia_solidarity_reconciliation(self):
        latvia = importlib.import_module("latvia")
        vectors = {
            20_000: (24_722.32, 15_018.50),
            200_000: (238_576.09, 134_990.65),
            600_000: (696_576.09, 389_500.65),
        }
        for gross, expected in vectors.items():
            with self.subTest(gross=gross):
                self.assertAmountsAlmostEqual(latvia.compute(gross), expected)

    def test_denmark_separate_tax_bases_and_deductions(self):
        denmark = importlib.import_module("denmark")
        vectors = {
            150_000: (158_182.00, 111_086.08),
            750_000: (758_182.00, 466_708.41),
            4_500_000: (4_508_182.00, 2_050_037.03),
        }
        for gross, expected in vectors.items():
            with self.subTest(gross=gross):
                self.assertAmountsAlmostEqual(denmark.compute(gross), expected)

    def test_finland_ordered_helsinki_tax_calculation(self):
        finland = importlib.import_module("finland")
        vectors = {
            20_000: (23_978.00, 18_083.50),
            60_000: (71_934.00, 42_379.24),
            600_000: (719_340.00, 317_842.58),
        }
        for gross, expected in vectors.items():
            with self.subTest(gross=gross):
                self.assertAmountsAlmostEqual(finland.compute(gross), expected)

    def test_greece_age30_and_payment_level_efka(self):
        greece = importlib.import_module("greece")
        vectors = {
            20_000: (24_378.00, 16_437.14),
            200_000: (225_120.10, 114_175.42),
            600_000: (625_389.90, 338_082.72),
        }
        for gross, expected in vectors.items():
            with self.subTest(gross=gross):
                self.assertAmountsAlmostEqual(greece.compute(gross), expected)

    def test_sweden_official_stockholm_tax_formulas(self):
        sweden = importlib.import_module("sweden")
        vectors = {
            200_000: (262_840.00, 171_894.00),
            1_000_000: (1_314_200.00, 680_954.00),
            6_000_000: (7_885_200.00, 3_149_954.00),
        }
        for gross, expected in vectors.items():
            with self.subTest(gross=gross):
                self.assertAmountsAlmostEqual(sweden.compute(gross), expected)

    def test_switzerland_zurich_fixed_core_benchmark(self):
        switzerland = importlib.import_module("switzerland")
        vectors = {
            20_000: (21_485.00, 18_462.74),
            100_000: (110_638.00, 78_358.83),
            600_000: (642_793.20, 369_883.21),
        }
        for gross, expected in vectors.items():
            with self.subTest(gross=gross):
                self.assertAmountsAlmostEqual(switzerland.compute(gross), expected)

    def test_austria_vienna_payment_specific_calculation(self):
        austria = importlib.import_module("austria")
        vectors = {
            20_000: (26_048.57, 17_984.29),
            100_000: (129_189.40, 62_631.05),
            600_000: (672_139.40, 329_577.93),
        }
        for gross, expected in vectors.items():
            with self.subTest(gross=gross):
                self.assertAmountsAlmostEqual(austria.compute(gross), expected)

    def test_france_deterministic_statutory_subtotal(self):
        france = importlib.import_module("france")
        vectors = {
            20_000: (20_622.40, 15_798.05),
            60_000: (84_618.97, 41_081.60),
            600_000: (802_975.32, 290_195.27),
        }
        for gross, expected in vectors.items():
            with self.subTest(gross=gross):
                actual = france.compute(gross)
                self.assertAlmostEqual(actual[0], expected[0], delta=0.02)
                self.assertAlmostEqual(actual[1], expected[1], delta=0.02)


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
