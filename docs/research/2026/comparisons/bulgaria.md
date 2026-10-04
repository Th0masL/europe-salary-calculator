# Bulgaria — 2026 implementation comparison

## Compared artifacts

- Dossier: `docs/research/2026/bulgaria.md` (official NRA/NSSI/legal sources, accessed 2026-10-04).
- Implementation: `tools/calc/bulgaria.py`.

## Current implementation scenario

EUR-denominated annual arithmetic, 13.78% employee and 18.52% employer core contributions, 0.5% office accident risk, and 10% PIT after employee contributions.

## Findings

| Severity | Classification | Area | Finding | Evidence / code |
|---|---|---|---|---|
| High | Confirmed mismatch | 2026 ceiling | The module holds the EUR2,111.64 monthly maximum for all twelve months. The official maximum rises to EUR2,300 from August; the equal-pay annual ceiling is EUR26,281.48 (BGN51,402.11), not EUR25,339.68. | Dossier §§2.2, 3; `bulgaria.py:27,35`. |
| Low | Scenario difference | Accident risk | 0.5% is a selected office-risk value. The dossier uses KID 82 at 0.4% for January-July and 0.5% thereafter; the statutory range is employer-activity-specific. | Dossier §§2.3, 3; `bulgaria.py:16-17,29`. |
| Low | Product decision | Currency | The module exposes EUR after euro adoption while the dossier retains the official BGN payroll grid for traceability. This is not itself a tax mismatch if conversion is exact. | Dossier §1; `bulgaria.py:22-24`. |

## Matches

- Employee 13.78%, employer core 18.52%, 10% PIT, and deduction of employee contributions before PIT match.
- Contributions are correctly capped while PIT remains uncapped.

## Output impact

For direct local-currency comparison, module EUR outputs were converted at the fixed EUR1 = BGN1.95583. At BGN40k the net matches; the BGN23.33 cost delta is the risk-rate timing. Above the cap:

| Gross BGN | Module net | Dossier net | Net delta | Module cost | Dossier cost | Cost delta |
|---:|---:|---:|---:|---:|---:|---:|
| 120,000 | 101,853.56 | 101,625.11 | +228.45 | 129,426.33 | 129,747.77 | -321.44 |
| 200,000 | 173,853.56 | 173,625.11 | +228.45 | 209,426.33 | 209,747.77 | -321.44 |
| 400,000 | 353,853.56 | 353,625.11 | +228.45 | 409,426.33 | 409,747.77 | -321.44 |
| 1,200,000 | 1,073,853.56 | 1,073,625.11 | +228.45 | 1,209,426.33 | 1,209,747.77 | -321.44 |

## Recommended disposition

Implement the January-July/August-December monthly ceilings and expose accident risk/activity. Preserve contribution-before-PIT order.

## Regression vectors

BGN40,000 tests below-cap arithmetic; BGN120,000 and above must converge to employee contributions BGN7,083.21 and employer contributions BGN9,747.77 under the dossier's KID 82 scenario.
