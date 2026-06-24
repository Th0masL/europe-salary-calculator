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

*** APPROXIMATE: the 2026 tax-credit amounts/taper points, the employer premium
rates, and especially the occupational-pension share (varies hugely by sector) are
estimates — verify. ***

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

GENERAL_MAX, GENERAL_TAPER, GENERAL_START = 3068, 0.06337, 24813
LABOUR_MAX, LABOUR_TAPER, LABOUR_START = 5599, 0.0651, 39958

MAX_PREMIUM_WAGE = 78000
ER_STATUTORY = 0.065 + 0.0274 + 0.01 + 0.065   # AOF + Awf + Whk + Zvw ≈ 16.74%, capped
ER_PENSION = 0.115             # representative employer occupational-pension share (CBA-based)
PENSION_CAP = 92000


def compute(gross):
    """Return (employer_cost, net) for an annual gross salary, in EUR."""
    tax = progressive(gross, BRACKETS)
    general = max(0.0, GENERAL_MAX - GENERAL_TAPER * max(0.0, gross - GENERAL_START))
    labour = max(0.0, LABOUR_MAX - LABOUR_TAPER * max(0.0, gross - LABOUR_START))
    tax = max(0.0, tax - general - labour)

    net = gross - tax
    employer_cost = (gross
                     + min(gross, MAX_PREMIUM_WAGE) * ER_STATUTORY
                     + min(gross, PENSION_CAP) * ER_PENSION)
    return employer_cost, net
