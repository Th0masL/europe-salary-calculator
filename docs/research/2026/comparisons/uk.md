# United Kingdom — implementation comparison

## Compared artifacts

- Independent dossier: `docs/research/2026/united-kingdom.md`
- Current implementation: `tools/calc/uk.py`
- Comparison date: 2026-10-04

## Current implementation scenario

England/Northern Ireland (also same 2026/27 employment-income rates for Wales), Category A, no pension, using annualized NIC thresholds. Scotland is outside the encoded scenario.

## Findings

| Severity | Classification | Area | Finding | Evidence / code |
|---|---|---|---|---|
| Low | Confirmed mismatch | NIC timing/rounding | NIC is period-based and penny-rounded; module annualizes thresholds, producing 52–60p net and 59–61p employer-cost differences. | Dossier §2.2; module annual formula. |
| Medium | Scenario difference | Scotland | The module supports only rUK tax. Scottish employment rates materially reduce net at higher vectors and are not parameterized. | Dossier §1.3. |

## Matches

Personal Allowance/taper, rUK 20/40/45% bands, Category-A NIC rates, 15% employer NIC, no-pension opt-out scenario, and exclusion of employer-wide Employment Allowance/Apprenticeship Levy from base cost agree.

## Output impact

| Gross GBP | Module net | Dossier rUK net | Delta | Module cost | Dossier base cost | Delta |
|---:|---:|---:|---:|---:|---:|---:|
| 20,000 | 17,919.60 | 17,920.12 | -0.52 | 22,250.00 | 22,249.39 | +0.61 |
| 60,000 | 45,357.40 | 45,358.00 | -0.60 | 68,250.00 | 68,249.40 | +0.60 |
| 100,000 | 68,557.40 | 68,557.96 | -0.56 | 114,250.00 | 114,249.41 | +0.59 |
| 200,000 | 117,786.40 | 117,787.04 | -0.64 | 229,250.00 | 229,249.39 | +0.61 |
| 600,000 | 329,786.40 | 329,787.00 | -0.60 | 689,250.00 | 689,249.40 | +0.60 |

## Recommended disposition

Implement pay-period NIC rounding. Expose Scotland as a tax-region option or relabel the module clearly as rUK. Keep employer-wide relief/levy as optional employer inputs.

## Regression vectors

Use all five monthly schedules from the dossier, allowance taper at GBP 100,000/125,140, NIC thresholds GBP 1,048/4,189/417 monthly, and at least one Scottish vector.
