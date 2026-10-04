# Switzerland — implementation comparison

## Compared artifacts

- Independent dossier: `docs/research/2026/switzerland.md`
- Current implementation: `tools/calc/switzerland.py`
- Comparison date: 2026-10-04

## Current implementation scenario

Both select Zürich City and an illustrative 5% employee/employer BVG old-age share. The module additionally invents flat NBU and bundled employer-extra rates and uses a synthetic tax table calibrated to third-party outputs.

## Findings

| Severity | Classification | Area | Finding | Evidence / code |
|---|---|---|---|---|
| Critical | Confirmed mismatch | Income tax | The synthetic `TAX` scale is neither the 2026 federal tariff nor Zürich simple tax × 2.14, and deductions/rounding/personal tax are absent. | Dossier §4; module `TAX`. |
| High | Confirmed mismatch | ALV | `ALV2=0.5%` above CHF 148,200 is obsolete; the solidarity percentage ended in 2023. | Dossier §2. |
| Medium | Confirmed mismatch | BVG thresholds | Module uses CHF 25,725/88,200/3,675 instead of 2026 CHF 26,460/90,720/3,780. | Dossier §§2–3. |
| High | Unsupported assumption | NBU | Employee NBU is hard-coded at 1% of uncapped gross; actual risk rate varies and insured pay is capped at CHF 148,200. | Dossier §2. |
| High | Unsupported assumption | Employer extras | `ER_EXTRA=4.5%` bundles accident, FAK and pension without authoritative allocation, omits known SVA-ZH FAK 1.025%, and cannot model fund/plan variables. | Dossier §§2, 5.3. |

## Matches

AHV/IV/EO 5.3% per side, ALV 1.1% below CHF 148,200, and the need for a location/pension scenario are recognized.

## Output impact

Employee comparison is against the dossier's explicitly zero-NBU/zero-risk-premium benchmark; employer comparison is against its identifiable SVA-ZH core, so deltas are scenario differences rather than exact real-payroll errors.

| Gross CHF | Module net | Dossier benchmark | Delta | Module cost | Dossier core | Delta |
|---:|---:|---:|---:|---:|---:|---:|
| 20,000 | 18,520.00 | 18,462.74 | +57.26 | 22,180.00 | 21,485.00 | +695.00 |
| 60,000 | 50,504.70 | 49,790.18 | +714.52 | 68,253.75 | 66,132.00 | +2,121.75 |
| 100,000 | 80,011.48 | 78,358.83 | +1,652.65 | 114,023.75 | 110,638.00 | +3,385.75 |
| 200,000 | 149,662.55 | 143,995.71 | +5,666.84 | 224,612.95 | 217,493.20 | +7,119.75 |
| 600,000 | 411,728.44 | 369,883.21 | +41,845.23 | 664,387.95 | 642,793.20 | +21,594.75 |

## Recommended disposition

Replace tax with official federal/Zürich formulas; remove ALV2; update BVG thresholds. Parameterize NBU/BU, pension plan/split, FAK, administration and vocational fund instead of bundling rates.

## Regression vectors

Use the five dossier benchmarks, CHF 148,200 ALV cap, BVG 22,680/26,460/3,780/90,720, Zürich multipliers 95%+119%, and official federal tariff anchor tests.
