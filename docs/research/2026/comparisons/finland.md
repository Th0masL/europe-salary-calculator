# Finland — 2026 implementation comparison

## Compared artifacts

- Dossier: `docs/research/2026/finland.md` (official Vero/ETK sources, accessed 2026-10-04).
- Implementation: `tools/calc/finland.py`.

## Current implementation scenario

Single employee, no church tax, but the implementation uses an average 7.57% municipality and a deliberately simplified deduction/credit model. Employer cost uses representative averages.

## Findings

| Severity | Classification | Area | Finding | Evidence / code |
|---|---|---|---|---|
| Critical | Confirmed mismatch | Tax deductions/credits | The module omits the basic allowance and uses a simplified one-slope earned-income credit (EUR3,225, 4.5% taper). The dossier's 2026 formula has a EUR750 acquisition deduction, earned-income deduction/basic allowance order, and EUR3,430 credit with statutory accrual/tapers and ordering across state/municipal/health tax. | Dossier §§3-6; `finland.py:35-38,51-55`. |
| High | Confirmed mismatch | Health bases/order | It deducts daily allowance before both state and municipal tax and charges 1.1% medical care directly on gross. The dossier derives separate state/municipal/health bases and applies the credit in statutory order; daily allowance remains a separate cash charge. | Dossier §§2, 4-7; `finland.py:33-34,48-58`. |
| High | Confirmed mismatch | YLE | Module uses 2.5% above EUR14,000 of its tax base capped EUR163; final 2026 dossier formula/results cap at EUR160 and use the statutory taxable earned/capital-income base. | Dossier §6; `finland.py:56`. |
| High | Scenario difference | Municipality | Module uses 7.57% average; dossier selects Helsinki 5.30%. Municipality must be explicit. | Dossier §§1, 4; `finland.py:41`. |
| Medium | Scenario difference | Employer averages | Employer accident 0.7% and group life 0.07% differ from dossier's explicit averages 0.51%/0.06%. TyEL is also employer-specific. | Dossier §8; `finland.py:16-17,43`. |

## Matches

- Employee TyEL 7.30%, unemployment 0.89%, daily allowance 0.88%, acquisition deduction EUR750, employer TyEL 17.10%, health 1.91% and unemployment 0.31% match the selected broad profile.

## Output impact

| Gross EUR | Module net | Dossier Helsinki net | Net delta | Module cost | Dossier average cost | Cost delta |
|---:|---:|---:|---:|---:|---:|---:|
| 20,000 | 17,581.28 | 18,083.50 | -502.22 | 24,018.00 | 23,978.00 | +40.00 |
| 60,000 | 39,495.70 | 42,379.24 | -2,883.54 | 72,054.00 | 71,934.00 | +120.00 |
| 100,000 | 57,455.94 | 62,783.93 | -5,327.99 | 120,090.00 | 119,890.00 | +200.00 |
| 200,000 | 106,303.79 | 113,795.66 | -7,491.87 | 240,180.00 | 239,780.00 | +400.00 |
| 600,000 | 301,695.19 | 317,842.58 | -16,147.39 | 720,540.00 | 719,340.00 | +1,200.00 |

Employee deltas combine confirmed formula errors with the municipality scenario difference; they should not be attributed solely to Helsinki's rate.

## Recommended disposition

Replace the simplified tax path with the dossier's ordered state, municipal, health, allowances and credit algorithm; update YLE; make municipality configurable. Label employer figures as an average scenario and update its selected rates.

## Regression vectors

Use all five dossier rows for Helsinki. EUR20k is essential for credit spillover that eliminates state, municipal and healthcare tax; EUR60k tests the fixed post-taper credit; EUR600k tests YLE cap and high brackets.
