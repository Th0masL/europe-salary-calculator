# Greece — implementation comparison

## Compared artifacts

- Independent dossier: `docs/research/2026/greece.md`
- Current implementation: `tools/calc/greece.py`
- Comparison date: 2026-10-04

## Implementation update — 2026-10-04

The research dossier's age-30 scenario was implemented first. The product's later
common-profile decision fixes age 40, so the live calculator now uses the general
2026 scale (20% from EUR10,000 to EUR20,000) while retaining Article 16,
payment-level EFKA ceilings, KPK 101 and the EUR20 ELPC scenario.

## Current implementation scenario

The module models an annual resident employee with ordinary KPK-style EFKA, but converts the monthly ceiling into a single `12 × €7,761.94` annual cap. It uses the general-age PIT scale, omits the Article 16 employment reduction, and excludes the dossier's conditional €20 ELPC employer charge.

## Findings

| Severity | Classification | Area | Finding | Evidence / code |
|---|---|---|---|---|
| Critical | Confirmed mismatch | PIT scale | The stated age-30 employee is entitled to 9% through €20,000 taxable income; the module charges 20% from €10,000 to €20,000. | Dossier §§1, 3; `greece.py:22,29`. |
| High | Confirmed mismatch | Employment tax reduction | The Article 16 reduction (€777 before taper, €670.48 at the €20,000 vector) is absent. The module comment that it is zero throughout the app range is false. | Dossier §1; `greece.py:5-6,25-31`. |
| High | Confirmed mismatch | EFKA ceiling/order | The annual `12C` shortcut is not equivalent to the statutory payment-by-payment ceiling for 12 salaries plus two half-month holiday payments. Under the dossier's constant-pay convention the base is €115,190.93 at €200,000 and approaches `15C = €116,429.10`; the module caps at €93,143.28. | Dossier §2; `greece.py:19,27,32`. |
| Low | Scenario difference | Employer ELPC | The dossier includes a conditional €20 annual ELPC for the selected ordinary employer; the generic module excludes it. This must be exposed as a scenario, not silently universalised. | Dossier §§2–3; `greece.py:32`. |

## Matches

- Employee and employer EFKA rates (13.37% and 21.79%) match the selected KPK 101 scenario.
- EFKA is deducted before PIT, and the 26%/34%/39%/44% upper age-30 rates match.
- Electronic-spend compliance is implicitly assumed by both calculations.

## Output impact

`Δ = implementation − dossier`, EUR:

| Gross | Impl. net | Dossier net | Δ net | Impl. cost | Dossier cost | Δ cost |
|---:|---:|---:|---:|---:|---:|---:|
| 20,000 | 14,960.80 | 16,437.14 | -1,476.34 | 24,358.00 | 24,378.00 | -20.00 |
| 60,000 | 38,406.58 | 39,506.58 | -1,100.00 | 73,074.00 | 73,094.00 | -20.00 |
| 100,000 | 58,726.18 | 59,312.80 | -586.62 | 120,295.92 | 121,810.00 | -1,514.08 |
| 200,000 | 114,726.18 | 114,175.42 | +550.76 | 220,295.92 | 225,120.10 | -4,824.18 |
| 600,000 | 338,726.18 | 338,082.72 | +643.46 | 620,295.92 | 625,389.90 | -5,093.98 |

## Recommended disposition

Replace the PIT scale with the age-sensitive 2026 schedule, implement Article 16, and calculate EFKA per contractual payment. Make age, payment pattern, KPK/supplementary-insurance status, and ELPC applicability explicit scenario inputs.

## Regression vectors

For the dossier's age-30, 14-payment, KPK 101 and €20-ELPC scenario, assert `(gross → employer_cost, net)`: `20,000 → 24,378.00, 16,437.14`; `60,000 → 73,094.00, 39,506.58`; `100,000 → 121,810.00, 59,312.80`; `200,000 → 225,120.10, 114,175.42`; `600,000 → 625,389.90, 338,082.72`.
