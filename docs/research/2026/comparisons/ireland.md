# Ireland — implementation comparison

## Compared artifacts

- Independent dossier: `docs/research/2026/ireland.md`
- Current implementation: `tools/calc/ireland.py`
- Comparison date: 2026-10-04

## Current implementation scenario

The module models a Class A employee using full-year pre-1-October PRSI rates and explicitly excludes MyFutureFund. The dossier fixes 52 Friday pays, no existing payroll pension, and continued enrolment in MyFutureFund, so its contribution timing is reproducible.

## Findings

| Severity | Classification | Area | Finding | Evidence / code |
|---|---|---|---|---|
| High | Confirmed mismatch | MyFutureFund | The stated employee is eligible and remains enrolled, so employee and employer contributions of 1.5% begin 1 January 2026 and continue through the pay period breaching €80,000. The module omits both sides. | Dossier §§3–4; `ireland.py:19-23,56-57`. |
| Medium | Confirmed mismatch | PRSI split-year rates | The module applies 4.20%/11.25% for all of 2026, omitting the 1 October rise to 4.35%/11.40%. Under 52 Friday pays, 39 pays use the old rates and 13 the new rates. | Dossier §§2, 4; `ireland.py:24-25,38-40,52,57`. |
| Low | Scenario difference | Pay frequency | Exact PRSI low-pay credits and the MyFutureFund breach payroll depend on pay dates/frequency. The dossier's 52-Friday convention is one reproducible scenario; an annual-only function cannot represent all payrolls. | Dossier §§1, 5. |

## Matches

- PAYE bands (€44,000 at 20%, then 40%) and combined €4,000 credits match.
- USC rates and thresholds match the dossier.
- PRSI is correctly separate from PAYE and USC and uncapped for ordinary Class A pay.

## Output impact

The comparison includes the dossier's MyFutureFund scenario; `Δ = implementation − dossier`, EUR:

| Gross | Impl. net | Dossier net | Δ net | Impl. cost | Dossier cost | Δ cost |
|---:|---:|---:|---:|---:|---:|---:|
| 20,000 | 18,940.18 | 18,974.10 | -33.92 | 22,250.00 | 22,107.50 | +142.50 |
| 60,000 | 44,947.18 | 44,024.68 | +922.50 | 66,750.00 | 67,672.50 | -922.50 |
| 100,000 | 64,569.38 | 63,320.34 | +1,249.04 | 111,250.00 | 112,499.04 | -1,249.04 |
| 200,000 | 112,369.38 | 111,082.84 | +1,286.54 | 222,500.00 | 223,786.54 | -1,286.54 |
| 600,000 | 303,569.38 | 302,132.84 | +1,436.54 | 667,500.00 | 668,936.54 | -1,436.54 |

At €20,000 the PRSI weekly credit makes the dossier's employee PRSI lower than a flat annual 4.2%, more than offsetting the €300 MyFutureFund deduction.

## Recommended disposition

Implement date/pay-period-aware Class A PRSI and expose MyFutureFund enrolment plus payroll frequency. If the product retains an annual approximation, label it and choose an explicit pay calendar rather than using the majority-of-year rate.

## Regression vectors

For 52 equal Friday pays and an enrolled worker with no existing pension, assert `(gross → employer_cost, net)`: `20,000 → 22,107.50, 18,974.10`; `60,000 → 67,672.50, 44,024.68`; `100,000 → 112,499.04, 63,320.34`; `200,000 → 223,786.54, 111,082.84`; `600,000 → 668,936.54, 302,132.84`.
