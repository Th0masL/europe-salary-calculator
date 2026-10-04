# Hungary — implementation comparison

## Compared artifacts

- Independent dossier: `docs/research/2026/hungary.md`
- Current implementation: `tools/calc/hungary.py`
- Comparison date: 2026-10-04

## Current implementation scenario

The computation is the ordinary resident employee baseline: 15% SZJA on gross, 18.5% employee social-security contribution, and 13% employer szocho, with no personal/family/age relief. All applicable rules are uncapped percentages, so the implementation correctly applies them directly to the comparison table's EUR input.

## Findings

| Severity | Classification | Area | Finding | Evidence / code |
|---|---|---|---|---|
| Low | Product decision | Rehabilitation contribution | The employer-wide rehabilitation contribution is conditional on headcount and disabled-worker quota, so its exclusion is defensible for a per-employee statutory baseline, but the limitation should be surfaced. | Dossier §4; `hungary.py:33`. |

## Matches

- The 15% gross-basis SZJA, 18.5% uncapped employee contribution, and 13% uncapped szocho all match.
- Calculation order and all five local-currency numeric outputs match exactly.
- Direct EUR calculation matches the comparison table's agreed currency contract and is valid because no applicable rule contains a nominal HUF threshold, cap, deduction, or rounding step.
- No 13th-month amount is added on top of entered annual gross.

## Output impact

The local-currency dossier vectors and direct-EUR implementation produce the same ratios:

| Gross HUF | Impl. net | Dossier net | Δ net | Impl. cost | Dossier cost | Δ cost |
|---:|---:|---:|---:|---:|---:|---:|
| 8,000,000 | 5,320,000 | 5,320,000 | 0 | 9,040,000 | 9,040,000 | 0 |
| 24,000,000 | 15,960,000 | 15,960,000 | 0 | 27,120,000 | 27,120,000 | 0 |
| 40,000,000 | 26,600,000 | 26,600,000 | 0 | 45,200,000 | 45,200,000 | 0 |
| 80,000,000 | 53,200,000 | 53,200,000 | 0 | 90,400,000 | 90,400,000 | 0 |
| 240,000,000 | 159,600,000 | 159,600,000 | 0 | 271,200,000 | 271,200,000 | 0 |

Within the documented scenario, skipping an HUF conversion avoids needless FX-rate sensitivity and does not change the result. This must be revisited if a nominal HUF rule is added later.

## Recommended disposition

Keep the EUR module contract and document why this scenario is currency-invariant. Keep rehabilitation contribution explicitly out of the employee marginal-cost baseline.

## Regression vectors

Assert `CURRENCY == "EUR"` and comparison-table vectors `(gross EUR → employer_cost, net)`: `20,000 → 22,600, 13,300`; `200,000 → 226,000, 133,000`; `600,000 → 678,000, 399,000`. Retain the dossier's HUF vectors as ratio checks.

## Implementation update

The arithmetic is retained for the age-40 ordinary-employment profile. The
employer note now explicitly excludes the conditional employer-wide
rehabilitation contribution.
