#!/usr/bin/env python3
"""
Refresh annual cost-of-living estimates from current Numbeo data and write
data/cost_of_living.json + data/cost_of_living.js.

Method (matches Boundless/Numbeo): for a single person in a 1-bedroom city-centre
apartment, annual cost = (single-person monthly costs excl. rent + 1-bed
city-centre rent) x 12, in EUR.

Numbeo shows the single-person summary in EUR but the rent table in the city's
LOCAL currency, so we convert rent via ECB rates (frankfurter.app). Currencies
ECB doesn't cover (Albanian lek, Serbian dinar, Moldovan leu, Ukrainian hryvnia)
and any fetch failure or implausible value fall back to the existing figure.

Usage:
    python3 tools/fetch_numbeo.py
"""
import html as htmlmod
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
URL = "https://www.numbeo.com/cost-of-living/in/{}"
FX_URL = "https://open.er-api.com/v6/latest/EUR"  # covers 160+ currencies incl. ALL/RSD/MDL/UAH

# A complete, realistic Chrome request — a bare UA can trip CloudFlare/bot checks.
HEADERS = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"),
    "Accept": ("text/html,application/xhtml+xml,application/xml;q=0.9,"
               "image/avif,image/webp,*/*;q=0.8"),
    "Accept-Language": "en-US,en;q=0.9",
    "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Upgrade-Insecure-Requests": "1",
}


def log(msg):
    print(msg, flush=True)  # flush so progress is visible live, not buffered

# location name -> (Numbeo city slug, local currency). European entries use the
# capital city; US entries use the city itself.
LOCATIONS = {
    "Albania": ("Tirana", "ALL"), "Austria": ("Vienna", "EUR"),
    "Belgium": ("Brussels", "EUR"), "Bulgaria": ("Sofia", "BGN"),
    "Croatia": ("Zagreb", "EUR"), "Cyprus": ("Nicosia", "EUR"),
    "Czech Republic": ("Prague", "CZK"), "Denmark": ("Copenhagen", "DKK"),
    "Estonia": ("Tallinn", "EUR"), "Finland": ("Helsinki", "EUR"),
    "France": ("Paris", "EUR"), "Germany": ("Berlin", "EUR"),
    "Greece": ("Athens", "EUR"), "Hungary": ("Budapest", "HUF"),
    "Ireland": ("Dublin", "EUR"), "Italy": ("Rome", "EUR"),
    "Latvia": ("Riga", "EUR"), "Lithuania": ("Vilnius", "EUR"),
    "Luxembourg": ("Luxembourg", "EUR"), "Malta": ("Valletta", "EUR"),
    "Moldova": ("Chisinau", "MDL"), "Montenegro": ("Podgorica", "EUR"),
    "Netherlands": ("Amsterdam", "EUR"), "Norway": ("Oslo", "NOK"),
    "Poland": ("Warsaw", "PLN"), "Portugal": ("Lisbon", "EUR"),
    "Romania": ("Bucharest", "RON"), "Serbia": ("Belgrade", "RSD"),
    "Slovakia": ("Bratislava", "EUR"), "Slovenia": ("Ljubljana", "EUR"),
    "Spain": ("Madrid", "EUR"), "Sweden": ("Stockholm", "SEK"),
    "Switzerland": ("Zurich", "CHF"), "Turkey": ("Istanbul", "TRY"),
    "Ukraine": ("Kiev", "UAH"), "United Kingdom": ("London", "GBP"),
    "Seattle, WA": ("Seattle", "USD"), "San Francisco, CA": ("San-Francisco", "USD"),
    "New York, NY": ("New-York", "USD"), "Austin, TX": ("Austin", "USD"),
    "Atlanta, GA": ("Atlanta", "USD"), "Miami, FL": ("Miami", "USD"),
}


DELAY = 5.0  # seconds between Numbeo requests — be gentle; the IP gets blocked fast


def http(url):
    """Single attempt, no retries (we must not hammer Numbeo's rate limit)."""
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def num(s):
    return float(s.replace(",", ""))


def _rent(page, label):
    m = re.search(label + r".*?first_currency\">\D*?([\d,]+(?:\.\d+)?)", page, re.S)
    return num(m.group(1)) if m else None


def parse(page):
    """Return (single_person_eur, rent_local) or None if missing.

    Rent = the AVERAGE of the 1-bed city-centre and outside-of-centre rents (a
    balanced figure). Numbeo encodes currency symbols as HTML entities
    (€ = &#8364;), whose digits would corrupt the numbers — so unescape first.
    """
    page = htmlmod.unescape(page)
    s = re.search(r"single person are\D*?([\d,]+(?:\.\d+)?)", page)
    centre = _rent(page, "1 Bedroom Apartment in City Centre")
    outside = _rent(page, "1 Bedroom Apartment Outside of City Centre")
    if not s or centre is None:
        return None
    rent = (centre + outside) / 2 if outside is not None else centre
    return num(s.group(1)), rent


def baseline():
    """Existing cost-of-living values (eBook countries + US cities) as fallback."""
    out = {}
    for fn in ("ebook.json", "us.json"):
        p = ROOT / "data" / fn
        if p.exists():
            for c in json.loads(p.read_text(encoding="utf-8"))["countries"]:
                if c.get("costOfLiving"):
                    out.setdefault(c["name"], c["costOfLiving"])
    return out


OUT_JSON = ROOT / "data" / "cost_of_living.json"
OUT_JS = ROOT / "data" / "cost_of_living.js"


def save(result, done):
    doc = {"meta": {"source": "Numbeo (current)",
                    "method": "single person + avg(1-bed city-centre, outside-centre) rent, annual EUR",
                    "refreshed": sorted(done)},
           "costOfLiving": result}
    OUT_JSON.write_text(json.dumps(doc, indent=2, ensure_ascii=False), encoding="utf-8")
    OUT_JS.write_text(
        "// AUTO-GENERATED from data/cost_of_living.json by tools/fetch_numbeo.py - do not edit.\n"
        "window.COST_OF_LIVING = " + json.dumps(result, ensure_ascii=False) + ";\n",
        encoding="utf-8")


def main():
    old = baseline()
    # resume: start from baseline, overlay anything already done in a prior run
    result, done = dict(old), set()
    if OUT_JSON.exists():
        prior = json.loads(OUT_JSON.read_text(encoding="utf-8"))
        result.update(prior.get("costOfLiving", {}))
        done = set(prior.get("meta", {}).get("refreshed", []))

    # optional batch size: `fetch_numbeo.py 5` only fetches 5 new cities, then stops
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else len(LOCATIONS)
    fetched = 0

    log("Fetching ECB FX rates …")
    rates = json.loads(http(FX_URL))["rates"]  # EUR -> currency
    log(f"  FX ok ({len(rates)} currencies). Already finalised: {len(done)}/{len(LOCATIONS)}"
        f"; this run will fetch up to {limit}.")

    total = len(LOCATIONS)
    for i, (name, (slug, cur)) in enumerate(LOCATIONS.items(), 1):
        prev = old.get(name)
        if name in done:
            log(f"[{i}/{total}] {name}: already done → skip")
            continue
        if fetched >= limit:
            log(f"      reached batch limit of {limit} — stopping (re-run to continue)")
            break
        if cur != "EUR" and cur not in rates:
            log(f"[{i}/{total}] {name} ({cur}): no ECB FX → keep €{prev} (final)")
            done.add(name)
            continue

        log(f"[{i}/{total}] {name} ({slug}, {cur}): fetching …")
        fetched += 1
        try:
            page = http(URL.format(slug))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                ra = (e.headers.get("Retry-After") or "").strip()
                log(f"      *** HTTP 429 RATE LIMITED (Retry-After={ra!r}). STOPPING. ***")
                log("      Reconnect the VPN to a fresh IP and re-run — it resumes here.")
                break  # do NOT keep requesting; protect the IP
            log(f"      HTTP {e.code} (bad slug?) → keep €{prev} (final)")
            done.add(name)
            time.sleep(DELAY)
            continue
        except Exception as e:  # noqa: BLE001
            log(f"      {type(e).__name__}: {e} → keep €{prev} (final)")
            done.add(name)
            time.sleep(DELAY)
            continue

        parsed = parse(page)
        if not parsed:
            log(f"      could not parse single/rent ({len(page)} bytes) → keep €{prev} (final)")
            done.add(name)
        else:
            single_eur, rent_local = parsed
            rent_eur = rent_local if cur == "EUR" else rent_local / rates[cur]
            annual = round((single_eur + rent_eur) * 12)
            detail = (f"single €{single_eur:.0f} + rent {rent_local:.0f} {cur} "
                      f"(€{rent_eur:.0f}) → €{annual}/yr (old €{prev})")
            if prev and abs(annual - prev) / prev > 1.0:  # only reject >100% (likely a parse error)
                log(f"      {detail}  SUSPECT (>100% change) → keep old")
            else:
                result[name] = annual
                log(f"      {detail}  ✓")
            done.add(name)
        save(result, done)  # persist after every city so progress is never lost
        time.sleep(DELAY)

    save(result, done)
    remaining = [n for n in LOCATIONS if n not in done]
    log(f"\n=== finalised {len(done)}/{total}; remaining: "
        f"{', '.join(remaining) if remaining else 'none — all done!'} ===")


if __name__ == "__main__":
    main()
