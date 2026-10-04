# Malta — implementation comparison

## Compared artifacts

- Independent dossier: `docs/research/2026/malta.md`
- Current implementation: `tools/calc/malta.py`
- Comparison date: 2026-10-04

## Implementation update — 2026-10-04

PIT is now charged on total taxable gross, while weekly SSC and maternity charges
use basic pay excluding the EUR 512.52 statutory payments. The total-gross input
convention is documented and the dossier's EUR 20k/60k/100k vectors are tested.

## Current implementation scenario

Annual gross is total taxable cash including the statutory €512.52 bonuses. The dossier treats those bonuses as non-basic pay for Class 1 SSC but as taxable emoluments for PIT; regular basic pay is spread over 52 weeks.

## Findings

| Severity | Classification | Area | Finding | Evidence / code |
|---|---|---|---|---|
| Critical | Confirmed mismatch | PIT base | Employee Class 1 SSC is not deductible from employment income. The module taxes `gross − SSC`, overstating net by €448.96–€1,017.93 in the vectors. Its own comment and docstring conflict over the tax base. | Dossier §§1, 6; `malta.py:8-12,42-43,50`. |
| Medium | Confirmed mismatch | SSC/MLTF base | Weekly SSC and maternity contributions apply to basic weekly wage, excluding the statutory bonuses. At €20k total gross, the module applies 10%/0.3% to all gross and overstates employer cost by €52.80; capped higher rows happen to agree. | Dossier §§2–3, 6; `malta.py:34-40,48-49`. |
| Low | Scenario difference | Gross definition | If a product input means basic salary rather than total gross, €512.52 must be added before PIT/net. The dossier and comparison use total annual gross; the UI must state that convention. | Dossier §§1, 6; `malta.py:20-21`. |

## Matches

- Single PIT bands and marginal rates match.
- The €55.93 weekly employee/employer SSC cap and €1.68 weekly maternity cap match.
- Employer cost matches exactly from €60k upward because both weekly charges are capped.

## Output impact

`Δ = implementation − dossier`, EUR:

| Gross | Impl. net | Dossier net | Δ net | Impl. cost | Dossier cost | Δ cost |
|---:|---:|---:|---:|---:|---:|---:|
| 20,000 | 16,900.00 | 16,451.04 | +448.96 | 22,060.00 | 22,007.20 | +52.80 |
| 60,000 | 46,218.73 | 45,491.64 | +727.09 | 62,995.72 | 62,995.72 | 0.00 |
| 100,000 | 72,509.57 | 71,491.64 | +1,017.93 | 102,995.72 | 102,995.72 | 0.00 |
| 200,000 | 137,509.57 | 136,491.64 | +1,017.93 | 202,995.72 | 202,995.72 | 0.00 |
| 600,000 | 397,509.57 | 396,491.64 | +1,017.93 | 602,995.72 | 602,995.72 | 0.00 |

## Recommended disposition

Calculate PIT on total taxable gross, then calculate SSC and maternity from basic weekly wage. Make total-gross versus basic-salary input semantics explicit.

## Regression vectors

For total gross including €512.52 statutory bonuses, assert: `20,000 → 22,007.20, 16,451.04`; `60,000 → 62,995.72, 45,491.64`; `100,000 → 102,995.72, 71,491.64`; `200,000 → 202,995.72, 136,491.64`; `600,000 → 602,995.72, 396,491.64`.
