"""Sweden salary calculation — computed from published tax rates.

Rates are 2026 for a single employee under 66 in Stockholm, no church membership.
The calculation follows SKV 433 for the basic allowance and earned-income credits.
Employer cost contains only the universal 31.42% statutory contribution; optional
collective-agreement pension and insurance are excluded.

Sources: Verksamt 2026 (employer 31.42%); SCB (municipal avg 32.38%); Skatteverket
(state-tax threshold).
"""

NAME = "Sweden"
CURRENCY = "SEK"
YEAR = 2026
EMPLOYER_BREAKDOWN = "Statutory employer contributions 31.42%; occupational pension/insurance excluded"

PBB = 59200
MUNICIPAL = 0.3055
BURIAL = 0.0007
STATE_RATE = 0.20
STATE_THRESHOLD = 643000
ER_RATE = 0.3142


def ceil_100(value):
    import math
    return math.ceil(value / 100) * 100


def basic_allowance(income):
    if income <= 0.99 * PBB:
        raw = 0.423 * PBB
    elif income <= 2.72 * PBB:
        raw = 0.423 * PBB + 0.20 * (income - 0.99 * PBB)
    elif income <= 3.11 * PBB:
        raw = 0.77 * PBB
    elif income <= 7.88 * PBB:
        raw = 0.77 * PBB - 0.10 * (income - 3.11 * PBB)
    else:
        raw = 0.293 * PBB
    return min(income, ceil_100(raw))


def employment_credit(work_income, allowance):
    ai = int(work_income // 100) * 100
    if ai <= 0.91 * PBB:
        amount = ai - allowance
    elif ai <= 3.24 * PBB:
        amount = 0.91 * PBB + 0.3874 * (ai - 0.91 * PBB) - allowance
    elif ai <= 8.08 * PBB:
        amount = 1.813 * PBB + 0.251 * (ai - 3.24 * PBB) - allowance
    else:
        amount = 3.027 * PBB - allowance
    return int(max(0.0, amount * MUNICIPAL))


def compute(gross):
    """Return (employer_cost, net) in SEK; build_formula converts to EUR."""
    fixed_income = int(gross // 100) * 100
    allowance = basic_allowance(fixed_income)
    taxable = max(0.0, fixed_income - allowance)
    municipal = int(taxable * MUNICIPAL)
    burial = int(taxable * BURIAL)
    state = int(STATE_RATE * max(0.0, taxable - STATE_THRESHOLD))
    jobb = employment_credit(gross, allowance)
    other_credit = (0 if taxable <= 40000 else
                    int(0.0075 * (taxable - 40000)) if taxable <= 240000 else 1500)
    public_service = int(min(0.01 * taxable, 1184))
    income_tax = municipal + burial + state - jobb - other_credit + public_service

    net = gross - income_tax
    employer_cost = gross * (1 + ER_RATE)
    return employer_cost, net
