# Threat Intel Field Brief: Thursday 19 November 2026

_TLP:CLEAR · generated 09:25 UK time · last 36 hours_

## Your morning in 30 seconds

- Read first: Company #239 listed by N0n ransomware (priority 75).
- 7 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 4 UK organisations named on ransomware leak sites (sectors: Not Found).
- 3 stories with strong UK relevance.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [Company #239 listed by N0n ransomware](https://www.ransomware.live/id/Q29tcGFueSAjMjM5QE4wbg==)
**Priority 75** · ransomware.live · UK relevant · _Ransomware, Retail, Not Found_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 2. [Company #234 listed by N0n ransomware](https://www.ransomware.live/id/Q29tcGFueSAjMjM0QE4wbg==)
**Priority 75** · ransomware.live · UK relevant · _Ransomware, Retail, Not Found_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 3. [Company #227 listed by N0n ransomware](https://www.ransomware.live/id/Q29tcGFueSAjMjI3QE4wbg==)
**Priority 75** · ransomware.live · UK relevant · _Ransomware, Retail, Not Found_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 4. [Company #225 listed by N0n ransomware](https://www.ransomware.live/id/Q29tcGFueSAjMjI1QE4wbg==)
**Priority 75** · ransomware.live · UK relevant · _Ransomware, Retail, Not Found_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 5. [Hackers Exploiting Critical Puppet RCE Flaw Affecting Enterprise Management Servers](https://thehackernews.com/2026/11/hackers-exploiting-critical-puppet-rce.html)
**Priority 43** · The Hacker News · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 6. [CVE-2026-40217: BerriAI LiteLLM Unprotected Alternate Channel Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-40217)
**Priority 43** · CISA KEV · KEV · EPSS 17% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-12-02): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 7. [CVE-2026-90817: Vanderbilt University Research Electronic Data Capture (REDCap) Code Injection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-90817)
**Priority 41** · CISA KEV · KEV · EPSS 4% · _Exploited vuln, Education_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-21): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 8. [CVE-2024-10441: Synology DiskStation Manager (DSM) Improper Encoding or Escaping of Output Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2024-10441)
**Priority 40** · CISA KEV · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-21): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

## Client request RFI-002: PHP2Shell: critical PHP flaws (CVE-2026-109618, CVE-2026-109619) (Client B)

**Status:** In progress, re-checked today.

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

### Lesson 323: Infostealers and stolen sessions

Infostealers (for example Lumma, RedLine, Vidar) are malware that grab saved passwords, browser cookies and session tokens. Stolen sessions let attackers skip MFA. Logs get sold on criminal markets and often lead to ransomware or data theft weeks later.

> **Think of it like this:** Stealing someone's house key is bad. Stealing the key and the alarm code together is how people get in without a sound.

**UK angle:** Many major breaches start with a stolen login. Checking whether client domains appear in stealer logs is high-value enrichment.

**Enrichment tip:** Watch for client email domains and SaaS login URLs in breach and stealer-log services, and treat a hit as an incident: reset passwords and revoke sessions.

**Try it today:** Find one infostealer family in today's ThreatFox stats and read what it steals.

**Quiz:** Why can a stolen session cookie bypass MFA?  
_Answer:_ It proves a login that already passed MFA, so the attacker does not have to log in again.

**Word of the day: ATT&CK** · MITRE's free catalogue of attacker tactics and techniques, each with an ID such as T1566.

### Review (spaced repetition)

- **Where UK victims report things** (1d ago): Where do UK users forward suspicious emails? _Answer: report@phishing.gov.uk._
- **Cyber Essentials** (3d ago): Name the five Cyber Essentials controls. _Answer: Firewalls, secure configuration, user access control, malware protection, security update management._
- **STIX, TAXII and MISP** (7d ago): Which one is the format and which is the transport: STIX or TAXII? _Answer: STIX is the format. TAXII is the transport._

### Enrichment drill: Company #239 listed by N0n ransomware

1. Search Companies House for 'Company #239'. Note its SIC code, size and registered region.
2. Look up N0n on ransomware.live. How many UK victims has it listed this year?
3. Search 'N0n initial access' to find how they usually break in (ATT&CK tactic TA0001).
4. Which of your clients share this sector or region? Write a two-line BLUF heads-up for them.
5. Grade your sources with the Admiralty Code, for example C3 for a leak-site claim.

---
Sources healthy: 14/17 (failed: ICO enforcement (UK regulator), URLhaus, ThreatFox)
