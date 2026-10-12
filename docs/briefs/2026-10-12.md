# Threat Intel Field Brief: Monday 12 October 2026

_TLP:CLEAR · generated 14:16 UK time · last 72 hours_

## Your morning in 30 seconds

- Read first: lopay listed by Black X ransomware (priority 60).
- 5 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 1 UK organisations named on ransomware leak sites (sectors: Financial Services).
- 3 stories with strong UK relevance.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [lopay listed by Black X ransomware](https://www.ransomware.live/id/bG9wYXlAQmxhY2sgWA==)
**Priority 60** · ransomware.live · UK relevant · _Ransomware, Finance, Financial Services_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 2. [CVE-2015-5477: ISC BIND Data Processing Errors Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2015-5477)
**Priority 55** · CISA KEV · KEV · EPSS 99% · _Exploited vuln, DDoS_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-11): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 3. [CVE-2015-3306: ProFTPD Improper Access Control Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2015-3306)
**Priority 55** · CISA KEV · KEV · EPSS 99% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-11): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 4. [CVE-2016-3081: Apache Struts Command Injection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2016-3081)
**Priority 54** · CISA KEV · KEV · EPSS 96% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-11): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 5. [CVE-2023-22894: Strapi Cleartext Storage of Sensitive Information Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2023-22894)
**Priority 49** · CISA KEV · KEV · EPSS 71% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-11): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 6. [Help the NCSC understand how organisations approach external attack surface risk](https://www.ncsc.gov.uk/blogs/help-ncsc-understand-how-organisations-approach-external-attack-surface-risk)
**Priority 46** · NCSC UK · UK relevant

**In plain English:** General security news worth knowing.

**Do this:** Skim it and note whether any client uses the vendor or product mentioned.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

### 7. [CVE-2021-3199: ONLYOFFICE Docs Server Path Traversal Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2021-3199)
**Priority 39** · CISA KEV · KEV · EPSS 19% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-11): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 8. [AI: Faster than the speed of safety](https://www.computerweekly.com/news/366651940/AI-Faster-than-the-speed-of-safety)
**Priority 38** · Computer Weekly Security · UK relevant · _Public sector_

**In plain English:** General security news worth knowing.

**Do this:** Skim it and note whether any client uses the vendor or product mentioned.

**Enrich next:** Sector (Public sector) → tag every client in that sector and send them a short heads-up

## Client request RFI-001: Okta vulnerabilities (Client A)

**Status:** In progress, re-checked today.

**Bottom line:** No Okta or Auth0 vulnerability is known to be exploited. The real risk to Okta customers is social engineering: phone-call phishing (vishing) that tricks staff or the help desk into handing over sign-ins and MFA.

- On CISA KEV today: none
- Matching stories today: 0
- New CVEs not yet covered: none
- Themed indicators in today's malware feeds: 1 (e.g. hxxps://raw[.]githubusercontent[.]com/fdaloiapp/okta-terraform-demo-template/HEAD/scripts/archive/okta-terraform-demo-template-grossularia[.]zip)

## Daily knowledge pack

### Lesson 285: False positives and allowlists

A false positive is a harmless thing flagged as malicious. Feeds sometimes include shared infrastructure like Google DNS (8.8.8.8), Microsoft or Cloudflare IPs. Blocking these can take a client offline. Allowlists (MISP calls them warninglists) catch them before sharing.

> **Think of it like this:** A smoke alarm that goes off every time you make toast. People soon take the battery out.

**UK angle:** Add UK-specific allowlists: gov.uk, nhs.uk, major UK banks, and the client's own IP ranges and suppliers.

**Enrichment tip:** Before sharing any IOC, check it against an allowlist of popular domains (for example the Tranco top list) and cloud provider ranges.

**Try it today:** List five domains that should never be blocked for a UK client.

**Quiz:** What is a MISP warninglist for?  
_Answer:_ Flagging indicators that are probably false positives, such as well-known legitimate services.

**Word of the day: C2** · Command and Control. The server an attacker uses to send orders to infected machines.

### Review (spaced repetition)

- **Indicators go stale: ageing and decay** (1d ago): Why should IP indicators expire faster than hashes? _Answer: IPs get reassigned to new, often innocent, owners, while a hash always identifies the same file._
- **The Cyber Kill Chain** (3d ago): Which stage is a C2 (command and control) server? _Answer: Stage 6, Command and Control._
- **Passive DNS and certificate transparency** (7d ago): What is 'pivoting' in threat intel? _Answer: Using one known indicator to discover related indicators, for example from a domain to its IP to other domains on that IP._

### Enrichment drill: lopay listed by Black X ransomware

1. Search Companies House for 'lopay'. Note its SIC code, size and registered region.
2. Look up Black X on ransomware.live. How many UK victims has it listed this year?
3. Search 'Black X initial access' to find how they usually break in (ATT&CK tactic TA0001).
4. Which of your clients share this sector or region? Write a two-line BLUF heads-up for them.
5. Grade your sources with the Admiralty Code, for example C3 for a leak-site claim.

---
Sources healthy: 15/17 (failed: ICO enforcement (UK regulator), SecurityWeek)
