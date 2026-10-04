# Italy — implementation comparison

## Compared artifacts

- Independent dossier: `docs/research/2026/italy.md`
- Current implementation: `tools/calc/italy.py`
- Comparison date: 2026-10-04

## Current implementation scenario

The module says its location and employer inputs are representative. The dossier instead fixes Milan, Lombardy, a post-1995 entrant, and an industrial/manufacturing employer with no more than 15 employees; annual gross already includes 13th and 14th instalments.

## Findings

| Severity | Classification | Area | Finding | Evidence / code |
|---|---|---|---|---|
| Critical | Confirmed mismatch | Low-income relief | The implementation omits the employment credit and 2025-permanent tax-free employee sum. At €20,000 this understates net by €3,969.04. | Dossier §§1, 4, 6; `italy.py:8-9,48-52`. |
| High | Confirmed mismatch | Regional/municipal surtaxes | Flat 2.2% Lombardy plus 0.8% Milan proxies do not implement the official progressive Lombardy schedule, Milan exemption/rate, or their actual bases. | Dossier §§3, 6; `italy.py:39-40,50`. |
| High | Confirmed mismatch | Employer INPS | `29.72% × capped gross` differs from the chosen employer's 23.81% capped IVS plus 5.503333% uncapped minor funds. | Dossier §§2, 6; `italy.py:34,45,53`. |
| High | Confirmed mismatch | TFR and extras | TFR is not a flat 6.91% of gross: the dossier uses `G/13.5 − 0.5% × capped base`. The extra 5% bucket is unsupported and double-counts 13th/14th salary already included in `G`. | Dossier §§1–2, 6; `italy.py:35,37,53`. |
| Medium | Confirmed mismatch | INAIL | The module assumes 1%; the selected office-risk scenario uses 0.4%. The rate is employer/activity-specific and must be parameterised. | Dossier §§2, 6; `italy.py:36,53`. |
| Low | Confirmed mismatch | Additional INPS threshold | The module uses an approximate €56,000 threshold instead of the sourced €56,224 for the extra employee 1%. | Dossier §2; `italy.py:31,46`. |

## Matches

- National IRPEF marginal rates 23%/33%/43%, employee 9.19% base rate, post-1995 €122,295 IVS maximum, and the existence of the extra 1% match.
- Employee INPS is deducted before national and local income taxes.

## Output impact

`Δ = implementation − dossier`, EUR:

| Gross | Impl. net | Dossier net | Δ net | Impl. cost | Dossier cost | Δ cost |
|---:|---:|---:|---:|---:|---:|---:|
| 20,000 | 13,439.88 | 17,408.92 | -3,969.04 | 28,526.00 | 27,324.15 | +1,201.85 |
| 60,000 | 37,200.84 | 37,500.19 | -299.35 | 85,578.00 | 81,972.44 | +3,605.56 |
| 100,000 | 56,599.80 | 57,031.68 | -431.88 | 142,630.00 | 136,620.74 | +6,009.26 |
| 200,000 | 109,373.00 | 110,173.41 | -800.41 | 262,166.07 | 255,128.45 | +7,037.62 |
| 600,000 | 325,373.00 | 327,690.28 | -2,317.28 | 713,806.07 | 708,371.41 | +5,434.66 |

## Recommended disposition

Replace representative percentages with an explicit location/sector/company-size scenario, implement statutory credits/sum, and calculate each INPS, INAIL and TFR component on its own base. Remove any 13th/14th uplift when input gross already includes those instalments.

## Regression vectors

For Milan/Lombardy, post-1995 entrant, selected small industrial employer, 0.4% INAIL, and 14 instalments included in gross, assert: `20,000 → 27,324.15, 17,408.92`; `60,000 → 81,972.44, 37,500.19`; `100,000 → 136,620.74, 57,031.68`; `200,000 → 255,128.45, 110,173.41`; `600,000 → 708,371.41, 327,690.28`.

## Implementation update

Implemented for the fixed Milan/Lombardy small-industrial-employer scenario:
ordinary employment credit, permanent tax-wedge relief, progressive regional
and Milan surtaxes, component-specific INPS bases, 0.4% INAIL, and statutory TFR.
The unsupported 5% extras bucket was removed.
