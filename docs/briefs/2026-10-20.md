# Threat Intel Field Brief: Tuesday 20 October 2026

_TLP:CLEAR · generated 11:09 UK time · last 36 hours_

## Your morning in 30 seconds

- Read first: Johnson & Pace listed by qilin ransomware (priority 66).
- 7 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 1 UK organisations named on ransomware leak sites (sectors: Not Found).
- 4 stories with strong UK relevance.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [Johnson & Pace listed by qilin ransomware](https://www.ransomware.live/id/Sm9obnNvbiAmIFBhY2VAcWlsaW4=)
**Priority 66** · ransomware.live · UK relevant · _Ransomware, Not Found_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 2. [Introducing a new AI chapter in the NCSC research problem book](https://www.ncsc.gov.uk/blogs/introducing-new-ai-chapter-ncsc-research-problem-book)
**Priority 46** · NCSC UK · UK relevant

**In plain English:** General security news worth knowing.

**Do this:** Skim it and note whether any client uses the vendor or product mentioned.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

### 3. [UK finance watchdog wants firms to report AI failures and close calls](https://www.theregister.com/ai-and-ml/2026/10/20/uk-finance-watchdog-wants-firms-to-report-ai-failures-and-close-calls/5304078)
**Priority 45** · The Register Security · UK relevant · _Finance_

**In plain English:** General security news worth knowing.

**Do this:** Skim it and note whether any client uses the vendor or product mentioned.

**Enrich next:** Sector (Finance) → tag every client in that sector and send them a short heads-up

### 4. [Why cyber resilience is now a boardroom priority for UK public services](https://www.theregister.com/security/2026/10/20/partner-content-why-cyber-resilience-is-now-a-boardroom-priority-for-uk-public-services/5301601)
**Priority 38** · The Register Security · UK relevant

**In plain English:** General security news worth knowing.

**Do this:** Skim it and note whether any client uses the vendor or product mentioned.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

### 5. [CVE-2026-105134: Ahsay AhsayCBS Command Injection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-105134)
**Priority 36** · CISA KEV · KEV · EPSS 5% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-17): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 6. [CVE-2026-102764: BeyondTrust Remote Support Authentication Bypass by Spoofing Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-102764)
**Priority 35** · CISA KEV · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-19): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 7. [CVE-2025-61624: Fortinet Multiple Products Path Traversal Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2025-61624)
**Priority 35** · CISA KEV · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-19): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 8. [CVE-2026-21589: Atlassian Multiple Products Files or Directories Accessible to External Parties Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-21589)
**Priority 35** · CISA KEV · KEV · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-18): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

## Client request RFI-001: Okta vulnerabilities (Client A)

**Status:** In progress, re-checked today.

**Bottom line:** No Okta or Auth0 vulnerability is known to be exploited. The real risk to Okta customers is social engineering: phone-call phishing (vishing) that tricks staff or the help desk into handing over sign-ins and MFA.

- On CISA KEV today: none
- Matching stories today: 0
- New CVEs not yet covered: none
- Themed indicators in today's malware feeds: 1 (e.g. hxxps://raw[.]githubusercontent[.]com/fdaloiapp/okta-terraform-demo-template/HEAD/scripts/archive/okta-terraform-demo-template-grossularia[.]zip)

## Daily knowledge pack

### Lesson 293: Writing for clients: BLUF

BLUF means Bottom Line Up Front. Start with the conclusion and the action, then give the detail. Busy readers stop after the first two lines, so those lines must carry the message.

> **Think of it like this:** A news headline and first paragraph tell you the whole story. The rest is for people who want more.

**UK angle:** UK client boards and service desks both want: what happened, does it affect us, what do we do, by when.

**Enrichment tip:** Your enrichment should end in a BLUF line: 'Action: patch FortiOS on the two internet-facing firewalls today. KEV-listed, EPSS 94%.'

**Try it today:** Write a two-line BLUF for today's number one story.

**Quiz:** What does BLUF stand for?  
_Answer:_ Bottom Line Up Front.

**Word of the day: Enrichment** · Adding context to raw data (owner, location, reputation, history) so people can decide what to do.

### Review (spaced repetition)

- **Typosquatting and brand monitoring** (1d ago): Why does an MX record on a lookalike domain matter? _Answer: It means the domain can handle email, so it can be used for phishing or invoice fraud._
- **Infostealers and stolen sessions** (3d ago): Why can a stolen session cookie bypass MFA? _Answer: It proves a login that already passed MFA, so the attacker does not have to log in again._
- **Matching threats to client assets** (7d ago): What does a CPE name identify? _Answer: A specific vendor and product (and optionally version) so vulnerabilities can be matched to it._

### Enrichment drill: Johnson & Pace listed by qilin ransomware

1. Search Companies House for 'Johnson & Pace'. Note its SIC code, size and registered region.
2. Look up qilin on ransomware.live. How many UK victims has it listed this year?
3. Search 'qilin initial access' to find how they usually break in (ATT&CK tactic TA0001).
4. Which of your clients share this sector or region? Write a two-line BLUF heads-up for them.
5. Grade your sources with the Admiralty Code, for example C3 for a leak-site claim.

---
Sources healthy: 16/17 (failed: ICO enforcement (UK regulator))
