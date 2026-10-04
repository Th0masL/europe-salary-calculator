"""Ukraine salary calculation — computed from published tax rates.

Rates are 2026 (single). Currency UAH (FX path — needed for the USC cap).
 - Employee: 18% PIT + 5% military tax on gross, no general allowance and no cap —
   so net is a flat 77% of gross.
 - Employer: 22% unified social contribution (USC/ЄСВ) on gross, capped at 20× the
   minimum wage per month (UAH 8,647 → UAH 172,940/mo). The cap sits at ~€45k/yr, so
   above that the employer USC is a flat cash amount and its % of gross falls.

Sources: Ukraine 2026 Budget Act; State Tax Service (18% PIT, 5% military tax,
22% USC, temporary 20× minimum-wage cap for 2026).
"""

NAME = "Ukraine"
CURRENCY = "UAH"
YEAR = 2026
EMPLOYER_BREAKDOWN = "Unified social contribution (USC) 22% (capped at 20× min wage/month; 12 equal pays)"

MIN_WAGE = 8647
MONTHLY_USC_CAP = MIN_WAGE * 20
PIT = 0.18
MILITARY = 0.05
USC = 0.22


def compute(gross):
    """Return (employer_cost, net) in UAH for 12 equal monthly payments."""
    monthly_gross = gross / 12
    usc_base = 12 * min(monthly_gross, MONTHLY_USC_CAP)
    net = gross * (1 - PIT - MILITARY)
    employer_cost = gross + USC * usc_base
    return employer_cost, net
