# Romania — implementation comparison

## Compared artifacts

- Independent dossier: `docs/research/2026/romania.md`
- Current implementation: `tools/calc/romania.py`
- Comparison date: 2026-10-04

## Current implementation scenario

Single employee in normal conditions, above all low-income relief bands. The module applies homogeneous rates directly to the comparison table's EUR input; this is valid for the currently documented high-income scope.

## Findings

| Severity | Classification | Area | Finding | Evidence / code |
|---|---|---|---|---|
| Medium | Product decision | Coverage | The high-income linear scenario cannot represent RON-denominated personal-deduction, minimum-base, and minimum-wage-relief rules. Supporting those rules requires conversion around the local statutory thresholds while preserving EUR presentation. | Dossier §§personal deduction/minimum-wage relief; module currency comment. |

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

Retain the direct-EUR formula for the documented high-income scenario. Add a local-currency calculation path for low-income rules before claiming general Romanian coverage, while keeping the table denominated in EUR.

## Regression vectors

Preserve all five exact matches. Add monthly tests immediately around RON 6,050 (H1) and RON 6,325 (H2), plus the two 2026 minimum wages.
