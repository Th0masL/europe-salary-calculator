# Romania — implementation comparison

## Compared artifacts

- Independent dossier: `docs/research/2026/romania.md`
- Current implementation: `tools/calc/romania.py`
- Comparison date: 2026-10-04

## Current implementation scenario

Single employee in normal conditions, above all low-income relief bands. The module applies homogeneous rates directly in EUR although Romanian payroll currency is RON.

## Findings

| Severity | Classification | Area | Finding | Evidence / code |
|---|---|---|---|---|
| Medium | Product decision | Currency/coverage | `CURRENCY="EUR"` is harmless only for the high-income linear regime. It prevents authoritative RON threshold, personal-deduction, minimum-base, and minimum-wage-relief tests. | Dossier §§personal deduction/minimum-wage relief; module currency comment. |

## Matches

At all dossier vectors, CAS 25%, CASS 10%, PIT 10% on gross less CAS/CASS, CAM 2.25%, net 58.5%, and employer cost 102.25% match exactly.

## Output impact

| Gross RON | Net delta | Employer-cost delta |
|---:|---:|---:|
| 100,000 | 0.00 | 0.00 |
| 300,000 | 0.00 | 0.00 |
| 500,000 | 0.00 | 0.00 |
| 1,000,000 | 0.00 | 0.00 |
| 3,000,000 | 0.00 | 0.00 |

## Recommended disposition

Retain the formula for the documented high-income scenario, but change/parameterize currency and add low-income rules before claiming general Romanian coverage.

## Regression vectors

Preserve all five exact matches. Add monthly tests immediately around RON 6,050 (H1) and RON 6,325 (H2), plus the two 2026 minimum wages.
