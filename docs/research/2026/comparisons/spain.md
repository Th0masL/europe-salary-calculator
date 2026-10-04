# Spain — implementation comparison

## Compared artifacts

- Independent dossier: `docs/research/2026/spain.md`
- Current implementation: `tools/calc/spain.py`
- Comparison date: 2026-10-04

## Current implementation scenario

Single under-65 employee and office accident rate 1.5%. The module uses a synthetic national-reference combined IRPF scale; the dossier selects Madrid and applies separate national/Madrid scales.

## Findings

| Severity | Classification | Area | Finding | Evidence / code |
|---|---|---|---|---|
| High | Scenario difference | Region | The module is not a Madrid calculation and does not expose autonomous community. Its reference scale materially differs from the dossier's reproducible Madrid result. | Dossier §5.2; module `TAX_BRACKETS`. |
| High | Confirmed mismatch | Low employment income | Article 20 reduction and the 2026 low-work-income credit are absent, understating EUR 20k net. | Dossier §§5.1, 5.3. |
| High | Confirmed mismatch | Solidarity contribution | Employee and employer solidarity tiers above EUR 61,214.40 are omitted. | Dossier §4.2; module comment acknowledges omission. |
| Medium | Confirmed mismatch | Tax architecture | A single combined reference scale cannot reproduce the statutory state plus autonomous scales and separate personal-minimum calculations. | Dossier §5.2. |

## Matches

The EUR 61,214.40 regular base cap, regular employee 6.50%, employer 32.15% office scenario, EUR 2,000 expense and national EUR 5,550 personal minimum agree.

## Output impact

| Gross EUR | Module net | Madrid dossier net | Net delta | Module cost | Dossier cost | Cost delta |
|---:|---:|---:|---:|---:|---:|---:|
| 20,000 | 16,369.00 | 16,828.65 | -459.65 | 26,430.00 | 26,430.00 | 0.00 |
| 60,000 | 41,436.00 | 42,183.56 | -747.56 | 79,290.00 | 79,290.00 | 0.00 |
| 100,000 | 63,864.59 | 65,227.27 | -1,362.68 | 119,680.43 | 120,093.62 | -413.19 |
| 200,000 | 118,864.59 | 122,090.47 | -3,225.88 | 219,680.43 | 221,313.62 | -1,633.19 |
| 600,000 | 332,984.16 | 343,688.51 | -10,704.35 | 619,680.43 | 626,193.62 | -6,513.19 |

## Recommended disposition

Parameterize autonomous community and implement separate official scales/minima. Add Article 20/2026 credit and both solidarity shares. Retain the 1.5% office accident assumption with a label.

## Regression vectors

Use all five Madrid rows, regular cap EUR 61,214.40, solidarity boundaries at 1.10× and 1.50× cap, and credit cutoff EUR 20,048.45.
