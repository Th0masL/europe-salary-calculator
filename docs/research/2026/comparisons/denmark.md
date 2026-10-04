# Denmark — 2026 implementation comparison

## Compared artifacts

- Dossier: `docs/research/2026/denmark.md` (official SKAT/Ministry/ATP sources, accessed 2026-10-04).
- Implementation: `tools/calc/denmark.py`.

## Current implementation scenario

Single non-church employee, national-average municipality and full-rate ATP. Employer funds are compressed into a representative DKK9,700 annual constant.

## Findings

| Severity | Classification | Area | Finding | Evidence / code |
|---|---|---|---|---|
| Critical | Confirmed mismatch | Tax bases/order | The module subtracts personal allowance and employment deduction from one base taxed by both bottom and municipal tax. Officially, bottom tax uses personal income less personal allowance; employment/job deductions reduce municipal taxable income only. | Dossier §§1, 3.1; `denmark.py:49-59`. |
| High | Confirmed mismatch | Employment deductions | The module uses a 2025 estimate, 10.65% capped DKK45,100, and omits job allowance. Final 2026 values are 12.75% capped DKK63,300 plus 4.5% above DKK235,200 capped DKK3,100. | Dossier §§1, 3.1; `denmark.py:14-17,37-38,53`. |
| High | Confirmed mismatch | Deduction base | Employment/job deductions use `G + employer ATP` in the dossier, not `G - employee ATP`; this changes their base by the total DKK3,564 ATP remittance. | Dossier §3.1; `denmark.py:49,53`. |
| High | Unsupported assumption | Employer funds | DKK9,700 is not an official universal per-worker amount. AUB relief, AES group, maternity scheme, holiday administration and insurance are conditional; the dossier's illustrative determinable selection is DKK5,806 plus employer ATP (DKK8,182 total), before unresolved accident insurance. | Dossier §2; `denmark.py:5-8,34,62`. |
| Medium | Scenario difference | Municipality | 25.049% is the official weighted average, not an employee's actual municipality. | Dossier §§1.5, 4; `denmark.py:40`. |

## Matches

- ATP employee/employer amounts, AM 8% and its base, personal allowance, bottom/high-income rates and thresholds match.
- The module correctly discloses the national-average municipal scenario and sector variability, though it should not collapse the latter into a total.

## Output impact

Employer delta compares two illustrative scenarios, not universal legal totals; both exclude an exact insurance premium.

| Gross DKK | Module net | Dossier net | Net delta | Module cost | Dossier known-cost scenario | Delta |
|---:|---:|---:|---:|---:|---:|---:|
| 150,000 | 112,092.87 | 111,086.08 | +1,006.79 | 162,076 | 158,182 | +3,894 |
| 450,000 | 296,650.35 | 295,161.01 | +1,489.34 | 462,076 | 458,182 | +3,894 |
| 750,000 | 466,789.48 | 466,708.41 | +81.07 | 762,076 | 758,182 | +3,894 |
| 1,500,000 | 804,256.85 | 804,175.78 | +81.07 | 1,512,076 | 1,508,182 | +3,894 |
| 4,500,000 | 2,050,118.10 | 2,050,037.03 | +81.07 | 4,512,076 | 4,508,182 | +3,894 |

## Recommended disposition

Separate bottom and municipal bases, update both deductions and their ATP-inclusive base, and calculate the tax ceiling where required. Replace DKK9,700 with itemized conditional employer inputs and label any selected bundle as illustrative.

## Regression vectors

Use all five dossier rows. DKK150k isolates lower-income base order; DKK450k tests both deductions; DKK750k/1.5m/4.5m cross middle, top and additional-top thresholds.
