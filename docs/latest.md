# Threat Intel Field Brief: Saturday 17 October 2026

_TLP:CLEAR · generated 10:28 UK time · last 36 hours_

## Your morning in 30 seconds

- Read first: JJS Justice listed by thegentlemen ransomware (priority 66).
- 9 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 1 UK organisations named on ransomware leak sites (sectors: Government & Defense).
- 1 stories with strong UK relevance.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [JJS Justice listed by thegentlemen ransomware](https://www.ransomware.live/id/SkpTIEp1c3RpY2VAdGhlZ2VudGxlbWVu)
**Priority 66** · ransomware.live · UK relevant · _Ransomware, Government & Defense_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Domain → WHOIS / Nominet for .uk, passive DNS, certificate transparency (crt.sh)

### 2. [China-Linked Hackers Exploited BeyondTrust Zero-Day to Take Over Remote Support Servers](https://thehackernews.com/2026/10/china-linked-hackers-exploited.html)
**Priority 46** · The Hacker News · KEV · EPSS 1% · _Zero-day, Exploited vuln, Nation-state / APT_

**In plain English:** A bug attackers found before the vendor could fix it, so there may be no patch yet.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Find out which clients run the product (asset inventory or Shodan/Censys search).

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 3. [PEERSTITCH Malware Deployed via FortiOS Flaw Bypasses Checks on Tagged VPN Sessions](https://thehackernews.com/2026/10/attackers-exploit-fortios-flaw-to.html)
**Priority 43** · The Hacker News · KEV · EPSS 1% · _Exploited vuln, Malware_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 4. [CVE-2026-104935: Ivanti Connect Secure Authentication Bypass by Spoofing Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-104935)
**Priority 40** · CISA KEV · KEV · EPSS 26% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-16): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 5. [CVE-2026-21589: Atlassian Multiple Products Files or Directories Accessible to External Parties Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-21589)
**Priority 38** · CISA KEV · KEV · EPSS 13% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-18): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 6. [CVE-2026-105134: Ahsay AhsayCBS Command Injection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-105134)
**Priority 36** · CISA KEV · KEV · EPSS 5% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-17): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 7. [CVE-2026-76519: Cisco Secure Email Gateway Relative Path Traversal Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-76519)
**Priority 35** · CISA KEV · KEV · EPSS 2% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-17): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 8. [CVE-2026-0322: Palo Alto Networks PAN-OS Code Injection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-0322)
**Priority 35** · CISA KEV · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-17): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

## Client request RFI-001: Okta vulnerabilities (Client A)

**Status:** In progress, re-checked today.

**Bottom line:** No Okta or Auth0 vulnerability is known to be exploited. The real risk to Okta customers is social engineering: phone-call phishing (vishing) that tricks staff or the help desk into handing over sign-ins and MFA.

- On CISA KEV today: none
- Matching stories today: 0
- New CVEs not yet covered: none
- Themed indicators in today's malware feeds: 1 (e.g. hxxps://raw[.]githubusercontent[.]com/fdaloiapp/okta-terraform-demo-template/HEAD/scripts/archive/okta-terraform-demo-template-grossularia[.]zip)

## Daily knowledge pack

### Lesson 290: Infostealers and stolen sessions

Infostealers (for example Lumma, RedLine, Vidar) are malware that grab saved passwords, browser cookies and session tokens. Stolen sessions let attackers skip MFA. Logs get sold on criminal markets and often lead to ransomware or data theft weeks later.

> **Think of it like this:** Stealing someone's house key is bad. Stealing the key and the alarm code together is how people get in without a sound.

**UK angle:** Many major breaches start with a stolen login. Checking whether client domains appear in stealer logs is high-value enrichment.

**Enrichment tip:** Watch for client email domains and SaaS login URLs in breach and stealer-log services, and treat a hit as an incident: reset passwords and revoke sessions.

**Try it today:** Find one infostealer family in today's ThreatFox stats and read what it steals.

**Quiz:** Why can a stolen session cookie bypass MFA?  
_Answer:_ It proves a login that already passed MFA, so the attacker does not have to log in again.

**Word of the day: CVSS** · Common Vulnerability Scoring System. Rates how severe a bug is, from 0 to 10.

### Review (spaced repetition)

- **Where UK victims report things** (1d ago): Where do UK users forward suspicious emails? _Answer: report@phishing.gov.uk._
- **Cyber Essentials** (3d ago): Name the five Cyber Essentials controls. _Answer: Firewalls, secure configuration, user access control, malware protection, security update management._
- **STIX, TAXII and MISP** (7d ago): Which one is the format and which is the transport: STIX or TAXII? _Answer: STIX is the format. TAXII is the transport._

### Enrichment drill: JJS Justice listed by thegentlemen ransomware

1. Search Companies House for 'JJS Justice'. Note its SIC code, size and registered region.
2. Look up thegentlemen on ransomware.live. How many UK victims has it listed this year?
3. Search 'thegentlemen initial access' to find how they usually break in (ATT&CK tactic TA0001).
4. Which of your clients share this sector or region? Write a two-line BLUF heads-up for them.
5. Grade your sources with the Admiralty Code, for example C3 for a leak-site claim.

---
Sources healthy: 16/17 (failed: ICO enforcement (UK regulator))
