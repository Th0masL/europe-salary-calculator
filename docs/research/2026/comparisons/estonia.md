# Estonia — 2026 implementation comparison

## Compared artifacts

- Dossier: `docs/research/2026/estonia.md` (official EMTA/Riigi Teataja sources, accessed 2026-10-04).
- Implementation: `tools/calc/estonia.py`.

## Current implementation scenario

Working-age employee continuously enrolled in pillar II at the default 2%, claiming the full EUR700 monthly basic exemption from this employer, with regular salary above the social-tax minimum and no sickness.

## Findings

| Severity | Classification | Area | Finding | Evidence / code |
|---|---|---|---|---|
| Medium | Scenario difference | Pillar II | Membership is not universal and members can elect 2%, 4% or 6%; the module hard-codes the dossier's default 2% scenario. | Dossier §§1.4, 4; `estonia.py:31,45`. |
| Medium | Product decision | Basic exemption | Full EUR8,400 requires an employee application and only one payer may apply it. The module assumes the application and has no election input. | Dossier §§1.2, 4; `estonia.py:35-37,47`. |
| Low | Unsupported assumption | Social-tax minimum | Annual gross arithmetic omits the EUR886 monthly employer base floor. It does not affect the five vectors under regular monthly pay but matters for low/irregular months. | Dossier §1.5; `estonia.py:23-27,42`. |
| Low | Unsupported assumption | Sickness | The module necessarily omits contingent employer payment of 70% for sickness days 4-8; this should be described as excluded rather than zero. | Dossier §1.6; `estonia.py:42`. |

## Matches

- For the stated scenario, 22% PIT, EUR8,400 exemption, deduction of 1.6% unemployment and 2% pillar II before PIT, 33% social tax and 0.8% employer unemployment all match.
- All five net and regular employer-cost values match to the cent.

## Output impact

| Gross EUR | Net (module=dossier) | Employer cost (module=dossier) |
|---:|---:|---:|
| 20,000 | 16,886.40 | 26,760.00 |
| 60,000 | 46,963.20 | 80,280.00 |
| 100,000 | 77,040.00 | 133,800.00 |
| 200,000 | 152,232.00 | 267,600.00 |
| 600,000 | 453,000.00 | 802,800.00 |

## Recommended disposition

No arithmetic change for the current scenario. Surface pillar membership/rate and exemption election; implement the monthly social-tax minimum if lower or irregular pay enters scope, and label sickness cost as contingent.

## Regression vectors

All five dossier cross-check rows are authoritative for the selected default scenario. Add separate future vectors for 0%/4%/6% pillar rates, no exemption application, and a monthly wage below EUR886.
