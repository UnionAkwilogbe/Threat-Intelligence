# Threat Intel Field Brief: Monday 23 November 2026

_TLP:CLEAR · generated 16:08 UK time · last 72 hours_

## Your morning in 30 seconds

- Read first: jcatkinson.co.uk listed by safepay ransomware (priority 75).
- 9 vulnerabilities added to CISA KEV this week, 1 linked to ransomware. Check clients run none of them.
- 4 UK organisations named on ransomware leak sites (sectors: Not Found, Professional Services).
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [jcatkinson.co.uk listed by safepay ransomware](https://www.ransomware.live/id/amNhdGtpbnNvbi5jby51a0BzYWZlcGF5)
**Priority 75** · ransomware.live · UK relevant · _Ransomware, Manufacturing, Professional Services_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Domain → WHOIS / Nominet for .uk, passive DNS, certificate transparency (crt.sh)

### 2. [Company #267 listed by N0n ransomware](https://www.ransomware.live/id/Q29tcGFueSAjMjY3QE4wbg==)
**Priority 75** · ransomware.live · UK relevant · _Ransomware, Not Found_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 3. [Company #254 listed by N0n ransomware](https://www.ransomware.live/id/Q29tcGFueSAjMjU0QE4wbg==)
**Priority 70** · ransomware.live · UK relevant · _Ransomware, Retail, Not Found_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 4. [Company #250 listed by N0n ransomware](https://www.ransomware.live/id/Q29tcGFueSAjMjUwQE4wbg==)
**Priority 70** · ransomware.live · UK relevant · _Ransomware, Not Found_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 5. [Critical Cisco Expressway Flaw Exploited in Attacks](https://www.infosecurity-magazine.com/news/critical-cisco-expressway-flaw/)
**Priority 65** · Infosecurity Magazine · KEV · EPSS 2% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 6. [CVE-2026-40217: BerriAI LiteLLM Unprotected Alternate Channel Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-40217)
**Priority 52** · CISA KEV · KEV · EPSS 83% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-12-02): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 7. [Hackers Exploit Critical ScreenConnect Flaw to Hijack MSP Technician PCs Without Warning](https://thehackernews.com/2026/11/hackers-exploit-critical-screenconnect.html)
**Priority 50** · The Hacker News · KEV · EPSS 1% · _Exploited vuln, Tech / MSP_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 8. [CVE-2024-10441: Synology DiskStation Manager (DSM) Improper Encoding or Escaping of Output Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2024-10441)
**Priority 46** · CISA KEV · KEV · EPSS 3% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-21): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

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

### Enrichment drill: jcatkinson.co.uk listed by safepay ransomware

1. Search Companies House for 'jcatkinson.co.uk'. Note its SIC code, size and registered region.
2. Look up safepay on ransomware.live. How many UK victims has it listed this year?
3. Search 'safepay initial access' to find how they usually break in (ATT&CK tactic TA0001).
4. Which of your clients share this sector or region? Write a two-line BLUF heads-up for them.
5. Grade your sources with the Admiralty Code, for example C3 for a leak-site claim.

---
Sources healthy: 14/17 (failed: ICO enforcement (UK regulator), URLhaus, ThreatFox)
