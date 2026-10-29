# Threat Intel Field Brief: Thursday 29 October 2026

_TLP:CLEAR · generated 11:35 UK time · last 36 hours_

## Your morning in 30 seconds

- Read first: EWM Group listed by aurora ransomware (priority 70).
- 8 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 1 UK organisations named on ransomware leak sites (sectors: Other).
- 1 stories with strong UK relevance.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [EWM Group listed by aurora ransomware](https://www.ransomware.live/id/RVdNIEdyb3VwQGF1cm9yYQ==)
**Priority 70** · ransomware.live · UK relevant · _Ransomware, Finance, Other_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 2. [Adobe Commerce PolyShell Attacks Breach Hundreds of Stores as Brotli Exploit Traffic Emerges](https://thehackernews.com/2026/10/adobe-commerce-polyshell-attacks-breach.html)
**Priority 61** · The Hacker News · KEV · EPSS 88% · _Data breach, Exploited vuln_

**In plain English:** Private data got out. Stolen data is later reused for scams and account takeover.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Check if client staff email domains appear in the leak (Have I Been Pwned domain search).

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 3. [CVE-2026-46300: Linux Kernel Missing Initialization of a Variable Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-46300)
**Priority 60** · CISA KEV · KEV · EPSS 100% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-31): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 4. [ShinyHunters-Exploited Oracle PeopleSoft Zero-Day Turns Out to Be Three Chained Flaws](https://thehackernews.com/2026/10/shinyhunters-exploited-oracle.html)
**Priority 59** · The Hacker News · KEV · EPSS 97% · _Zero-day, Exploited vuln_

**In plain English:** A bug attackers found before the vendor could fix it, so there may be no patch yet.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Find out which clients run the product (asset inventory or Shodan/Censys search).

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 5. [China-Linked Hackers Exploited VMware ESX Zero-Day to Reduce Audit Trail Visibility](https://thehackernews.com/2026/10/china-linked-hackers-exploited-vmware.html)
**Priority 56** · The Hacker News · KEV · EPSS 0% · _Zero-day, Exploited vuln, Nation-state / APT, Legal_

**In plain English:** A bug attackers found before the vendor could fix it, so there may be no patch yet.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Find out which clients run the product (asset inventory or Shodan/Censys search).

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 6. [CVE-2026-48356: Adobe Commerce and Magento Unrestricted Upload of File with Dangerous Type Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-48356)
**Priority 47** · CISA KEV · KEV · EPSS 59% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-10): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 7. [ICO Reprimands Staffordshire Police After Domestic Abuse Breach](https://www.infosecurity-magazine.com/news/ico-reprimand-staffordshire-police/)
**Priority 46** · Infosecurity Magazine · UK relevant · _Data breach, Public sector_

**In plain English:** Private data got out. Stolen data is later reused for scams and account takeover.

**Do this:** Check if client staff email domains appear in the leak (Have I Been Pwned domain search). Note the UK GDPR angle: serious breaches must be reported to the ICO within 72 hours.

**Enrich next:** Sector (Public sector) → tag every client in that sector and send them a short heads-up

### 8. [CVE-2026-110447: Collabora Online – Built-in CODE Server OS Command Injection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-110447)
**Priority 37** · CISA KEV · KEV · EPSS 12% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-26): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

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

### Lesson 302: NCSC Early Warning: free enrichment for UK clients

Early Warning is a free NCSC service. An organisation registers its IP addresses and domain names, and the NCSC sends alerts when those assets show up in threat feeds: infections, open vulnerable services, or links to attacker infrastructure.

> **Think of it like this:** It is like a neighbourhood watch that already knows your house number and phones you when someone suspicious is spotted outside.

**UK angle:** For a UK MSSP or consultancy this is a cheap win: help each client register. The alerts become another enrichment source tied to their exact assets.

**Enrichment tip:** Keep a list of each client's public IP ranges and domains. The same list powers Early Warning, Shodan checks, and matching IOCs against clients.

**Try it today:** Draft a one-line email to a client explaining Early Warning and why they should register.

**Quiz:** What two kinds of asset does an organisation register with Early Warning?  
_Answer:_ IP addresses and domain names.

**Word of the day: Lateral movement** · An attacker moving from the first machine they took over to other machines in the network.

### Review (spaced repetition)

- **The NCSC and what it gives you for free** (1d ago): Which UK intelligence agency is the NCSC part of? _Answer: GCHQ._
- **The Pyramid of Pain** (3d ago): Which is harder for an attacker to change: an IP address or a technique (TTP)? _Answer: A technique. TTPs sit at the top of the pyramid because changing them means changing how the attacker works._
- **Evaluating feeds** (7d ago): Name three criteria for evaluating a threat feed. _Answer: Any three of: relevance, timeliness, accuracy, completeness, uniqueness._

### Enrichment drill: EWM Group listed by aurora ransomware

1. Search Companies House for 'EWM Group'. Note its SIC code, size and registered region.
2. Look up aurora on ransomware.live. How many UK victims has it listed this year?
3. Search 'aurora initial access' to find how they usually break in (ATT&CK tactic TA0001).
4. Which of your clients share this sector or region? Write a two-line BLUF heads-up for them.
5. Grade your sources with the Admiralty Code, for example C3 for a leak-site claim.

---
Sources healthy: 14/17 (failed: ICO enforcement (UK regulator), URLhaus, ThreatFox)
