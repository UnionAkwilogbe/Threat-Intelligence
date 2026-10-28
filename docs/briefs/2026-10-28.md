# Threat Intel Field Brief: Wednesday 28 October 2026

_TLP:CLEAR · generated 11:25 UK time · last 36 hours_

## Your morning in 30 seconds

- Read first: Bristol City Council listed by Wallstreet ransomware (priority 70).
- 6 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 1 UK organisations named on ransomware leak sites (sectors: Government & Defense).
- 3 stories with strong UK relevance.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [Bristol City Council listed by Wallstreet ransomware](https://www.ransomware.live/id/QnJpc3RvbCBDaXR5IENvdW5jaWxAV2FsbHN0cmVldA==)
**Priority 70** · ransomware.live · UK relevant · _Ransomware, Public sector, Education_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 2. [ShinyHunters-Exploited Oracle PeopleSoft Zero-Day Turns Out to Be Three Chained Flaws](https://thehackernews.com/2026/10/shinyhunters-exploited-oracle.html)
**Priority 69** · The Hacker News · KEV · EPSS 97% · _Zero-day, Exploited vuln_

**In plain English:** A bug attackers found before the vendor could fix it, so there may be no patch yet.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Find out which clients run the product (asset inventory or Shodan/Censys search).

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 3. [Adobe Commerce PolyShell Attacks Breach Hundreds of Stores as Brotli Exploit Traffic Emerges](https://thehackernews.com/2026/10/adobe-commerce-polyshell-attacks-breach.html)
**Priority 64** · The Hacker News · KEV · EPSS 55% · _Data breach, Exploited vuln_

**In plain English:** Private data got out. Stolen data is later reused for scams and account takeover.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Check if client staff email domains appear in the leak (Have I Been Pwned domain search).

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 4. [CISA Confirms Active Exploitation of Two PHP2Shell Flaws Enabling Remote Code Execution](https://thehackernews.com/2026/10/cisa-confirms-active-exploitation-of.html)
**Priority 63** · The Hacker News · KEV · EPSS 100% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 5. [CVE-2026-109619: PHP Group PHP PHP Stale Internal Request-State Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-109619)
**Priority 55** · CISA KEV · KEV · EPSS 100% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-29): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 6. [Apple Backports Fix for Exploited CoreGraphics Flaw to Older iPhones and iPads](https://thehackernews.com/2026/10/apple-backports-fix-for-exploited.html)
**Priority 50** · The Hacker News · KEV · EPSS 26% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 7. [From industry concern to practical action: the value of working with regulators](https://www.ncsc.gov.uk/blogs/industry-concern-practical-action-value-working-regulators)
**Priority 48** · NCSC UK · UK relevant · _Finance_

**In plain English:** General security news worth knowing.

**Do this:** Skim it and note whether any client uses the vendor or product mentioned.

**Enrich next:** Sector (Finance) → tag every client in that sector and send them a short heads-up

### 8. [CVE-2026-48356: Adobe Commerce and Magento Unrestricted Upload of File with Dangerous Type Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-48356)
**Priority 46** · CISA KEV · KEV · EPSS 31% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-10): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

## Client request RFI-002: PHP2Shell: critical PHP flaws (CVE-2026-109618, CVE-2026-109619) (Client B)

**Status:** In progress, re-checked today.

**Bottom line:** Two critical PHP bugs let an unauthenticated attacker run code on a web server. They are now confirmed exploited and on CISA's Known Exploited Vulnerabilities list (added 26 October). Patch every internet-facing PHP system now, then check it was not compromised from 17 October onwards.

- On CISA KEV today: CVE-2026-109618, CVE-2026-109619
- Matching stories today: 6
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

### Lesson 301: The NCSC and what it gives you for free

The National Cyber Security Centre (NCSC) is the UK's technical authority for cyber security and part of GCHQ. It publishes advisories, joint alerts with Five Eyes partners, guidance, and runs free services for UK organisations.

> **Think of it like this:** Think of it as the Met Office for cyber: it forecasts, warns, and publishes guidance, but you still have to bring your own umbrella.

**UK angle:** Free NCSC services worth knowing: Early Warning (alerts you about malicious activity linked to your IPs and domains), Active Cyber Defence tools, Exercise in a Box, and the Suspicious Email Reporting Service.

**Enrichment tip:** When a story mentions a threat, check whether the NCSC has a matching advisory. An NCSC citation is a strong credibility boost for UK clients.

**Try it today:** Visit ncsc.gov.uk and find the Early Warning service page. Note which of your clients could sign up.

**Quiz:** Which UK intelligence agency is the NCSC part of?  
_Answer:_ GCHQ.

**Word of the day: KEV** · CISA's Known Exploited Vulnerabilities catalogue: bugs confirmed to be used in real attacks.

### Review (spaced repetition)

- **CVSS vs EPSS vs KEV** (1d ago): Which of the three tells you a vulnerability is already being used in real attacks? _Answer: KEV. CVSS is severity and EPSS is predicted likelihood._
- **What is data enrichment?** (3d ago): In one sentence, what is the goal of enrichment? _Answer: To add enough context to a raw indicator that someone can make a decision with it._
- **Strategic, operational, tactical, technical** (7d ago): Which level of intel is a list of malicious IPs? _Answer: Technical._

### Enrichment drill: Bristol City Council listed by Wallstreet ransomware

1. Search Companies House for 'Bristol City Council'. Note its SIC code, size and registered region.
2. Look up Wallstreet on ransomware.live. How many UK victims has it listed this year?
3. Search 'Wallstreet initial access' to find how they usually break in (ATT&CK tactic TA0001).
4. Which of your clients share this sector or region? Write a two-line BLUF heads-up for them.
5. Grade your sources with the Admiralty Code, for example C3 for a leak-site claim.

---
Sources healthy: 13/17 (failed: ICO enforcement (UK regulator), Infosecurity Magazine, URLhaus, ThreatFox)
