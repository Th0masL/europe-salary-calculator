"""Turkey salary calculation — computed from published tax rates.

Rates are 2026 (single). Currency TRY (FX path; lira is inflation-volatile, so the
EUR figures are FX-sensitive).
 - Employee: SGK social security 14% + unemployment 1%, on a base capped at the
   monthly floor/ceiling (TRY 33,030 / 297,270). Deductible from the income-tax base.
 - Income tax: progressive 15 / 20 / 27 / 35 / 40% on (gross − employee
   contributions).
 - Stamp tax (damga vergisi): 0.759% of gross, withheld from the employee.
 - Minimum-wage exemption: since 2022 the income tax and stamp tax on the
   minimum-wage portion (= the SGK floor) are exempt for ALL employees — a fixed
   reduction that lifts every net.
 - Employer: SGK 20.75% + unemployment 2%, same capped base.

Sources: PwC Turkey 2026 (15–40% brackets, deductible SGK, min-wage exemption);
2026 SGK base TRY 33,030–297,270.
"""
from engine import progressive

NAME = "Turkey"
CURRENCY = "TRY"
YEAR = 2026
EMPLOYER_BREAKDOWN = "Social security (SGK) 20.75% + unemployment 2% (capped at TRY 297,270/mo)"
INF = float("inf")

SGK_MIN = 33030 * 12
SGK_MAX = 297270 * 12
EE_SGK = 0.14
EE_UNEMP = 0.01
ER_SGK = 0.2075
ER_UNEMP = 0.02
STAMP = 0.00759
PIT = [(190000, 0.15), (400000, 0.20), (1500000, 0.27),
       (5300000, 0.35), (INF, 0.40)]


def compute(gross):
    """Return (employer_cost, net) in TRY; build_formula converts to EUR."""
    base = min(max(gross, SGK_MIN), SGK_MAX)
    ee_contrib = base * (EE_SGK + EE_UNEMP)

    # minimum-wage exemption: the income tax & stamp on the min wage (= SGK floor)
    # are exempt for everyone, so subtract them from what's otherwise due.
    mw_exempt_tax = progressive(SGK_MIN - SGK_MIN * (EE_SGK + EE_UNEMP), PIT)
    income_tax = max(0.0, progressive(gross - ee_contrib, PIT) - mw_exempt_tax)
    stamp = STAMP * max(0.0, gross - SGK_MIN)

    net = gross - ee_contrib - income_tax - stamp
    employer_cost = gross + base * (ER_SGK + ER_UNEMP)
    return employer_cost, net
