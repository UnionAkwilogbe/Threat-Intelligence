# Threat Intel Field Brief: Tuesday 24 November 2026

_TLP:CLEAR · generated 23:22 UK time · last 36 hours_

## Your morning in 30 seconds

- Read first: CVE-2026-40217: BerriAI LiteLLM Unprotected Alternate Channel Vulnerability (priority 52).
- 13 vulnerabilities added to CISA KEV this week, 1 linked to ransomware. Check clients run none of them.
- 3 stories with strong UK relevance.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [CVE-2026-40217: BerriAI LiteLLM Unprotected Alternate Channel Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-40217)
**Priority 52** · CISA KEV · KEV · EPSS 83% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-12-02): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 2. [CVE-2026-133968: Project MONAI MONAI Label Path Traversal Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-133968)
**Priority 50** · CISA KEV · KEV · EPSS 50% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-26): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 3. [Hackers Exploit N-able MailAssure Flaw While AI Agents Exploit MONAI Label Zero-Day](https://thehackernews.com/2026/11/hackers-exploit-n-able-mailassure-flaw.html)
**Priority 48** · The Hacker News · KEV · EPSS 1% · _Zero-day, Exploited vuln_

**In plain English:** A bug attackers found before the vendor could fix it, so there may be no patch yet.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Find out which clients run the product (asset inventory or Shodan/Censys search).

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 4. [Introducing CORNERSTONE: delivering external services for the NCSC](https://www.ncsc.gov.uk/blogs/introducing-cornerstone-delivering-external-services-for-the-ncsc)
**Priority 46** · NCSC UK · UK relevant

**In plain English:** General security news worth knowing.

**Do this:** Skim it and note whether any client uses the vendor or product mentioned.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

### 5. [CVE-2024-10441: Synology DiskStation Manager (DSM) Improper Encoding or Escaping of Output Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2024-10441)
**Priority 46** · CISA KEV · KEV · EPSS 3% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-21): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 6. [Familiar weaknesses, exploited faster: defending against agentic cyber attacks](https://www.ncsc.gov.uk/blogs/familiar-weaknesses-exploited-faster-defending-against-agentic-cyber-attacks)
**Priority 45** · NCSC UK · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** Treat as patch-now: check the CISA KEV due date and the EPSS score. Search client external attack surface for the affected product and version.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

### 7. [CVE-2026-132224: Optimizely Web Experimentation External Control of Critical State Data Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-132224)
**Priority 45** · CISA KEV · KEV · EPSS 0% · _Exploited vuln, Fraud / Scam_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-27): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 8. [CVE-2026-131914: Idunno AntiCsrf Deserialization of Untrusted Data Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-131914)
**Priority 45** · CISA KEV · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-27): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

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
- Matching stories today: 2
- New CVEs not yet covered: none
- Indicator feeds unavailable today

## Daily knowledge pack

### Lesson 328: Evaluating feeds

Not every feed is worth ingesting. Judge feeds on: relevance (does it cover threats to your clients?), timeliness, accuracy (false positive rate), completeness (context included?), and uniqueness (does it overlap with what you already have?).

> **Think of it like this:** Choosing newspapers: some are fast but wrong, some are slow but careful, some just copy each other.

**UK angle:** Check how much of a feed is UK-relevant. A feed with lots of US-only activity may be noise for UK clients.

**Enrichment tip:** Use the Source health table at the bottom of this dashboard and track which feeds produce stories you actually forward to clients.

**Try it today:** Look at today's Source health table. Which feed gave the most UK-relevant items?

**Quiz:** Name three criteria for evaluating a threat feed.  
_Answer:_ Any three of: relevance, timeliness, accuracy, completeness, uniqueness.

**Word of the day: CPE** · Common Platform Enumeration. A standard name for a product, used to match vulnerabilities to software.

### Review (spaced repetition)

- **Strategic, operational, tactical, technical** (1d ago): Which level of intel is a list of malicious IPs? _Answer: Technical._
- **Typosquatting and brand monitoring** (3d ago): Why does an MX record on a lookalike domain matter? _Answer: It means the domain can handle email, so it can be used for phishing or invoice fraud._
- **UK GDPR, the ICO and the 72-hour rule** (7d ago): How long does a UK organisation have to report a qualifying personal data breach to the ICO? _Answer: 72 hours from becoming aware of it._

### Enrichment drill: CVE-2026-40217: BerriAI LiteLLM Unprotected Alternate Channel Vulnerability

1. Open nvd.nist.gov/vuln/detail/CVE-2026-40217. Note the CVSS score and affected product.
2. Check CVE-2026-40217 on the CISA KEV list and its EPSS score at first.org/epss. Severity vs likelihood vs reality?
3. Find the vendor's own advisory. Is there a patch or only a workaround?
4. Search Shodan or Censys for the product with country:GB. How exposed is the UK?
5. Write a BLUF: which clients, what action, by when (Cyber Essentials allows 14 days, KEV says sooner).

---
Sources healthy: 14/17 (failed: ICO enforcement (UK regulator), URLhaus, ThreatFox)
