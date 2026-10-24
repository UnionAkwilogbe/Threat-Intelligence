# Threat Intel Field Brief: Saturday 24 October 2026

_TLP:CLEAR · generated 10:36 UK time · last 36 hours_

## Your morning in 30 seconds

- Read first: CISA Flags Two Actively Exploited Critical Flaws in Collabora Online and Arista VeloCloud (priority 53).
- 8 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 3 stories with strong UK relevance.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [CISA Flags Two Actively Exploited Critical Flaws in Collabora Online and Arista VeloCloud](https://thehackernews.com/2026/10/cisa-flags-two-actively-exploited.html)
**Priority 53** · The Hacker News · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 2. [CVE-2026-114625: Arista VeloCloud Orchestrator SQL Injection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-114625)
**Priority 40** · CISA KEV · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-26): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 3. [UK threatens subsea cable saboteurs with 14 years behind bars](https://www.theregister.com/networks/2026/10/23/uk-threatens-subsea-cable-saboteurs-with-14-years-behind-bars/5304794)
**Priority 38** · The Register Security · UK relevant · _Nation-state / APT, Telecoms_

**In plain English:** Government-backed hackers, usually after secrets, access, or disruption rather than quick cash.

**Do this:** Map the reported techniques to MITRE ATT&CK and check client detections cover them. Check if the NCSC has issued a joint advisory with indicators to hunt for.

**Enrich next:** Sector (Telecoms) → tag every client in that sector and send them a short heads-up

### 4. [CVE-2026-106931: EG Secure Solutions SiteGuard Server Edition OS Command Injection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-106931)
**Priority 35** · CISA KEV · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-23): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 5. [CVE-2026-96656: Plex Media Server External Control of File Name or Path Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-96656)
**Priority 35** · CISA KEV · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-23): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 6. [CVE-2026-110936: Siemens Software Center Uncontrolled Search Path Element Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-110936)
**Priority 35** · CISA KEV · KEV · EPSS 0% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-03): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 7. [UK proposes 14-year prison terms for undersea cable sabotage](https://therecord.media/uk-undersea-cables-sabotage-new-sentencing-guidelines)
**Priority 34** · The Record · UK relevant · _Public sector_

**In plain English:** General security news worth knowing.

**Do this:** Skim it and note whether any client uses the vendor or product mentioned.

**Enrich next:** Sector (Public sector) → tag every client in that sector and send them a short heads-up

### 8. [Attacks on Tech Firms Behind Most Third-Party Data Breach Victims](https://www.infosecurity-magazine.com/news/tech-third-party-breach-victims/)
**Priority 32** · Infosecurity Magazine · _Data breach, Supply chain_

**In plain English:** Private data got out. Stolen data is later reused for scams and account takeover.

**Do this:** Check if client staff email domains appear in the leak (Have I Been Pwned domain search). Note the UK GDPR angle: serious breaches must be reported to the ICO within 72 hours.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

## Client request RFI-002: PHP2Shell: critical PHP flaws (CVE-2026-109618, CVE-2026-109619) (Client B)

**Status: needs update, new evidence today.**

**Bottom line:** Two critical PHP bugs let an unauthenticated attacker run code on a web server. Fixes shipped on 21 October, details leaked a day earlier, and vendors report attacks already under way. Patch every internet-facing PHP system now, then check it was not compromised before the patch.

- On CISA KEV today: none
- Matching stories today: 6
- New CVEs not yet covered: CVE-2026-115560
- Indicator feeds unavailable today

## Client request RFI-001: Okta vulnerabilities (Client A)

**Status:** In progress, re-checked today.

**Bottom line:** No Okta or Auth0 vulnerability is known to be exploited. The real risk to Okta customers is social engineering: phone-call phishing (vishing) that tricks staff or the help desk into handing over sign-ins and MFA.

- On CISA KEV today: none
- Matching stories today: 0
- New CVEs not yet covered: none
- Indicator feeds unavailable today

## Daily knowledge pack

### Lesson 297: Critical national infrastructure and NIS

CNI covers services the UK depends on: energy, water, transport, health, telecoms, finance, government and more. The NIS Regulations 2018 set security duties for operators of essential services and some digital providers, and many are assessed against the NCSC Cyber Assessment Framework (CAF). The Cyber Security and Resilience Bill is set to widen these rules, so check its current status.

> **Think of it like this:** The load-bearing walls of the country. Everything else leans on them.

**UK angle:** If a client is a CNI operator or supplies one, nation-state and OT (operational technology) stories get a much higher priority.

**Enrichment tip:** Tag clients with 'CNI' and 'NIS regulated' flags. Boost Nation-state / APT and OT stories for those clients.

**Try it today:** Find the CAF on the NCSC website and read the four objectives (A to D).

**Quiz:** What is the NCSC framework used to assess many NIS-regulated organisations?  
_Answer:_ The Cyber Assessment Framework (CAF).

**Word of the day: IOA** · Indicator of Attack. Behaviour showing an attack in progress.

### Review (spaced repetition)

- **Building a UK relevance score** (1d ago): Why should a relevance score be explainable? _Answer: So analysts and clients can trust it, challenge it and tune it._
- **Strategic, operational, tactical, technical** (3d ago): Which level of intel is a list of malicious IPs? _Answer: Technical._
- **Infostealers and stolen sessions** (7d ago): Why can a stolen session cookie bypass MFA? _Answer: It proves a login that already passed MFA, so the attacker does not have to log in again._

### Enrichment drill: CISA Flags Two Actively Exploited Critical Flaws in Collabora Online and Arista VeloCloud

1. Open nvd.nist.gov/vuln/detail/CVE-2026-110447. Note the CVSS score and affected product.
2. Check CVE-2026-110447 on the CISA KEV list and its EPSS score at first.org/epss. Severity vs likelihood vs reality?
3. Find the vendor's own advisory. Is there a patch or only a workaround?
4. Search Shodan or Censys for the product with country:GB. How exposed is the UK?
5. Write a BLUF: which clients, what action, by when (Cyber Essentials allows 14 days, KEV says sooner).

---
Sources healthy: 14/17 (failed: ICO enforcement (UK regulator), URLhaus, ThreatFox)
