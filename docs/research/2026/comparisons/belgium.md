# Belgium — 2026 implementation comparison

## Compared artifacts

- Dossier: `docs/research/2026/belgium.md` (official FPS Finance/ONSS sources, accessed 2026-10-04).
- Implementation: `tools/calc/belgium.py`.

## Current implementation scenario

Single employee, 7% communal-tax proxy, annual gross treated as total cash compensation. The module applies flat employee/employer percentages and approximate federal inputs; it does not model 12 months plus double holiday pay.

## Findings

| Severity | Classification | Area | Finding | Evidence / code |
|---|---|---|---|---|
| High | Scenario difference | Gross/payment structure | The dossier's reproducible benchmark is 12 ordinary months plus white-collar double holiday pay (annual gross `12.92M`); the module uses one undifferentiated annual base. Monthly work-bonus, CSSS and quarterly employer caps therefore cannot be reproduced from the module input alone. | Dossier §§1, 3-4; `belgium.py:44-54`. |
| Critical | Confirmed mismatch | Employee reductions | The module omits the social work bonus and fiscal work-bonus credit and charges EUR731 CSSS at every salary. The dossier has EUR0 at EUR20k, EUR499.25 at EUR60k and EUR731.28 thereafter under its payment scenario. | Dossier §§3.2-4.3; `belgium.py:38,46-52`. |
| High | Confirmed mismatch | PIT parameters | Expense cap EUR5,750 and allowance EUR10,910 are not the dossier's final 2026 values, EUR6,070 and EUR11,180. The bracket thresholds themselves match. | Dossier §3.3; `belgium.py:34-41`. |
| Critical | Unsupported assumption | Employer cost | Flat 29.85% includes an unsupported 2.5% “sectoral” proxy, omits the statutory structural reduction and ignores quarterly caps. The dossier quantifies only determinable base SS and expressly excludes sector/company charges. | Dossier §§3.5, 4.3; `belgium.py:16-20,39,54`. |
| Medium | Scenario difference | Municipality | 7% is a disclosed scenario, not a universal communal rate. It matches the dossier's comparison scenario. | Dossier §§1, 3.4; `belgium.py:37,51`. |

## Matches

- The ordinary employee nominal ONSS rate is 13.07%, and professional expenses are 30% before their cap.
- The module and dossier both keep communal tax as a separate surcharge and flag sectoral/municipal variability, though only the dossier avoids quantifying unknown sector cost.

## Output impact

The net comparison uses the dossier's conservative EUR20k row. Employer figures compare the module with the dossier's base-SS subtotal, so the delta is not an all-in legal overstatement: excluded sector charges remain unresolved.

| Gross EUR | Module net | Dossier net | Net delta | Module cost | Dossier subtotal | Cost delta |
|---:|---:|---:|---:|---:|---:|---:|
| 20,000 | 16,317.90 | 19,105.88 | -2,787.98 | 25,970.00 | 20,000.00* | +5,970.00 |
| 60,000 | 36,262.32 | 36,742.40 | -480.08 | 77,910.00 | 73,931.89 | +3,978.11 |
| 100,000 | 52,680.71 | 52,956.79 | -276.08 | 129,850.00 | 123,219.81 | +6,630.19 |
| 200,000 | 93,103.16 | 93,412.17 | -309.01 | 259,700.00 | 246,439.63 | +13,260.37 |
| 600,000 | 254,792.96 | 255,233.68 | -440.72 | 779,100.00 | 687,567.00 | +91,533.00 |

`*` Low-pay stress case; real part-time facts are required.

## Recommended disposition

Make payment structure, municipality and sector explicit. Implement monthly work bonus/CSSS and final 2026 PIT constants. Replace the flat employer proxy with the benchmark base contribution/structural-reduction calculation and report unknown sector charges separately.

## Regression vectors

Use EUR60k, EUR100k, EUR200k and EUR600k dossier rows for the selected `12.92M`, 7% municipality scenario. Keep EUR20k as a marked stress vector, including both conservative and mechanically refundable-credit outcomes.

## Implementation update

Implemented in the calculator: the `12.92M` salary/holiday-pay split, period-specific
social work bonus, CSSS payroll advances, final 2026 PIT constants, structural
reduction, and quarterly high-salary cap. The live comparator deliberately uses
the conservative EUR20k result and excludes unknown sector/company charges and
the not-yet-finally-evidenced refundable fiscal work-bonus settlement.
