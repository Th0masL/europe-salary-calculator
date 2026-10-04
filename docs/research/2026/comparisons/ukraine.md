# Ukraine — implementation comparison

## Compared artifacts

- Independent dossier: `docs/research/2026/ukraine.md`
- Current implementation: `tools/calc/ukraine.py`
- Comparison date: 2026-10-04

## Current implementation scenario

Ordinary non-disabled employee, 12 regular months. PIT and military levy are flat; employer USC is annualized from a monthly cap.

## Findings

| Severity | Classification | Area | Finding | Evidence / code |
|---|---|---|---|---|
| Critical | Confirmed mismatch | 2026 USC cap | Module uses 15 minimum wages monthly; the 2026 Budget Act temporarily sets 20, i.e. UAH 172,940/month and UAH 456,561.60 maximum annual USC. | Dossier §3.1; `USC_CAP=MIN_WAGE*15*12`. |
| Low | Product decision | Payment timing | A single annual cap shortcut cannot reproduce a bonus concentrated in one month; the cap is calendar-month based. Regular-pay vectors remain comparable. | Dossier §§3.1–3.2. |

## Matches

PIT 18%, ordinary military levy 5%, no employee USC, employer USC 22%, and all employee net vectors agree exactly.

## Output impact

| Gross UAH | Net delta | Module cost | Dossier cost | Cost delta |
|---:|---:|---:|---:|---:|
| 1,000,000 | 0.00 | 1,220,000.00 | 1,220,000.00 | 0.00 |
| 3,000,000 | 0.00 | 3,342,421.20 | 3,456,561.60 | **-114,140.40** |
| 5,000,000 | 0.00 | 5,342,421.20 | 5,456,561.60 | **-114,140.40** |
| 10,000,000 | 0.00 | 10,342,421.20 | 10,456,561.60 | **-114,140.40** |
| 30,000,000 | 0.00 | 30,342,421.20 | 30,456,561.60 | **-114,140.40** |

## Recommended disposition

Change the 2026 cap to 20 minimum wages and calculate it per month. Keep disability/special regimes as explicit alternatives.

## Regression vectors

Use all five dossier rows, UAH 8,647 minimum, UAH 172,940 monthly cap, and a concentrated-bonus case demonstrating monthly rather than annual cap behavior.
