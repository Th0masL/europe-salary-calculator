# Lithuania — implementation comparison

## Compared artifacts

- Independent dossier: `docs/research/2026/lithuania.md`
- Current implementation: `tools/calc/lithuania.py`
- Comparison date: 2026-10-04

## Current implementation scenario

Both artifacts model a resident employee not making an additional second-pillar contribution. The dossier selects accident class I (0.14%) and follows monthly contribution/PIT withholding plus annual PIT reconciliation.

## Findings

| Severity | Classification | Area | Finding | Evidence / code |
|---|---|---|---|---|
| High | Confirmed mismatch | NPD | The implementation acknowledges but does not calculate NPD. At €20,000 the annual NPD is €5,943.64 and raises final net by €1,188.74. | Dossier §§2, 6; `lithuania.py:9-11,40`. |
| High | Confirmed mismatch | Employer components | The module uses 1.77% permanent unemployment plus an assumed 0.4% accident rate. For the dossier's ordinary indefinite contract the official rates are 1.31% unemployment and accident class I 0.14%; those two components are capped, while the 0.16% guarantee and 0.16% long-term funds remain uncapped. | Dossier §§4, 6; `lithuania.py:12-14,33,43`. |
| Low | Scenario difference | Monthly rounding | The annual formula misses cent-level differences from monthly sequencing and annual reconciliation, visible at €100k and above. | Dossier §§5–6; `lithuania.py:37-43`. |

## Matches

- Employee VSD 12.52% to 60 VDU and uncapped PSD 6.98% match.
- PIT is charged on gross, with 20%/25%/32% bands at 36 and 60 VDU; contributions are not deducted.
- The no-additional-second-pillar scenario matches.

## Output impact

`Δ = implementation − dossier`, EUR:

| Gross | Impl. net | Dossier net | Δ net | Impl. cost | Dossier cost | Δ cost |
|---:|---:|---:|---:|---:|---:|---:|
| 20,000 | 12,100.00 | 13,288.74 | -1,188.74 | 20,498.00 | 20,354.00 | +144.00 |
| 60,000 | 36,300.00 | 36,300.00 | 0.00 | 61,494.00 | 61,062.00 | +432.00 |
| 100,000 | 59,661.85 | 59,661.86 | -0.01 | 102,490.00 | 101,770.00 | +720.00 |
| 200,000 | 118,544.01 | 118,544.05 | -0.04 | 204,980.00 | 202,651.59 | +2,328.41 |
| 600,000 | 362,624.01 | 362,624.03 | -0.02 | 614,940.00 | 603,931.57 | +11,008.43 |

## Recommended disposition

Implement annual NPD and the four employer components separately, including the two different ceiling treatments and selectable accident class. Reconcile annual PIT rather than presenting withholding as final tax.

## Regression vectors

For accident class I, ordinary indefinite employment, and no second-pillar addition, assert: `20,000 → 20,354.00, 13,288.74`; `60,000 → 61,062.00, 36,300.00`; `100,000 → 101,770.00, 59,661.86`; `200,000 → 202,651.59, 118,544.05`; `600,000 → 603,931.57, 362,624.03`.
