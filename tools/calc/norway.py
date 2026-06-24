"""Norway salary calculation — computed from published tax rates.

Rates are 2026 (single). Currency NOK (FX path).
 - Income tax = ordinary income tax 22% on general income (= gross − minstefradrag
   − personfradrag) + bracket tax (trinnskatt, progressive on personal income).
 - Employee national insurance (trygdeavgift): 7.6% of personal income.
 - Employer: contribution (arbeidsgiveravgift) 14.1% (normal zone; the +5%
   high-salary surcharge was abolished in 2025) + mandatory occupational pension
   (OTP, min 2% on salary between 1G and 12G).

Notes / caveats:
 - The minstefradrag (max ~NOK 113k) and personfradrag (~NOK 114k) are 2026
   estimates (the research didn't give them); net (~75% at €60k) is therefore
   approximate. The EOR cross-refs are too inconsistent to calibrate against
   (net €38–47k at €60k, cost +20–37%).
 - We treat the entered gross as FULL annual comp, so holiday pay (feriepenger
   ~12%) is NOT added on top — that, plus a higher OTP, is why the EOR employer
   costs run to +20–37% vs our ~+16%.

Sources: Skatteetaten 2026 (bracket-tax steps, rates); PwC Norway 2026.
"""
from engine import progressive

NAME = "Norway"
CURRENCY = "NOK"
YEAR = 2026
EMPLOYER_BREAKDOWN = "Employer contribution (arbeidsgiveravgift) 14.1% + occupational pension (OTP, min 2%)"
INF = float("inf")

MINSTEFRADRAG_RATE = 0.46
MINSTEFRADRAG_MAX = 113000
PERSONFRADRAG = 114000
ORDINARY_RATE = 0.22
NI_RATE = 0.076
ER_RATE = 0.141
G = 124000                 # grunnbeløp (approx); OTP applies on 1G–12G
OTP_RATE = 0.02
BRACKET = [(226100, 0.0), (318300, 0.017), (725050, 0.04),
           (980100, 0.137), (1467200, 0.168), (INF, 0.178)]


def compute(gross):
    """Return (employer_cost, net) in NOK; build_formula converts to EUR."""
    minstefradrag = min(MINSTEFRADRAG_RATE * gross, MINSTEFRADRAG_MAX)
    taxable_general = max(0.0, gross - minstefradrag - PERSONFRADRAG)
    ordinary_tax = ORDINARY_RATE * taxable_general
    bracket_tax = progressive(gross, BRACKET)
    ni = NI_RATE * gross

    net = gross - ordinary_tax - bracket_tax - ni
    otp = OTP_RATE * max(0.0, min(gross, 12 * G) - G)
    employer_cost = gross * (1 + ER_RATE) + otp
    return employer_cost, net
