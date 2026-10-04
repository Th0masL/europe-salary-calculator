# Luxembourg — implementation comparison

## Compared artifacts

- Independent dossier: `docs/research/2026/luxembourg.md`
- Current implementation: `tools/calc/luxembourg.py`
- Comparison date: 2026-10-04

## Current implementation scenario

Both artifacts use tax class 1, no children, ordinary resident employment. The dossier treats €20,000 as a 60.7570% part-time minimum-wage case and otherwise uses 12 regular monthly payments. The module describes caps and approximations in comments but does not apply a contribution cap in code.

## Findings

| Severity | Classification | Area | Finding | Evidence / code |
|---|---|---|---|---|
| Critical | Confirmed mismatch | Social contribution cap | Employee pension/health and the employer aggregate are charged on all gross in the module. They must stop at the 2026 annual ceiling €164,589.81 for regular monthly pay. At €600k this alone drives very large errors. | Dossier §§2, 5; `luxembourg.py:10,33,36,65,73`. |
| High | Confirmed mismatch | Employer rate | The selected scenario's official component total is 12.57% on capped base; the module uses an unsupported approximate 13.05% and applies it uncapped. | Dossier §§2, 5; `luxembourg.py:15-16,30,36,73`. |
| High | Confirmed mismatch | Tax computation | The module omits the €480 special-expense minimum, statutory €50 taxable-income rounding, whole-euro tariff flooring, the 9% fund addition at high tax, and the CI-CO2 credit. | Dossier §§3, 5; `luxembourg.py:18-20,37-38,68-70`. |
| Medium | Confirmed mismatch | Dependency insurance | The annual abatement is €8,229.46 for the regular full-time cases, not €8,112; it is hours-prorated for the €20k part-time case. | Dossier §§2, 5; `luxembourg.py:35,66`. |
| Medium | Confirmed mismatch | Standard deductions | Taxable income subtracts both €540 employment expenses and €480 special expenses; only €540 is implemented. | Dossier §§3, 5; `luxembourg.py:37,68`. |

## Matches

- The 8.5% pension, 3.05% health and 1.4% dependency rates match.
- Dependency insurance is excluded from the income-tax deduction.
- The granular class-1 marginal scale and broad CIS shape are substantially aligned.

## Output impact

`Δ = implementation − dossier`, EUR:

| Gross | Impl. net | Dossier net | Δ net | Impl. cost | Dossier cost | Δ cost |
|---:|---:|---:|---:|---:|---:|---:|
| 20,000 | 17,523.57 | 17,992.00 | -468.43 | 22,610.00 | 22,514.00 | +96.00 |
| 60,000 | 43,798.09 | 44,104.21 | -306.12 | 67,830.00 | 67,542.00 | +288.00 |
| 100,000 | 63,570.71 | 63,786.21 | -215.50 | 113,050.00 | 112,570.00 | +480.00 |
| 200,000 | 113,078.05 | 115,356.09 | -2,278.04 | 226,100.00 | 220,688.94 | +5,411.06 |
| 600,000 | 302,906.38 | 327,234.09 | -24,327.71 | 678,300.00 | 620,688.94 | +57,611.06 |

## Recommended disposition

Implement each contribution on its statutory base and cap, then reproduce the ACD annual tariff sequence exactly, including deductions, rounding/flooring, fund addition and both refundable credits. Parameterise mutual-insurance class and accident rate if broader employer scenarios are added.

## Regression vectors

For the dossier scenario, assert: `20,000 → 22,514.00, 17,992.00`; `60,000 → 67,542.00, 44,104.21`; `100,000 → 112,570.00, 63,786.21`; `200,000 → 220,688.94, 115,356.09`; `600,000 → 620,688.94, 327,234.09`. The €20k vector must retain its explicit part-time status.
