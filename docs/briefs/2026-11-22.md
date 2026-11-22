# Threat Intel Field Brief: Sunday 22 November 2026

_TLP:CLEAR · generated 13:26 UK time · last 36 hours_

## Your morning in 30 seconds

- Read first: CVE-2026-40217: BerriAI LiteLLM Unprotected Alternate Channel Vulnerability (priority 51).
- 9 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [CVE-2026-40217: BerriAI LiteLLM Unprotected Alternate Channel Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-40217)
**Priority 51** · CISA KEV · KEV · EPSS 78% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-12-02): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 2. [Hackers Exploit Critical VMware, Cisco, and Apache Flaws as Espionage Attacks Emerge](https://thehackernews.com/2026/11/hackers-exploit-critical-vmware-cisco.html)
**Priority 44** · The Hacker News · KEV · EPSS 5% · _Exploited vuln, Nation-state / APT_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 3. [CVE-2026-90817: Vanderbilt University Research Electronic Data Capture (REDCap) Code Injection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-90817)
**Priority 42** · CISA KEV · KEV · EPSS 33% · _Exploited vuln, Education_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-21): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 4. [CVE-2026-129448: Apache Roller Deserialization of Untrusted Data Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-129448)
**Priority 36** · CISA KEV · KEV · EPSS 5% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-23): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 5. [CVE-2026-123890: Broadcom VMware vCenter VMWare vCenter Authentication Bypass Using an Alternate Path or Channel Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-123890)
**Priority 36** · CISA KEV · KEV · EPSS 3% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-23): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 6. [CVE-2024-10441: Synology DiskStation Manager (DSM) Improper Encoding or Escaping of Output Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2024-10441)
**Priority 36** · CISA KEV · KEV · EPSS 3% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-21): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 7. [CVE-2026-90436: Apache Axis Unsafe Reflection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-90436)
**Priority 36** · CISA KEV · KEV · EPSS 4% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-21): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 8. [CVE-2025-42884: SAP NetWeaver Improper Neutralization of Special Elements in Data Query Logic Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2025-42884)
**Priority 35** · CISA KEV · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-23): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

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

### Lesson 326: Writing for clients: BLUF

BLUF means Bottom Line Up Front. Start with the conclusion and the action, then give the detail. Busy readers stop after the first two lines, so those lines must carry the message.

> **Think of it like this:** A news headline and first paragraph tell you the whole story. The rest is for people who want more.

**UK angle:** UK client boards and service desks both want: what happened, does it affect us, what do we do, by when.

**Enrichment tip:** Your enrichment should end in a BLUF line: 'Action: patch FortiOS on the two internet-facing firewalls today. KEV-listed, EPSS 94%.'

**Try it today:** Write a two-line BLUF for today's number one story.

**Quiz:** What does BLUF stand for?  
_Answer:_ Bottom Line Up Front.

**Word of the day: CAF** · Cyber Assessment Framework. NCSC's framework for assessing organisations running essential services.

### Review (spaced repetition)

- **Typosquatting and brand monitoring** (1d ago): Why does an MX record on a lookalike domain matter? _Answer: It means the domain can handle email, so it can be used for phishing or invoice fraud._
- **Infostealers and stolen sessions** (3d ago): Why can a stolen session cookie bypass MFA? _Answer: It proves a login that already passed MFA, so the attacker does not have to log in again._
- **Matching threats to client assets** (7d ago): What does a CPE name identify? _Answer: A specific vendor and product (and optionally version) so vulnerabilities can be matched to it._

### Enrichment drill: CVE-2026-40217: BerriAI LiteLLM Unprotected Alternate Channel Vulnerability

1. Open nvd.nist.gov/vuln/detail/CVE-2026-40217. Note the CVSS score and affected product.
2. Check CVE-2026-40217 on the CISA KEV list and its EPSS score at first.org/epss. Severity vs likelihood vs reality?
3. Find the vendor's own advisory. Is there a patch or only a workaround?
4. Search Shodan or Censys for the product with country:GB. How exposed is the UK?
5. Write a BLUF: which clients, what action, by when (Cyber Essentials allows 14 days, KEV says sooner).

---
Sources healthy: 14/17 (failed: ICO enforcement (UK regulator), URLhaus, ThreatFox)
