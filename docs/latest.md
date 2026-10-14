# Threat Intel Field Brief: Wednesday 14 October 2026

_TLP:CLEAR · generated 11:18 UK time · last 36 hours_

## Your morning in 30 seconds

- Read first: AD***ed listed by AuditTeam ransomware (priority 70).
- 7 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 3 UK organisations named on ransomware leak sites (sectors: Manufacturing, Not Found).
- 4 stories with strong UK relevance.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [AD***ed listed by AuditTeam ransomware](https://www.ransomware.live/id/QUQqKiplZEBBdWRpdFRlYW0=)
**Priority 70** · ransomware.live · UK relevant · _Ransomware, Data breach, Not Found_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 2. [Sa***ge listed by AuditTeam ransomware](https://www.ransomware.live/id/U2EqKipnZUBBdWRpdFRlYW0=)
**Priority 70** · ransomware.live · UK relevant · _Ransomware, Data breach, Not Found_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 3. [Saddlers Court MFG listed by play ransomware](https://www.ransomware.live/id/U2FkZGxlcnMgQ291cnQgTUZHQHBsYXk=)
**Priority 61** · ransomware.live · UK relevant · _Ransomware, Manufacturing_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 4. [CVE-2015-5477: ISC BIND Data Processing Errors Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2015-5477)
**Priority 55** · CISA KEV · KEV · EPSS 99% · _Exploited vuln, DDoS_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-11): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 5. [CVE-2015-3306: ProFTPD Improper Access Control Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2015-3306)
**Priority 55** · CISA KEV · KEV · EPSS 99% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-11): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 6. [CVE-2016-3081: Apache Struts Command Injection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2016-3081)
**Priority 54** · CISA KEV · KEV · EPSS 96% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-11): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 7. [Microsoft Patches Record 1,413 Vulnerabilities, Including Exploited Windows Zero-Day](https://www.securityweek.com/microsoft-patches-record-1413-vulnerabilities-including-exploited-windows-zero-day/)
**Priority 53** · SecurityWeek · KEV · _Zero-day, Exploited vuln_

**In plain English:** A bug attackers found before the vendor could fix it, so there may be no patch yet.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Find out which clients run the product (asset inventory or Shodan/Censys search).

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 8. [CVE-2023-22894: Strapi Cleartext Storage of Sensitive Information Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2023-22894)
**Priority 49** · CISA KEV · KEV · EPSS 71% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-11): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

## Client request RFI-001: Okta vulnerabilities (Client A)

**Status:** In progress, re-checked today.

**Bottom line:** No Okta or Auth0 vulnerability is known to be exploited. The real risk to Okta customers is social engineering: phone-call phishing (vishing) that tricks staff or the help desk into handing over sign-ins and MFA.

- On CISA KEV today: none
- Matching stories today: 0
- New CVEs not yet covered: none
- Themed indicators in today's malware feeds: 1 (e.g. hxxps://raw[.]githubusercontent[.]com/fdaloiapp/okta-terraform-demo-template/HEAD/scripts/archive/okta-terraform-demo-template-grossularia[.]zip)

## Daily knowledge pack

### Lesson 287: Cyber Essentials

Cyber Essentials is the UK government-backed baseline certification. Five controls: firewalls, secure configuration, user access control, malware protection, and security update management. Cyber Essentials Plus adds a hands-on technical audit.

> **Think of it like this:** An MOT for a company's basic cyber hygiene.

**UK angle:** Many UK public sector contracts require it. Framing intel around the five controls ('this CVE falls under security update management, 14-day rule') lands well with UK SMEs.

**Enrichment tip:** Tag each story with the Cyber Essentials control it relates to. Clients immediately see which part of their certification is under pressure.

**Try it today:** Map today's top three stories to one of the five Cyber Essentials controls.

**Quiz:** Name the five Cyber Essentials controls.  
_Answer:_ Firewalls, secure configuration, user access control, malware protection, security update management.

**Word of the day: CNI** · Critical National Infrastructure. Services the country depends on, like energy, water and health.

### Review (spaced repetition)

- **Matching threats to client assets** (1d ago): What does a CPE name identify? _Answer: A specific vendor and product (and optionally version) so vulnerabilities can be matched to it._
- **Indicators go stale: ageing and decay** (3d ago): Why should IP indicators expire faster than hashes? _Answer: IPs get reassigned to new, often innocent, owners, while a hash always identifies the same file._
- **MITRE ATT&CK in five minutes** (7d ago): What is the difference between a tactic and a technique? _Answer: A tactic is the goal (why). A technique is the method used to reach it (how)._

### Enrichment drill: AD***ed listed by AuditTeam ransomware

1. Search Companies House for 'AD***ed'. Note its SIC code, size and registered region.
2. Look up AuditTeam on ransomware.live. How many UK victims has it listed this year?
3. Search 'AuditTeam initial access' to find how they usually break in (ATT&CK tactic TA0001).
4. Which of your clients share this sector or region? Write a two-line BLUF heads-up for them.
5. Grade your sources with the Admiralty Code, for example C3 for a leak-site claim.

---
Sources healthy: 16/17 (failed: ICO enforcement (UK regulator))
