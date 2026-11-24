# Threat Intel Field Brief: Tuesday 24 November 2026

_TLP:CLEAR · generated 15:58 UK time · last 36 hours_

## Your morning in 30 seconds

- Read first: jcatkinson.co.uk listed by safepay ransomware (priority 65).
- 10 vulnerabilities added to CISA KEV this week, 1 linked to ransomware. Check clients run none of them.
- 4 UK organisations named on ransomware leak sites (sectors: Not Found, Professional Services).
- 4 stories with strong UK relevance.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [jcatkinson.co.uk listed by safepay ransomware](https://www.ransomware.live/id/amNhdGtpbnNvbi5jby51a0BzYWZlcGF5)
**Priority 65** · ransomware.live · UK relevant · _Ransomware, Manufacturing, Professional Services_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Domain → WHOIS / Nominet for .uk, passive DNS, certificate transparency (crt.sh)

### 2. [Company #267 listed by N0n ransomware](https://www.ransomware.live/id/Q29tcGFueSAjMjY3QE4wbg==)
**Priority 65** · ransomware.live · UK relevant · _Ransomware, Not Found_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 3. [Company #254 listed by N0n ransomware](https://www.ransomware.live/id/Q29tcGFueSAjMjU0QE4wbg==)
**Priority 65** · ransomware.live · UK relevant · _Ransomware, Retail, Not Found_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 4. [Company #250 listed by N0n ransomware](https://www.ransomware.live/id/Q29tcGFueSAjMjUwQE4wbg==)
**Priority 65** · ransomware.live · UK relevant · _Ransomware, Not Found_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 5. [Critical Cisco Expressway Flaw Exploited in Attacks](https://www.infosecurity-magazine.com/news/critical-cisco-expressway-flaw/)
**Priority 55** · Infosecurity Magazine · KEV · EPSS 2% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 6. [Hackers Exploit N-able MailAssure Flaw While AI Agents Exploit MONAI Label Zero-Day](https://thehackernews.com/2026/11/hackers-exploit-n-able-mailassure-flaw.html)
**Priority 53** · The Hacker News · KEV · EPSS 1% · _Zero-day, Exploited vuln_

**In plain English:** A bug attackers found before the vendor could fix it, so there may be no patch yet.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Find out which clients run the product (asset inventory or Shodan/Censys search).

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 7. [CVE-2026-40217: BerriAI LiteLLM Unprotected Alternate Channel Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-40217)
**Priority 52** · CISA KEV · KEV · EPSS 83% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-12-02): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 8. [CVE-2026-133968: Project MONAI MONAI Label Path Traversal Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-133968)
**Priority 50** · CISA KEV · KEV · EPSS 50% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-26): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

## Client request RFI-002: PHP2Shell: critical PHP flaws (CVE-2026-109618, CVE-2026-109619) (Client B)

**Status:** In progress, re-checked today.

**Bottom line:** Two critical PHP bugs let an unauthenticated attacker run code on a web server. They are now confirmed exploited and on CISA's Known Exploited Vulnerabilities list (added 26 October). Patch every internet-facing PHP system now, then check it was not compromised from 17 October onwards.

- On CISA KEV today: CVE-2026-109618, CVE-2026-109619, CVE-2026-123039
- Matching stories today: 1
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

### Enrichment drill: jcatkinson.co.uk listed by safepay ransomware

1. Search Companies House for 'jcatkinson.co.uk'. Note its SIC code, size and registered region.
2. Look up safepay on ransomware.live. How many UK victims has it listed this year?
3. Search 'safepay initial access' to find how they usually break in (ATT&CK tactic TA0001).
4. Which of your clients share this sector or region? Write a two-line BLUF heads-up for them.
5. Grade your sources with the Admiralty Code, for example C3 for a leak-site claim.

---
Sources healthy: 14/17 (failed: ICO enforcement (UK regulator), URLhaus, ThreatFox)
