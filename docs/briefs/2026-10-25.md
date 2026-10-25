# Threat Intel Field Brief: Sunday 25 October 2026

_TLP:CLEAR · generated 09:53 UK time · last 36 hours_

## Your morning in 30 seconds

- Read first: Castle Howard Estate listed by qilin ransomware (priority 66).
- 8 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 1 UK organisations named on ransomware leak sites (sectors: Hospitality).
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [Castle Howard Estate listed by qilin ransomware](https://www.ransomware.live/id/Q2FzdGxlIEhvd2FyZCBFc3RhdGVAcWlsaW4=)
**Priority 66** · ransomware.live · UK relevant · _Ransomware, Hospitality_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 2. [CISA Flags Two Actively Exploited Critical Flaws in Collabora Online and Arista VeloCloud](https://thehackernews.com/2026/10/cisa-flags-two-actively-exploited.html)
**Priority 43** · The Hacker News · KEV · EPSS 2% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 3. [CVE-2026-114625: Arista VeloCloud Orchestrator SQL Injection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-114625)
**Priority 35** · CISA KEV · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-26): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

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

### 7. [CVE-2026-115995: A security vulnerability has been detected in Unitree Robotics Unitree Go2 up to 1.1.11.4. The impacted element is the function set_volume…](https://nvd.nist.gov/vuln/detail/CVE-2026-115995)
**Priority 23** · NVD

**In plain English:** General security news worth knowing.

**Do this:** Skim it and note whether any client uses the vendor or product mentioned.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 8. [Autonomous attack agent in 'Skynet mode' hijacks other models to carry out its evil deeds](https://www.theregister.com/security/2026/10/24/autonomous-attack-agent-in-skynet-mode-hijacks-other-models-to-carry-out-its-evil-deeds/5305215)
**Priority 22** · The Register Security

**In plain English:** General security news worth knowing.

**Do this:** Skim it and note whether any client uses the vendor or product mentioned.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

## Client request RFI-002: PHP2Shell: critical PHP flaws (CVE-2026-109618, CVE-2026-109619) (Client B)

**Status:** In progress, re-checked today.

**Bottom line:** Two critical PHP bugs let an unauthenticated attacker run code on a web server. Fixes shipped on 21 October, details leaked a day earlier, and vendors report attacks already under way. Patch every internet-facing PHP system now, then check it was not compromised before the patch.

- On CISA KEV today: none
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

### Lesson 298: What is data enrichment?

Enrichment means taking a bare fact (an IP address, a domain, a CVE number) and adding context until someone can make a decision with it. A raw IP tells you nothing. An IP that belongs to a bulletproof hosting company, was seen yesterday running a known ransomware C2 server, and talked to your client's firewall at 3am tells you to act.

> **Think of it like this:** A raw indicator is a car number plate. Enrichment is running the plate: owner, insurance, where it was last seen, whether it is reported stolen.

**UK angle:** UK clients mostly want three answers: does this affect us, how bad is it, and what do we do. Every enrichment step should move you closer to one of those answers.

**Enrichment tip:** Use a fixed checklist per indicator type so every analyst adds the same fields: who owns it, where it is, how bad it is, when it was seen, who else reported it.

**Try it today:** Pick one IP from today's brief. Write down five facts about it using RIPEstat (stat.ripe.net) and AbuseIPDB. That is enrichment.

**Quiz:** In one sentence, what is the goal of enrichment?  
_Answer:_ To add enough context to a raw indicator that someone can make a decision with it.

**Word of the day: IOC** · Indicator of Compromise. A clue that something bad happened: a hash, IP, domain or URL.

### Review (spaced repetition)

- **Critical national infrastructure and NIS** (1d ago): What is the NCSC framework used to assess many NIS-regulated organisations? _Answer: The Cyber Assessment Framework (CAF)._
- **Evaluating feeds** (3d ago): Name three criteria for evaluating a threat feed. _Answer: Any three of: relevance, timeliness, accuracy, completeness, uniqueness._
- **Help desk social engineering** (7d ago): What does the attacker usually ask the help desk for? _Answer: A password reset or to register a new MFA device._

### Enrichment drill: Castle Howard Estate listed by qilin ransomware

1. Search Companies House for 'Castle Howard Estate'. Note its SIC code, size and registered region.
2. Look up qilin on ransomware.live. How many UK victims has it listed this year?
3. Search 'qilin initial access' to find how they usually break in (ATT&CK tactic TA0001).
4. Which of your clients share this sector or region? Write a two-line BLUF heads-up for them.
5. Grade your sources with the Admiralty Code, for example C3 for a leak-site claim.

---
Sources healthy: 14/17 (failed: ICO enforcement (UK regulator), URLhaus, ThreatFox)
