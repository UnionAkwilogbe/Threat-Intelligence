# Threat Intel Field Brief: Saturday 31 October 2026

_TLP:CLEAR · generated 10:58 UK time · last 36 hours_

## Your morning in 30 seconds

- Read first: Palletline listed by qilin ransomware (priority 66).
- 10 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 1 UK organisations named on ransomware leak sites (sectors: Transportation).
- 2 stories with strong UK relevance.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [Palletline listed by qilin ransomware](https://www.ransomware.live/id/UGFsbGV0bGluZUBxaWxpbg==)
**Priority 66** · ransomware.live · UK relevant · _Ransomware, Transportation_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 2. [CVE-2026-118527: Ivanti Connect Secure Generation of Predictable Numbers or Identifiers Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-118527)
**Priority 57** · CISA KEV · KEV · EPSS 87% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-13): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 3. [CVE-2026-46300: Linux Kernel Missing Initialization of a Variable Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-46300)
**Priority 55** · CISA KEV · KEV · EPSS 100% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-31): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 4. [CVE-2026-111497: Google Brotli Unchecked Return Value Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-111497)
**Priority 52** · CISA KEV · KEV · EPSS 83% · _Exploited vuln, DDoS_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-10): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 5. [CISA Adds Actively Exploited GitLab RCE and Cisco Firewall DoS Flaws to KEV](https://thehackernews.com/2026/10/cisa-adds-actively-exploited-gitlab-rce.html)
**Priority 51** · The Hacker News · KEV · EPSS 27% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 6. [CVE-2026-48356: Adobe Commerce and Magento Unrestricted Upload of File with Dangerous Type Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-48356)
**Priority 44** · CISA KEV · KEV · EPSS 45% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-10): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 7. [CVE-2026-76418: Cisco Secure Firewall ASA Software and Cisco Secure FTD Software Unchecked Return Value to NULL Pointer Dereference Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-76418)
**Priority 35** · CISA KEV · KEV · EPSS 1% · _Exploited vuln, DDoS_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-01): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 8. [CVE-2026-41709: Broadcom VMWare ESX Insufficient Logging Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-41709)
**Priority 35** · CISA KEV · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-11): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

## Client request RFI-002: PHP2Shell: critical PHP flaws (CVE-2026-109618, CVE-2026-109619) (Client B)

**Status: needs update, new evidence today.**

**Bottom line:** Two critical PHP bugs let an unauthenticated attacker run code on a web server. They are now confirmed exploited and on CISA's Known Exploited Vulnerabilities list (added 26 October). Patch every internet-facing PHP system now, then check it was not compromised from 17 October onwards.

- On CISA KEV today: CVE-2026-109618, CVE-2026-109619
- Matching stories today: 5
- New CVEs not yet covered: CVE-2026-46300
- Indicator feeds unavailable today

## Client request RFI-001: Okta vulnerabilities (Client A)

**Status:** In progress, re-checked today.

**Bottom line:** No Okta or Auth0 vulnerability is known to be exploited. The real risk to Okta customers is social engineering: phone-call phishing (vishing) that tricks staff or the help desk into handing over sign-ins and MFA.

- On CISA KEV today: none
- Matching stories today: 0
- New CVEs not yet covered: none
- Indicator feeds unavailable today

## Daily knowledge pack

### Lesson 304: Traffic Light Protocol (TLP 2.0)

TLP labels tell the reader who they may share information with. TLP:CLEAR = anyone. TLP:GREEN = your community, not public. TLP:AMBER = your organisation and its clients who need to know. TLP:AMBER+STRICT = your organisation only. TLP:RED = named recipients only, no further sharing.

> **Think of it like this:** Like party invitations: CLEAR is a public poster, GREEN is the group chat, AMBER is your family, RED is a whisper to one person.

**UK angle:** UK information sharing groups and NCSC partners use TLP. Labelling your client briefs correctly shows maturity and keeps you trusted.

**Enrichment tip:** Enrichment can change the TLP. Mixing a public IOC with a client's internal log data makes the result sensitive, so label it AMBER or stricter.

**Try it today:** Decide a TLP label for today's brief if you forwarded it to a client. What would change if you added their log data?

**Quiz:** Which TLP label means 'share with anyone, publicly'?  
_Answer:_ TLP:CLEAR.

**Word of the day: MFA** · Multi-Factor Authentication. Proving who you are with more than a password, such as an app prompt.

### Review (spaced repetition)

- **The Admiralty Code: grading sources** (1d ago): In the grade 'B2', what does the B describe and what does the 2 describe? _Answer: B is source reliability (usually reliable). 2 is information credibility (probably true)._
- **The NCSC and what it gives you for free** (3d ago): Which UK intelligence agency is the NCSC part of? _Answer: GCHQ._
- **Critical national infrastructure and NIS** (7d ago): What is the NCSC framework used to assess many NIS-regulated organisations? _Answer: The Cyber Assessment Framework (CAF)._

### Enrichment drill: Palletline listed by qilin ransomware

1. Search Companies House for 'Palletline'. Note its SIC code, size and registered region.
2. Look up qilin on ransomware.live. How many UK victims has it listed this year?
3. Search 'qilin initial access' to find how they usually break in (ATT&CK tactic TA0001).
4. Which of your clients share this sector or region? Write a two-line BLUF heads-up for them.
5. Grade your sources with the Admiralty Code, for example C3 for a leak-site claim.

---
Sources healthy: 14/17 (failed: ICO enforcement (UK regulator), URLhaus, ThreatFox)
