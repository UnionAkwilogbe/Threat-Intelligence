"""Client requests for information (RFIs).

An RFI is a question a client has asked, for example "are there any Okta
vulnerabilities we should know about?". The analyst's answer lives in
ti/data/rfis.json. Every daily run then keeps the answer fresh by checking:

  * CISA KEV: has any CVE for this vendor been added to the exploited list?
  * today's stories: does anything mention the RFI's keywords?
  * today's indicators (URLhaus, ThreatFox): any URL, domain or IP whose
    value contains the keywords, for example a fake Okta login page

If any check finds something, the dashboard flags the RFI as needing an update.
"""

import json
import os
import re

from .nuggets import DATA_DIR


def load_rfis(path=None):
    path = path or os.path.join(DATA_DIR, "rfis.json")
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as fh:
        return json.load(fh).get("rfis", [])


def _hits(text, keywords):
    text = text.lower()
    return any(k.lower() in text for k in keywords)


def _token_hits(value, keywords):
    """Whole-word match inside an indicator: 'okta-terraform' matches okta, 'oktaymoral' does not."""
    tokens = set(re.split(r"[^a-z0-9]+", value.lower()))
    return any(k.lower() in tokens for k in keywords)


def defang(value):
    """Make an indicator unclickable before it is shown or shared: hxxp://evil[.]com."""
    return re.sub(r"^http", "hxxp", value).replace(".", "[.]")


def ioc_pool(stats):
    """All raw indicators collected today (URLhaus, ThreatFox), kept in memory only."""
    return [i for k, v in stats.items() if k.startswith("ioc_pool_") for i in v]


def track(rfis, stories, kev_index, iocs=None):
    """Attach today's KEV, story and indicator matches to each RFI.

    `iocs` is today's indicator pool; None means the IOC feeds were unavailable.
    """
    tracked = []
    for r in rfis:
        kw = r.get("keywords", [])
        kev = [{"id": cve, "name": v.get("vulnerabilityName", ""), "added": v.get("dateAdded", "")}
               for cve, v in sorted(kev_index.items())
               if _hits(f"{v.get('vendorProject', '')} {v.get('product', '')}", kw)]
        matches = [s for s in stories if _hits(f"{s['title']} {s.get('summary', '')}", kw)]
        known = {c["id"] for c in r.get("cves", [])}
        new_cves = sorted({c for s in matches for c in s.get("cves", [])} - known)
        ioc_kw = r.get("ioc_keywords", kw)
        known_iocs = set(r.get("known_iocs", []))  # already reviewed and reported to the client
        ioc_hits = [dict(i, value=defang(i["value"]), known=i["value"] in known_iocs)
                    for i in (iocs or []) if _token_hits(i["value"], ioc_kw)]
        new_iocs = [i for i in ioc_hits if not i["known"]]
        tracked.append(dict(r, kev_hits=kev, matches=matches[:6], new_cves=new_cves,
                            ioc_hits=ioc_hits[:25], ioc_count=len(ioc_hits), new_ioc_count=len(new_iocs),
                            ioc_checked=bool(iocs), kev_checked=bool(kev_index),
                            needs_update=bool(kev or new_cves or new_iocs)))
    return tracked
