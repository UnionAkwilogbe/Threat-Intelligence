# Threat Intel Field Brief: Saturday 14 November 2026

_TLP:CLEAR · generated 12:17 UK time · last 36 hours_

## Your morning in 30 seconds

- Read first: CVE-2026-114713: UnrealIRCd Improper Neutralization of Delimiters Vulnerability (priority 40).
- 12 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 1 stories with strong UK relevance.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [CVE-2026-114713: UnrealIRCd Improper Neutralization of Delimiters Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-114713)
**Priority 40** · CISA KEV · KEV · EPSS 0% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-16): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 2. [CVE-2026-123039: Check Point Multiple Products Incorrect Permission Assignment for Critical Resource Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-123039)
**Priority 40** · CISA KEV · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-16): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 3. [CVE-2026-123158: OpenBSD OpenSSH Unexpected Status Code or Return Value Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-123158)
**Priority 39** · CISA KEV · KEV · EPSS 19% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-12): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 4. [CVE-2026-111560: Barracuda Networks Multiple Products OS Command Injection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-111560)
**Priority 37** · CISA KEV · KEV · EPSS 11% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-13): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 5. [CVE-2026-124194: Microsoft Office Outlook Missing User Interaction for Potentially Unsafe Action Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-124194)
**Priority 35** · CISA KEV · KEV · EPSS 2% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-24): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 6. [CVE-2026-111793: Openwave Messaging Limited Webtop Media Transcoder Incorrect Resource Transfer Between Spheres Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-111793)
**Priority 35** · CISA KEV · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-24): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 7. [CVE-2026-20320: Cisco BroadWorks Improper Restriction of XML External Entity Reference Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-20320)
**Priority 35** · CISA KEV · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-24): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 8. [CVE-2026-125350: Google Chromium Use-After-Free Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-125350)
**Priority 35** · CISA KEV · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-24): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

## Client request RFI-002: PHP2Shell: critical PHP flaws (CVE-2026-109618, CVE-2026-109619) (Client B)

**Status: needs update, new evidence today.**

**Bottom line:** Two critical PHP bugs let an unauthenticated attacker run code on a web server. They are now confirmed exploited and on CISA's Known Exploited Vulnerabilities list (added 26 October). Patch every internet-facing PHP system now, then check it was not compromised from 17 October onwards.

- On CISA KEV today: CVE-2026-109618, CVE-2026-109619, CVE-2026-123039
- Matching stories today: 2
- New CVEs not yet covered: none
- Indicator feeds unavailable today

## Client request RFI-001: Okta vulnerabilities (Client A)

**Status:** In progress, re-checked today.

**Bottom line:** No Okta or Auth0 vulnerability is known to be exploited. The real risk to Okta customers is social engineering: phone-call phishing (vishing) that tricks staff or the help desk into handing over sign-ins and MFA.

- On CISA KEV today: none
- Matching stories today: 0
- New CVEs not yet covered: none
- Indicator feeds unavailable today

## Daily knowledge pack

### Lesson 318: False positives and allowlists

A false positive is a harmless thing flagged as malicious. Feeds sometimes include shared infrastructure like Google DNS (8.8.8.8), Microsoft or Cloudflare IPs. Blocking these can take a client offline. Allowlists (MISP calls them warninglists) catch them before sharing.

> **Think of it like this:** A smoke alarm that goes off every time you make toast. People soon take the battery out.

**UK angle:** Add UK-specific allowlists: gov.uk, nhs.uk, major UK banks, and the client's own IP ranges and suppliers.

**Enrichment tip:** Before sharing any IOC, check it against an allowlist of popular domains (for example the Tranco top list) and cloud provider ranges.

**Try it today:** List five domains that should never be blocked for a UK client.

**Quiz:** What is a MISP warninglist for?  
_Answer:_ Flagging indicators that are probably false positives, such as well-known legitimate services.

**Word of the day: Typosquatting** · Registering lookalike domains to trick people, for example paypa1.com.

### Review (spaced repetition)

- **Indicators go stale: ageing and decay** (1d ago): Why should IP indicators expire faster than hashes? _Answer: IPs get reassigned to new, often innocent, owners, while a hash always identifies the same file._
- **The Cyber Kill Chain** (3d ago): Which stage is a C2 (command and control) server? _Answer: Stage 6, Command and Control._
- **Passive DNS and certificate transparency** (7d ago): What is 'pivoting' in threat intel? _Answer: Using one known indicator to discover related indicators, for example from a domain to its IP to other domains on that IP._

### Enrichment drill: CVE-2026-114713: UnrealIRCd Improper Neutralization of Delimiters Vulnerability

1. Open nvd.nist.gov/vuln/detail/CVE-2026-114713. Note the CVSS score and affected product.
2. Check CVE-2026-114713 on the CISA KEV list and its EPSS score at first.org/epss. Severity vs likelihood vs reality?
3. Find the vendor's own advisory. Is there a patch or only a workaround?
4. Search Shodan or Censys for the product with country:GB. How exposed is the UK?
5. Write a BLUF: which clients, what action, by when (Cyber Essentials allows 14 days, KEV says sooner).

---
Sources healthy: 14/17 (failed: ICO enforcement (UK regulator), URLhaus, ThreatFox)
