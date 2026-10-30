# Threat Intel Field Brief: Friday 30 October 2026

_TLP:CLEAR · generated 11:27 UK time · last 36 hours_

## Your morning in 30 seconds

- Read first: Antwerp House Dentistry listed by Shiba ransomware (priority 70).
- 8 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 2 UK organisations named on ransomware leak sites (sectors: Healthcare, Technology).
- 3 stories with strong UK relevance.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [Antwerp House Dentistry listed by Shiba ransomware](https://www.ransomware.live/id/QW50d2VycCBIb3VzZSBEZW50aXN0cnlAU2hpYmE=)
**Priority 70** · ransomware.live · UK relevant · _Ransomware, Health / NHS, Healthcare_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 2. [W Interactive listed by qilin ransomware](https://www.ransomware.live/id/VyBJbnRlcmFjdGl2ZUBxaWxpbg==)
**Priority 66** · ransomware.live · UK relevant · _Ransomware, Technology_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 3. [Hackers exploit Cisco SD-WAN flaw to deploy custom KeyDrift malware](https://www.bleepingcomputer.com/news/security/hackers-exploit-cisco-sd-wan-flaw-to-deploy-custom-keydrift-malware/)
**Priority 63** · BleepingComputer · KEV · EPSS 89% · _Exploited vuln, Nation-state / APT, Malware_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 4. [CISA Adds Actively Exploited GitLab RCE and Cisco Firewall DoS Flaws to KEV](https://thehackernews.com/2026/10/cisa-adds-actively-exploited-gitlab-rce.html)
**Priority 60** · The Hacker News · KEV · EPSS 18% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 5. [CVE-2026-46300: Linux Kernel Missing Initialization of a Variable Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-46300)
**Priority 55** · CISA KEV · KEV · EPSS 100% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-31): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 6. [CVE-2026-111497: Google Brotli Unchecked Return Value Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-111497)
**Priority 52** · CISA KEV · KEV · EPSS 83% · _Exploited vuln, DDoS_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-10): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 7. [CVE-2026-48356: Adobe Commerce and Magento Unrestricted Upload of File with Dangerous Type Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-48356)
**Priority 44** · CISA KEV · KEV · EPSS 45% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-10): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 8. [Cisco Patches Actively Exploited ASA and FTD VPN Flaw That Can Crash Firewalls](https://thehackernews.com/2026/10/cisco-patches-actively-exploited-asa.html)
**Priority 43** · The Hacker News · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

## Client request RFI-002: PHP2Shell: critical PHP flaws (CVE-2026-109618, CVE-2026-109619) (Client B)

**Status: needs update, new evidence today.**

**Bottom line:** Two critical PHP bugs let an unauthenticated attacker run code on a web server. They are now confirmed exploited and on CISA's Known Exploited Vulnerabilities list (added 26 October). Patch every internet-facing PHP system now, then check it was not compromised from 17 October onwards.

- On CISA KEV today: CVE-2026-109618, CVE-2026-109619
- Matching stories today: 6
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

### Lesson 303: The Admiralty Code: grading sources

The Admiralty (NATO) system grades intel with a letter and a number. Letter = source reliability (A completely reliable to E unreliable, F cannot be judged). Number = information credibility (1 confirmed by other sources to 5 improbable, 6 cannot be judged). B2 means usually reliable source, probably true.

> **Think of it like this:** Like judging a football rumour: is it from the club's official account (A) or a random fan page (E)? And do other outlets confirm it (1) or does it sound made up (5)?

**UK angle:** The system has British Navy roots and UK police and government analysts still use versions of it, so UK public sector clients recognise it straight away.

**Enrichment tip:** Add an Admiralty grade to every item you forward. The dashboard's 'also reported by' list helps you judge the number: more independent sources means closer to 1.

**Try it today:** Grade the top three stories in today's brief, for example B2 or C3, and write one line on why.

**Quiz:** In the grade 'B2', what does the B describe and what does the 2 describe?  
_Answer:_ B is source reliability (usually reliable). 2 is information credibility (probably true).

**Word of the day: Leak site** · A website where ransomware gangs name victims and publish stolen data to pressure them into paying.

### Review (spaced repetition)

- **NCSC Early Warning: free enrichment for UK clients** (1d ago): What two kinds of asset does an organisation register with Early Warning? _Answer: IP addresses and domain names._
- **CVSS vs EPSS vs KEV** (3d ago): Which of the three tells you a vulnerability is already being used in real attacks? _Answer: KEV. CVSS is severity and EPSS is predicted likelihood._
- **Building a UK relevance score** (7d ago): Why should a relevance score be explainable? _Answer: So analysts and clients can trust it, challenge it and tune it._

### Enrichment drill: Antwerp House Dentistry listed by Shiba ransomware

1. Search Companies House for 'Antwerp House Dentistry'. Note its SIC code, size and registered region.
2. Look up Shiba on ransomware.live. How many UK victims has it listed this year?
3. Search 'Shiba initial access' to find how they usually break in (ATT&CK tactic TA0001).
4. Which of your clients share this sector or region? Write a two-line BLUF heads-up for them.
5. Grade your sources with the Admiralty Code, for example C3 for a leak-site claim.

---
Sources healthy: 14/17 (failed: ICO enforcement (UK regulator), URLhaus, ThreatFox)
