"""Denmark salary calculation — computed from published tax rates.

Rates are 2026 (single, no church tax). Currency DKK (FX path). Denmark's
"flexicurity" model: minimal employer payroll cost — ATP (~DKK 2,376/yr) plus the
mandatory funds (AES occupational injury, AUB, barsel) ~DKK 9,700/yr, ≈ +2.7% at
€60k (matches eBook/Rippling) — with the bulk of the burden on the employee's
income tax. The funds are roughly fixed DKK amounts (so the % falls as salary
rises) and vary by sector/risk; the research mentioned only ATP.

Employee side:
 - ATP DKK 1,188/yr (fixed) + AM-bidrag 8% of (gross − ATP).
 - "Personal income" = (gross − ATP) × 0.92.
 - Deductions before bund+municipal tax: personal allowance DKK 54,100 AND the
   beskæftigelsesfradrag (employment deduction) 10.65% of the AM-base, capped at
   ~DKK 45,100. *** The research OMITTED the beskæftigelsesfradrag — it's a real,
   sizeable deduction (~€2k of net at €60k), so it's added here; its exact 2026
   rate/cap and the smaller jobfradrag should be verified. ***
 - Bundskat 12.01% + municipal 25.049% (country average) on the post-deduction
   base; plus mellemskat 7.5% > DKK 641,200, topskat 7.5% > DKK 777,900, and 5%
   > DKK 2,592,700 (on personal income, no allowance). (Tax ceiling 52.07% doesn't
   bind in range.)

Sources: SKAT 2026 (AM-bidrag, brackets, allowance); PwC Denmark (municipal avg);
ATP private-sector rates.
"""

NAME = "Denmark"
CURRENCY = "DKK"
YEAR = 2026

ATP_EE = 99 * 12            # DKK 1,188/yr employee
ATP_ER = 198 * 12           # DKK 2,376/yr employer
EMPLOYER_FUNDS = 9700       # AES + AUB + barsel etc. (representative; ~fixed DKK)
AM_RATE = 0.08
PERSONAL_ALLOWANCE = 54100
EMPLOYMENT_DED_RATE = 0.1065     # beskæftigelsesfradrag
EMPLOYMENT_DED_CAP = 45100       # 2025 cap (2026 estimate)
BUNDSKAT = 0.1201
MUNICIPAL = 0.25049              # country average

MELLEM_RATE, MELLEM_THRESHOLD = 0.075, 641200
TOP_RATE, TOP_THRESHOLD = 0.075, 777900
ADDL_RATE, ADDL_THRESHOLD = 0.05, 2592700


def compute(gross):
    """Return (employer_cost, net) in DKK; build_formula converts to EUR."""
    am_base = gross - ATP_EE
    am_bidrag = AM_RATE * am_base
    personal_income = am_base - am_bidrag        # = (gross − ATP) × 0.92

    employment_ded = min(EMPLOYMENT_DED_RATE * am_base, EMPLOYMENT_DED_CAP)
    taxable = max(0.0, personal_income - PERSONAL_ALLOWANCE - employment_ded)

    tax = (BUNDSKAT + MUNICIPAL) * taxable
    tax += MELLEM_RATE * max(0.0, personal_income - MELLEM_THRESHOLD)
    tax += TOP_RATE * max(0.0, personal_income - TOP_THRESHOLD)
    tax += ADDL_RATE * max(0.0, personal_income - ADDL_THRESHOLD)

    net = gross - ATP_EE - am_bidrag - tax
    employer_cost = gross + ATP_ER + EMPLOYER_FUNDS
    return employer_cost, net
