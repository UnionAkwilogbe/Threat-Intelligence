# Threat Intel Field Brief: Monday 09 November 2026

_TLP:CLEAR · generated 14:00 UK time · last 72 hours_

## Your morning in 30 seconds

- Read first: Simply UK listed by qilin ransomware (priority 65).
- 3 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 3 UK organisations named on ransomware leak sites (sectors: Education, Not Found, Other).
- 1 stories with strong UK relevance.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [Simply UK listed by qilin ransomware](https://www.ransomware.live/id/U2ltcGx5IFVLQHFpbGlu)
**Priority 65** · ransomware.live · UK relevant · _Ransomware, Not Found_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 2. [Oak Green School listed by qilin ransomware](https://www.ransomware.live/id/T2FrIEdyZWVuIFNjaG9vbEBxaWxpbg==)
**Priority 61** · ransomware.live · UK relevant · _Ransomware, Education_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 3. [Amber Management Ltd listed by qilin ransomware](https://www.ransomware.live/id/QW1iZXIgTWFuYWdlbWVudCBMdGRAcWlsaW4=)
**Priority 61** · ransomware.live · UK relevant · _Ransomware, Other_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 4. [CISA Flags SonicWall SonicOS MFA Bypass Flaw Amid Reports of Possible Exploitation](https://thehackernews.com/2026/11/cisa-flags-sonicwall-sonicos-mfa-bypass.html)
**Priority 56** · The Hacker News · KEV · EPSS 1% · _Exploited vuln, Identity / MFA_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 5. [CVE-2024-27834: Apple Multiple Products Improper Authentication Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2024-27834)
**Priority 35** · CISA KEV · KEV · EPSS 2% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-18): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 6. [CVE-2026-119977: WordPress WordPress Core Time-of-check Time-of-use (TOCTOU) Race Condition Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-119977)
**Priority 35** · CISA KEV · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-06): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 7. [CVE-2026-6715: IBM Concert 1.0 through 3.0.1.1 allows an attacker can supply crafted input that is incorporated into an operating system command without…](https://nvd.nist.gov/vuln/detail/CVE-2026-6715)
**Priority 28** · NVD · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** Treat as patch-now: check the CISA KEV due date and the EPSS score. Search client external attack surface for the affected product and version.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 8. [CVE-2026-15266: IBM Concert 1.0 through 3.0.1.1 contains components that allow potentially unsafe command execution, which could be exploited to run…](https://nvd.nist.gov/vuln/detail/CVE-2026-15266)
**Priority 28** · NVD · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** Treat as patch-now: check the CISA KEV due date and the EPSS score. Search client external attack surface for the affected product and version.

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

### Lesson 313: MITRE ATT&CK in five minutes

ATT&CK is a free catalogue of attacker behaviour. Tactics are the attacker's goal (why), for example Initial Access. Techniques are how they achieve it, for example T1566 Phishing. Each technique has an ID, examples and detection advice.

> **Think of it like this:** A recipe book for attacks: tactics are chapters (starters, mains), techniques are individual recipes.

**UK angle:** NCSC and Five Eyes joint advisories list ATT&CK IDs. Mapping them to a client's detections shows gaps in language their technical team understands.

**Enrichment tip:** When a story has no ATT&CK IDs, add them yourself: phishing email = T1566, valid stolen accounts = T1078, ransomware encryption = T1486.

**Try it today:** Look up T1486 on attack.mitre.org and read the detection section.

**Quiz:** What is the difference between a tactic and a technique?  
_Answer:_ A tactic is the goal (why). A technique is the method used to reach it (how).

**Word of the day: SIEM** · Security Information and Event Management. A system that collects logs and raises alerts.

### Review (spaced repetition)

- **IOC vs IOA vs TTP** (1d ago): Is 'a new admin account created at 3am followed by backup deletion' an IOC or an IOA? _Answer: An IOA. It is suspicious behaviour, not a static artefact._
- **.uk domains, Nominet and WHOIS** (3d ago): Why is domain age a useful enrichment field? _Answer: Newly registered domains are much more likely to be used for phishing or malware._
- **The intelligence cycle** (7d ago): Which two stages of the cycle are most often skipped? _Answer: Direction (setting requirements) and Feedback._

### Enrichment drill: Simply UK listed by qilin ransomware

1. Search Companies House for 'Simply UK'. Note its SIC code, size and registered region.
2. Look up qilin on ransomware.live. How many UK victims has it listed this year?
3. Search 'qilin initial access' to find how they usually break in (ATT&CK tactic TA0001).
4. Which of your clients share this sector or region? Write a two-line BLUF heads-up for them.
5. Grade your sources with the Admiralty Code, for example C3 for a leak-site claim.

---
Sources healthy: 14/17 (failed: ICO enforcement (UK regulator), URLhaus, ThreatFox)
