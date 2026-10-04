# Germany — 2026 implementation comparison

## Compared artifacts

- Dossier: `docs/research/2026/germany.md` (official BMF/BMAS/BMG/DRV sources, accessed 2026-10-04).
- Implementation: `tools/calc/germany.py`.

## Current implementation scenario

Berlin/non-Saxony, age 30, childless, class I, statutory health with the official 2.9% average add-on, no church tax. Employer output adds representative accident insurance and a fixed U2 rate.

## Findings

| Severity | Classification | Area | Finding | Evidence / code |
|---|---|---|---|---|
| Medium | Confirmed mismatch | Wage-tax algorithm | The module uses continuous annual polynomial output and derived constants EUR11,135.90/EUR19,470.65. The final official 2026 algorithm floors taxable income and wage tax as specified and uses EUR11,135.63/EUR19,470.38; it also uses the payroll precautionary health share (8.45%), not the full actual 8.75%. Net differences reach EUR98.79. | Dossier §4 and official BMF check table; `germany.py:12-23,53-69,90-94`. |
| High | Unsupported assumption | Employer accident/U2 | The module assumes 1% accident and U2 0.44%. Accident is risk/assessment-specific and U2 is sickness-fund-specific; neither is a universal total. Only the 0.15% insolvency levy is fixed. | Dossier §§2 sources 10-12, 6; `germany.py:41-51,95-96`. |
| Medium | Product decision | Employer output | The module should return the dossier's fixed statutory floor plus explicit variable charges, not a representative amount labeled employer cost. | Dossier §§3, 6-8; `germany.py:32,95-96`. |

## Matches

- 2026 ceilings, pension/unemployment/health/care actual rates, childless supplement, average health add-on, basic allowance and solidarity exemption/rates match the selected scenario.
- Berlin/non-Saxony and continued voluntary statutory health above the compulsory-insurance threshold align with the dossier.

## Output impact

Cost delta compares module all-in assumptions with the dossier fixed floor; it is not an overcharge estimate because real U2/accident remain payable.

| Gross EUR | Module net | Official dossier net | Net delta | Module cost | Dossier floor | Difference |
|---:|---:|---:|---:|---:|---:|---:|
| 20,000 | 15,280.35 | 15,270.00 | +10.35 | 24,548.00 | 24,260.00 | +288.00 |
| 60,000 | 37,621.80 | 37,561.00 | +60.80 | 73,644.00 | 72,780.00 | +864.00 |
| 100,000 | 58,128.50 | 58,030.02 | +98.48 | 119,548.62 | 118,108.63 | +1,439.99 |
| 200,000 | 112,788.38 | 112,695.87 | +92.51 | 220,705.29 | 218,259.13 | +2,446.16 |
| 600,000 | 325,936.22 | 325,837.43 | +98.79 | 624,705.29 | 618,259.13 | +6,446.16 |

## Recommended disposition

Transcribe the final BMF 2026 PAP, including statutory rounding and precautionary allowance. Return a fixed employer floor; accept fund-specific U2 and BG accident parameters separately. Keep the 2.9% health add-on clearly labeled as an official average scenario.

## Regression vectors

The dossier's five employee rows were independently checked against BMF `2026Version1` and are authoritative. EUR100k tests the solidarity phase-in and health ceiling; EUR600k tests the top zone and full Soli. Employer floor rows are authoritative only before U1/U2/accident.
