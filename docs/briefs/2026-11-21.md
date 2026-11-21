# Threat Intel Field Brief: Saturday 21 November 2026

_TLP:CLEAR · generated 13:33 UK time · last 36 hours_

## Your morning in 30 seconds

- Read first: William Cook Holdings Limited listed by aurora ransomware (priority 70).
- 9 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 2 UK organisations named on ransomware leak sites (sectors: Manufacturing).
- 2 stories with strong UK relevance.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [William Cook Holdings Limited listed by aurora ransomware](https://www.ransomware.live/id/V2lsbGlhbSBDb29rIEhvbGRpbmdzIExpbWl0ZWRAYXVyb3Jh)
**Priority 70** · ransomware.live · UK relevant · _Ransomware, Manufacturing, Energy / Utilities_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 2. [SDJ Design Engineering Limited listed by spacebears ransomware](https://www.ransomware.live/id/U0RKIERlc2lnbiBFbmdpbmVlcmluZyBMaW1pdGVkQHNwYWNlYmVhcnM=)
**Priority 61** · ransomware.live · UK relevant · _Ransomware, Energy / Utilities, Manufacturing_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Domain → WHOIS / Nominet for .uk, passive DNS, certificate transparency (crt.sh)

### 3. [Hackers Exploit Critical VMware, Cisco, and Apache Flaws as Espionage Attacks Emerge](https://thehackernews.com/2026/11/hackers-exploit-critical-vmware-cisco.html)
**Priority 53** · The Hacker News · KEV · EPSS 1% · _Exploited vuln, Nation-state / APT_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 4. [CVE-2026-40217: BerriAI LiteLLM Unprotected Alternate Channel Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-40217)
**Priority 49** · CISA KEV · KEV · EPSS 69% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-12-02): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 5. [Hackers Exploit Critical Cisco Expressway Flaw, Breach Four Devices and Reach Internal Network](https://thehackernews.com/2026/11/hackers-exploit-critical-cisco.html)
**Priority 43** · The Hacker News · KEV · EPSS 0% · _Data breach, Exploited vuln, Nation-state / APT_

**In plain English:** Private data got out. Stolen data is later reused for scams and account takeover.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Check if client staff email domains appear in the leak (Have I Been Pwned domain search).

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 6. [China-Linked Hackers Exploit Critical VMware vCenter Zero-Day to Gain Admin Access and Steal Data](https://thehackernews.com/2026/11/china-linked-hackers-exploit-critical.html)
**Priority 43** · The Hacker News · KEV · EPSS 1% · _Zero-day, Exploited vuln, Nation-state / APT_

**In plain English:** A bug attackers found before the vendor could fix it, so there may be no patch yet.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Find out which clients run the product (asset inventory or Shodan/Censys search).

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 7. [CVE-2026-129448: Apache Roller Deserialization of Untrusted Data Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-129448)
**Priority 40** · CISA KEV · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-23): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 8. [CVE-2025-42884: SAP NetWeaver Improper Neutralization of Special Elements in Data Query Logic Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2025-42884)
**Priority 40** · CISA KEV · KEV · EPSS 0% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-23): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

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

### Lesson 325: Typosquatting and brand monitoring

Typosquatting means registering lookalike domains: cl1ent.co.uk, client-login.com, client.co instead of client.co.uk. Tools like dnstwist generate the possible variants and check which ones are registered.

> **Think of it like this:** A fake shop on the high street with a logo almost identical to the real one.

**UK angle:** UK clients are often impersonated across .uk, .co.uk, .com and .org.uk. Monitoring all of these is cheap and catches phishing early.

**Enrichment tip:** For each lookalike: add creation date, whether it has MX records (can send or receive email), whether it has a live website, and certificate data from crt.sh.

**Try it today:** Run dnstwist (pip install dnstwist) against a UK brand domain and count the registered lookalikes.

**Quiz:** Why does an MX record on a lookalike domain matter?  
_Answer:_ It means the domain can handle email, so it can be used for phishing or invoice fraud.

**Word of the day: C2** · Command and Control. The server an attacker uses to send orders to infected machines.

### Review (spaced repetition)

- **Help desk social engineering** (1d ago): What does the attacker usually ask the help desk for? _Answer: A password reset or to register a new MFA device._
- **Where UK victims report things** (3d ago): Where do UK users forward suspicious emails? _Answer: report@phishing.gov.uk._
- **False positives and allowlists** (7d ago): What is a MISP warninglist for? _Answer: Flagging indicators that are probably false positives, such as well-known legitimate services._

### Enrichment drill: William Cook Holdings Limited listed by aurora ransomware

1. Search Companies House for 'William Cook Holdings Limited'. Note its SIC code, size and registered region.
2. Look up aurora on ransomware.live. How many UK victims has it listed this year?
3. Search 'aurora initial access' to find how they usually break in (ATT&CK tactic TA0001).
4. Which of your clients share this sector or region? Write a two-line BLUF heads-up for them.
5. Grade your sources with the Admiralty Code, for example C3 for a leak-site claim.

---
Sources healthy: 14/17 (failed: ICO enforcement (UK regulator), URLhaus, ThreatFox)
