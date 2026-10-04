"""Belgium 2026 estimate for the documented representative scenario.

Annual gross contains 12 monthly salaries plus double holiday pay (12.92 months).
The inferred fiscal work-bonus credit and employer-specific charges are excluded.
"""
from engine import progressive

NAME, CURRENCY, YEAR = "Belgium", "EUR", 2026
EMPLOYER_BREAKDOWN = "25% ordinary ONSS on 12-month salary, after structural reduction and 2026 high-salary cap"
INF = float("inf")
BRACKETS = [(16_720, .25), (29_510, .40), (51_070, .45), (INF, .50)]
EE_SS, EXPENSE_CAP, TAX_CREDIT, COMMUNAL = .1307, 6_070, 2_795, .07


def _work_bonus(salary):
    periods = (
        (6, 125.04, 2_880.32, 3_336.98, .2738, 168.62, 2_255.50, 2_880.32, .2699),
        (2, 127.54, 2_937.93, 3_336.98, .3196, 171.99, 2_300.62, 2_937.93, .2699),
        (4, 127.54, 2_937.93, 3_403.62, .2739, 171.99, 2_300.62, 2_937.93, .2699),
    )
    total, contribution = 0.0, EE_SS * salary
    for months, af, ast, aend, asl, bf, bst, bend, bsl in periods:
        a = af if salary <= ast else max(0.0, af - asl * (salary - ast)) if salary < aend else 0.0
        b = bf if salary <= bst else max(0.0, bf - bsl * (salary - bst)) if salary < bend else 0.0
        total += months * min(contribution, a + b)
    return total


def _csss(salary):
    quarter = 3 * salary
    if salary < 1_945.38 or quarter < 5_836.14:
        advance = 0.0
    elif salary < 2_190.18 and quarter < 6_570.54:
        advance = .0422 * (salary - 1_945.38)
    elif salary < 3_737 and quarter < 11_211:
        advance = 30.99 + .011 * (salary - 2_190.18)
    elif salary < 4_100 and quarter < 12_300:
        advance = 82.05 + .0338 * (salary - 3_737)
    elif salary < 6_038.82 and quarter < 18_116.46:
        advance = 118.83 + .011 * (salary - 4_100)
    else:
        advance = 182.82
    return 4 * advance


def _employer_ss(salary):
    quarter = 3 * salary
    base = 2 * min(quarter, 86_700) + 2 * min(quarter, 88_434)
    reduction = .14 * max(11_687.74 - quarter, 0) + .16 * max(9_738.14 - quarter, 0)
    return max(0.0, .25 * base - 4 * reduction)


def compute(gross):
    salary = gross / 12.92
    ordinary = max(0.0, EE_SS * 12 * salary - _work_bonus(salary))
    employee_ss = ordinary + EE_SS * .85 * salary
    before_expenses = gross - employee_ss
    taxable = max(0.0, before_expenses - min(.30 * before_expenses, EXPENSE_CAP))
    federal = max(0.0, progressive(taxable, BRACKETS) - TAX_CREDIT)
    net = gross - employee_ss - federal - COMMUNAL * federal - _csss(salary)
    return gross + _employer_ss(salary), net
