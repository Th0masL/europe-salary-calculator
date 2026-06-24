"""Germany salary calculation — computed from published tax rates.

Rates are 2026 (single, no children, tax class I, statutory health insurance GKV).
(§32a verified against BMF; minor Vorsorge simplification noted below.)

Social contributions (clear): four branches, each split ~50/50, with TWO ceilings:
 - Pension 9.3% + unemployment 1.3%, capped at €101,400/yr.
 - Health 8.75% (7.3% + half the 2.9% average add-on), capped at €69,750/yr.
 - Care: employer 1.8%; employee 1.8% + 0.6% childless surcharge = 2.4%; €69,750 cap.
(The research's care split looked wrong; these are the standard rates.)

Income tax: Germany uses the continuous §32a polynomial tariff, not flat brackets.
The zone 2/3 coefficients (914.51 / 1,400 / 173.10 / 2,397 / 1,034.87) are the
official BMF 2026 values. The 42%/45% zone constants here (11,135.90 / 19,470.65)
are derived from tariff continuity: the values quoted in the research
(9,971.54 / 18,714.90) break continuity by ~€1,164 at €69,878 and 45% start, so
they are transcription errors. The tax base deducts the Vorsorgeaufwendungen
(pension + health + care; unemployment is effectively non-deductible, sitting in
the used-up €1,900 cap) plus the €1,230 Werbungskostenpauschale — a slight
simplification (it deducts full health rather than the ~96% basic share), so net
may be marginally high. Solidaritätszuschlag is ~0 for single filers here.

Sources: BMF §32a 2026 (verified coefficients + continuity); PwC Germany 2026
deductions; DRV/BMG 2026 rates + ceilings (€101,400 / €69,750); GFB €12,348.
"""

NAME = "Germany"
CURRENCY = "EUR"
YEAR = 2026
EMPLOYER_BREAKDOWN = "Pension+unemployment 10.6% + health+care 10.55% (both capped) + ~3% accident/U1-U2/insolvency levies"

PENSION_CAP = 101400          # pension + unemployment ceiling
HEALTH_CAP = 69750            # health + care ceiling

EMPLOYEE_PENS_UNEMP = 0.093 + 0.013      # 10.6%
EMPLOYEE_HEALTH_CARE = 0.0875 + 0.024    # 11.15% (health 8.75 + childless care 2.4)
EMPLOYER_PENS_UNEMP = 0.093 + 0.013      # 10.6%
EMPLOYER_HEALTH_CARE = 0.0875 + 0.018    # 10.55% (health 8.75 + care 1.8)
# Employer-only extras beyond the four branches: accident insurance
# (Berufsgenossenschaft ~1.3%) + U1/U2 Umlagen + insolvency levy ≈ 3%. Variable
# by sector/size; representative figure that matches the eBook/Rippling cluster.
EMPLOYER_EXTRAS = 0.03

DEDUCTIBLE_HEALTH_CARE = 0.0875 + 0.024  # Vorsorge: health + care (not unemployment)
LUMP_SUMS = 1230 + 36        # Werbungskostenpauschale + Sonderausgabenpauschbetrag


def _est(zve):
    """2026 §32a income tax (reconstructed coefficients)."""
    if zve <= 12348:
        return 0.0
    if zve <= 17799:
        y = (zve - 12348) / 10000.0
        return (914.51 * y + 1400) * y
    if zve <= 69878:
        z = (zve - 17799) / 10000.0
        return (173.10 * z + 2397) * z + 1034.87
    if zve <= 277825:
        return 0.42 * zve - 11135.9
    return 0.45 * zve - 19470.65


def compute(gross):
    """Return (employer_cost, net) for an annual gross salary, in EUR."""
    pu_base = min(gross, PENSION_CAP)
    hc_base = min(gross, HEALTH_CAP)

    employee = pu_base * EMPLOYEE_PENS_UNEMP + hc_base * EMPLOYEE_HEALTH_CARE

    vorsorge = pu_base * 0.093 + hc_base * DEDUCTIBLE_HEALTH_CARE
    zve = max(0.0, gross - vorsorge - LUMP_SUMS)
    income_tax = _est(zve)

    net = gross - employee - income_tax
    employer_cost = (gross + pu_base * EMPLOYER_PENS_UNEMP + hc_base * EMPLOYER_HEALTH_CARE
                     + pu_base * EMPLOYER_EXTRAS)
    return employer_cost, net
