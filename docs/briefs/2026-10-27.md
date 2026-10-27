# Threat Intel Field Brief: Tuesday 27 October 2026

_TLP:CLEAR · generated 09:57 UK time · last 36 hours_

## Your morning in 30 seconds

- Read first: CISA Confirms Active Exploitation of Two PHP2Shell Flaws Enabling Remote Code Execution (priority 70).
- 4 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 2 UK organisations named on ransomware leak sites (sectors: Financial Services, Manufacturing).
- 6 stories with strong UK relevance.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [CISA Confirms Active Exploitation of Two PHP2Shell Flaws Enabling Remote Code Execution](https://thehackernews.com/2026/10/cisa-confirms-active-exploitation-of.html)
**Priority 70** · The Hacker News · KEV · EPSS 100% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 2. [Bangor Wholesale Laminates listed by qilin ransomware](https://www.ransomware.live/id/QmFuZ29yIFdob2xlc2FsZSBMYW1pbmF0ZXNAcWlsaW4=)
**Priority 66** · ransomware.live · UK relevant · _Ransomware, Charity, Manufacturing_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 3. [Power Funding listed by qilin ransomware](https://www.ransomware.live/id/UG93ZXIgRnVuZGluZ0BxaWxpbg==)
**Priority 66** · ransomware.live · UK relevant · _Ransomware, Financial Services_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 4. [PHP2Shell security flaws now sucessfully exploited in the wild](https://www.bleepingcomputer.com/news/security/php2shell-security-flaws-now-sucessfully-exploited-in-the-wild/)
**Priority 66** · BleepingComputer · KEV · EPSS 100% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 5. [From industry concern to practical action: the value of working with regulators](https://www.ncsc.gov.uk/blogs/industry-concern-practical-action-value-working-regulators)
**Priority 53** · NCSC UK · UK relevant · _Finance_

**In plain English:** General security news worth knowing.

**Do this:** Skim it and note whether any client uses the vendor or product mentioned.

**Enrich next:** Sector (Finance) → tag every client in that sector and send them a short heads-up

### 6. [Britain bets big on AI to defend against the threats AI is helping create](https://www.theregister.com/security/2026/10/26/britain-bets-big-on-ai-to-defend-against-the-threats-ai-is-helping-create/5305319)
**Priority 38** · The Register Security · UK relevant

**In plain English:** General security news worth knowing.

**Do this:** Skim it and note whether any client uses the vendor or product mentioned.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

### 7. [CVE-2026-110447: Collabora Online – Built-in CODE Server OS Command Injection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-110447)
**Priority 37** · CISA KEV · KEV · EPSS 12% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-26): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 8. [CVE-2026-114625: Arista VeloCloud Orchestrator SQL Injection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-114625)
**Priority 35** · CISA KEV · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-26): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

## Client request RFI-002: PHP2Shell: critical PHP flaws (CVE-2026-109618, CVE-2026-109619) (Client B)

**Status:** In progress, re-checked today.

**Bottom line:** Two critical PHP bugs let an unauthenticated attacker run code on a web server. They are now confirmed exploited and on CISA's Known Exploited Vulnerabilities list (added 26 October). Patch every internet-facing PHP system now, then check it was not compromised from 17 October onwards.

- On CISA KEV today: CVE-2026-109618, CVE-2026-109619
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

### Lesson 300: CVSS vs EPSS vs KEV

CVSS (0-10) says how bad a bug could be if exploited. EPSS (0-1, from FIRST.org) estimates the chance it will be exploited in the next 30 days. KEV (CISA's Known Exploited Vulnerabilities list) says it is already being exploited. Severity, likelihood, reality.

> **Think of it like this:** CVSS is how deep the river is. EPSS is the chance it floods this month. KEV is: it is flooding now.

**UK angle:** Cyber Essentials requires critical and high-risk updates to be applied within 14 days. Using KEV and EPSS helps clients decide which of those to do on day one rather than day fourteen.

**Enrichment tip:** Never send a CVE to a client with only a CVSS score. Always add EPSS percentile and KEV status, plus whether they run the product.

**Try it today:** Look at the vulnerability table in today's brief. Find the CVE with the highest EPSS. Is it on KEV? What product is it?

**Quiz:** Which of the three tells you a vulnerability is already being used in real attacks?  
_Answer:_ KEV. CVSS is severity and EPSS is predicted likelihood.

**Word of the day: Infostealer** · Malware that steals saved passwords, cookies and session tokens from a computer.

### Review (spaced repetition)

- **The Pyramid of Pain** (1d ago): Which is harder for an attacker to change: an IP address or a technique (TTP)? _Answer: A technique. TTPs sit at the top of the pyramid because changing them means changing how the attacker works._
- **Critical national infrastructure and NIS** (3d ago): What is the NCSC framework used to assess many NIS-regulated organisations? _Answer: The Cyber Assessment Framework (CAF)._
- **Writing for clients: BLUF** (7d ago): What does BLUF stand for? _Answer: Bottom Line Up Front._

### Enrichment drill: CISA Confirms Active Exploitation of Two PHP2Shell Flaws Enabling Remote Code Execution

1. Open nvd.nist.gov/vuln/detail/CVE-2026-109618. Note the CVSS score and affected product.
2. Check CVE-2026-109618 on the CISA KEV list and its EPSS score at first.org/epss. Severity vs likelihood vs reality?
3. Find the vendor's own advisory. Is there a patch or only a workaround?
4. Search Shodan or Censys for the product with country:GB. How exposed is the UK?
5. Write a BLUF: which clients, what action, by when (Cyber Essentials allows 14 days, KEV says sooner).

---
Sources healthy: 14/17 (failed: ICO enforcement (UK regulator), URLhaus, ThreatFox)
