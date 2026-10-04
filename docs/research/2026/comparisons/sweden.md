# Sweden — implementation comparison

## Compared artifacts

- Independent dossier: `docs/research/2026/sweden.md`
- Current implementation: `tools/calc/sweden.py`
- Comparison date: 2026-10-04

## Current implementation scenario

The module uses national-average municipal tax and an estimated basic allowance/job credit, then adds a representative 4.5% occupational pension to employer cost. The dossier uses Stockholm, no church membership, and exact 2026 formulas.

## Findings

| Severity | Classification | Area | Finding | Evidence / code |
|---|---|---|---|---|
| Critical | Confirmed mismatch | Tax formulas | `GRUNDAVDRAG`, `JOBB_MAX` and the invented 3% phase-out do not implement the official 2026 formulas. Net errors reach SEK 155,334.16. | Dossier §§2, 5; module marked APPROXIMATE. |
| High | Scenario difference | Municipality | 32.38% average differs from Stockholm's 30.55% municipal/regional rate plus 0.07% burial fee. | Dossier §1. |
| High | Confirmed mismatch | Other tax items | Burial fee, public-service fee and general earned-income credit are omitted. | Dossier §§1.2, 5.2, 6. |
| Low | Confirmed mismatch | State threshold | Module uses SEK 643,100; official taxable-income threshold is SEK 643,000. | Dossier §3.2. |
| High | Unsupported assumption | Employer pension | The added 4.5% occupational pension is collective-agreement/plan dependent and is not a universal statutory charge. | Dossier §7.2. |

## Matches

No ordinary employee social deduction and statutory employer contribution 31.42% uncapped are correct.

## Output impact

| Gross SEK | Module net | Stockholm dossier net | Delta | Module cost | Statutory dossier cost | Excess from assumed pension |
|---:|---:|---:|---:|---:|---:|---:|
| 200,000 | 170,679.84 | 171,894 | -1,214.16 | 271,840 | 262,840 | +9,000 |
| 600,000 | 441,159.84 | 471,354 | -30,194.16 | 815,520 | 788,520 | +27,000 |
| 1,000,000 | 637,091.84 | 680,954 | -43,862.16 | 1,359,200 | 1,314,200 | +45,000 |
| 2,000,000 | 1,089,819.84 | 1,174,754 | -84,934.16 | 2,718,400 | 2,628,400 | +90,000 |
| 6,000,000 | 2,994,619.84 | 3,149,954 | -155,334.16 | 8,155,200 | 7,885,200 | +270,000 |

## Recommended disposition

Replace estimates with SKV 433 formulas, expose municipality, and separate statutory employer cost from optional occupational pension.

## Regression vectors

Use all five Stockholm rows, PBB SEK 59,200, high-income GA SEK 17,400, saturated job credit SEK 49,429, public-service cap SEK 1,184, and state threshold SEK 643,000.
