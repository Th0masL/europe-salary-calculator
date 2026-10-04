# Latvia — implementation comparison

## Compared artifacts

- Independent dossier: `docs/research/2026/latvia.md`
- Current implementation: `tools/calc/latvia.py`
- Comparison date: 2026-10-04

## Implementation update — 2026-10-04

The EUR6,600 minimum, full cash VSAOI, solidarity allocation, separate 3% annual
tax, employer reconciliation refund and risk fee are implemented. Final annual
net and post-reconciliation employer cost match the five dossier vectors.

## Current implementation scenario

The module treats the €105,300 social maximum as a cash cap for both employee and employer contributions and runs a conventional progressive tax over `gross − capped employee NSIC`. Latvian solidarity-tax accounting does not work that way.

## Findings

| Severity | Classification | Area | Finding | Evidence / code |
|---|---|---|---|---|
| Critical | Confirmed mismatch | Non-taxable minimum | The universal 2026 €550 monthly/€6,600 annual non-taxable minimum is omitted. Net is understated by €1,683 (=25.5% × €6,600) at €20k, €60k and €100k. | Dossier §§1, 4; `latvia.py:7-8,32`. |
| Critical | Confirmed mismatch | Solidarity/cash withholding | Employee cash withholding remains 10.5% and employer initial payment 23.59% on all gross above €105,300; the module caps both. Employer receives a later 9.09%-of-excess reconciliation refund, not an immediate ordinary-contribution cap. | Dossier §§2–4; `latvia.py:4,9-11,31,36`. |
| High | Confirmed mismatch | PIT base/order | Deductions are allocated to lower-rate income under the statute; the module subtracts contributions from gross and then shifts the progressive threshold. Above the social maximum it also fails to remove the 10% solidarity allocation from the deductible contribution. | Dossier §§1–4; `latvia.py:31-33`. |
| High | Confirmed mismatch | Additional 3% | The additional 3% is a separate annual tax on the statutory aggregate over €200,000, not a 36% marginal band beginning when post-deduction taxable income reaches €200,000. | Dossier §§1, 4; `latvia.py:26,33`. |
| Low | Confirmed mismatch | Business-risk fee | The €0.36 monthly (€4.32 annual) employer risk fee is absent. | Dossier §§2, 4; `latvia.py:36`. |

## Matches

- Ordinary employee/employer cash rates 10.5%/23.59%, annual social maximum €105,300, and PIT headline rates 25.5%/33% are present.
- Gross includes ordinary cash remuneration; no pension-choice deduction is assumed.

## Output impact

Employer cost uses the dossier's final post-reconciliation cost; `Δ = implementation − dossier`, EUR:

| Gross | Impl. net | Dossier net | Δ net | Impl. cost | Dossier cost | Δ cost |
|---:|---:|---:|---:|---:|---:|---:|
| 20,000 | 13,335.50 | 15,018.50 | -1,683.00 | 24,718.00 | 24,722.32 | -4.32 |
| 60,000 | 40,006.50 | 41,689.50 | -1,683.00 | 74,154.00 | 74,158.32 | -4.32 |
| 100,000 | 66,677.50 | 68,360.50 | -1,683.00 | 123,590.00 | 123,594.32 | -4.32 |
| 200,000 | 134,489.65 | 134,990.65 | -501.00 | 224,840.27 | 238,576.09 | -13,735.82 |
| 600,000 | 390,821.34 | 389,500.65 | +1,320.69 | 624,840.27 | 696,576.09 | -71,735.82 |

Cash-year employer costs are €247,184.32 and €741,544.32 at €200k/€600k, respectively; the final figures above incorporate the later refund.

## Recommended disposition

Model ordinary VSAOI cash flow, solidarity allocation/reconciliation, annual NPM, and the separate 3% assessment explicitly. Expose cash-year versus final employer cost rather than collapsing them into a capped contribution.

## Regression vectors

For final annual employee cash and post-reconciliation employer cost, assert: `20,000 → 24,722.32, 15,018.50`; `60,000 → 74,158.32, 41,689.50`; `100,000 → 123,594.32, 68,360.50`; `200,000 → 238,576.09, 134,990.65`; `600,000 → 696,576.09, 389,500.65`. Also test cash-year cost `247,184.32` and `741,544.32` for the last two rows.
