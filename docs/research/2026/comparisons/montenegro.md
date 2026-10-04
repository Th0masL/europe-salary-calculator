# Montenegro — implementation comparison

## Compared artifacts

- Independent dossier: `docs/research/2026/montenegro.md`
- Current implementation: `tools/calc/montenegro.py`
- Comparison date: 2026-10-04

## Current implementation scenario

Both artifacts use Podgorica and equal monthly salary. The dossier reports in-year payroll cash because the 2026 annual PIO maximum had not been officially located by the access date; any excess refund is a later employee procedure. The module hard-codes an unsupported annual cap and treats municipal surtax as an employee deduction.

## Findings

| Severity | Classification | Area | Finding | Evidence / code |
|---|---|---|---|---|
| Critical | Unsupported assumption | PIO maximum | The €68,765 annual ceiling is not supported for 2026 and is applied directly in payroll. Official rules require full in-year PIO withholding, with a possible later refund after the annual maximum is established. | Dossier §§2, 5; `montenegro.py:6-7,32,42`. |
| High | Confirmed mismatch | Municipal surtax | The Ministry payroll layout adds Podgorica's 15%-of-PIT surtax to employer funds needed; it is not deducted from payroll net in the dossier scenario. The module does the reverse. | Dossier §§1, 4; `montenegro.py:37,46,48-49`. |
| High | Confirmed mismatch | Employer levies | The module omits Labour Fund 0.2% and the 2026 Chamber contribution 0.27% on gross. | Dossier §§3–4; `montenegro.py:28,49`. |
| Low | Match | Europe Now rates | Zero health, employee PIO 10%, employee/employer unemployment 0.5%, and gross-basis monthly PIT bands match. | Dossier §§1–2; `montenegro.py:31-36,42-45`. |

## Matches

- Monthly 0%/9%/15% PIT thresholds and gross base match.
- No health contribution or employer PIO is added.
- Regular cash bonuses would enter gross; no special 13th-month relief is assumed.

## Output impact

These are in-year payroll results before any later PIO refund; `Δ = implementation − dossier`, EUR:

| Gross | Impl. net | Dossier net | Δ net | Impl. cost | Dossier cost | Δ cost |
|---:|---:|---:|---:|---:|---:|---:|
| 20,000 | 16,147.40 | 16,376.00 | -228.60 | 20,100.00 | 20,422.60 | -322.60 |
| 60,000 | 45,047.40 | 46,176.00 | -1,128.60 | 60,300.00 | 61,710.60 | -1,410.60 |
| 100,000 | 77,070.90 | 75,976.00 | +1,094.90 | 100,500.00 | 102,998.60 | -2,498.60 |
| 200,000 | 159,320.90 | 150,476.00 | +8,844.90 | 201,000.00 | 206,218.60 | -5,218.60 |
| 600,000 | 488,320.90 | 448,476.00 | +39,844.90 | 603,000.00 | 619,098.60 | -16,098.60 |

## Recommended disposition

Remove the unsupported payroll cap, move municipal surtax to employer cost for this official-layout scenario, and add Labour Fund and Chamber levies. If a final-after-refund view is desired, source the 2026 maximum and expose it separately from payroll cash.

## Regression vectors

For equal monthly pay in Podgorica, ordinary Chamber-member employer, before any PIO refund, assert: `20,000 → 20,422.60, 16,376.00`; `60,000 → 61,710.60, 46,176.00`; `100,000 → 102,998.60, 75,976.00`; `200,000 → 206,218.60, 150,476.00`; `600,000 → 619,098.60, 448,476.00`.
