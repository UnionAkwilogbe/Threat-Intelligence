"""Client requests for information (RFIs).

An RFI is a question a client has asked, for example "are there any Okta
vulnerabilities we should know about?". The analyst's answer lives in
ti/data/rfis.json. Every daily run then keeps the answer fresh by checking:

  * CISA KEV: has any CVE for this vendor been added to the exploited list?
  * today's stories: does anything mention the RFI's keywords?

If either finds something, the dashboard flags the RFI as needing an update.
"""

import json
import os

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


def track(rfis, stories, kev_index):
    """Attach today's KEV and story matches to each RFI."""
    tracked = []
    for r in rfis:
        kw = r.get("keywords", [])
        kev = [{"id": cve, "name": v.get("vulnerabilityName", ""), "added": v.get("dateAdded", "")}
               for cve, v in sorted(kev_index.items())
               if _hits(f"{v.get('vendorProject', '')} {v.get('product', '')}", kw)]
        matches = [s for s in stories if _hits(f"{s['title']} {s.get('summary', '')}", kw)]
        known = {c["id"] for c in r.get("cves", [])}
        new_cves = sorted({c for s in matches for c in s.get("cves", [])} - known)
        tracked.append(dict(r, kev_hits=kev, matches=matches[:6], new_cves=new_cves,
                            kev_checked=bool(kev_index),
                            needs_update=bool(kev or new_cves)))
    return tracked
