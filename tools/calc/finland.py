"""Finland salary calculation — computed from published tax rates.

Rates are 2026 (single, no church tax).

Employee contributions: TyEL pension 7.30% + unemployment 0.89% + health daily-
allowance 0.88% (all deductible from the tax base) + health medical-care 1.10%
(NOT deductible) = 10.17%.

Income tax: state progressive (post-2023 reform — the bottom 12.64% absorbed the
old municipal portion when healthcare funding moved to the state) PLUS a flat
municipal tax (~7.57% average post-reform), on (gross − deductible contributions −
€750 income-acquisition deduction). The työtulovähennys (earned-income credit,
tapers out by ~€95k) is applied as a credit; plus the Yle public-broadcasting tax
(2.5% above €14k, capped €163).

Employer: TyEL ~17.10% + health 1.91% + unemployment 0.31% + accident ~0.7% +
group life ~0.07% ≈ 20% (accident/TyEL vary by insurer/category).

*** APPROXIMATE: the research gave contributions + brackets but not the exact 2026
deduction formulas. The työtulovähennys here is a simplified single-taper estimate
and the municipal deductions are omitted — verify against the Vero calculator. ***

Sources: Vero 2026 (contributions, brackets); PwC Finland 2026; tyoelake.fi (TyEL).
"""
from engine import progressive

NAME = "Finland"
CURRENCY = "EUR"
YEAR = 2026
INF = float("inf")

EE_DEDUCTIBLE = 0.073 + 0.0089 + 0.0088    # pension + unemployment + daily allowance = 9.07%
EE_MEDICAL = 0.011                          # medical-care, NOT deductible
INCOME_DEDUCTION = 750
TTV_MAX = 3225                              # työtulovähennys, simplified
TTV_TAPER = 0.045
TTV_TAPER_START = 23420

STATE_BRACKETS = [(21200, 0.1264), (32600, 0.19), (40100, 0.3025), (52100, 0.3325), (INF, 0.375)]
MUNICIPAL = 0.0757

ER_RATE = 0.171 + 0.0191 + 0.0031 + 0.007 + 0.0007   # TyEL+health+unemp+accident+group life ≈ 20%


def compute(gross):
    """Return (employer_cost, net) for an annual gross salary, in EUR."""
    deductible = gross * EE_DEDUCTIBLE
    total_contrib = deductible + gross * EE_MEDICAL

    tax_base = max(0.0, gross - deductible - INCOME_DEDUCTION)
    state = progressive(tax_base, STATE_BRACKETS)
    municipal = MUNICIPAL * tax_base
    ttv = max(0.0, TTV_MAX - TTV_TAPER * max(0.0, gross - TTV_TAPER_START))
    income_tax = max(0.0, state + municipal - ttv)
    yle = min(0.025 * max(0.0, tax_base - 14000), 163)

    net = gross - total_contrib - income_tax - yle
    employer_cost = gross * (1 + ER_RATE)
    return employer_cost, net
