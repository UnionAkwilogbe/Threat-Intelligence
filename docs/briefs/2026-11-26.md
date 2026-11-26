# Threat Intel Field Brief: Thursday 26 November 2026

_TLP:CLEAR · generated 15:26 UK time · last 36 hours_

## Your morning in 30 seconds

- Read first: liverpool.ac.uk listed by Scarlettgroup ransomware (priority 70).
- 19 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 2 UK organisations named on ransomware leak sites (sectors: Education, Retail & E-Commerce).
- 4 stories with strong UK relevance.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [liverpool.ac.uk listed by Scarlettgroup ransomware](https://www.ransomware.live/id/bGl2ZXJwb29sLmFjLnVrQFNjYXJsZXR0Z3JvdXA=)
**Priority 70** · ransomware.live · UK relevant · _Ransomware, Education_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Domain → WHOIS / Nominet for .uk, passive DNS, certificate transparency (crt.sh)

### 2. [Plumbs Limited listed by aurora ransomware](https://www.ransomware.live/id/UGx1bWJzIExpbWl0ZWRAYXVyb3Jh)
**Priority 70** · ransomware.live · UK relevant · _Ransomware, Manufacturing, Retail & E-Commerce_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Domain → WHOIS / Nominet for .uk, passive DNS, certificate transparency (crt.sh)

### 3. [Drupal Warns of New Highly Critical Site Takeover Vulnerability Under Active Exploitation](https://thehackernews.com/2026/11/drupal-warns-of-new-highly-critical.html)
**Priority 55** · The Hacker News · KEV · EPSS 11% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 4. [Critical Juniper Session Smart Conductor Flaw Exploited in Attacks](https://www.securityweek.com/critical-juniper-session-smart-conductor-flaw-exploited-in-attacks/)
**Priority 53** · SecurityWeek · KEV · EPSS 2% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 5. [Hackers Exploit 10 Vulnerabilities Across Mitel, Juniper, Vates, and Danfoss Products](https://thehackernews.com/2026/11/hackers-exploit-10-vulnerabilities.html)
**Priority 53** · The Hacker News · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 6. [UK Home Office waved through border system without a working fix for bad data](https://www.theregister.com/security/2026/11/26/uk-home-office-waved-through-border-system-without-a-working-fix-for-bad-data/5312162)
**Priority 46** · The Register Security · UK relevant

**In plain English:** General security news worth knowing.

**Do this:** Skim it and note whether any client uses the vendor or product mentioned.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

### 7. [CVE-2026-133469: Vates Xen Orchestra Improper Validation of Specified Type of Input Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-133469)
**Priority 46** · CISA KEV · KEV · EPSS 32% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-28): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 8. [Hackers Exploit Unpatched Flaw in Defunct Idunno AntiCsrf Library](https://www.securityweek.com/hackers-exploit-unpatched-flaw-in-defunct-idunno-anticsrf-library/)
**Priority 44** · SecurityWeek · KEV · EPSS 4% · _Exploited vuln, Zero-day_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

## Client request RFI-002: PHP2Shell: critical PHP flaws (CVE-2026-109618, CVE-2026-109619) (Client B)

**Status:** In progress, re-checked today.

**Bottom line:** Two critical PHP bugs let an unauthenticated attacker run code on a web server. They are now confirmed exploited and on CISA's Known Exploited Vulnerabilities list (added 26 October). Patch every internet-facing PHP system now, then check it was not compromised from 17 October onwards.

- On CISA KEV today: CVE-2026-109618, CVE-2026-109619, CVE-2026-123039, CVE-2026-46300
- Matching stories today: 2
- New CVEs not yet covered: none
- Indicator feeds unavailable today

## Client request RFI-001: Okta vulnerabilities (Client A)

**Status:** In progress, re-checked today.

**Bottom line:** No Okta or Auth0 vulnerability is known to be exploited. The real risk to Okta customers is social engineering: phone-call phishing (vishing) that tricks staff or the help desk into handing over sign-ins and MFA.

- On CISA KEV today: none
- Matching stories today: 1
- New CVEs not yet covered: none
- Indicator feeds unavailable today

## Daily knowledge pack

### Lesson 330: Critical national infrastructure and NIS

CNI covers services the UK depends on: energy, water, transport, health, telecoms, finance, government and more. The NIS Regulations 2018 set security duties for operators of essential services and some digital providers, and many are assessed against the NCSC Cyber Assessment Framework (CAF). The Cyber Security and Resilience Bill is set to widen these rules, so check its current status.

> **Think of it like this:** The load-bearing walls of the country. Everything else leans on them.

**UK angle:** If a client is a CNI operator or supplies one, nation-state and OT (operational technology) stories get a much higher priority.

**Enrichment tip:** Tag clients with 'CNI' and 'NIS regulated' flags. Boost Nation-state / APT and OT stories for those clients.

**Try it today:** Find the CAF on the NCSC website and read the four objectives (A to D).

**Quiz:** What is the NCSC framework used to assess many NIS-regulated organisations?  
_Answer:_ The Cyber Assessment Framework (CAF).

**Word of the day: CVSS** · Common Vulnerability Scoring System. Rates how severe a bug is, from 0 to 10.

### Review (spaced repetition)

- **Building a UK relevance score** (1d ago): Why should a relevance score be explainable? _Answer: So analysts and clients can trust it, challenge it and tune it._
- **Strategic, operational, tactical, technical** (3d ago): Which level of intel is a list of malicious IPs? _Answer: Technical._
- **Infostealers and stolen sessions** (7d ago): Why can a stolen session cookie bypass MFA? _Answer: It proves a login that already passed MFA, so the attacker does not have to log in again._

### Enrichment drill: liverpool.ac.uk listed by Scarlettgroup ransomware

1. Search Companies House for 'liverpool.ac.uk'. Note its SIC code, size and registered region.
2. Look up Scarlettgroup on ransomware.live. How many UK victims has it listed this year?
3. Search 'Scarlettgroup initial access' to find how they usually break in (ATT&CK tactic TA0001).
4. Which of your clients share this sector or region? Write a two-line BLUF heads-up for them.
5. Grade your sources with the Admiralty Code, for example C3 for a leak-site claim.

---
Sources healthy: 14/17 (failed: ICO enforcement (UK regulator), URLhaus, ThreatFox)
