# Threat Intel Field Brief: Wednesday 11 November 2026

_TLP:CLEAR · generated 12:33 UK time · last 36 hours_

## Your morning in 30 seconds

- Read first: Signworx listed by play ransomware (priority 66).
- 11 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 2 UK organisations named on ransomware leak sites (sectors: Other, Professional Services).
- 4 stories with strong UK relevance.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [Signworx listed by play ransomware](https://www.ransomware.live/id/U2lnbndvcnhAcGxheQ==)
**Priority 66** · ransomware.live · UK relevant · _Ransomware, Other_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 2. [A&O Shearman listed by SilentRansomGroup ransomware](https://www.ransomware.live/id/QSZPIFNoZWFybWFuQFNpbGVudFJhbnNvbUdyb3Vw)
**Priority 66** · ransomware.live · UK relevant · _Ransomware, Legal, Professional Services_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 3. [Attackers Exploit AhsayCBS Flaws to Deploy Sandbox-Evading Python Backdoor](https://thehackernews.com/2026/11/attackers-exploit-ahsaycbs-flaws-to.html)
**Priority 62** · The Hacker News · KEV · EPSS 84% · _Exploited vuln, Malware_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 4. [Cisco BroadWorks and Openwave Flaws Actively Exploited Despite Available Patches](https://thehackernews.com/2026/11/cisco-broadworks-and-openwave-flaws.html)
**Priority 56** · The Hacker News · KEV · EPSS 0% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 5. [Threat Actors Exploit Openwave, Cisco BroadWorks Vulnerabilities](https://www.securityweek.com/threat-actors-exploit-openwave-cisco-broadworks-vulnerabilities/)
**Priority 53** · SecurityWeek · KEV · EPSS 0% · _Exploited vuln, Data breach_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 6. [Exploited Outlook Zero-Day Among 1,094 Flaws Patched by Microsoft](https://www.securityweek.com/exploited-outlook-zero-day-among-1094-flaws-patched-by-microsoft/)
**Priority 48** · SecurityWeek · KEV · _Zero-day, Exploited vuln_

**In plain English:** A bug attackers found before the vendor could fix it, so there may be no patch yet.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Find out which clients run the product (asset inventory or Shodan/Censys search).

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 7. [NCSC scheme will help critical organisations test their cyber defences](https://www.ncsc.gov.uk/news/ncsc-scheme-help-critical-organisations-test-their-cyber-defences)
**Priority 46** · NCSC UK · UK relevant

**In plain English:** General security news worth knowing.

**Do this:** Skim it and note whether any client uses the vendor or product mentioned.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

### 8. [Google Issues Chrome Security Update for Eighth Actively Exploited Zero-Day of 2026](https://thehackernews.com/2026/11/google-issues-chrome-security-update.html)
**Priority 43** · The Hacker News · KEV · _Zero-day, Exploited vuln_

**In plain English:** A bug attackers found before the vendor could fix it, so there may be no patch yet.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Find out which clients run the product (asset inventory or Shodan/Censys search).

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

### Lesson 315: The Cyber Kill Chain

Lockheed Martin's Kill Chain splits an attack into seven stages: Reconnaissance, Weaponisation, Delivery, Exploitation, Installation, Command and Control, Actions on Objectives. Stopping any stage breaks the chain.

> **Think of it like this:** Planning a burglary: case the house, get tools, approach, break the lock, move in, keep contact with the getaway driver, steal.

**UK angle:** Great for explaining to UK client boards why a phishing email (Delivery) matters even if nobody clicked: it is a stage you already stopped.

**Enrichment tip:** Tag each IOC with its kill chain stage. A C2 IP is stage 6, so a hit on it means the attacker is already inside.

**Try it today:** Place today's top story onto the kill chain. Which stage does it describe?

**Quiz:** Which stage is a C2 (command and control) server?  
_Answer:_ Stage 6, Command and Control.

**Word of the day: TAXII** · The protocol used to send and receive STIX data over the internet.

### Review (spaced repetition)

- **The Diamond Model** (1d ago): Name the four corners of the Diamond Model. _Answer: Adversary, Capability, Infrastructure, Victim._
- **IOC vs IOA vs TTP** (3d ago): Is 'a new admin account created at 3am followed by backup deletion' an IOC or an IOA? _Answer: An IOA. It is suspicious behaviour, not a static artefact._
- **Companies House as an enrichment source** (7d ago): What does a SIC code tell you about a company? _Answer: Its industry or type of business activity._

### Enrichment drill: Signworx listed by play ransomware

1. Search Companies House for 'Signworx'. Note its SIC code, size and registered region.
2. Look up play on ransomware.live. How many UK victims has it listed this year?
3. Search 'play initial access' to find how they usually break in (ATT&CK tactic TA0001).
4. Which of your clients share this sector or region? Write a two-line BLUF heads-up for them.
5. Grade your sources with the Admiralty Code, for example C3 for a leak-site claim.

---
Sources healthy: 14/17 (failed: ICO enforcement (UK regulator), URLhaus, ThreatFox)
