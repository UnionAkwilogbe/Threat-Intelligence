# Threat Intel Field Brief: Friday 13 November 2026

_TLP:CLEAR · generated 09:53 UK time · last 36 hours_

## Your morning in 30 seconds

- Read first: Exploit Attempts for GPUStack Authentication Bypass (CVE-2026-102895), (Thu, Nov 12th) (priority 48).
- 10 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 2 stories with strong UK relevance.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [Exploit Attempts for GPUStack Authentication Bypass (CVE-2026-102895), (Thu, Nov 12th)](https://isc.sans.edu/diary/rss/33514)
**Priority 48** · SANS Internet Storm Center · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 2. [SCKit Malware Turns ScreenConnect Support Sessions Into Potential MSP Attack Paths](https://thehackernews.com/2026/11/sckit-malware-targets-screenconnect.html)
**Priority 45** · The Hacker News · KEV · EPSS 1% · _Exploited vuln, Malware, Tech / MSP, Charity_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 3. [NCSC Launches Cyber Adversary Testing to Boost Resilience](https://www.infosecurity-magazine.com/news/ncsc-cyber-adversary-testing-boost/)
**Priority 43** · Infosecurity Magazine · UK relevant

**In plain English:** General security news worth knowing.

**Do this:** Skim it and note whether any client uses the vendor or product mentioned.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

### 4. [CVE-2026-123158: OpenBSD OpenSSH Unexpected Status Code or Return Value Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-123158)
**Priority 39** · CISA KEV · KEV · EPSS 19% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-12): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 5. [AI Set to Revolutionize Ransomware Following “Stagnant” Few Years](https://www.infosecurity-magazine.com/news/ai-revolutionize-ransomware/)
**Priority 37** · Infosecurity Magazine · _Ransomware_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

### 6. [CVE-2026-111560: Barracuda Networks Multiple Products OS Command Injection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-111560)
**Priority 37** · CISA KEV · KEV · EPSS 9% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-13): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 7. [CVE-2026-124194: Microsoft Office Outlook Missing User Interaction for Potentially Unsafe Action Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-124194)
**Priority 35** · CISA KEV · KEV · EPSS 2% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-24): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 8. [CVE-2026-111793: Openwave Messaging Limited Webtop Media Transcoder Incorrect Resource Transfer Between Spheres Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-111793)
**Priority 35** · CISA KEV · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-24): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

## Client request RFI-002: PHP2Shell: critical PHP flaws (CVE-2026-109618, CVE-2026-109619) (Client B)

**Status: needs update, new evidence today.**

**Bottom line:** Two critical PHP bugs let an unauthenticated attacker run code on a web server. They are now confirmed exploited and on CISA's Known Exploited Vulnerabilities list (added 26 October). Patch every internet-facing PHP system now, then check it was not compromised from 17 October onwards.

- On CISA KEV today: CVE-2026-109618, CVE-2026-109619
- Matching stories today: 2
- New CVEs not yet covered: CVE-2026-123039
- Indicator feeds unavailable today

## Client request RFI-001: Okta vulnerabilities (Client A)

**Status:** In progress, re-checked today.

**Bottom line:** No Okta or Auth0 vulnerability is known to be exploited. The real risk to Okta customers is social engineering: phone-call phishing (vishing) that tricks staff or the help desk into handing over sign-ins and MFA.

- On CISA KEV today: none
- Matching stories today: 0
- New CVEs not yet covered: none
- Indicator feeds unavailable today

## Daily knowledge pack

### Lesson 317: Indicators go stale: ageing and decay

IOCs lose value over time. An IP used for C2 today may be a clean cloud server next month. Hashes stay accurate forever but the attacker stops using them. Good intel records first-seen and last-seen dates and expires old indicators.

> **Think of it like this:** Like milk: great today, questionable next week, harmful next month if you keep blocking with it.

**UK angle:** Blocking a stale IP that now belongs to a UK cloud or CDN provider can break a client's business apps and destroy trust in your feed.

**Enrichment tip:** Add first_seen, last_seen and an expiry date to every IOC. A sensible default: IPs 30 days, domains 90 days, hashes much longer.

**Try it today:** Check the last_online date on one Feodo C2 entry in today's brief. Would you still block it?

**Quiz:** Why should IP indicators expire faster than hashes?  
_Answer:_ IPs get reassigned to new, often innocent, owners, while a hash always identifies the same file.

**Word of the day: TTP** · Tactics, Techniques and Procedures. How an attacker behaves.

### Review (spaced repetition)

- **STIX, TAXII and MISP** (1d ago): Which one is the format and which is the transport: STIX or TAXII? _Answer: STIX is the format. TAXII is the transport._
- **The Diamond Model** (3d ago): Name the four corners of the Diamond Model. _Answer: Adversary, Capability, Infrastructure, Victim._
- **.uk domains, Nominet and WHOIS** (7d ago): Why is domain age a useful enrichment field? _Answer: Newly registered domains are much more likely to be used for phishing or malware._

### Enrichment drill: Exploit Attempts for GPUStack Authentication Bypass (CVE-2026-102895), (Thu, Nov 12th)

1. Open nvd.nist.gov/vuln/detail/CVE-2026-102895. Note the CVSS score and affected product.
2. Check CVE-2026-102895 on the CISA KEV list and its EPSS score at first.org/epss. Severity vs likelihood vs reality?
3. Find the vendor's own advisory. Is there a patch or only a workaround?
4. Search Shodan or Censys for the product with country:GB. How exposed is the UK?
5. Write a BLUF: which clients, what action, by when (Cyber Essentials allows 14 days, KEV says sooner).

---
Sources healthy: 14/17 (failed: ICO enforcement (UK regulator), URLhaus, ThreatFox)
