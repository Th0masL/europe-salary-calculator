"""Ireland salary calculation — computed from published tax rates.

Rates are 2026 (single PAYE private-sector employee, no children, standard
credits, no occupational pension).

Distinctive features:
 - Three separate charges on GROSS, none deductible against the others: income
   tax, USC (Universal Social Charge), and PRSI. Net = gross − all three.
 - Income tax is 20% up to the €44,000 standard-rate band and 40% above, then
   reduced by TAX CREDITS (not an allowance). A single PAYE employee gets TWO:
   the Personal Tax Credit (€2,000) AND the Employee/PAYE Tax Credit (€2,000) =
   €4,000 (confirmed vs Revenue Budget 2026). The research originally listed only
   the €2,000 employee credit — missing the personal credit would have overstated
   tax by €2,000. The €44,000 band, the €4,000 credits and the USC bands are all
   confirmed unchanged for 2026.
 - Employer cost is just employer PRSI (11.25%): Ireland has no employer health or
   unemployment payroll charge, so employer cost is low vs the rest of Europe.

Not modelled (flagged):
 - Auto-enrolment pension ("My Future Fund") starts 2026 — 1.5% employee + 1.5%
   employer (capped €80,000). It applies to employees WITHOUT an existing pension,
   so at €60k+ (who usually have an occupational scheme) it typically doesn't
   apply; excluded from the base case.
 - PRSI rises 0.15pp on 1 Oct 2026 (employer 11.25→11.40, employee 4.20→4.35);
   we use the rates in force for most of 2026.

Sources: Revenue (income tax, USC, PRSI, tax credits); PwC Ireland 2026; Chartered
Accountants Ireland Budget 2026 (USC bands, €44,000 band).
"""
from engine import progressive

NAME = "Ireland"
CURRENCY = "EUR"
YEAR = 2026
EMPLOYER_BREAKDOWN = "Employer PRSI (Class A) 11.25%"
INF = float("inf")

# PRSI (Class A) on gross, no cap. Oct 2026: employee 4.35%, employer 11.40%.
EMPLOYEE_PRSI = 0.042
EMPLOYER_PRSI = 0.1125

# USC: progressive bands on gross (2026).
USC_BANDS = [(12012, 0.005), (28700, 0.02), (70044, 0.03), (INF, 0.08)]

# Income tax: 20% to the standard-rate band, 40% above; then reduced by credits.
TAX_BANDS = [(44000, 0.20), (INF, 0.40)]
TAX_CREDITS = 2000 + 2000        # personal + employee (PAYE)


def compute(gross):
    """Return (employer_cost, net) for an annual gross salary, in EUR."""
    prsi = gross * EMPLOYEE_PRSI
    usc = progressive(gross, USC_BANDS)
    income_tax = max(0.0, progressive(gross, TAX_BANDS) - TAX_CREDITS)

    net = gross - prsi - usc - income_tax
    employer_cost = gross + gross * EMPLOYER_PRSI
    return employer_cost, net
