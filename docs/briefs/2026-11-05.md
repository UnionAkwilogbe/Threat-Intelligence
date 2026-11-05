# Threat Intel Field Brief: Thursday 05 November 2026

_TLP:CLEAR · generated 13:17 UK time · last 36 hours_

## Your morning in 30 seconds

- Read first: Unilever listed by Whitearmor ransomware (priority 70).
- 4 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 2 UK organisations named on ransomware leak sites (sectors: Manufacturing, Professional Services).
- 3 stories with strong UK relevance.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [Unilever listed by Whitearmor ransomware](https://www.ransomware.live/id/VW5pbGV2ZXJAV2hpdGVhcm1vcg==)
**Priority 70** · ransomware.live · UK relevant · _Ransomware, Manufacturing_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 2. [Jobmongers listed by medusalocker ransomware](https://www.ransomware.live/id/Sm9ibW9uZ2Vyc0BtZWR1c2Fsb2NrZXI=)
**Priority 66** · ransomware.live · UK relevant · _Ransomware, Professional Services_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Domain → WHOIS / Nominet for .uk, passive DNS, certificate transparency (crt.sh)

### 3. [Hackers Exploit Patched Apple Flaw to Deliver Info-Stealing Malware, CISA Says](https://thehackernews.com/2026/11/hackers-exploit-patched-apple-flaw-to.html)
**Priority 53** · The Hacker News · KEV · EPSS 1% · _Exploited vuln, Malware_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 4. [CVE-2026-118527: Ivanti Connect Secure Generation of Predictable Numbers or Identifiers Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-118527)
**Priority 53** · CISA KEV · KEV · EPSS 89% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-13): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 5. [NATS Air Traffic Control Failure Cost UK Economy £33m](https://www.infosecurity-magazine.com/news/nats-air-traffic-control-fail-cost/)
**Priority 43** · Infosecurity Magazine · UK relevant

**In plain English:** General security news worth knowing.

**Do this:** Skim it and note whether any client uses the vendor or product mentioned.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

### 6. [CISA Confirms Hackers Exploiting WordPress Core Flaw During Software Upgrades](https://thehackernews.com/2026/11/cisa-confirms-hackers-exploiting.html)
**Priority 43** · The Hacker News · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 7. [3AM Ransomware Used Human-AI Hybrid Tactics in UK School Estate Compromise](https://www.infosecurity-magazine.com/news/3am-ransomware-hybrid-ai-uk-school/)
**Priority 38** · Infosecurity Magazine · UK relevant · _Ransomware, Data breach, Finance, Education_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Sector (Finance, Education) → tag every client in that sector and send them a short heads-up

### 8. [New York's Queens Public Library battles ransomware crims: Wi-Fi, checkouts, and website go dark](https://www.theregister.com/cyber-crime/2026/11/05/new-yorks-queens-public-library-battles-ransomware-crims-wi-fi-checkouts-and-website-go-dark/5307796)
**Priority 37** · The Register Security · _Ransomware_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

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

### Lesson 309: IPs, ASNs and RIPE

Every public IP belongs to a network called an Autonomous System, identified by an ASN (for example AS2856 is BT). RIPE NCC is the registry for Europe, including the UK. RIPEstat (stat.ripe.net) shows who owns an IP, its ASN, country and routing history for free.

> **Think of it like this:** The IP is a house number. The ASN is the estate or landlord who owns the whole street.

**UK angle:** Knowing whether a malicious IP sits in a UK ASN changes the response. UK hosting means UK law enforcement and UK providers can act, and it may mean a compromised UK business rather than attacker-owned infrastructure.

**Enrichment tip:** Always add ASN name and country to an IP. Flag known residential ISPs (BT, Sky, Virgin Media) because these IPs are often compromised home devices or proxies, not attacker servers.

**Try it today:** Look up one C2 IP from today's Feodo list on stat.ripe.net. Who owns it?

**Quiz:** Which regional registry covers UK IP addresses?  
_Answer:_ RIPE NCC.

**Word of the day: Pivot** · Using one indicator to discover related ones, for example from a domain to its IP to other domains.

### Review (spaced repetition)

- **Companies House as an enrichment source** (1d ago): What does a SIC code tell you about a company? _Answer: Its industry or type of business activity._
- **The intelligence cycle** (3d ago): Which two stages of the cycle are most often skipped? _Answer: Direction (setting requirements) and Feedback._
- **NCSC Early Warning: free enrichment for UK clients** (7d ago): What two kinds of asset does an organisation register with Early Warning? _Answer: IP addresses and domain names._

### Enrichment drill: Unilever listed by Whitearmor ransomware

1. Search Companies House for 'Unilever'. Note its SIC code, size and registered region.
2. Look up Whitearmor on ransomware.live. How many UK victims has it listed this year?
3. Search 'Whitearmor initial access' to find how they usually break in (ATT&CK tactic TA0001).
4. Which of your clients share this sector or region? Write a two-line BLUF heads-up for them.
5. Grade your sources with the Admiralty Code, for example C3 for a leak-site claim.

---
Sources healthy: 14/17 (failed: ICO enforcement (UK regulator), URLhaus, ThreatFox)
