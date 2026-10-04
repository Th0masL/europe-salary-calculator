"""Denmark salary calculation — computed from published tax rates.

Rates are 2026 (single, no church tax). Currency DKK (FX path). Denmark's
"flexicurity" model: minimal employer payroll cost — ATP (~DKK 2,376/yr) plus the
   selected determinable funds DKK 5,806/yr, before unresolved accident insurance,
   with the bulk of the burden on the employee's
income tax. The funds are roughly fixed DKK amounts (so the % falls as salary
rises) and vary by sector/risk; the research mentioned only ATP.

Employee side:
 - ATP DKK 1,188/yr (fixed) + AM-bidrag 8% of (gross − ATP).
 - "Personal income" = (gross − ATP) × 0.92.
 - Employment deduction 12.75% capped DKK63,300 and job allowance 4.5% above
   DKK235,200 capped DKK3,100 reduce municipal taxable income only.
 - Bundskat 12.01% uses personal income less the personal allowance; municipal
   25.049% also deducts employment/job allowances. Plus mellemskat 7.5% above
   DKK 641,200, topskat 7.5% above DKK 777,900, and 5%
   > DKK 2,592,700 (on personal income, no allowance). (Tax ceiling 52.07% doesn't
   bind in range.)

Sources: SKAT 2026 (AM-bidrag, brackets, allowance); PwC Denmark (municipal avg);
ATP private-sector rates.
"""

NAME = "Denmark"
CURRENCY = "DKK"
YEAR = 2026
EMPLOYER_BREAKDOWN = "Employer ATP DKK2,376 + selected AUB/AES/maternity funds DKK5,806; accident insurance excluded"

ATP_EE = 99 * 12            # DKK 1,188/yr employee
ATP_ER = 198 * 12           # DKK 2,376/yr employer
EMPLOYER_FUNDS = 5806       # selected official AUB/AES/maternity scenario
AM_RATE = 0.08
PERSONAL_ALLOWANCE = 54100
EMPLOYMENT_DED_RATE = 0.1275
EMPLOYMENT_DED_CAP = 63300
JOB_DED_RATE = 0.045
JOB_DED_START = 235200
JOB_DED_CAP = 3100
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

    deduction_base = gross + ATP_ER
    employment_ded = min(EMPLOYMENT_DED_RATE * deduction_base, EMPLOYMENT_DED_CAP)
    job_ded = min(JOB_DED_RATE * max(0.0, deduction_base - JOB_DED_START), JOB_DED_CAP)

    bottom_base = max(0.0, personal_income - PERSONAL_ALLOWANCE)
    municipal_base = max(0.0, personal_income - employment_ded - job_ded - PERSONAL_ALLOWANCE)
    tax = BUNDSKAT * bottom_base + MUNICIPAL * municipal_base
    tax += MELLEM_RATE * max(0.0, personal_income - MELLEM_THRESHOLD)
    tax += TOP_RATE * max(0.0, personal_income - TOP_THRESHOLD)
    tax += ADDL_RATE * max(0.0, personal_income - ADDL_THRESHOLD)

    net = gross - ATP_EE - am_bidrag - tax
    employer_cost = gross + ATP_ER + EMPLOYER_FUNDS
    return employer_cost, net
