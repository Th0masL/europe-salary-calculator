# 🇪🇺 Europe Salary Calculator

A simple static web page to compare **take-home pay** and the **real cost of
employment** for a salary across **36 European countries** and **11 US cities**.

It answers questions like:

- **“My employer will spend €100,000 total on me — where do I take home the most?”**
  Pick *Employer budget*, type `100,000`, and the table ranks every country by
  net pay (Bulgaria, Albania and Switzerland come out on top; France, Italy and
  Slovenia at the bottom).
- **“What does a €100,000 gross salary mean net, and what does it cost the employer?”**
  Pick *Gross salary*, type `100,000`, and each row shows the net take-home and
  the total employer cost.
- **“I want €50,000 net — which country is cheapest for my employer?”**
  Pick *Net pay* and sort by employer cost.

## Run it

It's a dependency-free static site — just open it:

```bash
# simplest: double-click index.html, or
xdg-open index.html
```

Or serve it (also how to deploy to GitHub Pages):

```bash
python3 -m http.server 8000   # then visit http://localhost:8000
```

Views are shareable: the URL captures the mode and amount, e.g.
`index.html?mode=cost&amount=100000`.

## How it works

Each location has **total employer cost** and **employee net pay** at a few
gross-salary points. Those become `{gross, cost, net}` data points, which all
increase together. The calculator:

1. **Interpolates** linearly between the points to estimate any salary, and
2. **Inverts** the relationship, so you can fix the employer cost, the gross, or
   the target net and solve for the other two.

Amounts outside the benchmark range are extrapolated from the nearest segment
and flagged with a `*`.

### Five data sources (toggle in the UI)

| Source | What | Provides | Locations |
|---|---|---|---|
| **Consensus** *(default)* | Median of the eBook/Skuad/Deel vendor sources, dropping outliers | cost + net | superset (47) |
| **Formula** | Computed from each country's **published 2026 tax rates** (`tools/calc/*.py`, no vendor) | cost + net | 36 European + 11 US |
| **2025 eBook** | Boundless' *“Understanding Employment Costs in Europe in 2025”* (fixed study) | cost + net | 36 EU + 5 US |
| **Skuad** | API behind Boundless' [online calculator](https://boundlesshq.com/cost-calculator/) | cost + net | 35 EU (no Slovenia) + 5 US |
| **Deel** | Deel's [employee-cost](https://www.deel.com/employee-cost-calculator/) + [take-home](https://www.deel.com/take-home-pay-calculator/) calculators (EOR fee removed) | cost + net | 36 EU + 6 US (per-state) |

The sources use **different methodologies and often disagree** (sometimes by
several points of net pay) — comparing them is the point, and **Consensus**
combines them robustly.

**Consensus** = per location and salary point, the **median** of the available
sources for cost and for net, after discarding any value &gt;**10%** from the median
of the others. So a single bad number can't skew it — e.g. Skuad overstates
Estonia's employer cost by ~49%, and that value is dropped rather than blended in.

Employer cost also draws on a fifth source, **[Rippling](https://www.rippling.com/en-GB/employee-cost-calculator)**
(cost only, no net), which is accurate where others drift (it's correct for
Estonia). Rippling's backend errors for a few countries (France, UK, Ireland,
Albania, Moldova, Montenegro), which are simply omitted from its contribution.

Skuad and Deel are **stored snapshots** of live APIs (they can change or
disappear), fetched on the date shown in the app. US cities are handled
separately per source — see [US cities](#us-cities-) below.

### The Formula source — computed from published rates

The other four sources are vendor calculators (or a blend of them). **Formula** is
different: it computes employer cost and net pay **from each country's published
2026 tax rates**, with no EOR vendor in the loop — one self-contained Python module
per country under `tools/calc/`, sharing `tools/calc/engine.py`.

Each module is written from official / authoritative figures (national tax
authorities, PwC / KPMG tax cards), then **cross-checked against the vendor sources
above** as a sanity check — and where a number was contested, verified against an
official worked example. The per-module docstrings record the rates, the reasoning,
and which figures are confirmed vs representative. Coverage: **all 36 European
entries (27 EU + Montenegro + Albania, Moldova, Norway, Serbia, Switzerland, Turkey,
Ukraine, UK) + 11 US cities** = 47 total (the US from `tools/calc_us.py`).

A recurring subtlety the formulas get right (and several vendor calculators get
wrong) is **whether employee social contributions are deductible from the
income-tax base** — it varies by country (e.g. Lithuania / Czechia *no*, Latvia /
Greece / Slovenia *yes*), so neighbours can't be assumed to match.

Non-euro countries (Poland, Denmark, Sweden, Czechia) compute in their local
currency and convert to EUR at FX rates fetched at build time (the FX date is shown
in the app); eurozone countries compute directly in EUR. Build with
`python3 tools/build_formula.py` → `data/formula.json` + `.js`; drop a new
`tools/calc/<country>.py` and it's picked up automatically.

#### Sources evaluated but **not used**

Two other calculators were investigated and deliberately left out — neither
feeds the table or the consensus:

| Source | Endpoint | Why excluded |
|---|---|---|
| **Remote.com** | `POST api.remote.com/api/v1/cost-calculator/estimation` | Employer cost wildly wrong for ~14 countries (e.g. France €195k vs ~€92k elsewhere — a spurious fixed add-on). |
| **Papaya Global** | `GET www.papayaglobal.com/wp-json/next-js/v1/cost-calculator/data/latest` | Its dataset is **stale** (tax rules from financial years **2021-2023**) and aligns poorly with the current sources (off by −10% to +20%). Returns raw tax rules, not computed totals. |

`tools/fetch_remote.py` is kept as a documented reference for its endpoint; the
Papaya fetcher was removed. Both are recorded here so the research isn't lost.

The **“After living costs”** column subtracts Numbeo's estimated annual cost of
living for a single person (capital city for countries, the city itself for US
entries) — a rough proxy for purchasing power.

### US cities (🇺🇸)

The 11 US cities are state-level: Seattle→WA, San Francisco→CA, New York→NY,
Austin→TX, Atlanta→GA, Miami→FL, Chicago→IL, Los Angeles→CA, Boston→MA,
Washington→DC, Denver→CO. (Miami/Florida, like Texas and Washington, has no state
income tax — a strong high-take-home example.) Their numbers come from different
places by source — note the five newest cities (Chicago, LA, Boston, DC, Denver)
have only the Formula/direct-calc figures; the vendor sources don't track them:

- **Consensus** — a **direct calculation from published rates** (`tools/calc_us.py`), with
  **no EOR vendor**: 2025 federal brackets + standard deduction, FICA (with the
  Social Security wage cap), and state income tax — including **NYC local tax** for
  New York. Employer cost = mandatory payroll taxes only (employer FICA + FUTA +
  SUTA; workers' comp/benefits excluded). Single filer, standard deduction.
  **Validated against Deel** — net agrees to **<1%** for every state (Texas/Florida
  exact); only New York differs (~5% lower), and that's because we include the NYC
  local tax Deel omits.
- **Deel** — Deel's own real per-state calc (cost from employee-cost, net from
  take-home). Used as the independent cross-check above. (No Miami in eBook/Skuad —
  the blog only covered 5 cities — so Miami shows under Deel and Consensus only.)
- **2025 eBook & Skuad** — a **single-benchmark blog estimate** from Boundless'
  [US vs Europe 2025 study](https://boundlesshq.com/blog/us-vs-europe-employment-costs-salaries-net-pay-compared-2025-study/):
  one USD data point (local developer rate), converted at `1 € = 1.13 $` and
  modelled at a flat rate. Rougher, flagged with `≈`.

US employer cost is small — **~8–10% on top of gross** (mostly the 7.65% employer
FICA, tapering above the Social Security cap) — versus 50%+ across much of Europe.
Skuad's *own* US tax data isn't used (it applies a flat ~10% "state tax" even
where there is none). Cost of living stays city-specific.

## Project layout

```
index.html                   # markup
styles.css                   # styling
app.js                       # interpolation + table rendering (vanilla JS)
data/
  ebook.json / .js           # 2025 eBook dataset
  skuad.json / .js           # Skuad live-API snapshot
  deel.json  / .js           # Deel live-API snapshot (cost + net)
  rippling.json / .js        # Rippling live-API snapshot (employer cost only)
  us.json    / .js           # US: direct calc from published rates (11 cities, no EOR)
  consensus.json / .js       # merged sources, used as the default
  formula.json   / .js       # per-country calc from published rates (build_formula.py)
tools/
  calc/                      # Formula source: one module per country + engine.py
    engine.py                #   shared maths (progressive brackets, caps)
    <country>.py             #   36 European modules — compute(gross) -> (cost, net)
    country-data-prompt.md   #   reusable research prompt for gathering a country's rates
  build_formula.py           # build data/formula.json/.js from tools/calc/* (+ FX, + US)
  extract_data.py            # eBook dataset (PDF → EU countries, + US cities)
  fetch_skuad.py             # Skuad dataset (live API)
  fetch_deel.py              # Deel dataset  (live API: cost + net, incl. US states)
  fetch_rippling.py          # Rippling dataset (live API: employer cost; accurate)
  fetch_remote.py            # Remote.com (kept for reference; excluded — unreliable)
  calc_us.py                 # US cost + net from published 2025 federal/state rates
  fetch_numbeo.py            # refresh cost-of-living from current Numbeo
  compare_sources.py         # prints a per-country alignment report at a given salary
  build_consensus.py         # merges the sources into data/consensus.json
```

The `.js` files just wrap the JSON in a `window.SALARY_DATA_*` global so the page
works when opened directly from `file://` (no server needed). Each `data/*.json`
is the canonical, human-readable copy.

### Regenerating the data

```bash
# 1. eBook — needs the gitignored PDF in the repo root + pdftotext (poppler-utils)
python3 tools/extract_data.py     # → data/ebook.json + .js

# 2. live API snapshots (no PDF needed; read ebook.json for flags / cost-of-living)
python3 tools/fetch_skuad.py      # → data/skuad.json + .js
python3 tools/fetch_deel.py       # → data/deel.json  + .js
python3 tools/fetch_rippling.py   # → data/rippling.json + .js  (employer cost)

# 3. US direct calc from published rates (no vendor; self-validates against Deel if present)
python3 tools/calc_us.py          # → data/us.json + .js

# 3b. Formula source — per-country calc from published rates (also pulls in US from step 3)
python3 tools/build_formula.py    # → data/formula.json + .js  (fetches FX for non-euro)

# 4. optional: refresh cost-of-living from current Numbeo (slow; rate-limited)
python3 tools/fetch_numbeo.py     # → data/cost_of_living.json + .js

# 5. inspect alignment, then build the consensus the website uses
python3 tools/compare_sources.py 60000   # report at €60k (writes data/comparison_<n>.json)
python3 tools/build_consensus.py         # → data/consensus.json + .js
```

For the eBook source, the European countries are parsed from the PDF; the US
cities are a hardcoded table (USD, sourced from the blog) converted to EUR — edit
`US_CITIES` / `FX_USD_PER_EUR` in `extract_data.py` to change them.

### Finding the API endpoints

`fetch_skuad.py` / `fetch_deel.py` / `fetch_remote.py` each document the exact
endpoint and request body they hit (reverse-engineered from each calculator's JS
and network traffic). Deel exposes two tools — `take_home_calculator/calculate`
(net) and `employment_cost` (employer cost, monthly salary, full country name) —
and `fetch_deel.py` combines them, stripping Deel's flat EOR management fee from
the cost.

### Data shape

```jsonc
{
  "name": "Austria",
  "flag": "🇦🇹",
  "eu": true,
  "devSalary": 61000,        // avg mid-level software developer gross (EUR/yr)
  "costOfLiving": 23387,     // single person, capital city (EUR/yr)
  "points": [
    { "gross": 32000, "cost": 42883, "net": 23122 },
    { "gross": 60000, "cost": 80406, "net": 37647 },
    { "gross": 61000, "cost": 81746, "net": 38108 },   // developer-average point
    { "gross": 150000, "cost": 188711, "net": 87014 }
  ]
}
```

US cities carry `"us": true` and `"approx": true`, and have just two points
(origin + the single market-rate benchmark), giving a flat effective rate:

```jsonc
{
  "name": "Austin, TX",
  "flag": "🇺🇸",
  "eu": false, "us": true, "approx": true,
  "devSalary": 100575,       // market-rate developer gross, EUR (from USD)
  "costOfLiving": 35197,
  "points": [
    { "gross": 0, "cost": 0, "net": 0 },
    { "gross": 100575, "cost": 111035, "net": 78176 }
  ]
}
```

## ⚠️ Disclaimer

These figures are **estimates for comparison only**. They ignore personal
allowances, marital status, children, regional taxes, optional benefits,
bonuses, and currency fluctuations, and are interpolated between three
benchmarks. **Do not use them as precise payroll or budgeting figures.**

Data © Boundless (2025) · cost of living © Numbeo · developer salaries © TalentUp.
