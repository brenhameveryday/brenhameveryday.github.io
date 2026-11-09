"""Fetch website visit stats from GoatCounter and write them to a JSON file.

Used by .github/workflows/goatcounter-stats.yml. Needs GOATCOUNTER_TOKEN
(a read-only GoatCounter API token) in the environment.
"""
import json
import os
import sys
import time
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta, timezone

SITE = "https://brenhameveryday.goatcounter.com/api/v0"
TOKEN = os.environ["GOATCOUNTER_TOKEN"].strip()
OUT = sys.argv[1] if len(sys.argv) > 1 else "goatcounter.json"
DAYS = 30


def get(path, **params):
    url = f"{SITE}{path}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
        "User-Agent": "brenhameveryday-stats",
    })
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < 3:
                time.sleep(2 ** attempt)
                continue
            print(f"GoatCounter {path} failed: {e.code} {e.read()[:300]!r}", file=sys.stderr)
            raise
    raise RuntimeError("unreachable")


today = date.today()
start = today - timedelta(days=DAYS - 1)
rng = {"start": f"{start}T00:00:00Z", "end": f"{today}T23:59:59Z"}

def try_get(path, **params):
    try:
        return get(path, **params)
    except Exception as e:  # keep going; the daily totals can come from hits
        print(f"Skipping {path}: {e}", file=sys.stderr)
        return {}


hits = get("/stats/hits", limit=100, **rng)
time.sleep(0.5)
refs = try_get("/stats/toprefs", limit=10, **rng)
time.sleep(0.5)
total = try_get("/stats/total", **rng)

by_day = {(start + timedelta(days=i)).isoformat(): 0 for i in range(DAYS)}
if total.get("stats"):
    for s in total["stats"]:
        by_day[s["day"][:10]] = s.get("daily", 0)
else:
    for h in hits.get("hits", []):
        if h.get("event"):
            continue
        for s in h.get("stats", []):
            day = s["day"][:10]
            by_day[day] = by_day.get(day, 0) + s.get("daily", 0)
daily = [{"day": d, "visits": v} for d, v in sorted(by_day.items())]


def window(end_offset, length=7):
    days = [(today - timedelta(days=end_offset + i)).isoformat() for i in range(length)]
    return sum(by_day.get(d, 0) for d in days)


out = {
    "updated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    "start": start.isoformat(),
    "end": today.isoformat(),
    "visits_30d": total.get("total") or sum(by_day.values()),
    "visits_7d": window(0),
    "visits_prev_7d": window(7),
    "daily": daily,
    "pages": [
        {"path": h.get("path"), "title": h.get("title") or "", "visits": h.get("count", 0)}
        for h in hits.get("hits", [])[:15] if not h.get("event")
    ],
    "referrers": [
        {"name": r.get("name") or "Direct / unknown", "visits": r.get("count", 0)}
        for r in refs.get("stats", [])
    ],
}

with open(OUT, "w") as f:
    json.dump(out, f, indent=1)
print(f"Wrote {OUT}: {out['visits_30d']} visits in 30 days, {out['visits_7d']} in last 7")
