# Threat Intel Field Brief: Monday 02 November 2026

_TLP:CLEAR · generated 13:37 UK time · last 72 hours_

## Your morning in 30 seconds

- Read first: My Cloud Grocer listed by direwolf ransomware (priority 61).
- 8 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 2 UK organisations named on ransomware leak sites (sectors: Retail & E-Commerce, Transportation).
- 1 stories with strong UK relevance.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [My Cloud Grocer listed by direwolf ransomware](https://www.ransomware.live/id/TXkgQ2xvdWQgR3JvY2VyQGRpcmV3b2xm)
**Priority 61** · ransomware.live · UK relevant · _Ransomware, Retail & E-Commerce_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 2. [Palletline listed by qilin ransomware](https://www.ransomware.live/id/UGFsbGV0bGluZUBxaWxpbg==)
**Priority 56** · ransomware.live · UK relevant · _Ransomware, Transportation_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 3. [CVE-2026-46300: Linux Kernel Missing Initialization of a Variable Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-46300)
**Priority 55** · CISA KEV · KEV · EPSS 100% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-31): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 4. [Ivanti Patches Two More Zero-Days Exploited in Connect Secure Attack Chain](https://www.securityweek.com/ivanti-patches-two-more-zero-days-exploited-in-connect-secure-attack-chain/)
**Priority 53** · SecurityWeek · KEV · EPSS 1% · _Zero-day, Exploited vuln_

**In plain English:** A bug attackers found before the vendor could fix it, so there may be no patch yet.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Find out which clients run the product (asset inventory or Shodan/Censys search).

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 5. [CVE-2026-118527: Ivanti Connect Secure Generation of Predictable Numbers or Identifiers Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-118527)
**Priority 52** · CISA KEV · KEV · EPSS 87% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-13): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 6. [CVE-2026-111497: Google Brotli Unchecked Return Value Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-111497)
**Priority 52** · CISA KEV · KEV · EPSS 83% · _Exploited vuln, DDoS_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-10): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 7. [CVE-2026-48356: Adobe Commerce and Magento Unrestricted Upload of File with Dangerous Type Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-48356)
**Priority 44** · CISA KEV · KEV · EPSS 45% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-10): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 8. [CVE-2026-97229: GitLab Community Edition and Enterprise Edition Integer Overflow or Wraparound Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-97229)
**Priority 40** · CISA KEV · KEV · EPSS 27% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-01): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

## Client request RFI-002: PHP2Shell: critical PHP flaws (CVE-2026-109618, CVE-2026-109619) (Client B)

**Status: needs update, new evidence today.**

**Bottom line:** Two critical PHP bugs let an unauthenticated attacker run code on a web server. They are now confirmed exploited and on CISA's Known Exploited Vulnerabilities list (added 26 October). Patch every internet-facing PHP system now, then check it was not compromised from 17 October onwards.

- On CISA KEV today: CVE-2026-109618, CVE-2026-109619
- Matching stories today: 2
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

### Lesson 306: The intelligence cycle

Intel work runs in a loop: Direction (what do we need to know?), Collection (gather data), Processing (clean and structure it), Analysis (make sense of it), Dissemination (share it), Feedback (was it useful?). Then round again.

> **Think of it like this:** Like cooking for a client: ask what they want to eat, buy ingredients, prep them, cook, serve, and ask how it tasted.

**UK angle:** Most weak UK client intel programmes skip Direction and Feedback. They collect everything and ask nothing, so the output is noise.

**Enrichment tip:** Enrichment lives in Processing and Analysis. If you do not know the client's questions (Direction), you do not know which enrichment matters.

**Try it today:** Write down one question a client of yours would want answered every morning. That is a requirement.

**Quiz:** Which two stages of the cycle are most often skipped?  
_Answer:_ Direction (setting requirements) and Feedback.

**Word of the day: Passive DNS** · A historical record of which domains pointed to which IP addresses over time.

### Review (spaced repetition)

- **The PHIA probability yardstick** (1d ago): Which yardstick term covers roughly 55-75%? _Answer: Likely (or probable)._
- **The Admiralty Code: grading sources** (3d ago): In the grade 'B2', what does the B describe and what does the 2 describe? _Answer: B is source reliability (usually reliable). 2 is information credibility (probably true)._
- **The Pyramid of Pain** (7d ago): Which is harder for an attacker to change: an IP address or a technique (TTP)? _Answer: A technique. TTPs sit at the top of the pyramid because changing them means changing how the attacker works._

### Enrichment drill: My Cloud Grocer listed by direwolf ransomware

1. Search Companies House for 'My Cloud Grocer'. Note its SIC code, size and registered region.
2. Look up direwolf on ransomware.live. How many UK victims has it listed this year?
3. Search 'direwolf initial access' to find how they usually break in (ATT&CK tactic TA0001).
4. Which of your clients share this sector or region? Write a two-line BLUF heads-up for them.
5. Grade your sources with the Admiralty Code, for example C3 for a leak-site claim.

---
Sources healthy: 14/17 (failed: ICO enforcement (UK regulator), URLhaus, ThreatFox)
