# Moldova — implementation comparison

## Compared artifacts

- Independent dossier: `docs/research/2026/moldova.md`
- Current implementation: `tools/calc/moldova.py`
- Comparison date: 2026-10-04

## Current implementation scenario

Both artifacts model an ordinary private employer subject to 24% employer BASS and a resident employee subject to 9% AOAM and 12% PIT. The implementation additionally deducts a nonexistent 6% employee social contribution.

## Findings

| Severity | Classification | Area | Finding | Evidence / code |
|---|---|---|---|---|
| Critical | Confirmed mismatch | Employee social insurance | Ordinary employees do not pay a 6% BASS/CAS contribution in 2026. The module both withholds it and deducts it from PIT base, understating net by 5.28% of gross. | Dossier §§2, 5; `moldova.py:3-6,12-13,24,34-39`. |
| Medium | Confirmed mismatch | Personal-exemption test | The MDL 360,000 limit tests pre-exemption taxable income after mandatory AOAM, with loss at `>= 360,000`; the module tests gross with `<=`. This affects gross roughly MDL 360,000–395,604.40, though none of the five dossier vectors. | Dossier §§1, 5; `moldova.py:27-28,35-36`. |

## Matches

- Employee AOAM 9%, employer BASS 24%, PIT 12%, and the MDL 29,700 exemption amount match.
- Employer cost matches all requested vectors exactly.
- Bonuses included in employment gross receive the same ordinary treatment.

## Output impact

`Δ = implementation − dossier`, MDL:

| Gross | Impl. net | Dossier net | Δ net | Impl. cost | Dossier cost | Δ cost |
|---:|---:|---:|---:|---:|---:|---:|
| 400,000 | 299,200 | 320,320 | -21,120 | 496,000 | 496,000 | 0 |
| 1,200,000 | 897,600 | 960,960 | -63,360 | 1,488,000 | 1,488,000 | 0 |
| 2,000,000 | 1,496,000 | 1,601,600 | -105,600 | 2,480,000 | 2,480,000 | 0 |
| 4,000,000 | 2,992,000 | 3,203,200 | -211,200 | 4,960,000 | 4,960,000 | 0 |
| 12,000,000 | 8,976,000 | 9,609,600 | -633,600 | 14,880,000 | 14,880,000 | 0 |

## Recommended disposition

Remove employee BASS entirely and test the personal exemption against `gross − 9% AOAM`, using the statutory strict boundary. Keep special employer categories outside the ordinary 24% scenario.

## Regression vectors

Assert `(gross MDL → employer_cost, net)`: `400,000 → 496,000, 320,320`; `1,200,000 → 1,488,000, 960,960`; `2,000,000 → 2,480,000, 1,601,600`; `4,000,000 → 4,960,000, 3,203,200`; `12,000,000 → 14,880,000, 9,609,600`. Add boundary tests immediately below and at `T0 = 360,000`.
