# Threat Intel Field Brief: Sunday 01 November 2026

_TLP:CLEAR · generated 11:53 UK time · last 36 hours_

## Your morning in 30 seconds

- Read first: CVE-2026-46300: Linux Kernel Missing Initialization of a Variable Vulnerability (priority 55).
- 10 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [CVE-2026-46300: Linux Kernel Missing Initialization of a Variable Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-46300)
**Priority 55** · CISA KEV · KEV · EPSS 100% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-31): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 2. [CVE-2026-118527: Ivanti Connect Secure Generation of Predictable Numbers or Identifiers Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-118527)
**Priority 52** · CISA KEV · KEV · EPSS 87% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-13): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 3. [CVE-2026-111497: Google Brotli Unchecked Return Value Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-111497)
**Priority 52** · CISA KEV · KEV · EPSS 83% · _Exploited vuln, DDoS_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-10): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 4. [CVE-2026-48356: Adobe Commerce and Magento Unrestricted Upload of File with Dangerous Type Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-48356)
**Priority 44** · CISA KEV · KEV · EPSS 45% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-10): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 5. [CVE-2026-97229: GitLab Community Edition and Enterprise Edition Integer Overflow or Wraparound Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-97229)
**Priority 40** · CISA KEV · KEV · EPSS 27% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-01): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 6. [CVE-2026-76418: Cisco Secure Firewall ASA Software and Cisco Secure FTD Software Unchecked Return Value to NULL Pointer Dereference Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-76418)
**Priority 35** · CISA KEV · KEV · EPSS 1% · _Exploited vuln, DDoS_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-01): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 7. [CVE-2026-41709: Broadcom VMWare ESX Insufficient Logging Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-41709)
**Priority 35** · CISA KEV · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-11): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 8. [FBI Links North Korea's TraderTraitor to Record $6.43 Billion Binance Crypto Heist](https://thehackernews.com/2026/11/fbi-links-north-koreas-tradertraitor-to.html)
**Priority 25** · The Hacker News · _Nation-state / APT, Finance_

**In plain English:** Government-backed hackers, usually after secrets, access, or disruption rather than quick cash.

**Do this:** Map the reported techniques to MITRE ATT&CK and check client detections cover them. Check if the NCSC has issued a joint advisory with indicators to hunt for.

**Enrich next:** Sector (Finance) → tag every client in that sector and send them a short heads-up

## Client request RFI-002: PHP2Shell: critical PHP flaws (CVE-2026-109618, CVE-2026-109619) (Client B)

**Status: needs update, new evidence today.**

**Bottom line:** Two critical PHP bugs let an unauthenticated attacker run code on a web server. They are now confirmed exploited and on CISA's Known Exploited Vulnerabilities list (added 26 October). Patch every internet-facing PHP system now, then check it was not compromised from 17 October onwards.

- On CISA KEV today: CVE-2026-109618, CVE-2026-109619
- Matching stories today: 3
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

### Lesson 305: The PHIA probability yardstick

The UK Professional Head of Intelligence Assessment (PHIA) yardstick links words to probability ranges so 'likely' means the same thing to everyone. Roughly: remote chance (under 5%), highly unlikely (10-20%), unlikely (25-35%), realistic possibility (40-50%), likely (55-75%), highly likely (80-90%), almost certain (95% and above).

> **Think of it like this:** Like a weather forecast saying '70% chance of rain' instead of 'it might rain'. Everyone knows how seriously to take it.

**UK angle:** The NCSC and UK government assessments use this language. Using it in client reports makes your intel sound professional and makes it hard to misread.

**Enrichment tip:** After enriching a story, write one assessment sentence with a yardstick term, for example: 'It is likely (55-75%) that UK retailers will be targeted with this technique this quarter.'

**Try it today:** Rewrite one headline from today's brief as a PHIA-style assessment sentence.

**Quiz:** Which yardstick term covers roughly 55-75%?  
_Answer:_ Likely (or probable).

**Word of the day: MISP** · Free, open source platform for storing, enriching and sharing threat intel.

### Review (spaced repetition)

- **Traffic Light Protocol (TLP 2.0)** (1d ago): Which TLP label means 'share with anyone, publicly'? _Answer: TLP:CLEAR._
- **NCSC Early Warning: free enrichment for UK clients** (3d ago): What two kinds of asset does an organisation register with Early Warning? _Answer: IP addresses and domain names._
- **What is data enrichment?** (7d ago): In one sentence, what is the goal of enrichment? _Answer: To add enough context to a raw indicator that someone can make a decision with it._

### Enrichment drill: CVE-2026-46300: Linux Kernel Missing Initialization of a Variable Vulnerability

1. Open nvd.nist.gov/vuln/detail/CVE-2026-109618. Note the CVSS score and affected product.
2. Check CVE-2026-109618 on the CISA KEV list and its EPSS score at first.org/epss. Severity vs likelihood vs reality?
3. Find the vendor's own advisory. Is there a patch or only a workaround?
4. Search Shodan or Censys for the product with country:GB. How exposed is the UK?
5. Write a BLUF: which clients, what action, by when (Cyber Essentials allows 14 days, KEV says sooner).

---
Sources healthy: 14/17 (failed: ICO enforcement (UK regulator), URLhaus, ThreatFox)
