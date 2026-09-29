"""Collectors: one small function per threat intel source.

Each collector returns a dict:
    {"items": [ ...story dicts... ], "stats": { ...anything extra... }}

A story dict always has: source, kind, title, url, published (ISO string),
summary, uk_source (bool). Collectors never crash the run: `collect_all()`
catches errors and records them in the source health table instead.
"""

import csv
import html
import io
import json
import os
import re
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime

from .http import fetch, fetch_json

# ---------------------------------------------------------------------------
# News and advisory RSS feeds. `uk` marks sources that are UK based or UK
# focused, which gives their stories a relevance boost later on.
# ---------------------------------------------------------------------------
RSS_FEEDS = [
    # UK government and UK focused
    {"id": "ncsc", "name": "NCSC UK", "uk": True, "kind": "advisory",
     "url": "https://www.ncsc.gov.uk/api/1/services/v1/all-rss-feed.xml"},
    {"id": "ico", "name": "ICO (UK regulator)", "uk": True, "kind": "news",
     "url": "https://ico.org.uk/global/rss-feeds/news/"},
    {"id": "computerweekly", "name": "Computer Weekly Security", "uk": True, "kind": "news",
     "url": "https://www.computerweekly.com/rss/IT-security.xml"},
    {"id": "theregister", "name": "The Register Security", "uk": True, "kind": "news",
     "url": "https://www.theregister.com/security/headlines.atom"},
    {"id": "infosecmag", "name": "Infosecurity Magazine", "uk": True, "kind": "news",
     "url": "https://www.infosecurity-magazine.com/rss/news/"},
    # Global news and research
    {"id": "bleeping", "name": "BleepingComputer", "uk": False, "kind": "news",
     "url": "https://www.bleepingcomputer.com/feed/"},
    {"id": "therecord", "name": "The Record", "uk": False, "kind": "news",
     "url": "https://therecord.media/feed"},
    {"id": "thehackernews", "name": "The Hacker News", "uk": False, "kind": "news",
     "url": "https://feeds.feedburner.com/TheHackersNews"},
    {"id": "krebs", "name": "Krebs on Security", "uk": False, "kind": "news",
     "url": "https://krebsonsecurity.com/feed/"},
    {"id": "sans", "name": "SANS Internet Storm Center", "uk": False, "kind": "research",
     "url": "https://isc.sans.edu/rssfeed_full.xml"},
    {"id": "securityweek", "name": "SecurityWeek", "uk": False, "kind": "news",
     "url": "https://www.securityweek.com/feed/"},
    {"id": "cisa_adv", "name": "CISA Advisories", "uk": False, "kind": "advisory",
     "url": "https://www.cisa.gov/cybersecurity-advisories/all.xml"},
]

KEV_URL = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
NVD_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"
RANSOMWARE_URL = "https://api.ransomware.live/v2/recentvictims"
FEODO_URL = "https://feodotracker.abuse.ch/downloads/ipblocklist.json"
URLHAUS_URL = "https://urlhaus.abuse.ch/downloads/csv_recent/"
THREATFOX_URL = "https://threatfox.abuse.ch/export/json/recent/"

UK_COUNTRY_CODES = {"GB", "UK", "GBR", "UNITED KINGDOM"}

_TAG_RE = re.compile(r"<[^>]+>")
_WS_RE = re.compile(r"\s+")


def clean_text(value, limit=600):
    """Strip HTML tags and squash whitespace so summaries read cleanly."""
    if not value:
        return ""
    text = html.unescape(_TAG_RE.sub(" ", value))
    text = _WS_RE.sub(" ", text).strip()
    if len(text) > limit:
        text = text[: limit - 1].rsplit(" ", 1)[0] + "…"
    return text


def parse_date(value):
    """Turn the many date formats feeds use into an aware UTC datetime (or None)."""
    if not value:
        return None
    value = value.strip()
    try:
        dt = parsedate_to_datetime(value)  # RFC 822, used by RSS
    except (TypeError, ValueError, IndexError):
        dt = None
    if dt is None:
        cleaned = value.replace("Z", "+00:00")
        for fmt in (None, "%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M:%S.%f", "%Y-%m-%d"):
            try:
                dt = datetime.fromisoformat(cleaned) if fmt is None else datetime.strptime(value, fmt)
                break
            except ValueError:
                continue
    if dt is None:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def _iso(dt):
    return dt.isoformat() if dt else ""


def _local(tag):
    """'{namespace}title' -> 'title'."""
    return tag.rsplit("}", 1)[-1]


def parse_feed(raw):
    """Parse RSS 2.0 or Atom bytes into a list of {title, url, published, summary}."""
    root = ET.fromstring(raw)
    entries = []
    for node in root.iter():
        if _local(node.tag) not in ("item", "entry"):
            continue
        entry = {"title": "", "url": "", "published": None, "summary": ""}
        for child in node:
            name = _local(child.tag)
            text = (child.text or "").strip()
            if name == "title":
                entry["title"] = clean_text(text, 300)
            elif name == "link":
                entry["url"] = child.attrib.get("href") or text or entry["url"]
            elif name in ("pubDate", "published", "updated", "date") and not entry["published"]:
                entry["published"] = parse_date(text)
            elif name in ("description", "summary", "content", "encoded") and not entry["summary"]:
                entry["summary"] = clean_text(text)
        if entry["title"]:
            entries.append(entry)
    return entries


# ---------------------------------------------------------------------------
# Collectors
# ---------------------------------------------------------------------------

def collect_rss(feed, since):
    raw = fetch(f"rss_{feed['id']}.xml", feed["url"])
    items = []
    for entry in parse_feed(raw):
        published = entry["published"]
        if published and published < since:
            continue
        items.append({
            "source": feed["name"],
            "source_id": feed["id"],
            "kind": feed["kind"],
            "title": entry["title"],
            "url": entry["url"],
            "published": _iso(published),
            "summary": entry["summary"],
            "uk_source": feed["uk"],
        })
    return {"items": items, "stats": {}}


def collect_kev(since):
    """CISA Known Exploited Vulnerabilities: bugs attackers are using right now."""
    data = fetch_json("kev.json", KEV_URL)
    vulns = data.get("vulnerabilities", [])
    kev_index = {v["cveID"]: v for v in vulns if v.get("cveID")}
    items = []
    for v in vulns:
        added = parse_date(v.get("dateAdded"))
        if not added or added < since:
            continue
        ransomware = (v.get("knownRansomwareCampaignUse") or "").lower() == "known"
        items.append({
            "source": "CISA KEV",
            "source_id": "kev",
            "kind": "vuln",
            "title": f"{v['cveID']}: {v.get('vendorProject', '')} {v.get('product', '')} "
                     f"{v.get('vulnerabilityName', '')}".strip(),
            "url": f"https://nvd.nist.gov/vuln/detail/{v['cveID']}",
            "published": _iso(added),
            "summary": clean_text(v.get("shortDescription")),
            "uk_source": False,
            "cves": [v["cveID"]],
            "extra": {
                "vendor": v.get("vendorProject", ""),
                "product": v.get("product", ""),
                "due_date": v.get("dueDate", ""),
                "ransomware_use": ransomware,
                "required_action": clean_text(v.get("requiredAction"), 300),
            },
        })
    return {"items": items, "stats": {"kev_index": kev_index, "kev_total": len(kev_index)}}


def collect_nvd(since):
    """NVD: newly published CRITICAL CVEs (CVSS 9.0 and above)."""
    now = datetime.now(timezone.utc)
    params = (
        f"?pubStartDate={since.strftime('%Y-%m-%dT%H:%M:%S.000')}"
        f"&pubEndDate={now.strftime('%Y-%m-%dT%H:%M:%S.000')}"
        "&cvssV3Severity=CRITICAL&resultsPerPage=200"
    )
    headers = {}
    if os.environ.get("NVD_API_KEY"):
        headers["apiKey"] = os.environ["NVD_API_KEY"]
    data = fetch_json("nvd.json", NVD_URL + params, headers=headers, timeout=60)
    items = []
    for wrap in data.get("vulnerabilities", []):
        cve = wrap.get("cve", {})
        cve_id = cve.get("id")
        if not cve_id:
            continue
        desc = next((d["value"] for d in cve.get("descriptions", []) if d.get("lang") == "en"), "")
        score = None
        for key in ("cvssMetricV31", "cvssMetricV30"):
            for metric in cve.get("metrics", {}).get(key, []):
                score = metric.get("cvssData", {}).get("baseScore", score)
        items.append({
            "source": "NVD",
            "source_id": "nvd",
            "kind": "vuln",
            "title": f"{cve_id}: {clean_text(desc, 140)}",
            "url": f"https://nvd.nist.gov/vuln/detail/{cve_id}",
            "published": _iso(parse_date(cve.get("published"))),
            "summary": clean_text(desc),
            "uk_source": False,
            "cves": [cve_id],
            "extra": {"cvss": score},
        })
    return {"items": items, "stats": {"critical_cves": len(items)}}


def _first(d, *keys):
    for k in keys:
        if d.get(k):
            return d[k]
    return ""


def collect_ransomware(since):
    """ransomware.live: victims posted on ransomware gang leak sites. We keep UK ones."""
    data = fetch_json("ransomware.json", RANSOMWARE_URL)
    if isinstance(data, dict):
        data = data.get("victims") or data.get("data") or []
    items, groups, total = [], {}, 0
    for v in data:
        found = parse_date(_first(v, "discovered", "attackdate", "published"))
        if found and found < since:
            continue
        total += 1
        group = _first(v, "group", "group_name")
        groups[group] = groups.get(group, 0) + 1
        country = str(_first(v, "country")).upper()
        if country not in UK_COUNTRY_CODES:
            continue
        victim = _first(v, "victim", "post_title")
        sector = _first(v, "activity", "sector") or "Unknown sector"
        items.append({
            "source": "ransomware.live",
            "source_id": "ransomware",
            "kind": "ransomware",
            "title": f"{victim} listed by {group} ransomware",
            "url": _first(v, "url", "post_url") or "https://www.ransomware.live/",
            "published": _iso(found),
            "summary": clean_text(_first(v, "description")) or
                       f"UK organisation ({sector}) named on the {group} leak site.",
            "uk_source": True,
            "extra": {"group": group, "sector": sector, "victim": victim,
                      "website": _first(v, "website", "domain")},
        })
    top = sorted(groups.items(), key=lambda kv: -kv[1])[:8]
    return {"items": items, "stats": {"victims_total": total, "victims_uk": len(items),
                                      "top_groups": top}}


def collect_feodo(since):
    """Feodo Tracker: live botnet command and control (C2) servers."""
    data = fetch_json("feodo.json", FEODO_URL)
    online = [d for d in data if (d.get("status") or "").lower() == "online"]
    uk = [d for d in data if str(d.get("country", "")).upper() in UK_COUNTRY_CODES]
    families = {}
    for d in data:
        fam = d.get("malware") or "unknown"
        families[fam] = families.get(fam, 0) + 1
    uk_c2 = [{"ip": d.get("ip_address"), "port": d.get("port"), "malware": d.get("malware"),
              "as_name": d.get("as_name"), "asn": d.get("as_number"), "status": d.get("status"),
              "last_online": d.get("last_online")} for d in uk][:25]
    return {"items": [], "stats": {"c2_total": len(data), "c2_online": len(online),
                                   "c2_uk": uk_c2, "c2_families": sorted(families.items(),
                                                                         key=lambda kv: -kv[1])[:6]}}


def collect_urlhaus(since):
    """URLhaus: web addresses currently handing out malware."""
    raw = fetch("urlhaus.csv", URLHAUS_URL).decode("utf-8", "replace")
    lines = [l for l in raw.splitlines() if l and not l.startswith("#")]
    reader = csv.reader(io.StringIO("\n".join(lines)))
    total, uk_hosted, tags = 0, [], {}
    for row in reader:
        if len(row) < 7:
            continue
        total += 1
        url = row[2]
        for t in (row[6] or "").split(","):
            t = t.strip()
            if t and t != "None":
                tags[t] = tags.get(t, 0) + 1
        host = re.sub(r"^[a-z]+://", "", url).split("/")[0].split(":")[0].lower()
        if host.endswith(".uk") and len(uk_hosted) < 15:
            uk_hosted.append({"url": url, "threat": row[5], "tags": row[6]})
    return {"items": [], "stats": {"urls_total": total, "urls_uk": uk_hosted,
                                   "url_tags": sorted(tags.items(), key=lambda kv: -kv[1])[:8]}}


def collect_threatfox(since):
    """ThreatFox: fresh indicators of compromise (IOCs) shared by researchers."""
    headers = {}
    if os.environ.get("ABUSECH_AUTH_KEY"):
        headers["Auth-Key"] = os.environ["ABUSECH_AUTH_KEY"]
    data = fetch_json("threatfox.json", THREATFOX_URL, headers=headers)
    rows = []
    if isinstance(data, dict):
        for v in data.values():
            rows.extend(v if isinstance(v, list) else [v])
    families, types = {}, {}
    for r in rows:
        fam = r.get("malware_printable") or r.get("malware") or "unknown"
        families[fam] = families.get(fam, 0) + 1
        t = r.get("ioc_type") or "unknown"
        types[t] = types.get(t, 0) + 1
    return {"items": [], "stats": {"iocs_total": len(rows),
                                   "ioc_families": sorted(families.items(), key=lambda kv: -kv[1])[:8],
                                   "ioc_types": sorted(types.items(), key=lambda kv: -kv[1])}}


def collect_all(lookback_hours=36):
    """Run every collector. Returns (items, stats, health)."""
    since = datetime.now(timezone.utc) - timedelta(hours=lookback_hours)
    kev_since = datetime.now(timezone.utc) - timedelta(days=7)  # KEV is weekly-ish, look further back
    jobs = [(f["name"], f["id"], (lambda f=f: collect_rss(f, since))) for f in RSS_FEEDS]
    jobs += [
        ("CISA KEV", "kev", lambda: collect_kev(kev_since)),
        ("NVD critical CVEs", "nvd", lambda: collect_nvd(since)),
        ("ransomware.live", "ransomware", lambda: collect_ransomware(since)),
        ("Feodo Tracker (C2)", "feodo", lambda: collect_feodo(since)),
        ("URLhaus", "urlhaus", lambda: collect_urlhaus(since)),
        ("ThreatFox", "threatfox", lambda: collect_threatfox(since)),
    ]
    items, stats, health = [], {}, []
    for name, sid, job in jobs:
        try:
            result = job()
            items.extend(result["items"])
            stats.update(result["stats"])
            health.append({"name": name, "id": sid, "ok": True, "count": len(result["items"]),
                           "error": ""})
        except Exception as err:  # noqa: BLE001 - one bad feed must never stop the brief
            health.append({"name": name, "id": sid, "ok": False, "count": 0,
                           "error": str(err)[:200]})
    return items, stats, health


def dump_json(obj):
    return json.dumps(obj, indent=2, default=str)
