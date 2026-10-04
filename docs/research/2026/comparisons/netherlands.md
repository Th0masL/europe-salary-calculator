# Netherlands — implementation comparison

## Compared artifacts

- Independent dossier: `docs/research/2026/netherlands.md`
- Current implementation: `tools/calc/netherlands.py`
- Comparison date: 2026-10-04

## Current implementation scenario

The employee side is the dossier's resident, under-AOW, no-30%-facility case and treats entered gross as including holiday allowance. Employer cost combines approximate statutory premiums with a representative occupational-pension assumption. The dossier instead keeps non-universal pension/CAO costs unresolved and provides coherent statutory small/large-employer scenarios.

## Findings

| Severity | Classification | Area | Finding | Evidence / code |
|---|---|---|---|---|
| High | Unsupported assumption | Occupational pension | A flat 11.5% employer pension up to €92,000 is neither universal nor tied to a named fund/CAO and conflicts with the module's stated “no occupational pension” employee scenario. It adds €2,300–€10,580 to the vectors. | Dossier §§1, 4–5; `netherlands.py:3,14-15,19,43-44,71`. |
| High | Unsupported assumption | Statutory employer premiums | The 16.74% aggregate, €78,000 cap, and 1% Whk proxy do not represent a reproducible 2026 employer. The dossier's low-Awf small-employer scenario is 16.77% to €79,409; its high-Awf/large scenario is 23.49%. | Dossier §§3, 5; `netherlands.py:12-13,41-42,70`. |
| Low | Product decision | Employee rounding | The dossier rounds final annual levy to whole euros; the module returns cents. Numeric differences are at most €0.47 in these vectors. | Dossier §§1, 5; `netherlands.py:65-68`. |
| Low | Scenario difference | Holiday allowance | Both include holiday allowance in entered gross. A base-salary input would require an explicit 8% calculation subject to statutory/contractual exceptions. | Dossier §4; `netherlands.py:20`. |

## Matches

- Box 1 thresholds/rates, general credit and labour-credit formulas match.
- Employee net matches every authoritative vector to annual whole-euro rounding.
- No separate employee social contribution is incorrectly deducted.

## Output impact

Employer comparison uses dossier scenario A (small employer, permanent written contract, low Awf, no pension); `Δ = implementation − dossier`, EUR:

| Gross | Impl. net | Dossier net | Δ net | Impl. cost | Dossier A cost | Δ cost |
|---:|---:|---:|---:|---:|---:|---:|
| 20,000 | 19,452.57 | 19,453 | -0.43 | 25,648.00 | 23,354.00 | +2,294.00 |
| 60,000 | 44,093.53 | 44,094 | -0.47 | 76,944.00 | 70,062.00 | +6,882.00 |
| 100,000 | 62,710.89 | 62,711 | -0.11 | 123,637.20 | 113,316.89 | +10,320.31 |
| 200,000 | 111,067.85 | 111,068 | -0.15 | 223,637.20 | 213,316.89 | +10,320.31 |
| 600,000 | 313,067.85 | 313,068 | -0.15 | 623,637.20 | 613,316.89 | +10,320.31 |

Scenario B employer costs are €24,698; €74,094; €118,653.17; €218,653.17; and €618,653.17. Neither scenario includes unresolved occupational pension/CAO cost.

## Recommended disposition

Keep the employee calculation, apply statutory final rounding, and replace the blended employer estimate with named selectable scenarios. Pension should be a separate plan input, never embedded as a universal statutory charge.

## Regression vectors

Employee net vectors: `20,000 → 19,453`; `60,000 → 44,094`; `100,000 → 62,711`; `200,000 → 111,068`; `600,000 → 313,068`. Scenario A costs: `23,354.00`, `70,062.00`, `113,316.89`, `213,316.89`, `613,316.89`; scenario B costs: `24,698.00`, `74,094.00`, `118,653.17`, `218,653.17`, `618,653.17` in the same gross order.
