# Threat Intel Field Brief: Tuesday 10 November 2026

_TLP:CLEAR · generated 13:34 UK time · last 36 hours_

## Your morning in 30 seconds

- Read first: Company #189 listed by N0n ransomware (priority 65).
- 6 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 3 UK organisations named on ransomware leak sites (sectors: Not Found).
- 2 stories with strong UK relevance.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [Company #189 listed by N0n ransomware](https://www.ransomware.live/id/Q29tcGFueSAjMTg5QE4wbg==)
**Priority 65** · ransomware.live · UK relevant · _Ransomware, Retail, Not Found_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 2. [Company #157 listed by N0n ransomware](https://www.ransomware.live/id/Q29tcGFueSAjMTU3QE4wbg==)
**Priority 65** · ransomware.live · UK relevant · _Ransomware, Retail, Not Found_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 3. [Company #156 listed by N0n ransomware](https://www.ransomware.live/id/Q29tcGFueSAjMTU2QE4wbg==)
**Priority 65** · ransomware.live · UK relevant · _Ransomware, Retail, Manufacturing_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 4. [CISA Warns of Active Exploitation of OpenSSH, GPUStack, FreeSWITCH, and IBM Flaws](https://thehackernews.com/2026/11/cisa-warns-of-active-exploitation-of.html)
**Priority 56** · The Hacker News · KEV · EPSS 0% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 5. [IBM Aspera Faspex, SignalWire FreeSwitch Vulnerabilities Exploited in Attacks](https://www.securityweek.com/ibm-aspera-faspex-signalwire-freeswitch-vulnerabilities-exploited-in-attacks/)
**Priority 53** · SecurityWeek · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 6. [Hackers exploit SSHole OpenSSH flaw to breach Linux systems](https://www.bleepingcomputer.com/news/security/hackers-exploit-sshole-openssh-flaw-to-breach-linux-systems/)
**Priority 48** · BleepingComputer · KEV · EPSS 1% · _Exploited vuln, Data breach_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 7. [Who Gives A Crap? Hackers, apparently, after toilet paper maker's customer data exposed](https://www.theregister.com/security/2026/11/09/who-gives-a-crap-hackers-apparently-after-toilet-paper-makers-customer-data-exposed/5308419)
**Priority 43** · The Register Security · UK relevant · _Supply chain_

**In plain English:** Attackers break into a supplier or software package to reach that supplier's customers.

**Do this:** List which clients use the affected supplier or package. Ask the supplier for their incident statement and indicators.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

### 8. [CISA Flags SonicWall SonicOS MFA Bypass Flaw Amid Reports of Possible Exploitation](https://thehackernews.com/2026/11/cisa-flags-sonicwall-sonicos-mfa-bypass.html)
**Priority 43** · The Hacker News · KEV · EPSS 1% · _Exploited vuln, Identity / MFA_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

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

### Lesson 314: The Diamond Model

The Diamond Model describes every intrusion with four corners: Adversary (who), Capability (their tools), Infrastructure (servers, domains) and Victim (who was hit). If you know one corner, you can pivot to the others.

> **Think of it like this:** A crime scene board: suspect, weapon, getaway car, victim, with string between them.

**UK angle:** For a UK ransomware victim: Victim from the leak site, Adversary = the gang, Capability = their ransomware, Infrastructure = their C2 and leak site. Each corner is an enrichment job.

**Enrichment tip:** Organise enrichment notes under the four corners. It shows at a glance which corner you know least about.

**Try it today:** Fill in a diamond for one ransomware entry in today's brief. Which corners are empty?

**Quiz:** Name the four corners of the Diamond Model.  
_Answer:_ Adversary, Capability, Infrastructure, Victim.

**Word of the day: STIX** · Structured Threat Information eXpression. A standard JSON format for sharing threat intel.

### Review (spaced repetition)

- **MITRE ATT&CK in five minutes** (1d ago): What is the difference between a tactic and a technique? _Answer: A tactic is the goal (why). A technique is the method used to reach it (how)._
- **Passive DNS and certificate transparency** (3d ago): What is 'pivoting' in threat intel? _Answer: Using one known indicator to discover related indicators, for example from a domain to its IP to other domains on that IP._
- **Priority Intelligence Requirements (PIRs)** (7d ago): Why do PIRs make enrichment faster? _Answer: They tell you which context matters, so you only enrich what answers the client's questions._

### Enrichment drill: Company #189 listed by N0n ransomware

1. Search Companies House for 'Company #189'. Note its SIC code, size and registered region.
2. Look up N0n on ransomware.live. How many UK victims has it listed this year?
3. Search 'N0n initial access' to find how they usually break in (ATT&CK tactic TA0001).
4. Which of your clients share this sector or region? Write a two-line BLUF heads-up for them.
5. Grade your sources with the Admiralty Code, for example C3 for a leak-site claim.

---
Sources healthy: 14/17 (failed: ICO enforcement (UK regulator), URLhaus, ThreatFox)
