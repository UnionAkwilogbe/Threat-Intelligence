# Threat Intel Field Brief: Monday 26 October 2026

_TLP:CLEAR · generated 11:13 UK time · last 72 hours_

## Your morning in 30 seconds

- Read first: Castle Howard Estate listed by qilin ransomware (priority 61).
- 8 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 1 UK organisations named on ransomware leak sites (sectors: Hospitality).
- 2 stories with strong UK relevance.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [Castle Howard Estate listed by qilin ransomware](https://www.ransomware.live/id/Q2FzdGxlIEhvd2FyZCBFc3RhdGVAcWlsaW4=)
**Priority 61** · ransomware.live · UK relevant · _Ransomware, Hospitality_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 2. [PHP2Shell security flaws now sucessfully exploited in the wild](https://www.bleepingcomputer.com/news/security/php2shell-security-flaws-now-sucessfully-exploited-in-the-wild/)
**Priority 45** · BleepingComputer · EPSS 100% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** Treat as patch-now: check the CISA KEV due date and the EPSS score. Search client external attack surface for the affected product and version.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 3. [CISA Flags Two Actively Exploited Critical Flaws in Collabora Online and Arista VeloCloud](https://thehackernews.com/2026/10/cisa-flags-two-actively-exploited.html)
**Priority 40** · The Hacker News · KEV · EPSS 12% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 4. [CVE-2026-106931: EG Secure Solutions SiteGuard Server Edition OS Command Injection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-106931)
**Priority 36** · CISA KEV · KEV · EPSS 3% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-23): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 5. [CVE-2026-114625: Arista VeloCloud Orchestrator SQL Injection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-114625)
**Priority 35** · CISA KEV · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-26): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 6. [CVE-2026-96656: Plex Media Server External Control of File Name or Path Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-96656)
**Priority 35** · CISA KEV · KEV · EPSS 2% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-23): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 7. [CVE-2026-110936: Siemens Software Center Uncontrolled Search Path Element Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-110936)
**Priority 35** · CISA KEV · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-03): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 8. [PHP Publishes Mitigation Advice for New RCE Flaw](https://www.infosecurity-magazine.com/news/php-publishes-mitigation-advice/)
**Priority 30** · Infosecurity Magazine

**In plain English:** General security news worth knowing.

**Do this:** Skim it and note whether any client uses the vendor or product mentioned.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

## Client request RFI-002: PHP2Shell: critical PHP flaws (CVE-2026-109618, CVE-2026-109619) (Client B)

**Status:** In progress, re-checked today.

**Bottom line:** Two critical PHP bugs let an unauthenticated attacker run code on a web server. Fixes shipped on 21 October, details leaked a day earlier, and vendors report attacks already under way. Patch every internet-facing PHP system now, then check it was not compromised before the patch.

- On CISA KEV today: none
- Matching stories today: 5
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

### Lesson 299: The Pyramid of Pain

David Bianco's Pyramid of Pain ranks indicators by how much it hurts the attacker when you block them. Bottom to top: hash values (trivial to change), IP addresses (easy), domain names (simple), network and host artefacts (annoying), tools (challenging), TTPs: tactics, techniques and procedures (tough).

> **Think of it like this:** Blocking a hash is like confiscating a burglar's gloves. Blocking a TTP is like making every window in the street burglar-proof.

**UK angle:** Many UK SMEs only receive IP and hash blocklists. Enrichment that climbs the pyramid (which tool, which technique) gives them protection that lasts longer than a day.

**Enrichment tip:** For every hash or IP you share, try to add the tool name and the ATT&CK technique. That moves your intel up the pyramid.

**Try it today:** Take one malware story from the brief and write down: one hash, one domain, one tool name, one technique. Label each with its pyramid level.

**Quiz:** Which is harder for an attacker to change: an IP address or a technique (TTP)?  
_Answer:_ A technique. TTPs sit at the top of the pyramid because changing them means changing how the attacker works.

**Word of the day: Initial access** · The first foothold an attacker gets inside a network, for example through phishing or a vulnerable VPN.

### Review (spaced repetition)

- **What is data enrichment?** (1d ago): In one sentence, what is the goal of enrichment? _Answer: To add enough context to a raw indicator that someone can make a decision with it._
- **Building a UK relevance score** (3d ago): Why should a relevance score be explainable? _Answer: So analysts and clients can trust it, challenge it and tune it._
- **Typosquatting and brand monitoring** (7d ago): Why does an MX record on a lookalike domain matter? _Answer: It means the domain can handle email, so it can be used for phishing or invoice fraud._

### Enrichment drill: Castle Howard Estate listed by qilin ransomware

1. Search Companies House for 'Castle Howard Estate'. Note its SIC code, size and registered region.
2. Look up qilin on ransomware.live. How many UK victims has it listed this year?
3. Search 'qilin initial access' to find how they usually break in (ATT&CK tactic TA0001).
4. Which of your clients share this sector or region? Write a two-line BLUF heads-up for them.
5. Grade your sources with the Admiralty Code, for example C3 for a leak-site claim.

---
Sources healthy: 13/17 (failed: ICO enforcement (UK regulator), The Register Security, URLhaus, ThreatFox)
