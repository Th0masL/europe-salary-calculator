# Slovenia — implementation comparison

## Compared artifacts

- Independent dossier: `docs/research/2026/slovenia.md`
- Current implementation: `tools/calc/slovenia.py`
- Comparison date: 2026-10-04

## Implementation update — 2026-10-04

LTC and split-year OZP now reduce the PIT base, the correct EUR 467.94 OZP is used,
and the two full-year minimum regresses are included in employer cash cost. The
below-range contribution-floor case remains unsupported by the annual input model.

## Current implementation scenario

Single age-30 employee; salary-only cost. The module deducts ordinary 22.1% contributions for PIT but explicitly leaves LTC and OZP outside the PIT base deduction.

## Findings

| Severity | Classification | Area | Finding | Evidence / code |
|---|---|---|---|---|
| High | Confirmed mismatch | PIT base | Both mandatory 1% LTC and fixed OZP reduce the Article 41 employment tax base; the module excludes both. | Dossier §§1.2, 2.2–2.3. |
| Medium | Confirmed mismatch | OZP | `39.36×12=472.32` is wrong for 2026: Jan–Feb are EUR 37.17 and Mar–Dec EUR 39.36, total EUR 467.94. | Dossier §2.3. |
| High | Confirmed mismatch | Mandatory regresses | Employer cost omits minimum vacation regress EUR 1,481.88 and winter regress EUR 740.94. | Dossier §§3.2–3.3. |
| Low | Confirmed mismatch | Contribution floor | The Jan–Feb EUR 1,436.95 and Mar–Dec EUR 1,521.62 minimum bases are not implemented; vectors are above them. | Dossier §2.4. |

## Matches

The 22.1% ordinary employee, 1% LTC employee, 16.1% ordinary employer, 1% employer LTC, 2026 PIT scale and basic EUR 5,551.93 allowance agree.

## Output impact

| Gross EUR | Module net | Dossier salary net | Delta | Module salary cost | Dossier salary cost | Mandatory-regress-inclusive dossier cost |
|---:|---:|---:|---:|---:|---:|---:|
| 20,000 | 13,272.52 | 13,414.44 | -141.92 | 23,420 | 23,420 | 25,642.82 |
| 60,000 | 35,049.23 | 35,406.03 | -356.80 | 70,260 | 70,260 | 72,482.82 |
| 100,000 | 54,616.64 | 55,193.51 | -576.87 | 117,100 | 117,100 | 119,322.82 |
| 200,000 | 93,666.44 | 94,904.78 | -1,238.34 | 234,200 | 234,200 | 236,422.82 |
| 600,000 | 245,466.44 | 248,704.78 | -3,238.34 | 702,600 | 702,600 | 704,822.82 |

## Recommended disposition

Fix PIT deductibility and the split-year OZP immediately. Add the two statutory regresses to total employer cash cost or expose salary-only versus all-mandatory-cost outputs. Add minimum-base handling for general coverage.

## Regression vectors

Use all five rows, OZP EUR 467.94, regresses EUR 2,222.82, and contribution-base tests around EUR 1,436.95/1,521.62 monthly.
