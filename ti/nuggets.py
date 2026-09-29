"""Daily knowledge pack.

Every day you get:
  * one new lesson (rotates through ti/data/nuggets.json)
  * review cards for lessons from 1, 3 and 7 days ago (spaced repetition,
    so things come back just as you are about to forget them)
  * a word of the day from ti/data/glossary.json
  * a hands-on enrichment drill built from today's real top story

Repetition is deliberate. Add your own lessons to nuggets.json at any time.
"""

import json
import os
from datetime import date

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
EPOCH = date(2026, 1, 1)
REVIEW_GAPS = (1, 3, 7)


def _load(name):
    with open(os.path.join(DATA_DIR, name), encoding="utf-8") as fh:
        return json.load(fh)


def build_pack(today, stories):
    nuggets = _load("nuggets.json")
    glossary = _load("glossary.json")
    day = (today - EPOCH).days
    lesson = nuggets[day % len(nuggets)]
    reviews = []
    for gap in REVIEW_GAPS:
        n = nuggets[(day - gap) % len(nuggets)]
        if n["id"] != lesson["id"] and n["id"] not in {r["id"] for r in reviews}:
            reviews.append(dict(n, gap=gap))
    term, meaning = glossary[day % len(glossary)]
    return {
        "lesson": lesson,
        "reviews": reviews,
        "word": {"term": term, "meaning": meaning},
        "drill": build_drill(stories),
        "day_number": day + 1,
        "total_lessons": len(nuggets),
    }


def build_drill(stories):
    """Turn today's best story with something to look up into a guided exercise."""
    def has_hook(s):
        return s.get("cves") or s.get("iocs") or s.get("kind") == "ransomware"

    story = next((s for s in stories if has_hook(s)), stories[0] if stories else None)
    if not story:
        return None
    steps = []
    if story.get("kind") == "ransomware":
        victim = story.get("extra", {}).get("victim", "the victim")
        group = story.get("extra", {}).get("group", "the group")
        steps = [
            f"Search Companies House for '{victim}'. Note its SIC code, size and registered region.",
            f"Look up {group} on ransomware.live. How many UK victims has it listed this year?",
            f"Search '{group} initial access' to find how they usually break in (ATT&CK tactic TA0001).",
            "Which of your clients share this sector or region? Write a two-line BLUF heads-up for them.",
            "Grade your sources with the Admiralty Code, for example C3 for a leak-site claim.",
        ]
    elif story.get("cves"):
        cve = story["cves"][0]
        steps = [
            f"Open nvd.nist.gov/vuln/detail/{cve}. Note the CVSS score and affected product.",
            f"Check {cve} on the CISA KEV list and its EPSS score at first.org/epss. Severity vs likelihood vs reality?",
            "Find the vendor's own advisory. Is there a patch or only a workaround?",
            "Search Shodan or Censys for the product with country:GB. How exposed is the UK?",
            "Write a BLUF: which clients, what action, by when (Cyber Essentials allows 14 days, KEV says sooner).",
        ]
    else:
        ioc_type, values = next(iter(story["iocs"].items()))
        sample = values[0]
        steps = [
            f"Take the {ioc_type} indicator {sample} (it is defanged, keep it that way when sharing).",
            "IP: look it up on stat.ripe.net and AbuseIPDB. Domain: WHOIS, crt.sh and passive DNS.",
            "Is it on any allowlist (cloud provider, popular site)? If so it may be a false positive.",
            "Add first_seen, last_seen and an expiry date.",
            "Place it on the Pyramid of Pain and the Kill Chain.",
        ]
    return {"story_title": story["title"], "story_url": story.get("url", ""), "steps": steps}
