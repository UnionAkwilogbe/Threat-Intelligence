"""Enrichment: turning raw headlines into something a UK client can act on.

For every story we add:
  * cves           CVE IDs mentioned anywhere in the text
  * kev            is any of those CVEs on the CISA "actively exploited" list?
  * epss           highest EPSS score (chance of exploitation in the next 30 days)
  * attack         MITRE ATT&CK technique IDs mentioned (T1566 etc.)
  * iocs           IPs, domains, hashes pulled out of the text (defanged)
  * threat_types   ransomware, phishing, data breach, zero-day ...
  * sectors        which UK sectors it touches (NHS, finance, councils ...)
  * uk_score       0-100, how relevant this is to UK organisations
  * priority       0-100, the overall "read this first" score
  * rookie         a plain English "what this means" line
  * actions        what to do or check for your clients
  * enrich_steps   which extra lookups would make this story more useful
"""

import re
from datetime import datetime, timezone

from .http import fetch_json

CVE_RE = re.compile(r"\bCVE-\d{4}-\d{4,7}\b", re.I)
ATTACK_RE = re.compile(r"\bT1\d{3}(?:\.\d{3})?\b")
IPV4_RE = re.compile(r"\b(?:(?:25[0-5]|2[0-4]\d|1?\d?\d)(?:\[\.\]|\.)){3}(?:25[0-5]|2[0-4]\d|1?\d?\d)\b")
SHA256_RE = re.compile(r"\b[a-fA-F0-9]{64}\b")
MD5_RE = re.compile(r"\b[a-fA-F0-9]{32}\b")
DOMAIN_RE = re.compile(r"\b(?:[a-z0-9-]+(?:\[\.\]|\.))+(?:com|net|org|io|ru|cn|top|xyz|info|biz|co\.uk|uk|online|site)\b", re.I)

# Words that suggest a story is about the UK. Weights are rough on purpose.
UK_TERMS = {
    r"\bUK\b": 30, r"\bUnited Kingdom\b": 30, r"\bBritain\b": 30, r"\bBritish\b": 25,
    r"\bEngland\b": 20, r"\bScotland\b": 20, r"\bScottish\b": 20, r"\bWales\b": 20,
    r"\bWelsh\b": 15, r"\bNorthern Ireland\b": 20, r"\bLondon\b": 20, r"\bManchester\b": 15,
    r"\bBirmingham\b": 15, r"\bNCSC\b": 30, r"\bICO\b": 25, r"\bNHS\b": 35, r"\bGCHQ\b": 30,
    r"\bFCA\b": 20, r"\bOfcom\b": 20, r"\bAction Fraud\b": 25, r"\bNational Crime Agency\b": 30,
    r"\bNCA\b": 20, r"\bHMRC\b": 25, r"\bDWP\b": 20, r"\bMoD\b": 20, r"\bMinistry of Defence\b": 25,
    r"\bcouncil\b": 10, r"\bGOV\.UK\b": 25, r"\.co\.uk\b": 20, r"\.gov\.uk\b": 25,
    r"\bpounds?\b|£": 15, r"\bFTSE\b": 20, r"\bCyber Essentials\b": 30, r"\bUK GDPR\b": 30,
    r"\bFive Eyes\b": 10, r"\bM&S\b|\bMarks & Spencer\b": 30, r"\bCo-op\b": 25,
    r"\bHarrods\b": 30, r"\bJaguar Land Rover\b|\bJLR\b": 30, r"\bBT\b": 15,
    r"\bScattered Spider\b": 15,
}
UK_TERMS = [(re.compile(p, re.I if p.islower() else 0), w) for p, w in UK_TERMS.items()]

SECTORS = {
    "Health / NHS": r"\bNHS\b|hospital|health ?care|patient|pharma|GP surger|clinic",
    "Finance": r"\bbank|financ|insur|payment|fintech|crypto|building societ|\bFCA\b",
    "Retail": r"retail|e-?commerce|supermarket|high street|online shop|M&S|Co-op|Harrods",
    "Public sector": r"council|government|\bgov\b|ministry|\bHMRC\b|\bDWP\b|public sector|police",
    "Education": r"universit|school|college|academ|education|student",
    "Legal": r"law firm|solicitor|legal|barrister",
    "Manufacturing": r"manufactur|factory|automotive|industrial|\bOT\b|\bICS\b|SCADA|JLR|Jaguar",
    "Energy / Utilities": r"\benergy|\butilit(y|ies)|water (company|supplier|utility)|electricity|\bgas\b|power grid|nuclear",
    "Telecoms": r"telecom|mobile operator|\bISP\b|broadband|\bBT\b|Vodafone|carrier",
    "Tech / MSP": r"\bMSP\b|managed service|SaaS|cloud provider|software supplier|IT provider",
    "Charity": r"charit|non-?profit|NGO",
    "Transport / Logistics": r"airport|airline|\brail(way)?\b|logistic|shipping|transport",
}
SECTORS = {k: re.compile(v, re.I) for k, v in SECTORS.items()}

THREAT_TYPES = {
    "Ransomware": r"ransomware|extortion|leak site|encrypt(ed|ion) files|lockbit|akira|qilin|play ransomware",
    "Phishing": r"phish|smish|vish|credential harvest|fake login|business email compromise|\bBEC\b",
    "Data breach": r"breach|leak(ed)?\b|exposed data|stolen data|data theft|exfiltrat",
    "Zero-day": r"zero-?day|0-?day|unpatched",
    "Exploited vuln": r"actively exploited|in the wild|exploit(ed|ation)",
    "Supply chain": r"supply.chain|third.party|vendor compromise|dependency|npm|pypi",
    "Nation-state / APT": r"\bAPT\d*|nation.state|state.sponsored|espionage|china|russia|iran|north korea|lazarus|volt typhoon|salt typhoon",
    "Malware": r"malware|trojan|infostealer|stealer|botnet|loader|backdoor|\bRAT\b",
    "DDoS": r"\bDDoS\b|denial.of.service",
    "Fraud / Scam": r"fraud|scam|impersonat",
    "Identity / MFA": r"\bMFA\b|multi-factor|help ?desk|social engineering|SIM swap|session token|OAuth",
}
THREAT_TYPES = {k: re.compile(v, re.I) for k, v in THREAT_TYPES.items()}

# Plain English explainers and next steps per threat type. These are what make
# the brief rookie friendly and client ready.
PLAYBOOK = {
    "Ransomware": (
        "Criminals lock (encrypt) or steal a company's files, then demand money.",
        ["Check whether any client shares the victim's sector, suppliers or software.",
         "Confirm clients have offline or immutable backups and have tested a restore.",
         "Look up the gang on ransomware.live to see its usual way in (initial access)."]),
    "Phishing": (
        "Fake emails, texts or calls that trick people into handing over passwords or money.",
        ["Pull any sender domains or URLs and check them against client mail logs.",
         "Remind clients they can forward suspicious email to report@phishing.gov.uk (SERS)."]),
    "Data breach": (
        "Private data got out. Stolen data is later reused for scams and account takeover.",
        ["Check if client staff email domains appear in the leak (Have I Been Pwned domain search).",
         "Note the UK GDPR angle: serious breaches must be reported to the ICO within 72 hours."]),
    "Zero-day": (
        "A bug attackers found before the vendor could fix it, so there may be no patch yet.",
        ["Find out which clients run the product (asset inventory or Shodan/Censys search).",
         "Apply the vendor's workaround or mitigation until a patch ships."]),
    "Exploited vuln": (
        "Attackers are already using this weakness in real attacks, not just in theory.",
        ["Treat as patch-now: check the CISA KEV due date and the EPSS score.",
         "Search client external attack surface for the affected product and version."]),
    "Supply chain": (
        "Attackers break into a supplier or software package to reach that supplier's customers.",
        ["List which clients use the affected supplier or package.",
         "Ask the supplier for their incident statement and indicators."]),
    "Nation-state / APT": (
        "Government-backed hackers, usually after secrets, access, or disruption rather than quick cash.",
        ["Map the reported techniques to MITRE ATT&CK and check client detections cover them.",
         "Check if the NCSC has issued a joint advisory with indicators to hunt for."]),
    "Malware": (
        "Malicious software, for example info-stealers that grab saved passwords and cookies.",
        ["Extract hashes, domains and IPs and push them to client blocklists or the SIEM.",
         "Check the malware family on MalwareBazaar or ThreatFox for more indicators."]),
    "DDoS": (
        "Flooding a website or service with junk traffic until it falls over.",
        ["Check which clients have public services in the targeted sector.",
         "Confirm clients know how to reach their ISP or CDN DDoS support fast."]),
    "Fraud / Scam": (
        "Tricks aimed at stealing money, often by pretending to be a trusted brand or person.",
        ["Watch for lookalike domains of client brands (typosquats).",
         "UK victims report to Action Fraud (England, Wales, NI) or Police Scotland."]),
    "Identity / MFA": (
        "Attacks on logins: fooling the help desk, stealing session cookies, or MFA fatigue.",
        ["Check clients' help desk identity checks for password and MFA resets.",
         "Look for sign-ins from new devices or countries in identity logs."]),
}

GENERIC_ACTION = (
    "General security news worth knowing.",
    ["Skim it and note whether any client uses the vendor or product mentioned."],
)


def extract_iocs(text):
    """Pull indicators out of free text. Results are defanged so they are safe to share."""
    def defang(s):
        return s.replace("[.]", ".").replace(".", "[.]")
    iocs = {
        "ips": sorted({defang(m) for m in IPV4_RE.findall(text)
                       if not m.replace("[.]", ".").startswith(("10.", "192.168.", "127."))}),
        "sha256": sorted(set(SHA256_RE.findall(text))),
        "md5": sorted(set(MD5_RE.findall(text)) - {h[:32] for h in SHA256_RE.findall(text)}),
    }
    domains = {defang(m.lower()) for m in DOMAIN_RE.findall(text)}
    # drop the obvious news-site noise
    noise = ("bleepingcomputer", "therecord", "thehackernews", "securityweek", "krebsonsecurity",
             "ncsc[.]gov[.]uk", "cisa[.]gov", "github[.]com", "microsoft[.]com", "google[.]com")
    iocs["domains"] = sorted(d for d in domains if not any(n in d for n in noise))[:10]
    return {k: v for k, v in iocs.items() if v}


def uk_relevance(story):
    text = f"{story.get('title', '')} {story.get('summary', '')}"
    score = 35 if story.get("uk_source") else 0
    if story.get("kind") == "ransomware":
        score = 90  # UK victim on a leak site
    for pattern, weight in UK_TERMS:
        if pattern.search(text):
            score += weight
    return min(score, 100)


def fetch_epss(cves):
    """EPSS from FIRST.org: probability (0-1) a CVE is exploited in the next 30 days."""
    scores = {}
    cves = sorted(set(cves))
    for i in range(0, len(cves), 80):
        chunk = cves[i:i + 80]
        try:
            data = fetch_json("epss.json", "https://api.first.org/data/v1/epss?cve=" + ",".join(chunk))
        except Exception:  # noqa: BLE001 - EPSS is a bonus, never fatal
            continue
        for row in data.get("data", []):
            try:
                scores[row["cve"].upper()] = {"epss": float(row["epss"]),
                                              "percentile": float(row["percentile"])}
            except (KeyError, ValueError):
                continue
    return scores


def _recency_points(published, now):
    if not published:
        return 5
    try:
        age_h = (now - datetime.fromisoformat(published)).total_seconds() / 3600
    except ValueError:
        return 5
    if age_h <= 12:
        return 15
    if age_h <= 24:
        return 10
    if age_h <= 48:
        return 5
    return 0


def enrich_story(story, kev_index, epss, now):
    text = f"{story.get('title', '')} {story.get('summary', '')}"
    cves = sorted({c.upper() for c in CVE_RE.findall(text)} | set(story.get("cves", [])))
    story["cves"] = cves
    story["kev"] = [c for c in cves if c in kev_index]
    story["epss"] = max((epss[c]["epss"] for c in cves if c in epss), default=None)
    story["attack"] = sorted(set(ATTACK_RE.findall(text)))
    story["iocs"] = extract_iocs(text)
    story["threat_types"] = [k for k, rx in THREAT_TYPES.items() if rx.search(text)]
    if story.get("kind") == "ransomware" and "Ransomware" not in story["threat_types"]:
        story["threat_types"].insert(0, "Ransomware")
    if story["kev"] and "Exploited vuln" not in story["threat_types"]:
        story["threat_types"].insert(0, "Exploited vuln")
    story["sectors"] = [k for k, rx in SECTORS.items() if rx.search(text)]
    if story.get("kind") == "ransomware":
        sector = story.get("extra", {}).get("sector")
        if sector and sector not in story["sectors"]:
            story["sectors"].append(sector)
    story["uk_score"] = uk_relevance(story)

    # ---- priority: a simple, explainable points system -------------------
    points = {"UK relevance": round(story["uk_score"] * 0.35)}
    if story["kev"]:
        points["Actively exploited (KEV)"] = 25
    if story["epss"] is not None:
        points["EPSS"] = round(story["epss"] * 20)
    cvss = story.get("extra", {}).get("cvss")
    if cvss:
        points["CVSS"] = round((cvss - 7) * 3) if cvss >= 7 else 0
    if story.get("extra", {}).get("ransomware_use"):
        points["Used by ransomware"] = 10
    heavy = {"Ransomware", "Zero-day", "Exploited vuln", "Supply chain", "Nation-state / APT"}
    if heavy & set(story["threat_types"]):
        points["Serious threat type"] = 10
    if story.get("kind") == "advisory":
        points["Official advisory"] = 8
    if story.get("kind") == "ransomware":
        points["UK victim named"] = 15
    points["Fresh"] = _recency_points(story.get("published"), now)
    story["priority"] = min(sum(points.values()), 100)
    story["priority_why"] = points

    # ---- rookie explainer and actions -----------------------------------
    types = [t for t in story["threat_types"] if t in PLAYBOOK][:2]
    explain, actions = PLAYBOOK.get(types[0], GENERIC_ACTION) if types else GENERIC_ACTION
    story["rookie"] = explain
    story["actions"] = list(actions)
    if len(types) > 1:  # add the second threat type's first action too
        story["actions"].append(PLAYBOOK[types[1]][1][0])
    if story["kev"]:
        due = story.get("extra", {}).get("due_date")
        story["actions"].insert(0, f"On CISA KEV{f' (US federal patch deadline {due})' if due else ''}: "
                                   "patch or mitigate for UK clients now, do not wait.")
    story["enrich_steps"] = enrichment_steps(story)
    return story


def enrichment_steps(story):
    """Suggest the next lookups that would turn this story into client-specific intel."""
    steps = []
    if story["cves"]:
        steps.append("CVE → EPSS + KEV + vendor advisory → which client assets run it "
                     "(Shodan/Censys query filtered to country:GB)")
    if story["iocs"].get("ips"):
        steps.append("IP → ASN and hosting provider (RIPE Stat), UK geolocation, AbuseIPDB reputation")
    if story["iocs"].get("domains"):
        steps.append("Domain → WHOIS / Nominet for .uk, passive DNS, certificate transparency (crt.sh)")
    if story["iocs"].get("sha256") or story["iocs"].get("md5"):
        steps.append("Hash → MalwareBazaar / VirusTotal family, first seen date, related samples")
    if story.get("kind") == "ransomware":
        steps.append("Victim → Companies House (sector SIC code, size, directors) → "
                     "which clients share suppliers or sector")
    if story["attack"]:
        steps.append("ATT&CK IDs → check client detection coverage for each technique")
    if story["sectors"] and not steps:
        steps.append(f"Sector ({', '.join(story['sectors'][:2])}) → tag every client in that "
                     "sector and send them a short heads-up")
    if not steps:
        steps.append("Add a TLP label and an Admiralty rating (source reliability + credibility) "
                     "before sharing")
    return steps


def dedupe(stories):
    """Merge duplicate stories. Many sources reporting the same thing = more confidence."""
    seen_urls, by_key, out = set(), {}, []
    for s in stories:
        url = (s.get("url") or "").split("?")[0].rstrip("/")
        if url and url in seen_urls:
            continue
        seen_urls.add(url)
        key = re.sub(r"[^a-z0-9]", "", s["title"].lower())[:60]
        if key in by_key:
            by_key[key].setdefault("also_reported_by", []).append(s["source"])
            continue
        by_key[key] = s
        out.append(s)
    # stories about the same CVE are corroboration too
    cve_owner = {}
    for s in out:
        for c in s.get("cves", []):
            if c in cve_owner and cve_owner[c] is not s:
                cve_owner[c].setdefault("also_reported_by", []).append(s["source"])
            else:
                cve_owner.setdefault(c, s)
    for s in out:
        s["also_reported_by"] = sorted(set(s.get("also_reported_by", [])) - {s["source"]})
        if s["also_reported_by"]:
            s["priority_why"]["Corroborated"] = min(3 * len(s["also_reported_by"]), 9)
            s["priority"] = min(sum(s["priority_why"].values()), 100)
    return out


def load_clients(path=None):
    """Read clients.json (your watchlist). Returns [] if it does not exist."""
    import json
    import os
    if os.environ.get("CLIENTS_JSON") and not path:  # GitHub secret: keeps names out of the repo
        return json.loads(os.environ["CLIENTS_JSON"]).get("clients", [])
    path = path or os.environ.get("TI_CLIENTS") or os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "clients.json")
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as fh:
        return json.load(fh).get("clients", [])


def match_clients(story, clients):
    """Tag a story with every client whose sector, vendors or keywords it mentions."""
    text = f"{story.get('title', '')} {story.get('summary', '')} " \
           f"{story.get('extra', {}).get('vendor', '')} {story.get('extra', {}).get('product', '')}".lower()
    hits = []
    for c in clients:
        reasons = [v for v in c.get("vendors", []) + c.get("keywords", []) if v.lower() in text]
        reasons += [sec for sec in c.get("sectors", []) if sec in story.get("sectors", [])]
        if reasons:
            hits.append({"client": c["name"], "why": sorted(set(reasons))})
    story["clients"] = hits
    if hits:
        # a vendor match is worth more than a sector match
        vendor_hit = any(set(h["why"]) - set(story.get("sectors", [])) for h in hits)
        story["priority_why"]["Matches your clients"] = 20 if vendor_hit else 10
        story["priority"] = min(sum(story["priority_why"].values()), 100)
        names = ", ".join(h["client"] for h in hits)
        story["actions"].insert(0, f"Matches your watchlist ({names}): send them a heads-up.")
    return story


def enrich_all(items, stats, clients=None):
    now = datetime.now(timezone.utc)
    kev_index = stats.get("kev_index", {})
    all_cves = set()
    for s in items:
        text = f"{s.get('title', '')} {s.get('summary', '')}"
        all_cves |= {c.upper() for c in CVE_RE.findall(text)} | set(s.get("cves", []))
    epss = fetch_epss(all_cves) if all_cves else {}
    enriched = [enrich_story(s, kev_index, epss, now) for s in items]
    enriched = dedupe(enriched)
    clients = load_clients() if clients is None else clients
    enriched = [match_clients(s, clients) for s in enriched]
    enriched.sort(key=lambda s: (s["priority"], s.get("published") or ""), reverse=True)
    return enriched, epss
