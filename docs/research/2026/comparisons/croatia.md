# Croatia — 2026 implementation comparison

## Compared artifacts

- Dossier: `docs/research/2026/croatia.md` (official Tax Administration/legal sources, accessed 2026-10-04).
- Implementation: `tools/calc/croatia.py`.

## Current implementation scenario

Zagreb resident, pillar-I/II member, EUR7,200 allowance, 23%/33% Zagreb PIT, capped 20% employee pension and uncapped 16.5% employer health. The module implicitly models the no-youth-relief alternative.

## Findings

| Severity | Classification | Area | Finding | Evidence / code |
|---|---|---|---|---|
| High | Confirmed mismatch | Youth relief | The dossier's requested age-30 profile (born 1996) receives a 50% reduction of PIT attributable to the lower band, capped at half of EUR13,800. The module omits it. | Dossier §§1, 2.4, 4; `croatia.py:42-55`. |
| Medium | Scenario difference | Age ambiguity | The module exactly reproduces the dossier's alternative employee born in 1995 and turning 31 during 2026. The product currently has no age/birth-year input, so that scenario choice is silent. | Dossier §4; `croatia.py:47-55`. |
| Medium | Scenario difference | Municipality | Zagreb 23%/33% is explicit and valid but not national; local-government rates vary. | Dossier §§1, 2.3; `croatia.py:11-13,44`. |

## Matches

- Pension cap EUR143,496, employee 15%+5%, allowance EUR7,200, taxable-base order, Zagreb threshold EUR60,000, and employer health 16.5% match exactly.
- Employer cost matches at all five vectors.

## Output impact

| Gross EUR | Module net | Dossier age-30 net | Net delta | Module and dossier cost |
|---:|---:|---:|---:|---:|
| 20,000 | 13,976.00 | 14,988.00 | -1,012.00 | 23,300.00 |
| 60,000 | 38,616.00 | 43,308.00 | -4,692.00 | 69,900.00 |
| 100,000 | 61,976.00 | 68,876.00 | -6,900.00 | 116,500.00 |
| 200,000 | 123,147.54 | 130,047.54 | -6,900.00 | 233,000.00 |
| 600,000 | 391,147.54 | 398,047.54 | -6,900.00 | 699,000.00 |

## Recommended disposition

Add birth year/age eligibility or state a no-youth-relief product scope. For the existing documented age-30 profile, implement the 50% lower-band reduction after preliminary PIT.

## Regression vectors

All five dossier rows are authoritative for Zagreb and birth year 1996. EUR100k is the key vector: preliminary PIT EUR18,024, youth reduction EUR6,900, final PIT EUR11,124.
