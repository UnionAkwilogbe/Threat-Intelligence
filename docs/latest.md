# Threat Intel Field Brief: Thursday 12 November 2026

_TLP:CLEAR · generated 14:57 UK time · last 36 hours_

## Your morning in 30 seconds

- Read first: baronandbudd.com listed by Curious Worm ransomware (priority 66).
- 11 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 1 UK organisations named on ransomware leak sites (sectors: Professional Services).
- 3 stories with strong UK relevance.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [baronandbudd.com listed by Curious Worm ransomware](https://www.ransomware.live/id/YmFyb25hbmRidWRkLmNvbUBDdXJpb3VzIFdvcm0=)
**Priority 66** · ransomware.live · UK relevant · _Ransomware, Data breach, Legal, Professional Services_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Domain → WHOIS / Nominet for .uk, passive DNS, certificate transparency (crt.sh)

### 2. [Exploit Attempts for GPUStack Authentication Bypass (CVE-2026-102895), (Thu, Nov 12th)](https://isc.sans.edu/diary/rss/33514)
**Priority 53** · SANS Internet Storm Center · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 3. [NCSC Launches Cyber Adversary Testing to Boost Resilience](https://www.infosecurity-magazine.com/news/ncsc-cyber-adversary-testing-boost/)
**Priority 48** · Infosecurity Magazine · UK relevant

**In plain English:** General security news worth knowing.

**Do this:** Skim it and note whether any client uses the vendor or product mentioned.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

### 4. [Cisco BroadWorks and Openwave Flaws Actively Exploited Despite Available Patches](https://thehackernews.com/2026/11/cisco-broadworks-and-openwave-flaws.html)
**Priority 43** · The Hacker News · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 5. [CVE-2026-123158: OpenBSD OpenSSH Unexpected Status Code or Return Value Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-123158)
**Priority 39** · CISA KEV · KEV · EPSS 19% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-12): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 6. [Hackers exploiting ScreenConnect plugin flaw to spread malware across hundreds of PCs](https://www.theregister.com/security/2026/11/12/hackers-exploiting-screenconnect-plugin-flaw-to-spread-malware-across-hundreds-of-pcs/5309361)
**Priority 37** · The Register Security · _Supply chain, Malware, Identity / MFA_

**In plain English:** Attackers break into a supplier or software package to reach that supplier's customers.

**Do this:** List which clients use the affected supplier or package. Ask the supplier for their incident statement and indicators.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

### 7. [Maersk Reveals Data Breach as Extortion Group Demands $5m](https://www.infosecurity-magazine.com/news/maersk-data-breach-extortion-group/)
**Priority 37** · Infosecurity Magazine · _Ransomware, Data breach_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

### 8. [CVE-2026-111560: Barracuda Networks Multiple Products OS Command Injection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-111560)
**Priority 37** · CISA KEV · KEV · EPSS 9% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-13): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

## Client request RFI-002: PHP2Shell: critical PHP flaws (CVE-2026-109618, CVE-2026-109619) (Client B)

**Status:** In progress, re-checked today.

**Bottom line:** Two critical PHP bugs let an unauthenticated attacker run code on a web server. They are now confirmed exploited and on CISA's Known Exploited Vulnerabilities list (added 26 October). Patch every internet-facing PHP system now, then check it was not compromised from 17 October onwards.

- On CISA KEV today: CVE-2026-109618, CVE-2026-109619
- Matching stories today: 0
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

### Lesson 316: STIX, TAXII and MISP

STIX is a standard format (JSON) for describing threat intel: indicators, malware, threat actors and the links between them. TAXII is a standard way to send STIX over the internet. MISP is popular free software for storing, enriching and sharing intel, and it speaks both.

> **Think of it like this:** STIX is the language, TAXII is the postal service, MISP is the filing cabinet and post room together.

**UK angle:** Many UK sector sharing groups and MSSPs use MISP. Being able to export your enriched data as STIX makes it easy for clients' tools to consume.

**Enrichment tip:** Store enrichment as MISP attributes or tags (for example tlp:amber, admiralty-scale, sector) rather than free text, so machines can filter on them.

**Try it today:** Open this dashboard's docs/data JSON file and spot which fields would become STIX indicators.

**Quiz:** Which one is the format and which is the transport: STIX or TAXII?  
_Answer:_ STIX is the format. TAXII is the transport.

**Word of the day: TLP** · Traffic Light Protocol. Labels (CLEAR, GREEN, AMBER, AMBER+STRICT, RED) that set who may see shared info.

### Review (spaced repetition)

- **The Cyber Kill Chain** (1d ago): Which stage is a C2 (command and control) server? _Answer: Stage 6, Command and Control._
- **MITRE ATT&CK in five minutes** (3d ago): What is the difference between a tactic and a technique? _Answer: A tactic is the goal (why). A technique is the method used to reach it (how)._
- **IPs, ASNs and RIPE** (7d ago): Which regional registry covers UK IP addresses? _Answer: RIPE NCC._

### Enrichment drill: baronandbudd.com listed by Curious Worm ransomware

1. Search Companies House for 'baronandbudd.com'. Note its SIC code, size and registered region.
2. Look up Curious Worm on ransomware.live. How many UK victims has it listed this year?
3. Search 'Curious Worm initial access' to find how they usually break in (ATT&CK tactic TA0001).
4. Which of your clients share this sector or region? Write a two-line BLUF heads-up for them.
5. Grade your sources with the Admiralty Code, for example C3 for a leak-site claim.

---
Sources healthy: 14/17 (failed: ICO enforcement (UK regulator), URLhaus, ThreatFox)
