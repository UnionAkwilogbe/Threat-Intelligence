# Threat Intel Field Brief: Sunday 11 October 2026

_TLP:CLEAR · generated 12:27 UK time · last 36 hours_

## Your morning in 30 seconds

- Read first: CVE-2015-5477: ISC BIND Data Processing Errors Vulnerability (priority 55).
- 5 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [CVE-2015-5477: ISC BIND Data Processing Errors Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2015-5477)
**Priority 55** · CISA KEV · KEV · EPSS 99% · _Exploited vuln, DDoS_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-11): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 2. [CVE-2015-3306: ProFTPD Improper Access Control Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2015-3306)
**Priority 55** · CISA KEV · KEV · EPSS 99% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-11): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 3. [CVE-2016-3081: Apache Struts Command Injection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2016-3081)
**Priority 54** · CISA KEV · KEV · EPSS 96% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-11): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 4. [CVE-2023-22894: Strapi Cleartext Storage of Sensitive Information Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2023-22894)
**Priority 49** · CISA KEV · KEV · EPSS 71% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-11): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 5. [CVE-2021-3199: ONLYOFFICE Docs Server Path Traversal Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2021-3199)
**Priority 39** · CISA KEV · KEV · EPSS 19% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-11): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 6. [CVE-2026-108540: A flaw has been found in OpenSpug Spug up to 3.4.0/4.0.1. This impacts an unknown function of the file /exec/transfer of the component…](https://nvd.nist.gov/vuln/detail/CVE-2026-108540)
**Priority 24** · NVD

**In plain English:** General security news worth knowing.

**Do this:** Skim it and note whether any client uses the vendor or product mentioned.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 7. [CVE-2026-108707: Wukong_HRM through commit 186115e contains an authentication bypass vulnerability in ParamAspect that allows unauthenticated attackers to…](https://nvd.nist.gov/vuln/detail/CVE-2026-108707)
**Priority 23** · NVD

**In plain English:** General security news worth knowing.

**Do this:** Skim it and note whether any client uses the vendor or product mentioned.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 8. [Cyber exec arrested in case allegedly tied to ShinyHunters hackers](https://www.bleepingcomputer.com/news/security/cyber-exec-arrested-in-case-allegedly-tied-to-shinyhunters-hackers/)
**Priority 20** · BleepingComputer · _Ransomware, Charity_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Sector (Charity) → tag every client in that sector and send them a short heads-up

## Client request RFI-001: Okta vulnerabilities (Client A)

**Status:** Answered, re-checked today.

**Bottom line:** No Okta or Auth0 vulnerability is known to be exploited. The real risk to Okta customers is social engineering: phone-call phishing (vishing) that tricks staff or the help desk into handing over sign-ins and MFA.

- On CISA KEV today: none
- Matching stories today: 0
- New CVEs not yet covered: none

## Daily knowledge pack

### Lesson 284: Indicators go stale: ageing and decay

IOCs lose value over time. An IP used for C2 today may be a clean cloud server next month. Hashes stay accurate forever but the attacker stops using them. Good intel records first-seen and last-seen dates and expires old indicators.

> **Think of it like this:** Like milk: great today, questionable next week, harmful next month if you keep blocking with it.

**UK angle:** Blocking a stale IP that now belongs to a UK cloud or CDN provider can break a client's business apps and destroy trust in your feed.

**Enrichment tip:** Add first_seen, last_seen and an expiry date to every IOC. A sensible default: IPs 30 days, domains 90 days, hashes much longer.

**Try it today:** Check the last_online date on one Feodo C2 entry in today's brief. Would you still block it?

**Quiz:** Why should IP indicators expire faster than hashes?  
_Answer:_ IPs get reassigned to new, often innocent, owners, while a hash always identifies the same file.

**Word of the day: BEC** · Business Email Compromise. Fraud where attackers use or fake a real business email account to redirect payments.

### Review (spaced repetition)

- **STIX, TAXII and MISP** (1d ago): Which one is the format and which is the transport: STIX or TAXII? _Answer: STIX is the format. TAXII is the transport._
- **The Diamond Model** (3d ago): Name the four corners of the Diamond Model. _Answer: Adversary, Capability, Infrastructure, Victim._
- **.uk domains, Nominet and WHOIS** (7d ago): Why is domain age a useful enrichment field? _Answer: Newly registered domains are much more likely to be used for phishing or malware._

### Enrichment drill: CVE-2015-5477: ISC BIND Data Processing Errors Vulnerability

1. Open nvd.nist.gov/vuln/detail/CVE-2015-5477. Note the CVSS score and affected product.
2. Check CVE-2015-5477 on the CISA KEV list and its EPSS score at first.org/epss. Severity vs likelihood vs reality?
3. Find the vendor's own advisory. Is there a patch or only a workaround?
4. Search Shodan or Censys for the product with country:GB. How exposed is the UK?
5. Write a BLUF: which clients, what action, by when (Cyber Essentials allows 14 days, KEV says sooner).

---
Sources healthy: 16/17 (failed: ICO enforcement (UK regulator))
