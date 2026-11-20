# Threat Intel Field Brief: Friday 20 November 2026

_TLP:CLEAR · generated 14:07 UK time · last 36 hours_

## Your morning in 30 seconds

- Read first: SDJ Design Engineering Limited listed by spacebears ransomware (priority 71).
- 5 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 2 UK organisations named on ransomware leak sites (sectors: Agriculture and Food Production, Manufacturing).
- 6 stories with strong UK relevance.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [SDJ Design Engineering Limited listed by spacebears ransomware](https://www.ransomware.live/id/U0RKIERlc2lnbiBFbmdpbmVlcmluZyBMaW1pdGVkQHNwYWNlYmVhcnM=)
**Priority 71** · ransomware.live · UK relevant · _Ransomware, Energy / Utilities, Manufacturing_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Domain → WHOIS / Nominet for .uk, passive DNS, certificate transparency (crt.sh)

### 2. [Boutinot Limited listed by aurora ransomware](https://www.ransomware.live/id/Qm91dGlub3QgTGltaXRlZEBhdXJvcmE=)
**Priority 65** · ransomware.live · UK relevant · _Ransomware, Retail, Agriculture and Food Production_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 3. [Everything Is a Web Application, Including Your Firewall](https://thehackernews.com/2026/11/everything-is-web-application-including.html)
**Priority 60** · The Hacker News · KEV · EPSS 100% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 4. [CVE-2026-40217: BerriAI LiteLLM Unprotected Alternate Channel Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-40217)
**Priority 47** · CISA KEV · KEV · EPSS 62% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-12-02): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 5. [CVE-2026-90817: Vanderbilt University Research Electronic Data Capture (REDCap) Code Injection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-90817)
**Priority 40** · CISA KEV · KEV · EPSS 25% · _Exploited vuln, Education_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-21): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 6. [UK government can't keep its encryption-busting order to Apple a secret, tribunal rules](https://www.theregister.com/security/2026/11/20/uk-government-cant-keep-its-encryption-busting-order-to-apple-a-secret-tribunal-rules/5311292)
**Priority 38** · The Register Security · UK relevant · _Public sector_

**In plain English:** General security news worth knowing.

**Do this:** Skim it and note whether any client uses the vendor or product mentioned.

**Enrich next:** Sector (Public sector) → tag every client in that sector and send them a short heads-up

### 7. [JPMorgan Confirms Customer Data Breach Following Third-Party Compromise](https://www.infosecurity-magazine.com/news/jpmorgan-data-breach-third-party/)
**Priority 37** · Infosecurity Magazine · _Ransomware, Data breach, Supply chain_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

### 8. [Suspected North Korea-Aligned Group Hides C2 on Solana Blockchain](https://www.infosecurity-magazine.com/news/overlord-rat-solana-blockchain-c2/)
**Priority 37** · Infosecurity Magazine · _Nation-state / APT, Malware_

**In plain English:** Government-backed hackers, usually after secrets, access, or disruption rather than quick cash.

**Do this:** Map the reported techniques to MITRE ATT&CK and check client detections cover them. Check if the NCSC has issued a joint advisory with indicators to hunt for.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

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
- Matching stories today: 0
- New CVEs not yet covered: none
- Indicator feeds unavailable today

## Daily knowledge pack

### Lesson 324: Help desk social engineering

Groups like Scattered Spider phone IT help desks pretending to be staff and ask for password or MFA resets. No malware needed: they talk their way in, then add their own devices and move to ransomware or data theft.

> **Think of it like this:** Ringing the hotel reception, claiming you lost your room key, and being handed a new one.

**UK angle:** Major UK retail attacks in 2025 were linked to this style of social engineering. It is a top concern for UK retail, finance and anyone with an outsourced help desk.

**Enrichment tip:** For identity attack stories, enrich with the targeted help desk provider or outsourcer. Clients sharing that supplier face higher risk.

**Try it today:** Write three questions a help desk should ask before resetting MFA.

**Quiz:** What does the attacker usually ask the help desk for?  
_Answer:_ A password reset or to register a new MFA device.

**Word of the day: BEC** · Business Email Compromise. Fraud where attackers use or fake a real business email account to redirect payments.

### Review (spaced repetition)

- **Infostealers and stolen sessions** (1d ago): Why can a stolen session cookie bypass MFA? _Answer: It proves a login that already passed MFA, so the attacker does not have to log in again._
- **UK GDPR, the ICO and the 72-hour rule** (3d ago): How long does a UK organisation have to report a qualifying personal data breach to the ICO? _Answer: 72 hours from becoming aware of it._
- **Indicators go stale: ageing and decay** (7d ago): Why should IP indicators expire faster than hashes? _Answer: IPs get reassigned to new, often innocent, owners, while a hash always identifies the same file._

### Enrichment drill: SDJ Design Engineering Limited listed by spacebears ransomware

1. Search Companies House for 'SDJ Design Engineering Limited'. Note its SIC code, size and registered region.
2. Look up spacebears on ransomware.live. How many UK victims has it listed this year?
3. Search 'spacebears initial access' to find how they usually break in (ATT&CK tactic TA0001).
4. Which of your clients share this sector or region? Write a two-line BLUF heads-up for them.
5. Grade your sources with the Admiralty Code, for example C3 for a leak-site claim.

---
Sources healthy: 14/17 (failed: ICO enforcement (UK regulator), URLhaus, ThreatFox)
