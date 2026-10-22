# Threat Intel Field Brief: Thursday 22 October 2026

_TLP:CLEAR · generated 09:45 UK time · last 36 hours_

## Your morning in 30 seconds

- Read first: novagroupgbc.com listed by BrainCipher ransomware (priority 71).
- 8 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 2 UK organisations named on ransomware leak sites (sectors: Manufacturing, Other).
- 4 stories with strong UK relevance.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [novagroupgbc.com listed by BrainCipher ransomware](https://www.ransomware.live/id/bm92YWdyb3VwZ2JjLmNvbUBCcmFpbkNpcGhlcg==)
**Priority 71** · ransomware.live · UK relevant · _Ransomware, Other_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Domain → WHOIS / Nominet for .uk, passive DNS, certificate transparency (crt.sh)

### 2. [Allmand-Smith Limited listed by aurora ransomware](https://www.ransomware.live/id/QWxsbWFuZC1TbWl0aCBMaW1pdGVkQGF1cm9yYQ==)
**Priority 70** · ransomware.live · UK relevant · _Ransomware, Finance, Manufacturing_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 3. [Critical security issue affecting PHP](https://www.ncsc.gov.uk/news/critical-security-issue-affecting-php)
**Priority 60** · NCSC UK · UK relevant

**In plain English:** General security news worth knowing.

**Do this:** Skim it and note whether any client uses the vendor or product mentioned.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 4. [Children’s Data Stolen After Ransomware Attack Compromises ‘Password1’ Account](https://www.infosecurity-magazine.com/news/children-data-stolen-password1/)
**Priority 46** · Infosecurity Magazine · UK relevant · _Ransomware, Public sector_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Sector (Public sector) → tag every client in that sector and send them a short heads-up

### 5. [CISA Orders Federal Agencies to Patch Exploited Plex2Shell, Siemens, and SiteGuard Flaws](https://thehackernews.com/2026/10/cisa-orders-federal-agencies-to-patch.html)
**Priority 43** · The Hacker News · KEV · EPSS 0% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 6. [PHP blames supply chain security biz Chainguard for putting huge chunks of the web at risk](https://www.theregister.com/security/2026/10/22/php-blames-supply-chain-security-biz-chainguard-for-putting-huge-chunks-of-the-web-at-risk/5304611)
**Priority 37** · The Register Security · _Exploited vuln, Supply chain_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** Treat as patch-now: check the CISA KEV due date and the EPSS score. Search client external attack surface for the affected product and version.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

### 7. [CVE-2026-106931: EG Secure Solutions SiteGuard Server Edition OS Command Injection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-106931)
**Priority 35** · CISA KEV · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-23): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 8. [CVE-2026-96656: Plex Media Server External Control of File Name or Path Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-96656)
**Priority 35** · CISA KEV · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-23): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

## Client request RFI-002: PHP2Shell: critical PHP flaws (CVE-2026-109618, CVE-2026-109619) (Client B)

**Status:** In progress, re-checked today.

**Bottom line:** Two critical PHP bugs let an unauthenticated attacker run code on a web server. Fixes shipped on 21 October, details leaked a day earlier, and vendors report attacks already under way. Patch every internet-facing PHP system now, then check it was not compromised before the patch.

- On CISA KEV today: none
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

### Lesson 295: Evaluating feeds

Not every feed is worth ingesting. Judge feeds on: relevance (does it cover threats to your clients?), timeliness, accuracy (false positive rate), completeness (context included?), and uniqueness (does it overlap with what you already have?).

> **Think of it like this:** Choosing newspapers: some are fast but wrong, some are slow but careful, some just copy each other.

**UK angle:** Check how much of a feed is UK-relevant. A feed with lots of US-only activity may be noise for UK clients.

**Enrichment tip:** Use the Source health table at the bottom of this dashboard and track which feeds produce stories you actually forward to clients.

**Try it today:** Look at today's Source health table. Which feed gave the most UK-relevant items?

**Quiz:** Name three criteria for evaluating a threat feed.  
_Answer:_ Any three of: relevance, timeliness, accuracy, completeness, uniqueness.

**Word of the day: Exfiltration** · Stealing data by copying it out of a network.

### Review (spaced repetition)

- **Strategic, operational, tactical, technical** (1d ago): Which level of intel is a list of malicious IPs? _Answer: Technical._
- **Typosquatting and brand monitoring** (3d ago): Why does an MX record on a lookalike domain matter? _Answer: It means the domain can handle email, so it can be used for phishing or invoice fraud._
- **UK GDPR, the ICO and the 72-hour rule** (7d ago): How long does a UK organisation have to report a qualifying personal data breach to the ICO? _Answer: 72 hours from becoming aware of it._

### Enrichment drill: novagroupgbc.com listed by BrainCipher ransomware

1. Search Companies House for 'novagroupgbc.com'. Note its SIC code, size and registered region.
2. Look up BrainCipher on ransomware.live. How many UK victims has it listed this year?
3. Search 'BrainCipher initial access' to find how they usually break in (ATT&CK tactic TA0001).
4. Which of your clients share this sector or region? Write a two-line BLUF heads-up for them.
5. Grade your sources with the Admiralty Code, for example C3 for a leak-site claim.

---
Sources healthy: 14/17 (failed: ICO enforcement (UK regulator), URLhaus, ThreatFox)
