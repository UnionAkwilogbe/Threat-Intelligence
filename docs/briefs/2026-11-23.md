# Threat Intel Field Brief: Monday 23 November 2026

_TLP:CLEAR · generated 09:41 UK time · last 72 hours_

## Your morning in 30 seconds

- Read first: Company #267 listed by N0n ransomware (priority 75).
- 9 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 3 UK organisations named on ransomware leak sites (sectors: Not Found).
- 2 stories with strong UK relevance.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [Company #267 listed by N0n ransomware](https://www.ransomware.live/id/Q29tcGFueSAjMjY3QE4wbg==)
**Priority 75** · ransomware.live · UK relevant · _Ransomware, Not Found_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 2. [Company #254 listed by N0n ransomware](https://www.ransomware.live/id/Q29tcGFueSAjMjU0QE4wbg==)
**Priority 75** · ransomware.live · UK relevant · _Ransomware, Retail, Not Found_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 3. [Company #250 listed by N0n ransomware](https://www.ransomware.live/id/Q29tcGFueSAjMjUwQE4wbg==)
**Priority 75** · ransomware.live · UK relevant · _Ransomware, Not Found_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 4. [CVE-2026-40217: BerriAI LiteLLM Unprotected Alternate Channel Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-40217)
**Priority 51** · CISA KEV · KEV · EPSS 78% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-12-02): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 5. [CVE-2026-90817: Vanderbilt University Research Electronic Data Capture (REDCap) Code Injection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-90817)
**Priority 42** · CISA KEV · KEV · EPSS 34% · _Exploited vuln, Education_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-21): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 6. [Hackers Exploit Critical VMware, Cisco, and Apache Flaws as Espionage Attacks Emerge](https://thehackernews.com/2026/11/hackers-exploit-critical-vmware-cisco.html)
**Priority 39** · The Hacker News · KEV · EPSS 5% · _Exploited vuln, Nation-state / APT_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 7. [Hackers Exploit Critical Cisco Expressway Flaw, Breach Four Devices and Reach Internal Network](https://thehackernews.com/2026/11/hackers-exploit-critical-cisco.html)
**Priority 38** · The Hacker News · KEV · EPSS 2% · _Data breach, Exploited vuln, Nation-state / APT_

**In plain English:** Private data got out. Stolen data is later reused for scams and account takeover.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Check if client staff email domains appear in the leak (Have I Been Pwned domain search).

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 8. [Google claims last week’s critical VMware bug was under attack in September](https://www.theregister.com/virtualization/2026/11/23/google-claims-last-weeks-critical-vmware-bug-was-under-attack-in-september/5311547)
**Priority 37** · The Register Security · _Nation-state / APT, Malware_

**In plain English:** Government-backed hackers, usually after secrets, access, or disruption rather than quick cash.

**Do this:** Map the reported techniques to MITRE ATT&CK and check client detections cover them. Check if the NCSC has issued a joint advisory with indicators to hunt for.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

## Client request RFI-002: PHP2Shell: critical PHP flaws (CVE-2026-109618, CVE-2026-109619) (Client B)

**Status:** In progress, re-checked today.

**Bottom line:** Two critical PHP bugs let an unauthenticated attacker run code on a web server. They are now confirmed exploited and on CISA's Known Exploited Vulnerabilities list (added 26 October). Patch every internet-facing PHP system now, then check it was not compromised from 17 October onwards.

- On CISA KEV today: CVE-2026-109618, CVE-2026-109619, CVE-2026-123039
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

### Lesson 327: Strategic, operational, tactical, technical

Strategic intel is for leaders: trends and risk ('ransomware against UK retail is rising'). Operational is about specific campaigns and actors. Tactical covers TTPs for defenders. Technical is the raw IOCs for tools.

> **Think of it like this:** Planning a trip: the country's safety (strategic), a planned strike on travel day (operational), which neighbourhoods to avoid (tactical), the exact address of a pickpocket gang (technical).

**UK angle:** A UK SME board needs strategic plus one action. Their MSP needs tactical and technical. Same enrichment, different packaging.

**Enrichment tip:** Tag each output with its level and audience so the right people get the right version.

**Try it today:** Rewrite one story from today's brief at the strategic level for a board.

**Quiz:** Which level of intel is a list of malicious IPs?  
_Answer:_ Technical.

**Word of the day: CNI** · Critical National Infrastructure. Services the country depends on, like energy, water and health.

### Review (spaced repetition)

- **Writing for clients: BLUF** (1d ago): What does BLUF stand for? _Answer: Bottom Line Up Front._
- **Help desk social engineering** (3d ago): What does the attacker usually ask the help desk for? _Answer: A password reset or to register a new MFA device._
- **Cyber Essentials** (7d ago): Name the five Cyber Essentials controls. _Answer: Firewalls, secure configuration, user access control, malware protection, security update management._

### Enrichment drill: Company #267 listed by N0n ransomware

1. Search Companies House for 'Company #267'. Note its SIC code, size and registered region.
2. Look up N0n on ransomware.live. How many UK victims has it listed this year?
3. Search 'N0n initial access' to find how they usually break in (ATT&CK tactic TA0001).
4. Which of your clients share this sector or region? Write a two-line BLUF heads-up for them.
5. Grade your sources with the Admiralty Code, for example C3 for a leak-site claim.

---
Sources healthy: 14/17 (failed: ICO enforcement (UK regulator), URLhaus, ThreatFox)
