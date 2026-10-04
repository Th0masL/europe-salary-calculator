"""Montenegro salary calculation — computed from published tax rates.

Rates are 2026 (single private-sector employee). Confirmed against PwC Tax
Summaries (post-"Europe Now 2.0", Oct 2024):
 - Health contributions ABOLISHED (0% both sides).
 - Employee: pension & disability (PIO) 10% + unemployment 0.5%. Payroll withholds
   PIO on full gross; any excess over the later-published annual maximum is handled
   through a separate refund procedure.
 - Employer: unemployment 0.5%, Labour Fund 0.2%, and 2026 Chamber contribution
   0.27%; employer pension and health are 0% after the Europe Now reforms.
 - Salary tax: progressive on MONTHLY GROSS — 0% to €700, 9% €700–1,000, 15%
   above. Brackets are gross amounts; contributions do NOT reduce the base.
 - Municipal surtax is 15% of PIT in Podgorica and is included on the employer
   side following the Ministry's official payroll layout.

Lesson logged: three EOR calculators put employer cost at +5–7% and net ~€46k —
BOTH wrong (legacy/non-statutory items; taxing after contributions). The statutory
reconstruction here, verified vs PwC, is +0.5% employer and tax-on-gross. A clean
case of clustered third-party calculators agreeing *and* being wrong together.

Sources: PwC Montenegro tax summaries (PIT brackets, surtax base, contributions).
"""
from engine import progressive

NAME = "Montenegro"
CURRENCY = "EUR"
YEAR = 2026
EMPLOYER_BREAKDOWN = "Unemployment 0.5% + Labour Fund 0.2% + Chamber 0.27% + Podgorica surtax (15% of PIT)"
INF = float("inf")

PENSION_RATE = 0.10
UNEMPLOYMENT = 0.005           # employee and employer each
LABOUR_FUND = 0.002
CHAMBER = 0.0027

# Salary tax: progressive on MONTHLY gross.
TAX_BANDS_MONTHLY = [(700, 0.0), (1000, 0.09), (INF, 0.15)]
SURTAX = 0.15                  # Podgorica municipal surtax, charged on the income tax


def compute(gross):
    """Return (employer_cost, net) for an annual gross salary, in EUR."""
    pension = gross * PENSION_RATE
    unemployment = gross * UNEMPLOYMENT

    income_tax = progressive(gross / 12, TAX_BANDS_MONTHLY) * 12

    net = gross - pension - unemployment - income_tax
    employer_cost = (gross + gross * (UNEMPLOYMENT + LABOUR_FUND + CHAMBER)
                     + income_tax * SURTAX)
    return employer_cost, net
