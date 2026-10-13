# Threat Intel Field Brief: Tuesday 13 October 2026

_TLP:CLEAR · generated 13:46 UK time · last 36 hours_

## Your morning in 30 seconds

- Read first: BMT IQ (marine surveying and inspection) listed by N0n ransomware (priority 70).
- 5 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 3 UK organisations named on ransomware leak sites (sectors: Manufacturing, Technology, Transportation).
- 4 stories with strong UK relevance.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [BMT IQ (marine surveying and inspection) listed by N0n ransomware](https://www.ransomware.live/id/Qk1UIElRIChtYXJpbmUgc3VydmV5aW5nIGFuZCBpbnNwZWN0aW9uKUBOMG4=)
**Priority 70** · ransomware.live · UK relevant · _Ransomware, Transportation_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 2. [Saddlers Court MFG listed by play ransomware](https://www.ransomware.live/id/U2FkZGxlcnMgQ291cnQgTUZHQHBsYXk=)
**Priority 66** · ransomware.live · UK relevant · _Ransomware, Manufacturing_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 3. [Cognosis Limited listed by nightspire ransomware](https://www.ransomware.live/id/Q29nbm9zaXMgTGltaXRlZEBuaWdodHNwaXJl)
**Priority 66** · ransomware.live · UK relevant · _Ransomware, Technology_

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

### 7. [CVE-2023-22894: Strapi Cleartext Storage of Sensitive Information Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2023-22894)
**Priority 49** · CISA KEV · KEV · EPSS 71% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-11): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 8. [CVE-2021-3199: ONLYOFFICE Docs Server Path Traversal Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2021-3199)
**Priority 39** · CISA KEV · KEV · EPSS 19% · _Exploited vuln_

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

### Lesson 286: Matching threats to client assets

The most valuable enrichment is 'does this client have the thing?'. That needs an asset inventory: which vendors, products and versions each client runs, and which are internet facing. Vulnerabilities use CPE names (for example cpe:2.3:a:fortinet:fortios) to identify products.

> **Think of it like this:** A recall notice for a car is only useful if you know which car you drive.

**UK angle:** Shodan and Censys searches with country:GB and a client's IP ranges show what they expose. Pair that with KEV each morning for a very high-value brief.

**Enrichment tip:** Keep a simple per-client file: vendor, product, internet facing (yes/no). Match each morning's CVEs against it. That is personalised intel.

**Try it today:** Write down the five most important internet-facing products for one client (VPN, firewall, email, remote access, website CMS).

**Quiz:** What does a CPE name identify?  
_Answer:_ A specific vendor and product (and optionally version) so vulnerabilities can be matched to it.

**Word of the day: CAF** · Cyber Assessment Framework. NCSC's framework for assessing organisations running essential services.

### Review (spaced repetition)

- **False positives and allowlists** (1d ago): What is a MISP warninglist for? _Answer: Flagging indicators that are probably false positives, such as well-known legitimate services._
- **STIX, TAXII and MISP** (3d ago): Which one is the format and which is the transport: STIX or TAXII? _Answer: STIX is the format. TAXII is the transport._
- **IOC vs IOA vs TTP** (7d ago): Is 'a new admin account created at 3am followed by backup deletion' an IOC or an IOA? _Answer: An IOA. It is suspicious behaviour, not a static artefact._

### Enrichment drill: BMT IQ (marine surveying and inspection) listed by N0n ransomware

1. Search Companies House for 'BMT IQ (marine surveying and inspection)'. Note its SIC code, size and registered region.
2. Look up N0n on ransomware.live. How many UK victims has it listed this year?
3. Search 'N0n initial access' to find how they usually break in (ATT&CK tactic TA0001).
4. Which of your clients share this sector or region? Write a two-line BLUF heads-up for them.
5. Grade your sources with the Admiralty Code, for example C3 for a leak-site claim.

---
Sources healthy: 16/17 (failed: ICO enforcement (UK regulator))
