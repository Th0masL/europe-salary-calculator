# Poland — implementation comparison

## Compared artifacts

- Independent dossier: `docs/research/2026/poland.md`
- Current implementation: `tools/calc/poland.py`
- Comparison date: 2026-10-04

## Implementation update — 2026-10-04

The 4% solidarity levy is now included in final annual net and tested below and
above its PLN 1m statutory-income threshold. The representative 1.67% accident
rate and no-PPK scenario remain fixed; payslip-level grosz differences are accepted
under the comparator's material-accuracy contract.

## Current implementation scenario

Resident single age-30 employee, one ordinary employment contract, standard PLN 3,000 expense, no PPK, and the dossier's 1.67% small-payer accident scenario. It uses annualized arithmetic rather than the dossier's monthly grosz calculation.

## Findings

| Severity | Classification | Area | Finding | Evidence / code |
|---|---|---|---|---|
| Critical | Confirmed mismatch | Solidarity levy | The module omits the 4% levy on qualifying income above PLN 1,000,000. At PLN 3m it overstates net by PLN 75,666.64 versus the dossier's monthly-rounded result. | Dossier §4 and row PLN 3m; `compute()` returns no solidarity item. |
| Low | Confirmed mismatch | Rounding | Contributions and PIT are calculated as annual floating-point products instead of monthly grosz and whole-złoty rules. Differences are PLN 0.16 to PLN 0.33 in net at the first four vectors and a few grosz in employer cost. | Dossier §§6–7; module annual formulas. |

## Matches

PIT bands/reduction, PLN 3,000 expense, capped pension/disability, uncapped sickness, health base/rate, employer rates, cap, and accident scenario agree materially. No-PPK is the same explicit scenario.

## Output impact

| Gross PLN | Module net | Dossier net | Net delta | Module employer cost | Dossier employer cost | Cost delta |
|---:|---:|---:|---:|---:|---:|---:|
| 100,000 | 72,129.10 | 72,128.94 | +0.16 | 120,480.00 | 120,480.05 | -0.05 |
| 300,000 | 182,449.25 | 182,449.55 | -0.30 | 358,610.76 | 358,610.76 | 0.00 |
| 500,000 | 297,558.25 | 297,558.58 | -0.33 | 567,050.76 | 567,050.72 | +0.04 |
| 1,000,000 | 585,330.75 | 585,331.08 | -0.33 | 1,088,150.76 | 1,088,150.80 | -0.04 |
| 3,000,000 | 1,736,420.75 | 1,660,754.11 | **+75,666.64** | 3,172,550.76 | 3,172,550.76 | 0.00 |

## Recommended disposition

Implement solidarity assessment and statutory rounding. Retain and label the 1.67% accident/no-PPK scenario.

## Regression vectors

Use all five dossier rows; especially PLN 1m (no levy) and PLN 3m (PLN 75,667 levy). Add cap-edge tests at PLN 282,600 and solidarity-base values immediately around PLN 1m.
