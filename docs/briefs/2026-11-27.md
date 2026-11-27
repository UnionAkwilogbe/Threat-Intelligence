# Threat Intel Field Brief: Friday 27 November 2026

_TLP:CLEAR · generated 09:54 UK time · last 36 hours_

## Your morning in 30 seconds

- Read first: Critical Juniper Session Smart Conductor Flaw Exploited in Attacks (priority 48).
- 15 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 4 stories with strong UK relevance.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [Critical Juniper Session Smart Conductor Flaw Exploited in Attacks](https://www.securityweek.com/critical-juniper-session-smart-conductor-flaw-exploited-in-attacks/)
**Priority 48** · SecurityWeek · KEV · EPSS 2% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 2. [Drupal Warns of New Highly Critical Site Takeover Vulnerability Under Active Exploitation](https://thehackernews.com/2026/11/drupal-warns-of-new-highly-critical.html)
**Priority 45** · The Hacker News · KEV · EPSS 11% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 3. [Hackers Exploit 10 Vulnerabilities Across Mitel, Juniper, Vates, and Danfoss Products](https://thehackernews.com/2026/11/hackers-exploit-10-vulnerabilities.html)
**Priority 43** · The Hacker News · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 4. [CVE-2026-133469: Vates Xen Orchestra Improper Validation of Specified Type of Input Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-133469)
**Priority 41** · CISA KEV · KEV · EPSS 32% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-28): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 5. [CVE-2026-133968: Project MONAI MONAI Label Path Traversal Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-133968)
**Priority 40** · CISA KEV · KEV · EPSS 27% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-26): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 6. [UK Home Office waved through border system without a working fix for bad data](https://www.theregister.com/security/2026/11/26/uk-home-office-waved-through-border-system-without-a-working-fix-for-bad-data/5312162)
**Priority 36** · The Register Security · UK relevant

**In plain English:** General security news worth knowing.

**Do this:** Skim it and note whether any client uses the vendor or product mentioned.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

### 7. [CVE-2025-41450: Danfoss AK-SM 800A Series Improper Authentication Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2025-41450)
**Priority 36** · CISA KEV · KEV · EPSS 4% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-12-09): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 8. [CVE-2026-133323: Mitel MiCollab OS Command Injection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-133323)
**Priority 36** · CISA KEV · KEV · EPSS 6% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-28): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

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
- Matching stories today: 1
- New CVEs not yet covered: none
- Indicator feeds unavailable today

## Daily knowledge pack

### Lesson 331: What is data enrichment?

Enrichment means taking a bare fact (an IP address, a domain, a CVE number) and adding context until someone can make a decision with it. A raw IP tells you nothing. An IP that belongs to a bulletproof hosting company, was seen yesterday running a known ransomware C2 server, and talked to your client's firewall at 3am tells you to act.

> **Think of it like this:** A raw indicator is a car number plate. Enrichment is running the plate: owner, insurance, where it was last seen, whether it is reported stolen.

**UK angle:** UK clients mostly want three answers: does this affect us, how bad is it, and what do we do. Every enrichment step should move you closer to one of those answers.

**Enrichment tip:** Use a fixed checklist per indicator type so every analyst adds the same fields: who owns it, where it is, how bad it is, when it was seen, who else reported it.

**Try it today:** Pick one IP from today's brief. Write down five facts about it using RIPEstat (stat.ripe.net) and AbuseIPDB. That is enrichment.

**Quiz:** In one sentence, what is the goal of enrichment?  
_Answer:_ To add enough context to a raw indicator that someone can make a decision with it.

**Word of the day: Defanging** · Changing an indicator so it cannot be clicked by accident, for example evil[.]com or hxxp://.

### Review (spaced repetition)

- **Critical national infrastructure and NIS** (1d ago): What is the NCSC framework used to assess many NIS-regulated organisations? _Answer: The Cyber Assessment Framework (CAF)._
- **Evaluating feeds** (3d ago): Name three criteria for evaluating a threat feed. _Answer: Any three of: relevance, timeliness, accuracy, completeness, uniqueness._
- **Help desk social engineering** (7d ago): What does the attacker usually ask the help desk for? _Answer: A password reset or to register a new MFA device._

### Enrichment drill: Critical Juniper Session Smart Conductor Flaw Exploited in Attacks

1. Open nvd.nist.gov/vuln/detail/CVE-2026-103406. Note the CVSS score and affected product.
2. Check CVE-2026-103406 on the CISA KEV list and its EPSS score at first.org/epss. Severity vs likelihood vs reality?
3. Find the vendor's own advisory. Is there a patch or only a workaround?
4. Search Shodan or Censys for the product with country:GB. How exposed is the UK?
5. Write a BLUF: which clients, what action, by when (Cyber Essentials allows 14 days, KEV says sooner).

---
Sources healthy: 14/17 (failed: ICO enforcement (UK regulator), URLhaus, ThreatFox)
