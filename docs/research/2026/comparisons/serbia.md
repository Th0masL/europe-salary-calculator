# Serbia — implementation comparison

## Compared artifacts

- Independent dossier: `docs/research/2026/serbia.md`
- Current implementation: `tools/calc/serbia.py`
- Comparison date: 2026-10-04

## Current implementation scenario

Single resident employee with 12 regular payments. Ordinary payroll is annualized; supplementary annual personal-income tax is explicitly excluded.

## Findings

| Severity | Classification | Area | Finding | Evidence / code |
|---|---|---|---|---|
| Critical | Confirmed mismatch | Annual tax | The statutory supplementary annual tax is omitted. Its exact 2026 threshold awaits the 2026 average salary, but omission materially overstates high-earner final net. | Dossier §3; module docstring. |
| High | Confirmed mismatch | Contribution ceiling | `MAX_BASE=700,000×12` is an estimate; the official 2026 monthly maximum is RSD 732,820 (annual RSD 8,793,840). | Dossier §2. |
| Medium | Confirmed mismatch | Contribution floor | The official monthly minimum RSD 51,297 is absent. It does not affect the five requested vectors. | Dossier §2; module uses only `min`. |

## Matches

The RSD 34,221 monthly salary-tax allowance, 10% salary tax, 19.9% employee split, 15.15% employer split, and ordinary-payroll results at RSD 2m/6m match.

## Output impact

These net figures exclude the unresolved supplementary annual tax in both columns.

| Gross RSD | Module ordinary net | Dossier ordinary net | Delta | Module employer cost | Dossier employer cost | Delta |
|---:|---:|---:|---:|---:|---:|---:|
| 2,000,000 | 1,443,065.20 | 1,443,065.20 | 0.00 | 2,303,000.00 | 2,303,000.00 | 0.00 |
| 6,000,000 | 4,247,065.20 | 4,247,065.20 | 0.00 | 6,909,000.00 | 6,909,000.00 | 0.00 |
| 10,000,000 | 7,369,465.20 | 7,291,091.04 | +78,374.16 | 11,272,600.00 | 11,332,266.76 | -59,666.76 |
| 20,000,000 | 16,369,465.20 | 16,291,091.04 | +78,374.16 | 21,272,600.00 | 21,332,266.76 | -59,666.76 |
| 60,000,000 | 52,369,465.20 | 52,291,091.04 | +78,374.16 | 61,272,600.00 | 61,332,266.76 | -59,666.76 |

## Recommended disposition

Fix the official ceiling and floor now. Implement the annual-tax formula with the official average salary as a versioned parameter, or label net “before supplementary annual tax” until the 2026 statistic is published.

## Regression vectors

Use the five ordinary-payroll rows, monthly bases RSD 51,297 and 732,820, and the dossier's symbolic annual-tax formula `Q/D/B/S(A)` once `A` is official.

## Implementation update

Implemented the official contribution floor and ceiling. The live result is
explicitly ordinary payroll before supplementary annual tax until the official
2026 average salary is published. Under the common age-40 profile, no under-40
additional annual-tax deduction will apply when that layer is completed.
