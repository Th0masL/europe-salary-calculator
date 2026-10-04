# Turkey — implementation comparison

## Compared artifacts

- Independent dossier: `docs/research/2026/turkey.md`
- Current implementation: `tools/calc/turkey.py`
- Comparison date: 2026-10-04

## Implementation update — 2026-10-04

The employer SGK rate was corrected to 21.75% and regression-tested against the
TRY 5,000,000 dossier vector. The finding below is retained as audit history.

## Current implementation scenario

Resident single employee, 12 equal pays, no employer incentives. Employee-side treatment matches the dossier.

## Findings

| Severity | Classification | Area | Finding | Evidence / code |
|---|---|---|---|---|
| High | Confirmed mismatch | Employer SGK | Module uses 20.75% employer SGK; the unincentivised 2026 rate is 21.75%, plus 2% unemployment. Employer cost is understated by 1% of the SGK base. | Dossier §2; `ER_SGK=0.2075`. |

## Matches

2026 SGK minimum/maximum, employee 14%+1%, cumulative wage tariff, minimum-wage income/stamp exemptions, 0.759% stamp rate, and employee net match all five vectors exactly.

## Output impact

| Gross TRY | Net delta | Module cost | Dossier cost | Cost delta |
|---:|---:|---:|---:|---:|
| 1,000,000 | 0.00 | 1,227,500.00 | 1,237,500.00 | -10,000.00 |
| 3,000,000 | 0.00 | 3,682,500.00 | 3,712,500.00 | -30,000.00 |
| 5,000,000 | 0.00 | 5,811,547.10 | 5,847,219.50 | -35,672.40 |
| 10,000,000 | 0.00 | 10,811,547.10 | 10,847,219.50 | -35,672.40 |
| 30,000,000 | 0.00 | 30,811,547.10 | 30,847,219.50 | -35,672.40 |

## Recommended disposition

Change the unincentivised employer SGK rate to 21.75%; parameterize discounts separately if later supported.

## Regression vectors

Use all five dossier rows and SGK base boundaries TRY 33,030 and 297,270 monthly; assert full employer total 23.75%.
