"""Ireland salary calculation — computed from published tax rates.

Rates are 2026 for the age-40, single, no-child PAYE employee, paid on 52 Fridays,
with no existing payroll pension and continued MyFutureFund enrolment.

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
 - PRSI uses 39 weekly pays at the pre-October rate and 13 at the new rate.
 - MyFutureFund employee/employer contributions are 1.5% through the whole weekly
   payroll that first breaches €80,000 cumulative pay.

Sources: Revenue (income tax, USC, PRSI, tax credits); PwC Ireland 2026; Chartered
Accountants Ireland Budget 2026 (USC bands, €44,000 band).
"""
import math

from engine import progressive

NAME = "Ireland"
CURRENCY = "EUR"
YEAR = 2026
EMPLOYER_BREAKDOWN = "52-Friday scenario: split-year Class A employer PRSI + 1.5% MyFutureFund through the €80k breach payroll"
INF = float("inf")

# USC: progressive bands on gross (2026).
USC_BANDS = [(12012, 0.005), (28700, 0.02), (70044, 0.03), (INF, 0.08)]

# Income tax: 20% to the standard-rate band, 40% above; then reduced by credits.
TAX_BANDS = [(44000, 0.20), (INF, 0.40)]
TAX_CREDITS = 2000 + 2000        # personal + employee (PAYE)


def compute(gross):
    """Return (employer_cost, net) for an annual gross salary, in EUR."""
    weekly = gross / 52
    if weekly <= 352:
        old_employee = new_employee = 0.0
    else:
        credit = max(0.0, 12 - (weekly - 352.01) / 6)
        old_employee = max(0.0, .042 * weekly - credit)
        new_employee = max(0.0, .0435 * weekly - credit)
    prsi = 39 * old_employee + 13 * new_employee
    old_er_rate, new_er_rate = ((.09, .0915) if weekly <= 552 else (.1125, .114))
    employer_prsi = 39 * old_er_rate * weekly + 13 * new_er_rate * weekly

    contributory_weeks = min(52, math.ceil(80_000 / weekly)) if gross >= 20_000 else 0
    mff_gross = contributory_weeks * weekly
    mff = .015 * mff_gross
    usc = progressive(gross, USC_BANDS)
    income_tax = max(0.0, progressive(gross, TAX_BANDS) - TAX_CREDITS)

    net = gross - prsi - usc - income_tax - mff
    employer_cost = gross + employer_prsi + mff
    return employer_cost, net
