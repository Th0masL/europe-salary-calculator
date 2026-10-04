# Austria — 2026 implementation comparison

## Compared artifacts

- Dossier: `docs/research/2026/austria.md` (official BMF/ÖGK/USP sources, accessed 2026-10-04).
- Implementation: `tools/calc/austria.py`.

## Implementation update — 2026-10-04

The Vienna 14-payment benchmark now applies payment-sensitive employee SV, final
ceilings, statutory credits/refund, special-payment bands and overflow, distinct
employer SV rates, and the EUR106 Vienna DGA. It matches the dossier vectors.

## Current implementation scenario

Vienna-style 14 equal payments, but with estimated ceilings, one blended employee/employer SV rate, a calibrated credit, and uncapped percentage employer levies.

## Findings

| Severity | Classification | Area | Finding | Evidence / code |
|---|---|---|---|---|
| Critical | Confirmed mismatch | Employee SV | The module uses 18.07% for regular and special pay. The dossier requires contribution-specific regular/special rates, low-income unemployment reductions, and Vienna chamber/housing treatment; examples use 15.37% regular/14.12% special at EUR20k and 18.32%/17.07% at the ceiling. | Dossier §§2.2, 4-5; `austria.py:35-38,56-57`. |
| High | Confirmed mismatch | Ceilings | EUR6,630/EUR13,260 are estimates; final 2026 regular/special ceilings are EUR6,930/EUR13,860. | Dossier §2.2; `austria.py:35-36`. |
| Critical | Confirmed mismatch | Tax credits/refund | The hard-coded EUR548 credit omits the statutory EUR496 transport credit, EUR804 surcharge and refundable-SV negative-tax mechanism. It understates the EUR20k net by EUR1,701.54. | Dossier §§2.4-2.5, 5.1; `austria.py:40,59`. |
| High | Confirmed mismatch | Special-payment tax | The first band is coded as EUR25,000 after the EUR620 exemption, rather than a EUR24,380 remaining width; amounts above the EUR83,333 net special-pay limit are taxed at 50% instead of being moved into ordinary income. | Dossier §§2.6, 4; `austria.py:41-44,60`. |
| High | Confirmed mismatch | Employer SV | A blended 20.38% ignores distinct 21.23% regular and 20.48% special rates and uses the wrong ceilings. | Dossier §5.2; `austria.py:38,64`. |
| Medium | Confirmed mismatch | Employer charges | The module omits the fixed EUR106 Vienna DGA. BV/DB/DZ/municipal bases otherwise match the selected no-small-payroll-relief scenario. | Dossier §§3, 5.2; `austria.py:39,65`. |
| Low | Scenario difference | DZ/location | 0.36% is the dossier's explicit Vienna DZ selection; it is not nationally universal. | Dossier §3; `austria.py:39`. |

## Matches

- The seven ordinary tax brackets and 14-equal-payment convention match.
- DB 3.70%, Vienna DZ 0.36%, municipal tax 3%, and BV 1.53% match the selected scenario.

## Output impact

| Gross EUR | Module net | Dossier net | Net delta | Module cost | Dossier cost | Cost delta |
|---:|---:|---:|---:|---:|---:|---:|
| 20,000 | 16,282.75 | 17,984.29 | -1,701.54 | 25,794.00 | 26,048.57 | -254.57 |
| 60,000 | 41,020.47 | 41,024.70 | -4.23 | 77,382.00 | 77,933.71 | -551.71 |
| 100,000 | 63,039.11 | 62,631.05 | +408.06 | 127,506.72 | 129,189.40 | -1,682.68 |
| 200,000 | 119,878.62 | 119,355.24 | +523.38 | 236,096.72 | 237,779.40 | -1,682.68 |
| 600,000 | 330,160.39 | 329,577.93 | +582.46 | 670,456.72 | 672,139.40 | -1,682.68 |

## Recommended disposition

Replace blended SV and credit logic with payment-type and income-sensitive rules; update final ceilings; implement the statutory special-payment overflow; add DGA as an explicit Vienna scenario input.

## Regression vectors

Use all five dossier rows. The EUR20k negative-tax case and EUR600k EUR15.38 special-payment overflow are essential boundary vectors; EUR100k tests both contribution ceilings.
