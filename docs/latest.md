# Threat Intel Field Brief: Sunday 15 November 2026

_TLP:CLEAR · generated 12:49 UK time · last 36 hours_

## Your morning in 30 seconds

- Read first: fittleworth.com listed by Scarlettgroup ransomware (priority 70).
- 12 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 1 UK organisations named on ransomware leak sites (sectors: Retail & E-Commerce).
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [fittleworth.com listed by Scarlettgroup ransomware](https://www.ransomware.live/id/Zml0dGxld29ydGguY29tQFNjYXJsZXR0Z3JvdXA=)
**Priority 70** · ransomware.live · UK relevant · _Ransomware, Health / NHS, Retail & E-Commerce_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Domain → WHOIS / Nominet for .uk, passive DNS, certificate transparency (crt.sh)

### 2. [Attackers Exploit UnrealIRCd Flaw That Enables Server-Level Command Injection](https://thehackernews.com/2026/11/attackers-exploit-unrealircd-flaw-that.html)
**Priority 43** · The Hacker News · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 3. [CVE-2026-123158: OpenBSD OpenSSH Unexpected Status Code or Return Value Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-123158)
**Priority 39** · CISA KEV · KEV · EPSS 19% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-12): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 4. [CVE-2026-111560: Barracuda Networks Multiple Products OS Command Injection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-111560)
**Priority 37** · CISA KEV · KEV · EPSS 11% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-13): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 5. [CVE-2026-123039: Check Point Multiple Products Incorrect Permission Assignment for Critical Resource Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-123039)
**Priority 35** · CISA KEV · KEV · EPSS 2% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-16): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 6. [CVE-2026-124194: Microsoft Office Outlook Missing User Interaction for Potentially Unsafe Action Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-124194)
**Priority 35** · CISA KEV · KEV · EPSS 2% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-24): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 7. [CVE-2026-111793: Openwave Messaging Limited Webtop Media Transcoder Incorrect Resource Transfer Between Spheres Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-111793)
**Priority 35** · CISA KEV · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-24): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 8. [CVE-2026-20320: Cisco BroadWorks Improper Restriction of XML External Entity Reference Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-20320)
**Priority 35** · CISA KEV · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-24): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

## Client request RFI-002: PHP2Shell: critical PHP flaws (CVE-2026-109618, CVE-2026-109619) (Client B)

**Status: needs update, new evidence today.**

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

### Lesson 319: Matching threats to client assets

The most valuable enrichment is 'does this client have the thing?'. That needs an asset inventory: which vendors, products and versions each client runs, and which are internet facing. Vulnerabilities use CPE names (for example cpe:2.3:a:fortinet:fortios) to identify products.

> **Think of it like this:** A recall notice for a car is only useful if you know which car you drive.

**UK angle:** Shodan and Censys searches with country:GB and a client's IP ranges show what they expose. Pair that with KEV each morning for a very high-value brief.

**Enrichment tip:** Keep a simple per-client file: vendor, product, internet facing (yes/no). Match each morning's CVEs against it. That is personalised intel.

**Try it today:** Write down the five most important internet-facing products for one client (VPN, firewall, email, remote access, website CMS).

**Quiz:** What does a CPE name identify?  
_Answer:_ A specific vendor and product (and optionally version) so vulnerabilities can be matched to it.

**Word of the day: Zero-day** · A vulnerability attackers use before the vendor has released a fix.

### Review (spaced repetition)

- **False positives and allowlists** (1d ago): What is a MISP warninglist for? _Answer: Flagging indicators that are probably false positives, such as well-known legitimate services._
- **STIX, TAXII and MISP** (3d ago): Which one is the format and which is the transport: STIX or TAXII? _Answer: STIX is the format. TAXII is the transport._
- **IOC vs IOA vs TTP** (7d ago): Is 'a new admin account created at 3am followed by backup deletion' an IOC or an IOA? _Answer: An IOA. It is suspicious behaviour, not a static artefact._

### Enrichment drill: fittleworth.com listed by Scarlettgroup ransomware

1. Search Companies House for 'fittleworth.com'. Note its SIC code, size and registered region.
2. Look up Scarlettgroup on ransomware.live. How many UK victims has it listed this year?
3. Search 'Scarlettgroup initial access' to find how they usually break in (ATT&CK tactic TA0001).
4. Which of your clients share this sector or region? Write a two-line BLUF heads-up for them.
5. Grade your sources with the Admiralty Code, for example C3 for a leak-site claim.

---
Sources healthy: 13/17 (failed: ICO enforcement (UK regulator), NVD critical CVEs, URLhaus, ThreatFox)
