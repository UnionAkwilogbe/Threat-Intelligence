# Threat Intel Field Brief: Tuesday 17 November 2026

_TLP:CLEAR · generated 10:01 UK time · last 36 hours_

## Your morning in 30 seconds

- Read first: Waterman Group listed by rhysida ransomware (priority 70).
- 2 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 3 UK organisations named on ransomware leak sites (sectors: Financial Services, Professional Services).
- 3 stories with strong UK relevance.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [Waterman Group listed by rhysida ransomware](https://www.ransomware.live/id/V2F0ZXJtYW4gR3JvdXBAcmh5c2lkYQ==)
**Priority 70** · ransomware.live · UK relevant · _Ransomware, Finance, Professional Services_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 2. [Burney Wealth listed by Shiba ransomware](https://www.ransomware.live/id/QnVybmV5IFdlYWx0aEBTaGliYQ==)
**Priority 66** · ransomware.live · UK relevant · _Ransomware, Finance, Financial Services_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 3. [Scans for LiteLLM/Starlette (CVE-2026-42271, CVE-2026-48710), (Mon, Nov 16th)](https://isc.sans.edu/diary/rss/33522)
**Priority 63** · SANS Internet Storm Center · KEV · EPSS 91% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 4. [CARRINGTON listed by Vortex ransomware](https://www.ransomware.live/id/Q0FSUklOR1RPTkBWb3J0ZXg=)
**Priority 61** · ransomware.live · UK relevant · _Ransomware, Financial Services_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 5. [Recent UnrealIRCd Vulnerability Exploited in Attacks](https://www.securityweek.com/recent-unrealircd-vulnerability-exploited-in-attacks/)
**Priority 48** · SecurityWeek · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 6. [King Charles opens new HQ for National Cyber Force, UK’s offensive hacking unit](https://therecord.media/uk-national-cyber-force-headquarters-opens)
**Priority 38** · The Record · UK relevant

**In plain English:** General security news worth knowing.

**Do this:** Skim it and note whether any client uses the vendor or product mentioned.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

### 7. [Why threat hunting should matter to every board](https://www.ncsc.gov.uk/blogs/why-threat-hunting-should-matter-to-every-board)
**Priority 35** · NCSC UK

**In plain English:** General security news worth knowing.

**Do this:** Skim it and note whether any client uses the vendor or product mentioned.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

### 8. [CVE-2026-123039: Check Point Multiple Products Incorrect Permission Assignment for Critical Resource Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-123039)
**Priority 35** · CISA KEV · KEV · EPSS 2% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-16): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

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
- Matching stories today: 0
- New CVEs not yet covered: none
- Indicator feeds unavailable today

## Daily knowledge pack

### Lesson 321: UK GDPR, the ICO and the 72-hour rule

UK GDPR and the Data Protection Act 2018 govern personal data in the UK. The Information Commissioner's Office (ICO) is the regulator. A personal data breach that poses a risk to people must be reported to the ICO within 72 hours of becoming aware of it.

> **Think of it like this:** Like reporting a car accident to your insurer: there is a deadline, and missing it makes things worse.

**UK angle:** When a UK breach hits the news, the regulatory angle (ICO report, possible fine) is often what gets a client's leadership to pay attention.

**Enrichment tip:** For breach stories, add a 'regulatory' field: ICO, FCA (finance), Ofcom (telecoms), NIS regulator (critical services). That shows clients who they might answer to.

**Try it today:** Look at the ICO news feed in today's brief. Is there an enforcement action? What went wrong?

**Quiz:** How long does a UK organisation have to report a qualifying personal data breach to the ICO?  
_Answer:_ 72 hours from becoming aware of it.

**Word of the day: APT** · Advanced Persistent Threat. A skilled, patient, usually government-backed hacking group.

### Review (spaced repetition)

- **Cyber Essentials** (1d ago): Name the five Cyber Essentials controls. _Answer: Firewalls, secure configuration, user access control, malware protection, security update management._
- **False positives and allowlists** (3d ago): What is a MISP warninglist for? _Answer: Flagging indicators that are probably false positives, such as well-known legitimate services._
- **The Diamond Model** (7d ago): Name the four corners of the Diamond Model. _Answer: Adversary, Capability, Infrastructure, Victim._

### Enrichment drill: Waterman Group listed by rhysida ransomware

1. Search Companies House for 'Waterman Group'. Note its SIC code, size and registered region.
2. Look up rhysida on ransomware.live. How many UK victims has it listed this year?
3. Search 'rhysida initial access' to find how they usually break in (ATT&CK tactic TA0001).
4. Which of your clients share this sector or region? Write a two-line BLUF heads-up for them.
5. Grade your sources with the Admiralty Code, for example C3 for a leak-site claim.

---
Sources healthy: 14/17 (failed: ICO enforcement (UK regulator), URLhaus, ThreatFox)
