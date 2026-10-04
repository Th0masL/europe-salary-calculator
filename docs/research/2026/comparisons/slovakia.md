# Slovakia — implementation comparison

## Compared artifacts

- Independent dossier: `docs/research/2026/slovakia.md`
- Current implementation: `tools/calc/slovakia.py`
- Comparison date: 2026-10-04

## Current implementation scenario

Single ordinary employee, annualized regular salary. The module assumes the taxpayer allowance is zero for every supported salary and excludes employer financial-transaction tax.

## Findings

| Severity | Classification | Area | Finding | Evidence / code |
|---|---|---|---|---|
| High | Confirmed mismatch | NČZD | At EUR 20k the 2026 allowance is EUR 5,966.73; the module omits it and understates net by EUR 1,133.89. | Dossier §1 and worked table. |
| Low | Confirmed mismatch | Payroll rounding | Statutory per-fund/month downward rounding is not implemented, causing cent-level differences at other vectors. | Dossier §6. |
| Low | Product decision | DFT | Employer financial-transaction tax is not represented. The dossier correctly leaves it variable because it cannot be derived per employee. | Dossier §5. |

## Matches

The four PIT bands, employee/employer social and health rates, EUR 16,764 monthly social ceiling, uncapped accident/health, and employer cost structure materially agree.

## Output impact

| Gross EUR | Module net | Dossier net | Delta | Module cost | Dossier cost excl. DFT | Delta |
|---:|---:|---:|---:|---:|---:|---:|
| 20,000 | 13,867.20 | 15,001.09 | **-1,133.89** | 27,240.00 | 27,239.57 | +0.43 |
| 60,000 | 41,159.00 | 41,159.00 | 0.00 | 81,720.00 | 81,720.00 | 0.00 |
| 100,000 | 65,046.98 | 65,047.21 | -0.23 | 136,200.00 | 136,199.47 | +0.53 |
| 200,000 | 120,686.98 | 120,687.14 | -0.16 | 272,400.00 | 272,399.57 | +0.43 |
| 600,000 | 367,615.61 | 367,615.66 | -0.05 | 719,884.99 | 719,884.92 | +0.07 |

## Recommended disposition

Implement the income-dependent NČZD and payroll rounding. Retain DFT as a documented employer-level variable.

## Regression vectors

Use all five dossier rows; add §5-base tests at EUR 26,083.13 and where `14,661.11-B/3` reaches zero, plus monthly social base EUR 16,764.
