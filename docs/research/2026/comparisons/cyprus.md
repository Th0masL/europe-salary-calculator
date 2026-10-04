# Cyprus — 2026 implementation comparison

## Compared artifacts

- Dossier: `docs/research/2026/cyprus.md` (official Ministry/Social Insurance/legal sources, accessed 2026-10-04).
- Implementation: `tools/calc/cyprus.py`.

## Current implementation scenario

Ordinary resident employee with an employer assumed exempt from the Central Holiday Fund (CHF). SI/GHS are deducted before PIT; capped employer funds, uncapped cohesion and capped GHS are added.

## Findings

| Severity | Classification | Area | Finding | Evidence / code |
|---|---|---|---|---|
| High | Unsupported assumption | Holiday Fund | The module silently assumes CHF exemption. Exemption depends on the employer's approved leave scheme; a non-exempt employer pays 8%, which also changes contribution earnings and employee net. | Dossier §§1, 7; omission from `cyprus.py:39-62`. |
| Medium | Product decision | Scenario exposure | The exempt scenario is fully correct, but the calculator needs an explicit CHF exemption/holiday-fund input or an unambiguous product scope. | Dossier §§6-7; `cyprus.py:48-62`. |

## Matches

- The module matches every employee rate, cap, PIT bracket/base, employer rate and base in the dossier's CHF-exempt scenario.
- All five primary scenario net and employer-cost outputs match to the cent.

## Output impact

| Gross EUR | Exempt module net/cost | Non-exempt dossier net | Net delta | Non-exempt cost | Cost delta |
|---:|---:|---:|---:|---:|---:|
| 20,000 | 17,710.00 / 23,080.00 | 17,526.80 | -183.20 | 24,926.40 | +1,846.40 |
| 60,000 | 45,291.00 / 69,240.00 | 44,906.28 | -384.72 | 74,779.20 | +5,539.20 |
| 100,000 | 71,036.19 / 112,134.92 | 70,941.24 | -94.95 | 117,917.34 | +5,782.42 |
| 200,000 | 134,658.19 / 216,454.92 | 134,658.19 | 0.00 | 222,077.49 | +5,622.57 |
| 600,000 | 394,658.19 / 624,454.92 | 394,658.19 | 0.00 | 630,077.49 | +5,622.57 |

The deltas are scenario differences, not errors in the implemented exempt formula.

## Recommended disposition

Retain the arithmetic and label the current outputs “CHF-exempt employer”; preferably add the official non-exempt path.

## Regression vectors

Use all five primary dossier rows for the exempt path and all five §7 rows for the non-exempt path. EUR100k tests the interaction of the CHF, the SI ceiling and the still-open GHS base.
