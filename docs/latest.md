# Threat Intel Field Brief: Wednesday 04 November 2026

_TLP:CLEAR · generated 13:04 UK time · last 36 hours_

## Your morning in 30 seconds

- Read first: IHG Hotels & Resorts (Estate) listed by BYOD ransomware (priority 71).
- 5 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 2 UK organisations named on ransomware leak sites (sectors: Hospitality, Other).
- 7 stories with strong UK relevance.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [IHG Hotels & Resorts (Estate) listed by BYOD ransomware](https://www.ransomware.live/id/SUhHIEhvdGVscyAmIFJlc29ydHMgKEVzdGF0ZSlAQllPRA==)
**Priority 71** · ransomware.live · UK relevant · _Ransomware, Finance, Hospitality_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 2. [Boardman Park listed by Booba Project ransomware](https://www.ransomware.live/id/Qm9hcmRtYW4gUGFya0BCb29iYSBQcm9qZWN0)
**Priority 61** · ransomware.live · UK relevant · _Ransomware, Data breach, Other_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 3. [CISA Confirms Hackers Exploiting WordPress Core Flaw During Software Upgrades](https://thehackernews.com/2026/11/cisa-confirms-hackers-exploiting.html)
**Priority 53** · The Hacker News · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 4. [CVE-2026-118527: Ivanti Connect Secure Generation of Predictable Numbers or Identifiers Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-118527)
**Priority 53** · CISA KEV · KEV · EPSS 89% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-13): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 5. [NCSC Chief Warns of Imminent AI Ransomware Threat to UK Critical Infrastructure](https://www.infosecurity-magazine.com/news/ncsc-ai-ransomware-threat-uk-cni/)
**Priority 50** · Infosecurity Magazine · UK relevant · _Ransomware, Malware_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

### 6. [3AM Ransomware Used Human-AI Hybrid Tactics in UK School Estate Compromise](https://www.infosecurity-magazine.com/news/3am-ransomware-hybrid-ai-uk-school/)
**Priority 48** · Infosecurity Magazine · UK relevant · _Ransomware, Data breach, Finance, Education_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Sector (Finance, Education) → tag every client in that sector and send them a short heads-up

### 7. [Cyber chief: UK facing AI-powered attacks on critical infrastructure within two years](https://www.ncsc.gov.uk/news/cyber-chief-uk-facing-ai-powered-attacks-on-critical-infrastructure-in-two-years)
**Priority 46** · NCSC UK · UK relevant

**In plain English:** General security news worth knowing.

**Do this:** Skim it and note whether any client uses the vendor or product mentioned.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

### 8. [CVE-2026-97229: GitLab Community Edition and Enterprise Edition Integer Overflow or Wraparound Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-97229)
**Priority 41** · CISA KEV · KEV · EPSS 28% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-01): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

## Client request RFI-002: PHP2Shell: critical PHP flaws (CVE-2026-109618, CVE-2026-109619) (Client B)

**Status:** In progress, re-checked today.

**Bottom line:** Two critical PHP bugs let an unauthenticated attacker run code on a web server. They are now confirmed exploited and on CISA's Known Exploited Vulnerabilities list (added 26 October). Patch every internet-facing PHP system now, then check it was not compromised from 17 October onwards.

- On CISA KEV today: CVE-2026-109618, CVE-2026-109619
- Matching stories today: 0
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

### Lesson 308: Companies House as an enrichment source

Companies House is the UK register of companies. Its free API returns a company's registered address, status, SIC codes (what industry it is in), officers (directors), filing history and parent companies.

> **Think of it like this:** A UK company's birth certificate, CV and family tree in one place.

**UK angle:** When a UK victim appears on a ransomware leak site, Companies House tells you its sector, size and group structure. That lets you warn clients in the same sector or supply chain.

**Enrichment tip:** Map SIC codes to your sectors. For example 86xxx = human health, 64xxx = financial services, 69xxx = legal and accounting. Tag victims and clients the same way so matches are automatic.

**Try it today:** Search a UK company from today's ransomware list at find-and-update.company-information.service.gov.uk and note its SIC code.

**Quiz:** What does a SIC code tell you about a company?  
_Answer:_ Its industry or type of business activity.

**Word of the day: PIR** · Priority Intelligence Requirement. One of the key questions a client needs answered.

### Review (spaced repetition)

- **Priority Intelligence Requirements (PIRs)** (1d ago): Why do PIRs make enrichment faster? _Answer: They tell you which context matters, so you only enrich what answers the client's questions._
- **The PHIA probability yardstick** (3d ago): Which yardstick term covers roughly 55-75%? _Answer: Likely (or probable)._
- **The NCSC and what it gives you for free** (7d ago): Which UK intelligence agency is the NCSC part of? _Answer: GCHQ._

### Enrichment drill: IHG Hotels & Resorts (Estate) listed by BYOD ransomware

1. Search Companies House for 'IHG Hotels & Resorts (Estate)'. Note its SIC code, size and registered region.
2. Look up BYOD on ransomware.live. How many UK victims has it listed this year?
3. Search 'BYOD initial access' to find how they usually break in (ATT&CK tactic TA0001).
4. Which of your clients share this sector or region? Write a two-line BLUF heads-up for them.
5. Grade your sources with the Admiralty Code, for example C3 for a leak-site claim.

---
Sources healthy: 14/17 (failed: ICO enforcement (UK regulator), URLhaus, ThreatFox)
