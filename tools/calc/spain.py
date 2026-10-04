"""Spain 2026 estimate for a single employee resident in Madrid."""
from engine import progressive

NAME, CURRENCY, YEAR = "Spain", "EUR", 2026
EMPLOYER_BREAKDOWN = "Madrid office employee: 32.15% on capped base plus 2026 tiered solidarity contribution above it"
INF = float("inf")
BASE_MIN, BASE_CAP = 17_092.80, 61_214.40
STATE = [(12_450, .095), (20_200, .12), (35_200, .15), (60_000, .185), (300_000, .225), (INF, .245)]
MADRID = [(13_362.22, .085), (19_004.63, .107), (35_425.68, .128), (57_320.40, .174), (INF, .205)]


def _solidarity_bases(gross):
    return (min(max(gross - BASE_CAP, 0), .10 * BASE_CAP),
            min(max(gross - 1.10 * BASE_CAP, 0), .40 * BASE_CAP),
            max(gross - 1.50 * BASE_CAP, 0))


def _article20(income):
    if income <= 14_852:
        return 7_302.0
    if income <= 17_673.52:
        return 7_302 - 1.75 * (income - 14_852)
    if income < 19_747.50:
        return 2_364.34 - 1.14 * (income - 17_673.52)
    return 0.0


def _low_income_credit(gross):
    if gross <= 17_094:
        return 590.89
    if gross <= 20_048.45:
        return 590.89 - .20 * (gross - 17_094)
    return 0.0


def compute(gross):
    base = min(max(gross, BASE_MIN), BASE_CAP)
    t1, t2, t3 = _solidarity_bases(gross)
    ee_solidarity = .0019 * t1 + .0021 * t2 + .0024 * t3
    employee_ss = .065 * base + ee_solidarity
    work_income = gross - employee_ss
    liquidable = max(0.0, gross - employee_ss - 2_000 - _article20(work_income))
    state = progressive(liquidable, STATE) - progressive(5_550, STATE)
    madrid = progressive(liquidable, MADRID) - progressive(5_956.65, MADRID)
    irpf = max(0.0, state + madrid - _low_income_credit(gross))
    employer_solidarity = .0096 * t1 + .0104 * t2 + .0122 * t3
    return gross + .3215 * base + employer_solidarity, gross - employee_ss - irpf
