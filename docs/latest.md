# Threat Intel Field Brief: Monday 16 November 2026

_TLP:CLEAR · generated 13:46 UK time · last 72 hours_

## Your morning in 30 seconds

- Read first: CARRINGTON listed by Vortex ransomware (priority 71).
- 8 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 2 UK organisations named on ransomware leak sites (sectors: Financial Services, Retail & E-Commerce).
- 2 stories with strong UK relevance.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [CARRINGTON listed by Vortex ransomware](https://www.ransomware.live/id/Q0FSUklOR1RPTkBWb3J0ZXg=)
**Priority 71** · ransomware.live · UK relevant · _Ransomware, Financial Services_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 2. [Scans for LiteLLM/Starlette (CVE-2026-42271, CVE-2026-48710), (Mon, Nov 16th)](https://isc.sans.edu/diary/rss/33522)
**Priority 68** · SANS Internet Storm Center · KEV · EPSS 91% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 3. [fittleworth.com listed by Scarlettgroup ransomware](https://www.ransomware.live/id/Zml0dGxld29ydGguY29tQFNjYXJsZXR0Z3JvdXA=)
**Priority 65** · ransomware.live · UK relevant · _Ransomware, Health / NHS, Retail & E-Commerce_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Domain → WHOIS / Nominet for .uk, passive DNS, certificate transparency (crt.sh)

### 4. [Recent UnrealIRCd Vulnerability Exploited in Attacks](https://www.securityweek.com/recent-unrealircd-vulnerability-exploited-in-attacks/)
**Priority 50** · SecurityWeek · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 5. [Information Commissioner’s Office Receives 300+ Reports of Medical Snooping](https://www.infosecurity-magazine.com/news/ico-300-reports-of-medical-snooping/)
**Priority 38** · Infosecurity Magazine · UK relevant

**In plain English:** General security news worth knowing.

**Do this:** Skim it and note whether any client uses the vendor or product mentioned.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

### 6. [UK councils lead on email anti-spoofing but lock into Microsoft](https://www.computerweekly.com/news/366654774/UK-councils-lead-on-email-anti-spoofing-but-lock-into-Microsoft)
**Priority 38** · Computer Weekly Security · UK relevant · _Public sector_

**In plain English:** General security news worth knowing.

**Do this:** Skim it and note whether any client uses the vendor or product mentioned.

**Enrich next:** Sector (Public sector) → tag every client in that sector and send them a short heads-up

### 7. [CVE-2026-111560: Barracuda Networks Multiple Products OS Command Injection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-111560)
**Priority 37** · CISA KEV · KEV · EPSS 11% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-13): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 8. [CVE-2026-123039: Check Point Multiple Products Incorrect Permission Assignment for Critical Resource Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-123039)
**Priority 35** · CISA KEV · KEV · EPSS 2% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-16): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

## Client request RFI-002: PHP2Shell: critical PHP flaws (CVE-2026-109618, CVE-2026-109619) (Client B)

**Status:** In progress, re-checked today.

**Bottom line:** Two critical PHP bugs let an unauthenticated attacker run code on a web server. They are now confirmed exploited and on CISA's Known Exploited Vulnerabilities list (added 26 October). Patch every internet-facing PHP system now, then check it was not compromised from 17 October onwards.

- On CISA KEV today: CVE-2026-109618, CVE-2026-109619, CVE-2026-123039
- Matching stories today: 1
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

### Lesson 320: Cyber Essentials

Cyber Essentials is the UK government-backed baseline certification. Five controls: firewalls, secure configuration, user access control, malware protection, and security update management. Cyber Essentials Plus adds a hands-on technical audit.

> **Think of it like this:** An MOT for a company's basic cyber hygiene.

**UK angle:** Many UK public sector contracts require it. Framing intel around the five controls ('this CVE falls under security update management, 14-day rule') lands well with UK SMEs.

**Enrichment tip:** Tag each story with the Cyber Essentials control it relates to. Clients immediately see which part of their certification is under pressure.

**Try it today:** Map today's top three stories to one of the five Cyber Essentials controls.

**Quiz:** Name the five Cyber Essentials controls.  
_Answer:_ Firewalls, secure configuration, user access control, malware protection, security update management.

**Word of the day: Admiralty Code** · A grading system for intel: source reliability (A-F) plus information credibility (1-6).

### Review (spaced repetition)

- **Matching threats to client assets** (1d ago): What does a CPE name identify? _Answer: A specific vendor and product (and optionally version) so vulnerabilities can be matched to it._
- **Indicators go stale: ageing and decay** (3d ago): Why should IP indicators expire faster than hashes? _Answer: IPs get reassigned to new, often innocent, owners, while a hash always identifies the same file._
- **MITRE ATT&CK in five minutes** (7d ago): What is the difference between a tactic and a technique? _Answer: A tactic is the goal (why). A technique is the method used to reach it (how)._

### Enrichment drill: CARRINGTON listed by Vortex ransomware

1. Search Companies House for 'CARRINGTON'. Note its SIC code, size and registered region.
2. Look up Vortex on ransomware.live. How many UK victims has it listed this year?
3. Search 'Vortex initial access' to find how they usually break in (ATT&CK tactic TA0001).
4. Which of your clients share this sector or region? Write a two-line BLUF heads-up for them.
5. Grade your sources with the Admiralty Code, for example C3 for a leak-site claim.

---
Sources healthy: 14/17 (failed: ICO enforcement (UK regulator), URLhaus, ThreatFox)
