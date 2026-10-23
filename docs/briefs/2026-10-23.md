# Threat Intel Field Brief: Friday 23 October 2026

_TLP:CLEAR · generated 10:30 UK time · last 36 hours_

## Your morning in 30 seconds

- Read first: PWC listed by everest ransomware (priority 70).
- 6 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 1 UK organisations named on ransomware leak sites (sectors: Professional Services).
- 2 stories with strong UK relevance.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [PWC listed by everest ransomware](https://www.ransomware.live/id/UFdDQGV2ZXJlc3Q=)
**Priority 70** · ransomware.live · UK relevant · _Ransomware, Health / NHS, Finance_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 2. [UK threatens subsea cable saboteurs with 14 years behind bars](https://www.theregister.com/networks/2026/10/23/uk-threatens-subsea-cable-saboteurs-with-14-years-behind-bars/5304794)
**Priority 48** · The Register Security · UK relevant · _Nation-state / APT, Telecoms_

**In plain English:** Government-backed hackers, usually after secrets, access, or disruption rather than quick cash.

**Do this:** Map the reported techniques to MITRE ATT&CK and check client detections cover them. Check if the NCSC has issued a joint advisory with indicators to hunt for.

**Enrich next:** Sector (Telecoms) → tag every client in that sector and send them a short heads-up

### 3. [CVE-2026-106931: EG Secure Solutions SiteGuard Server Edition OS Command Injection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-106931)
**Priority 35** · CISA KEV · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-23): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 4. [CVE-2026-96656: Plex Media Server External Control of File Name or Path Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-96656)
**Priority 35** · CISA KEV · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-23): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 5. [CVE-2026-110936: Siemens Software Center Uncontrolled Search Path Element Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-110936)
**Priority 35** · CISA KEV · KEV · EPSS 0% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-03): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 6. [PHP2Shell puts dozens of UK government services out of service](https://www.theregister.com/security/2026/10/22/php2shell-puts-dozens-of-uk-government-services-out-of-service/5304840)
**Priority 33** · The Register Security · UK relevant · _Public sector_

**In plain English:** General security news worth knowing.

**Do this:** Skim it and note whether any client uses the vendor or product mentioned.

**Enrich next:** Sector (Public sector) → tag every client in that sector and send them a short heads-up

### 7. [Iranian Hacking Group Found Hosting C2 Infrastructure in the US](https://www.infosecurity-magazine.com/news/iranian-hacking-group-hosting-c2/)
**Priority 32** · Infosecurity Magazine · _Nation-state / APT, Malware_

**In plain English:** Government-backed hackers, usually after secrets, access, or disruption rather than quick cash.

**Do this:** Map the reported techniques to MITRE ATT&CK and check client detections cover them. Check if the NCSC has issued a joint advisory with indicators to hunt for.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

### 8. [PHP2Shell Exploitation Attempt Detected by Amazon Four Days Before Vulnerability Disclosure](https://www.infosecurity-magazine.com/news/php2shell-exploitation-attempt/)
**Priority 32** · Infosecurity Magazine · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** Treat as patch-now: check the CISA KEV due date and the EPSS score. Search client external attack surface for the affected product and version.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

## Client request RFI-002: PHP2Shell: critical PHP flaws (CVE-2026-109618, CVE-2026-109619) (Client B)

**Status:** In progress, re-checked today.

**Bottom line:** Two critical PHP bugs let an unauthenticated attacker run code on a web server. Fixes shipped on 21 October, details leaked a day earlier, and vendors report attacks already under way. Patch every internet-facing PHP system now, then check it was not compromised before the patch.

- On CISA KEV today: none
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

### Lesson 296: Building a UK relevance score

A relevance score combines simple signals into one number so you know what to read first. This dashboard adds points for UK keywords, UK sources, KEV status, EPSS, severity, threat type, freshness and corroboration. Every point is explained in the 'why' line.

> **Think of it like this:** A credit score for news stories: many small signals turned into one number you can sort by.

**UK angle:** Tune the weights to your clients: a legal-sector client should boost 'law firm' and 'solicitor'; a council client should boost 'council' and 'public sector'.

**Enrichment tip:** Keep scoring explainable. If a client asks 'why is this top?', you should be able to point to each factor.

**Try it today:** Open ti/enrich.py and find UK_TERMS. Add one keyword that matters to your clients.

**Quiz:** Why should a relevance score be explainable?  
_Answer:_ So analysts and clients can trust it, challenge it and tune it.

**Word of the day: Hash** · A fingerprint of a file, such as SHA-256. Change one byte and the hash changes completely.

### Review (spaced repetition)

- **Evaluating feeds** (1d ago): Name three criteria for evaluating a threat feed. _Answer: Any three of: relevance, timeliness, accuracy, completeness, uniqueness._
- **Writing for clients: BLUF** (3d ago): What does BLUF stand for? _Answer: Bottom Line Up Front._
- **Where UK victims report things** (7d ago): Where do UK users forward suspicious emails? _Answer: report@phishing.gov.uk._

### Enrichment drill: PWC listed by everest ransomware

1. Search Companies House for 'PWC'. Note its SIC code, size and registered region.
2. Look up everest on ransomware.live. How many UK victims has it listed this year?
3. Search 'everest initial access' to find how they usually break in (ATT&CK tactic TA0001).
4. Which of your clients share this sector or region? Write a two-line BLUF heads-up for them.
5. Grade your sources with the Admiralty Code, for example C3 for a leak-site claim.

---
Sources healthy: 14/17 (failed: ICO enforcement (UK regulator), URLhaus, ThreatFox)
