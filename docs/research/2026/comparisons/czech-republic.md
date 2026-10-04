# Czech Republic — 2026 implementation comparison

## Compared artifacts

- Dossier: `docs/research/2026/czech-republic.md` (official CSSA/health/tax/legal sources, accessed 2026-10-04).
- Implementation: `tools/calc/czechia.py`.

## Current implementation scenario

Ordinary office employee paid evenly over twelve months. Annual continuous arithmetic applies statutory rates and ceilings but omits payroll/final-assessment rounding and employer accident insurance.

## Findings

| Severity | Classification | Area | Finding | Evidence / code |
|---|---|---|---|---|
| High | Unsupported assumption | Employer accident insurance | Statutory employer accident insurance is absent. Its rate depends on the employer's predominant activity and cannot be inferred from salary; the module presents its subtotal as total employer cost. | Dossier §§2.4, 4-5; `czechia.py:19,39`. |
| Low | Confirmed mismatch | Monthly/annual rounding | The module applies annual unrounded percentages. Czech payroll rounds monthly health bases/contributions and annual social amounts under statutory rules; final PIT is whole-crown. Differences are CZK0-9 in net and CZK0-10 in cost floor. | Dossier §§3-4; `czechia.py:31-39`. |

## Matches

- PIT rates/threshold and CZK30,840 credit, PIT-on-gross order, 7.1% capped social, 4.5% uncapped health, 24.8% capped employer social and 9% uncapped employer health all match.
- The annual social cap CZK2,350,416 matches.

## Output impact

Employer comparison is against the dossier floor before the unresolved accident premium.

| Gross CZK | Module net | Dossier final cash | Net delta | Module cost | Dossier floor | Cost delta |
|---:|---:|---:|---:|---:|---:|---:|
| 500,000 | 397,840.00 | 397,831.00 | +9.00 | 669,000.00 | 669,010.00 | -10.00 |
| 1,500,000 | 1,131,840.00 | 1,131,840.00 | 0.00 | 2,007,000.00 | 2,007,000.00 | 0.00 |
| 2,500,000 | 1,817,485.42 | 1,817,479.00 | +6.42 | 3,307,903.17 | 3,307,908.00 | -4.83 |
| 5,000,000 | 3,629,985.42 | 3,629,979.00 | +6.42 | 6,032,903.17 | 6,032,908.00 | -4.83 |
| 15,000,000 | 10,879,985.42 | 10,879,984.00 | +1.42 | 16,932,903.17 | 16,932,904.00 | -0.83 |

## Recommended disposition

Implement Czech monthly/annual rounding if payroll precision is a product goal. Relabel employer output as a floor and expose or separately add the employer activity-based accident premium.

## Regression vectors

Use the five final-cash/floor rows in dossier §4. CZK2.5m is the strongest boundary vector because it crosses both the PIT threshold and annual social cap.
