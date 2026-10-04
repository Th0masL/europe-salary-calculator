"""Norway salary calculation — computed from published tax rates.

Rates are 2026 for the age-40, single, no-child profile and an Oslo/zone-I
employer. Currency NOK (FX path).
 - Income tax = ordinary income tax 22% on general income (= gross − minstefradrag
   − personfradrag) + bracket tax (trinnskatt, progressive on personal income).
 - Employee national insurance: the statutory lower threshold/taper, then 7.6%.
 - Employer: contribution (arbeidsgiveravgift) 14.1% (normal zone; the +5%
   high-salary surcharge was abolished in 2025) + mandatory occupational pension
   (OTP, min 2% from the first krone through 12G), including employer NI on OTP.

We treat the entered gross as FULL annual comp, so holiday pay (feriepenger
   ~12%) is NOT added on top — that, plus a higher OTP, is why the EOR employer
   costs run to +20–37% vs our ~+16%.

Sources: Skatteetaten 2026 (bracket-tax steps, rates); PwC Norway 2026.
"""
from engine import progressive

NAME = "Norway"
CURRENCY = "NOK"
YEAR = 2026
EMPLOYER_BREAKDOWN = "Zone-I floor: employer NI 14.1% + minimum OTP 2% through 12G + employer NI on OTP; variable premiums excluded"
INF = float("inf")

MINSTEFRADRAG_RATE = 0.46
MINSTEFRADRAG_MAX = 95700
PERSONFRADRAG = 114540
ORDINARY_RATE = 0.22
NI_RATE = 0.076
ER_RATE = 0.141
NI_THRESHOLD = 99650
G = 134419
OTP_RATE = 0.02
BRACKET = [(226100, 0.0), (318300, 0.017), (725050, 0.04),
           (980100, 0.137), (1467200, 0.168), (INF, 0.178)]


def compute(gross):
    """Return (employer_cost, net) in NOK; build_formula converts to EUR."""
    minstefradrag = min(MINSTEFRADRAG_RATE * gross, MINSTEFRADRAG_MAX)
    taxable_general = max(0.0, gross - minstefradrag - PERSONFRADRAG)
    ordinary_tax = ORDINARY_RATE * taxable_general
    bracket_tax = progressive(gross, BRACKET)
    ni = 0.0 if gross < NI_THRESHOLD else min(NI_RATE * gross, .25 * (gross - NI_THRESHOLD))

    net = gross - ordinary_tax - bracket_tax - ni
    otp = OTP_RATE * min(gross, 12 * G)
    employer_cost = gross * (1 + ER_RATE) + otp * (1 + ER_RATE)
    return employer_cost, net
