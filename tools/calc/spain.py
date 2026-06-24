"""Spain salary calculation — computed from published tax rates.

Rates are 2026 (single private-sector employee under 65, no children, permanent
contract, General Social Security Scheme).

Spain is the most approximate module here — caveats, all flagged:
 - Social Security has a CAPPED contribution base: €5,101.20/mo = €61,214.40/yr
   in 2026. Almost every contribution is charged on min(salary, that cap), so
   above ~€61k the SS cost stops growing — that's why the employer-cost % drops
   sharply for high earners.
 - Employer rate on the base = 32.15%: common contingencies 23.60 + unemployment
   5.50 + FOGASA 0.20 + vocational training 0.60 + MEI 0.75 + occupational
   accident 1.50. The accident rate is occupation-dependent (office ~1.5%) — not
   one universal number.
 - The "solidarity contribution" on pay ABOVE the cap (tiered ~1.15–1.46%) is NOT
   modelled; it adds ~€0.3–1.0k of employer cost above €61k. Flagged.
 - IRPF is progressive AND regional (state + autonomous-community halves). We use
   the national-reference brackets; a specific region (Madrid lower, Catalonia
   higher) would shift net. We include the standard €2,000 employment-expense
   deduction and the €5,550 personal minimum, so this is more complete than the
   research's worked example — which omitted both and overstated tax by ~€1.8k at
   €60k.

All inputs here were confirmed against authoritative sources (Seg-Social / PwC /
ASU): the employee-SS package + €61,214.40 base cap, the €2,000 + €5,550 IRPF
deductions, and the 1.5% office accident rate. An end-to-end official calculator
output (AEAT / bank) wasn't retrievable, so the net rests on those confirmed
inputs rather than a third-party result. Employer cost is independently
corroborated (eBook €79,637, Skuad €79,018 vs our €79,290 at €60k).

Sources: Seg-Social 2026 contribution order; Garrigues / PwC 2026 notes; LIRPF
brackets; ASU Spain insights (accident rate).
"""
from engine import progressive

NAME = "Spain"
CURRENCY = "EUR"
YEAR = 2026
EMPLOYER_BREAKDOWN = "Common contingencies 23.6% + unemployment 5.5% + FOGASA 0.2% + training 0.6% + MEI 0.75% + accident ~1.5%, on base capped at €61,214"
INF = float("inf")

# Social Security contribution-base ceiling (2026).
BASE_CAP = 5101.20 * 12                   # €61,214.40 / yr

# Rates applied to the capped base:
EMPLOYER_RATE = 0.2360 + 0.0550 + 0.0020 + 0.0060 + 0.0075 + 0.0150  # 32.15% (incl. 1.5% accident)
EMPLOYEE_RATE = 0.0470 + 0.0155 + 0.0010 + 0.0015                    # 6.50%

# IRPF (national reference = state + default regional halves).
TAX_BRACKETS = [(12450, 0.19), (20200, 0.24), (35200, 0.30),
                (60000, 0.37), (300000, 0.45), (INF, 0.47)]
EMPLOYMENT_EXPENSES = 2000                # art. 19 "otros gastos"
PERSONAL_MINIMUM = 5550                   # mínimo personal, under 65


def compute(gross):
    """Return (employer_cost, net) for an annual gross salary, in EUR."""
    base = min(gross, BASE_CAP)
    employee_ss = base * EMPLOYEE_RATE

    taxable = max(0.0, gross - employee_ss - EMPLOYMENT_EXPENSES)
    # IRPF applies the personal minimum as a credit at the lowest brackets:
    # tax = tariff(base) − tariff(minimum).
    irpf = max(0.0, progressive(taxable, TAX_BRACKETS)
                    - progressive(PERSONAL_MINIMUM, TAX_BRACKETS))
    net = gross - employee_ss - irpf

    employer_cost = gross + base * EMPLOYER_RATE   # solidarity surcharge above cap not modelled
    return employer_cost, net
