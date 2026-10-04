"""Luxembourg 2026 estimate, tax class 1 representative scenario."""
import math
from engine import progressive

NAME, CURRENCY, YEAR = "Luxembourg", "EUR", 2026
EMPLOYER_BREAKDOWN = "Capped 12.57%: pension/health plus class-1 mutuality, accident factor 1.00, and STM occupational health"
INF = float("inf")
CAP, FULL_TIME_MINIMUM, DEPENDENCY_ABATEMENT = 164_589.81, 32_918.01, 8_229.46
SCALE = [
    (13_230, 0), (15_435, .08), (17_640, .09), (19_845, .10), (22_050, .11),
    (24_255, .12), (26_550, .14), (28_845, .16), (31_140, .18), (33_435, .20),
    (35_730, .22), (38_025, .24), (40_320, .26), (42_615, .28), (44_910, .30),
    (47_205, .32), (49_500, .34), (51_795, .36), (54_090, .38), (117_450, .39),
    (176_160, .40), (234_870, .41), (INF, .42),
]


def _credits(gross):
    if gross < 936 or gross >= 80_000:
        return 0.0
    cis = (300 + .029 * (gross - 936) if gross <= 11_265 else 600.0
           if gross <= 40_000 else 600 - .015 * (gross - 40_000))
    co2 = 216.0 if gross <= 40_000 else 216 - .0054 * (gross - 40_000)
    return cis + co2


def compute(gross):
    capped = min(gross, CAP)
    deductible_ss = .1155 * capped
    abatement = .25 * gross if gross < FULL_TIME_MINIMUM else DEPENDENCY_ABATEMENT
    dependency = .014 * max(gross - abatement, 0)
    taxable_raw = max(0.0, gross - deductible_ss - 540 - 480)
    taxable = math.floor(taxable_raw / 50) * 50
    base_tax = math.floor(progressive(taxable, SCALE))
    fund = math.floor(.07 * base_tax) if taxable <= 150_000 else math.floor(.09 * base_tax - 931.80)
    net_tax = base_tax + fund - _credits(gross)
    return gross + .1257 * capped, gross - deductible_ss - dependency - net_tax
