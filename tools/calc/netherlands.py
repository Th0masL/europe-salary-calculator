"""Netherlands salary calculation — computed from published tax rates.

Rates are 2026 (single, no 30% ruling, no occupational pension). The Dutch system
is distinctive: the EMPLOYEE pays no separate social contributions — "national
insurance" is baked into the first Box-1 bracket — so net = gross − wage tax + tax
credits. The EMPLOYER pays the employee-insurance premiums (WW/WIA/AOF) and the
income-related health contribution (Zvw), capped at the maximum premium wage.

 - Box 1 brackets 2026: 35.75% to €38,883, 37.56% to €78,426, 49.50% above.
 - Tax credits (reduce the tax, both phase out with income): general (algemene
   heffingskorting) and labour (arbeidskorting).
 - Employer ≈ 28%: statutory premiums AOF ~6.5% + Awf(WW) ~2.74% + Whk ~1% + Zvw
   ~6.5% (≈16.7%, capped at the ~€78k premium wage) PLUS a representative
   occupational-pension share ~11.5% (capped ~€92k). The pension is CBA-based, not
   statutory, but near-universal; ~11.5% lands the total at eBook's +28%. (The
   +42–48% EOR figures also add holiday-allowance provisioning.)

Net is computed PRE-pension on the employee side too (no occupational-pension
deduction), which matches eBook; deducting the employee pension share would lower
net ~€4–6k. Holiday allowance 8% is treated as part of the entered gross.

The 2026 tax credits are the official Belastingdienst figures (general €3,115
tapering from €29,736; labour builds up, peaks €5,685, tapers to €0 at €132,920) —
net is validated at €20k→€19,453 and €30k→€27,754. The employer premium rates and
especially the occupational-pension share (varies hugely by sector) remain
representative estimates.

Sources: Belastingdienst 2026 (brackets); Deloitte Belastingplan 2026 (credits);
UWV/Belastingdienst (employer premiums, max premium wage).
"""
from engine import progressive

NAME = "Netherlands"
CURRENCY = "EUR"
YEAR = 2026
EMPLOYER_BREAKDOWN = "Statutory premiums (AOF+Awf+Whk+Zvw) ~16.7% (capped) + ~11.5% occupational pension (CBA-based)"
INF = float("inf")

BRACKETS = [(38883, 0.3575), (78426, 0.3756), (INF, 0.495)]

MAX_PREMIUM_WAGE = 78000
ER_STATUTORY = 0.065 + 0.0274 + 0.01 + 0.065   # AOF + Awf + Whk + Zvw ≈ 16.74%, capped
ER_PENSION = 0.115             # representative employer occupational-pension share (CBA-based)
PENSION_CAP = 92000


def _general_credit(income):
    """Algemene heffingskorting 2026 (under AOW age): €3,115, tapering to €0 by €78,426."""
    return max(0.0, 3115 - 0.06398 * max(0.0, income - 29736))


def _labour_credit(income):
    """Arbeidskorting 2026 (under AOW age): builds up, peaks €5,685, then tapers to €0."""
    if income <= 11965:
        return 0.08324 * income
    if income <= 25845:
        return 996 + 0.31009 * (income - 11965)
    if income <= 45592:
        return 5300 + 0.01950 * (income - 25845)
    return max(0.0, 5685 - 0.06510 * (income - 45592))   # €0 at €132,920


def compute(gross):
    """Return (employer_cost, net) for an annual gross salary, in EUR."""
    tax = progressive(gross, BRACKETS)
    tax = max(0.0, tax - _general_credit(gross) - _labour_credit(gross))

    net = gross - tax
    employer_cost = (gross
                     + min(gross, MAX_PREMIUM_WAGE) * ER_STATUTORY
                     + min(gross, PENSION_CAP) * ER_PENSION)
    return employer_cost, net
