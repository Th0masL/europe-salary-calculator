"""Belgium salary calculation — computed from published tax rates.

Rates are 2026 (single, no children). Belgium has the heaviest tax wedge in the
set: 13.07% employee social security (uncapped), steep progressive federal tax,
plus a communal surcharge charged ON the tax.

Employee side confirmed vs KPMG / PwC / BDO 2026:
 - Employee SS (ONSS/RSZ): 13.07% of gross, no cap.
 - Professional-expense deduction: 30% of (gross − SS), capped at ~€5,750.
 - Federal tax: progressive 25/40/45/50% on (gross − SS − expenses), minus the
   tax-free allowance (€10,910, worth 25% × 10,910 = €2,727.50 as a reduction).
 - Communal surcharge: ~7% of the federal tax (average; ranges 0–9%).
 - Special SS contribution: ~€731/yr for higher earners (small, fixed-ish).
Net at €60k is ~60% — matches eBook; Deel/Skuad (~50%) conflate the total wedge.

Employer ≈ 29.85%: basic ONSS 25% (capped at €346,800/yr — doesn't bite) +
wage-moderation 2.35% + sectoral ~2.5% (uncapped). This treats the entered gross
as full annual compensation; the white-collar DOUBLE HOLIDAY PAY provisioning
(~+8% if gross is the 12-month base) is NOT added on top — that holiday-pay
provisioning is what pushes some EOR calculators to +40%+.

Sources: KPMG/PwC Belgium 2026 (SS, employer cap €86,700/quarter); BDO 2026
indexed brackets + €10,910 allowance.
"""
from engine import progressive

NAME = "Belgium"
CURRENCY = "EUR"
YEAR = 2026
EMPLOYER_BREAKDOWN = "Basic ONSS 25% + wage moderation 2.35% + sectoral ~2.5% (double-holiday-pay provisioning not added)"
INF = float("inf")

EE_SS = 0.1307
EXPENSE_RATE = 0.30
EXPENSE_CAP = 5750
ALLOWANCE = 10910
COMMUNAL = 0.07
SPECIAL_CONTRIB = 731       # annual, higher earners (approx)
ER_SS = 0.25 + 0.0235 + 0.025   # basic ONSS + wage moderation + sectoral ≈ 29.85%

BRACKETS = [(16720, 0.25), (29510, 0.40), (51070, 0.45), (INF, 0.50)]


def compute(gross):
    """Return (employer_cost, net) for an annual gross salary, in EUR."""
    ss = gross * EE_SS
    expenses = min(EXPENSE_RATE * (gross - ss), EXPENSE_CAP)
    taxable = max(0.0, gross - ss - expenses)

    federal = max(0.0, progressive(taxable, BRACKETS) - 0.25 * ALLOWANCE)
    communal = federal * COMMUNAL
    net = gross - ss - federal - communal - SPECIAL_CONTRIB

    employer_cost = gross * (1 + ER_SS)
    return employer_cost, net
