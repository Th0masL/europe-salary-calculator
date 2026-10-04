# Hungary — implementation comparison

## Compared artifacts

- Independent dossier: `docs/research/2026/hungary.md`
- Current implementation: `tools/calc/hungary.py`
- Comparison date: 2026-10-04

## Current implementation scenario

The computation is the ordinary resident employee baseline: 15% SZJA on gross, 18.5% employee social-security contribution, and 13% employer szocho, with no personal/family/age relief. However, the module declares EUR even though the country and dossier vectors are HUF.

## Findings

| Severity | Classification | Area | Finding | Evidence / code |
|---|---|---|---|---|
| Critical | Confirmed mismatch | Currency metadata | `CURRENCY = "EUR"` contradicts the statutory HUF unit and causes the surrounding FX/product layer to label or convert Hungarian amounts incorrectly. Percentage invariance does not make monetary inputs currency-invariant. | Dossier §§1, 5; `hungary.py:10-13,19,29`. |
| Low | Product decision | Rehabilitation contribution | The employer-wide rehabilitation contribution is conditional on headcount and disabled-worker quota, so its exclusion is defensible for a per-employee statutory baseline, but the limitation should be surfaced. | Dossier §4; `hungary.py:33`. |

## Matches

- The 15% gross-basis SZJA, 18.5% uncapped employee contribution, and 13% uncapped szocho all match.
- Calculation order and all five local-currency numeric outputs match exactly.
- No 13th-month amount is added on top of entered annual gross.

## Output impact

Direct local-number calls produce the right ratios but under the wrong currency metadata:

| Gross HUF | Impl. net | Dossier net | Δ net | Impl. cost | Dossier cost | Δ cost |
|---:|---:|---:|---:|---:|---:|---:|
| 8,000,000 | 5,320,000 | 5,320,000 | 0 | 9,040,000 | 9,040,000 | 0 |
| 24,000,000 | 15,960,000 | 15,960,000 | 0 | 27,120,000 | 27,120,000 | 0 |
| 40,000,000 | 26,600,000 | 26,600,000 | 0 | 45,200,000 | 45,200,000 | 0 |
| 80,000,000 | 53,200,000 | 53,200,000 | 0 | 90,400,000 | 90,400,000 | 0 |
| 240,000,000 | 159,600,000 | 159,600,000 | 0 | 271,200,000 | 271,200,000 | 0 |

The end-user impact of the metadata error depends on the shared FX path and is potentially orders of magnitude; it is not represented by the zero local-number deltas.

## Recommended disposition

Change the currency contract to HUF and let the shared layer perform the normal HUF conversion. Keep rehabilitation contribution explicitly out of the employee marginal-cost baseline.

## Regression vectors

Assert both `CURRENCY == "HUF"` and `(gross HUF → employer_cost, net)`: `8,000,000 → 9,040,000, 5,320,000`; `24,000,000 → 27,120,000, 15,960,000`; `40,000,000 → 45,200,000, 26,600,000`; `80,000,000 → 90,400,000, 53,200,000`; `240,000,000 → 271,200,000, 159,600,000`.
