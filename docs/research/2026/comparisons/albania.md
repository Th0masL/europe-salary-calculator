# Albania — 2026 implementation comparison

## Compared artifacts

- Independent dossier: `docs/research/2026/albania.md` (official-source clean-room reconstruction, accessed 2026-10-04).
- Implementation: `tools/calc/albania.py`.

## Implementation update — 2026-10-04

The signed-declaration personal deduction and 13%/23% taxable-income schedule are
now implemented for twelve equal payments. Dossier vectors at ALL 2m, 6m and 60m
are regression-tested. Unusual or partial-month contribution-floor cases remain
outside the representative annual-salary scenario.

## Current implementation scenario

Resident ordinary employee, twelve regular payments; annual gross in ALL. Social insurance is floored/capped monthly after annualisation, health is uncapped, and PIT is computed directly on gross using an old monthly withholding table.

## Findings

| Severity | Classification | Area | Finding | Evidence / code |
|---|---|---|---|---|
| High | Confirmed mismatch | PIT base and bands | The module taxes gross at 0%/13%/23% with annual breaks ALL 360,000/1,800,000. Law 29/2023 instead deducts ALL 30,000 per month and applies 13% through annual taxable income ALL 2,040,000, then 23%. This is a base-and-band error, not rounding. | Dossier §§1, 3; `albania.py:30-38`. |
| Low | Unsupported assumption | Contribution floor | `max(gross, 600,000)` treats a sub-floor annual salary as twelve full contribution months. The dossier says floors are monthly and part-month/irregular cases require payroll facts. It does not affect the five vectors. | Dossier §§4-5; `albania.py:24-25,36`. |

## Matches

- Employee social 9.5%, employee health 1.7%, employer social 15%, employer health 1.7%, the ALL 186,416 monthly social ceiling, and uncapped health match.
- At the regular equal-payment vectors, employee contributions and employer cost match exactly.

## Output impact

| Gross ALL | Module net | Dossier net | Net delta | Module cost | Dossier cost | Cost delta |
|---:|---:|---:|---:|---:|---:|---:|
| 2,000,000 | 1,542,800.00 | 1,562,800.00 | -20,000.00 | 2,334,000.00 | 2,334,000.00 | 0.00 |
| 6,000,000 | 4,532,285.76 | 4,592,285.76 | -60,000.00 | 6,437,548.80 | 6,437,548.80 | 0.00 |
| 10,000,000 | 7,544,285.76 | 7,604,285.76 | -60,000.00 | 10,505,548.80 | 10,505,548.80 | 0.00 |
| 20,000,000 | 15,074,285.76 | 15,134,285.76 | -60,000.00 | 20,675,548.80 | 20,675,548.80 | 0.00 |
| 60,000,000 | 45,194,285.76 | 45,254,285.76 | -60,000.00 | 61,355,548.80 | 61,355,548.80 | 0.00 |

## Recommended disposition

Replace the PIT schedule with the statutory deduction-plus-taxable-income schedule. Preserve the contribution code for the stated twelve-equal-payment scenario; document that other payment patterns require monthly computation.

## Regression vectors

The five dossier rows above are authoritative for regular equal monthly pay. In particular, ALL 6,000,000 must yield contributions ALL 314,514.24, PIT ALL 1,093,200, net ALL 4,592,285.76, and cost ALL 6,437,548.80.
