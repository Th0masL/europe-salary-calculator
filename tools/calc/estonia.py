"""Estonia salary calculation — computed from published tax rates.

Rates are 2026, from the Estonian Tax and Customs Board (EMTA) and the KPMG 2026
tax card. Confirmed against EMTA's official calculation: €60k gross → net
€46,963.20, employer cost €80,280.00 — this module matches to the cent. The
default funded-pension rate is 2% (4%/6% are opt-in only).

Key 2026 change vs 2025: the basic exemption is a FLAT EUR 700/mo (8,400/yr) with
the income-based phase-out ("tax hump") removed — so it now applies at every
salary level, not just low incomes.

Sources:
  - EMTA tax rates: https://www.emta.ee/en/private-client/taxes-and-payment/declaration-income/tax-rates
  - EMTA basic exemption: https://www.emta.ee/en/private-client/taxes-and-payment/tax-incentives/calculation-basic-exemption
  - KPMG 2026 tax card.
"""

NAME = "Estonia"
CURRENCY = "EUR"
YEAR = 2026

# --- employer pays ON TOP of gross ---
SOCIAL_TAX = 0.33               # sotsiaalmaks: 20% pension + 13% health, uncapped
EMPLOYER_UNEMPLOYMENT = 0.008   # töötuskindlustus, employer share
# (Min. social-tax base is EUR 886/mo => EUR 292.38/mo minimum; only bites below
#  ~EUR 10.6k/yr, so it doesn't affect this app's salary levels.)

# --- deducted from the employee's gross ---
EMPLOYEE_UNEMPLOYMENT = 0.016   # töötuskindlustus, employee share
FUNDED_PENSION = 0.02           # II pillar; default 2% (the employee may pick 4% or 6%)
INCOME_TAX = 0.22               # tulumaks, flat (no security surtax in 2026)
# No employee health-insurance contribution (health is funded by employer social tax).

# Basic exemption (maksuvaba tulu), 2026: flat EUR 8,400/yr for non-pensioners,
# no phase-out. (Pensioners get more; not modelled here.)
BASIC_EXEMPTION = 8400


def compute(gross):
    """Return (employer_cost, net) for an annual gross salary, in EUR."""
    employer_cost = gross * (1 + SOCIAL_TAX + EMPLOYER_UNEMPLOYMENT)

    unemployment = gross * EMPLOYEE_UNEMPLOYMENT
    pension = gross * FUNDED_PENSION
    # social contributions and the basic exemption reduce taxable income
    taxable = max(0.0, gross - unemployment - pension - BASIC_EXEMPTION)
    income_tax = taxable * INCOME_TAX

    net = gross - unemployment - pension - income_tax
    return employer_cost, net
