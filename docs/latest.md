# Threat Intel Field Brief: Wednesday 25 November 2026

_TLP:CLEAR · generated 09:35 UK time · last 36 hours_

## Your morning in 30 seconds

- Read first: Hackers Exploit Unpatched Flaw in Defunct Idunno AntiCsrf Library (priority 53).
- 9 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 4 stories with strong UK relevance.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [Hackers Exploit Unpatched Flaw in Defunct Idunno AntiCsrf Library](https://www.securityweek.com/hackers-exploit-unpatched-flaw-in-defunct-idunno-anticsrf-library/)
**Priority 53** · SecurityWeek · KEV · EPSS 1% · _Exploited vuln, Zero-day_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 2. [CVE-2026-133968: Project MONAI MONAI Label Path Traversal Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-133968)
**Priority 45** · CISA KEV · KEV · EPSS 50% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-26): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 3. [UK Authorized Push Payment Losses Surge 22% as Fraudsters Steal £660m](https://www.infosecurity-magazine.com/news/uk-app-losses-surge-22-fraudsters/)
**Priority 43** · Infosecurity Magazine · UK relevant · _Fraud / Scam, Finance_

**In plain English:** Tricks aimed at stealing money, often by pretending to be a trusted brand or person.

**Do this:** Watch for lookalike domains of client brands (typosquats). UK victims report to Action Fraud (England, Wales, NI) or Police Scotland.

**Enrich next:** Sector (Finance) → tag every client in that sector and send them a short heads-up

### 4. [Hackers Exploit N-able MailAssure Flaw While AI Agents Exploit MONAI Label Zero-Day](https://thehackernews.com/2026/11/hackers-exploit-n-able-mailassure-flaw.html)
**Priority 43** · The Hacker News · KEV · EPSS 1% · _Zero-day, Exploited vuln_

**In plain English:** A bug attackers found before the vendor could fix it, so there may be no patch yet.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Find out which clients run the product (asset inventory or Shodan/Censys search).

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 5. [CVE-2026-129448: Apache Roller Deserialization of Untrusted Data Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-129448)
**Priority 43** · CISA KEV · KEV · EPSS 40% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-23): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 6. [Introducing CORNERSTONE: delivering external services for the NCSC](https://www.ncsc.gov.uk/blogs/introducing-cornerstone-delivering-external-services-for-the-ncsc)
**Priority 41** · NCSC UK · UK relevant

**In plain English:** General security news worth knowing.

**Do this:** Skim it and note whether any client uses the vendor or product mentioned.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

### 7. [Familiar weaknesses, exploited faster: defending against agentic cyber attacks](https://www.ncsc.gov.uk/blogs/familiar-weaknesses-exploited-faster-defending-against-agentic-cyber-attacks)
**Priority 40** · NCSC UK · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** Treat as patch-now: check the CISA KEV due date and the EPSS score. Search client external attack surface for the affected product and version.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

### 8. [CVE-2026-132224: Optimizely Web Experimentation External Control of Critical State Data Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-132224)
**Priority 40** · CISA KEV · KEV · EPSS 0% · _Exploited vuln, Fraud / Scam_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-27): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

## Client request RFI-002: PHP2Shell: critical PHP flaws (CVE-2026-109618, CVE-2026-109619) (Client B)

**Status:** In progress, re-checked today.

**Bottom line:** Two critical PHP bugs let an unauthenticated attacker run code on a web server. They are now confirmed exploited and on CISA's Known Exploited Vulnerabilities list (added 26 October). Patch every internet-facing PHP system now, then check it was not compromised from 17 October onwards.

- On CISA KEV today: CVE-2026-109618, CVE-2026-109619, CVE-2026-123039, CVE-2026-46300
- Matching stories today: 1
- New CVEs not yet covered: none
- Indicator feeds unavailable today

## Client request RFI-001: Okta vulnerabilities (Client A)

**Status:** In progress, re-checked today.

**Bottom line:** No Okta or Auth0 vulnerability is known to be exploited. The real risk to Okta customers is social engineering: phone-call phishing (vishing) that tricks staff or the help desk into handing over sign-ins and MFA.

- On CISA KEV today: none
- Matching stories today: 4
- New CVEs not yet covered: none
- Indicator feeds unavailable today

## Daily knowledge pack

### Lesson 329: Building a UK relevance score

A relevance score combines simple signals into one number so you know what to read first. This dashboard adds points for UK keywords, UK sources, KEV status, EPSS, severity, threat type, freshness and corroboration. Every point is explained in the 'why' line.

> **Think of it like this:** A credit score for news stories: many small signals turned into one number you can sort by.

**UK angle:** Tune the weights to your clients: a legal-sector client should boost 'law firm' and 'solicitor'; a council client should boost 'council' and 'public sector'.

**Enrichment tip:** Keep scoring explainable. If a client asks 'why is this top?', you should be able to point to each factor.

**Try it today:** Open ti/enrich.py and find UK_TERMS. Add one keyword that matters to your clients.

**Quiz:** Why should a relevance score be explainable?  
_Answer:_ So analysts and clients can trust it, challenge it and tune it.

**Word of the day: CVE** · Common Vulnerabilities and Exposures. A unique ID for a publicly known security bug, for example CVE-2024-3400.

### Review (spaced repetition)

- **Evaluating feeds** (1d ago): Name three criteria for evaluating a threat feed. _Answer: Any three of: relevance, timeliness, accuracy, completeness, uniqueness._
- **Writing for clients: BLUF** (3d ago): What does BLUF stand for? _Answer: Bottom Line Up Front._
- **Where UK victims report things** (7d ago): Where do UK users forward suspicious emails? _Answer: report@phishing.gov.uk._

### Enrichment drill: Hackers Exploit Unpatched Flaw in Defunct Idunno AntiCsrf Library

1. Open nvd.nist.gov/vuln/detail/CVE-2026-131914. Note the CVSS score and affected product.
2. Check CVE-2026-131914 on the CISA KEV list and its EPSS score at first.org/epss. Severity vs likelihood vs reality?
3. Find the vendor's own advisory. Is there a patch or only a workaround?
4. Search Shodan or Censys for the product with country:GB. How exposed is the UK?
5. Write a BLUF: which clients, what action, by when (Cyber Essentials allows 14 days, KEV says sooner).

---
Sources healthy: 14/17 (failed: ICO enforcement (UK regulator), URLhaus, ThreatFox)
