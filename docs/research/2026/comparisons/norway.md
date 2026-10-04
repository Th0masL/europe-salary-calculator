# Norway — implementation comparison

## Compared artifacts

- Independent dossier: `docs/research/2026/norway.md`
- Current implementation: `tools/calc/norway.py`
- Comparison date: 2026-10-04

## Current implementation scenario

Both use employer-contribution zone I (14.1%), an under-pension-age resident, and gross cash actually paid in 2026. The dossier applies the statutory minimum OTP from the first krone and uses the 2026 average G; variable injury insurance and plan administration are excluded from its numeric floor.

## Findings

| Severity | Classification | Area | Finding | Evidence / code |
|---|---|---|---|---|
| High | Confirmed mismatch | Income deductions | The module uses an estimated NOK 113,000 maximum minstefradrag instead of NOK 95,700 and NOK 114,000 personfradrag instead of NOK 114,540. From NOK 600k upward it overstates net by NOK 3,687.20. | Dossier §§1, 5; `norway.py:11-14,30-32,44-46`. |
| High | Confirmed mismatch | OTP base | Statutory minimum OTP is 2% from the first krone through 12G; the implementation incorrectly excludes the first 1G and uses an approximate NOK 124,000 G instead of the 2026 average NOK 134,419. | Dossier §§3, 6; `norway.py:8-9,36-37,51`. |
| Medium | Confirmed mismatch | AGA on OTP | Employer national-insurance contribution also applies to the employer OTP contribution; the module applies 14.1% only to salary. | Dossier §§2–3, 6; `norway.py:52`. |
| Medium | Confirmed mismatch | Low-income NI | The statutory employee NI calculation includes the lower threshold and 25% taper limitation. A flat 7.6% is wrong below the crossover, although all requested vectors are above it. | Dossier §2; `norway.py:34,48`. |
| Low | Scenario difference | Variable employer costs | Occupational-injury insurance and OTP administration are mandatory but no universal premium exists; both should remain disclosed variables above the numeric floor. | Dossier §§3, 6. |

## Matches

- Ordinary-income rate 22%, bracket-tax thresholds/rates, employee NI 7.6% above the taper range, zone-I AGA 14.1%, and removal of the former high-income AGA surcharge match.
- Gross is cash actually paid, so holiday pay is not added mechanically on top.

## Output impact

Employer figures are statutory floors excluding variable insurance/administration; `Δ = implementation − dossier`, NOK:

| Gross | Impl. net | Dossier net | Δ net | Impl. cost | Dossier cost | Δ cost |
|---:|---:|---:|---:|---:|---:|---:|
| 200,000 | 184,800.00 | 184,800.00 | 0.00 | 229,720.00 | 232,764.00 | -3,044.00 |
| 600,000 | 459,504.60 | 455,817.40 | +3,687.20 | 694,120.00 | 698,292.00 | -4,172.00 |
| 1,000,000 | 697,817.55 | 694,130.35 | +3,687.20 | 1,158,520.00 | 1,163,820.00 | -5,300.00 |
| 2,000,000 | 1,228,489.55 | 1,224,802.35 | +3,687.20 | 2,309,280.00 | 2,318,809.30 | -9,529.30 |
| 6,000,000 | 3,332,489.55 | 3,328,802.35 | +3,687.20 | 6,873,280.00 | 6,882,809.30 | -9,529.30 |

## Recommended disposition

Replace estimated deductions with official 2026 values, implement the NI threshold/taper, and calculate OTP on `min(gross, 12 × 134,419)` from the first krone plus 14.1% AGA on OTP. Keep the selected zone and variable premiums explicit.

## Regression vectors

For zone I and minimum OTP, excluding variable insurance/administration, assert: `200,000 → 232,764.00, 184,800.00`; `600,000 → 698,292.00, 455,817.40`; `1,000,000 → 1,163,820.00, 694,130.35`; `2,000,000 → 2,318,809.30, 1,224,802.35`; `6,000,000 → 6,882,809.30, 3,328,802.35`. Add NI tests at NOK 99,650 and the 25%/7.6% crossover.
