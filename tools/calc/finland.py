"""Finland salary calculation — computed from published tax rates.

Rates are 2026 (single, no church tax).

Representative scenario: single employee under 65, Helsinki 5.30% municipal tax,
no church tax. The calculation follows the 2026 acquisition deduction, basic
allowance and employment-credit order across state, municipal and health tax.
Employer accident/group-life rates use official average assumptions.

Sources: Vero 2026 (contributions, brackets); PwC Finland 2026; tyoelake.fi (TyEL).
"""
from engine import progressive

NAME = "Finland"
CURRENCY = "EUR"
YEAR = 2026
EMPLOYER_BREAKDOWN = "TyEL 17.1% + health 1.91% + unemployment 0.31% + average accident 0.51% + group life 0.06%"
INF = float("inf")

EE_TYEL = 0.073
EE_UNEMPLOYMENT = 0.0089
EE_DAILY = 0.0088
INCOME_DEDUCTION = 750
TTV_MAX = 3430

STATE_BRACKETS = [(22000, 0.1264), (32600, 0.19), (40100, 0.3025), (52100, 0.3325), (INF, 0.375)]
MUNICIPAL = 0.053
HEALTH_CARE = 0.011

ER_RATE = 0.171 + 0.0191 + 0.0031 + 0.0051 + 0.0006


def compute(gross):
    """Return (employer_cost, net) for an annual gross salary, in EUR."""
    tyel = gross * EE_TYEL
    unemployment = gross * EE_UNEMPLOYMENT
    daily = gross * EE_DAILY if gross >= 17255 else 0.0
    pure_income = gross - min(gross, INCOME_DEDUCTION)
    pre_basic = max(0.0, pure_income - tyel - unemployment - daily)
    basic = (pre_basic if pre_basic <= 4265
             else max(0.0, 4265 - 0.18 * (pre_basic - 4265)))
    taxable = max(0.0, pre_basic - basic)

    state_raw = progressive(taxable, STATE_BRACKETS)
    municipal_raw = MUNICIPAL * taxable
    health_raw = HEALTH_CARE * taxable
    credit_before_taper = min(0.18 * gross, TTV_MAX)
    taper = 0.02 * min(max(pure_income - 35000, 0.0), 15550)
    credit = max(0.0, credit_before_taper - taper)
    state = max(0.0, state_raw - credit)
    credit_left = max(0.0, credit - state_raw)
    local_total = municipal_raw + health_raw
    if local_total and credit_left:
        local_factor = max(0.0, 1 - credit_left / local_total)
        municipal = municipal_raw * local_factor
        health = health_raw * local_factor
    else:
        municipal, health = municipal_raw, health_raw
    yle = min(160, 0.025 * max(0.0, pure_income - 15150))

    net = gross - tyel - unemployment - daily - state - municipal - health - yle
    employer_cost = gross * (1 + ER_RATE)
    return employer_cost, net
