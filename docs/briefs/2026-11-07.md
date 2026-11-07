# Threat Intel Field Brief: Saturday 07 November 2026

_TLP:CLEAR · generated 11:47 UK time · last 36 hours_

## Your morning in 30 seconds

- Read first: SonicWall Patches Exploited SonicOS Vulnerability That Weakens VPN Logins (priority 53).
- 3 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 3 stories with strong UK relevance.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [SonicWall Patches Exploited SonicOS Vulnerability That Weakens VPN Logins](https://www.securityweek.com/sonicwall-patches-exploited-sonicos-bug-that-weakens-vpn-logins/)
**Priority 53** · SecurityWeek · KEV · _Exploited vuln, Identity / MFA_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 2. [NHS breach helpline left staff carrying a 'significant emotional burden'](https://www.theregister.com/security/2026/11/07/nhs-breach-helpline-left-staff-carrying-a-significant-emotional-burden/5308201)
**Priority 39** · The Register Security · UK relevant · _Data breach, Health / NHS_

**In plain English:** Private data got out. Stolen data is later reused for scams and account takeover.

**Do this:** Check if client staff email domains appear in the leak (Have I Been Pwned domain search). Note the UK GDPR angle: serious breaches must be reported to the ICO within 72 hours.

**Enrich next:** Sector (Health / NHS) → tag every client in that sector and send them a short heads-up

### 3. [CVE-2024-27834: Apple Multiple Products Improper Authentication Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2024-27834)
**Priority 35** · CISA KEV · KEV · EPSS 2% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-18): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 4. [CVE-2026-119977: WordPress WordPress Core Time-of-check Time-of-use (TOCTOU) Race Condition Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-119977)
**Priority 35** · CISA KEV · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-06): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 5. [UK ministers seek powers to investigate when AI agents are let off the leash](https://www.theregister.com/ai-and-ml/2026/11/06/uk-ministers-seek-powers-to-investigate-when-ai-agents-are-let-off-the-leash/5307889)
**Priority 28** · The Register Security · UK relevant

**In plain English:** General security news worth knowing.

**Do this:** Skim it and note whether any client uses the vendor or product mentioned.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

### 6. [AI agents are a 'bane' for some website operators, says Cloudflare](https://www.theregister.com/networks/2026/11/06/ai-agents-are-a-bane-for-some-website-operators-says-cloudflare/5308022)
**Priority 27** · The Register Security · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** Treat as patch-now: check the CISA KEV due date and the EPSS score. Search client external attack surface for the affected product and version.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

### 7. [SonicWall warns of new SSL-VPN MFA bypass flaw exploited in attacks](https://www.bleepingcomputer.com/news/security/sonicwall-warns-of-new-ssl-vpn-mfa-bypass-flaw-exploited-in-attacks/)
**Priority 25** · BleepingComputer · _Exploited vuln, Identity / MFA_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** Treat as patch-now: check the CISA KEV due date and the EPSS score. Search client external attack surface for the affected product and version.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

### 8. [CVE-2026-123961: A security vulnerability has been detected in TOTOLINK CA300-PoE 6.2c.884. This impacts the function setWiFiBasicConfig of the file…](https://nvd.nist.gov/vuln/detail/CVE-2026-123961)
**Priority 24** · NVD

**In plain English:** General security news worth knowing.

**Do this:** Skim it and note whether any client uses the vendor or product mentioned.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

## Client request RFI-002: PHP2Shell: critical PHP flaws (CVE-2026-109618, CVE-2026-109619) (Client B)

**Status:** In progress, re-checked today.

**Bottom line:** Two critical PHP bugs let an unauthenticated attacker run code on a web server. They are now confirmed exploited and on CISA's Known Exploited Vulnerabilities list (added 26 October). Patch every internet-facing PHP system now, then check it was not compromised from 17 October onwards.

- On CISA KEV today: CVE-2026-109618, CVE-2026-109619
- Matching stories today: 1
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

### Lesson 311: Passive DNS and certificate transparency

Passive DNS is a history of which domains pointed to which IPs over time. Certificate transparency (crt.sh) logs every public TLS certificate issued. Together they let you pivot: from one bad domain to the IP, to other domains on that IP, to certificates with similar names.

> **Think of it like this:** Like checking who else has lived at a suspect's address over the years, and who else ordered the same custom number plate.

**UK angle:** Search crt.sh for your clients' brand names (for example %clientname%) to find lookalike sites issued certificates, often before a phishing campaign starts.

**Enrichment tip:** A pivot is only useful with a limit. Record why each pivot is linked (same IP, same certificate, same registrar) and stop after two or three hops.

**Try it today:** Search crt.sh for a UK brand name and see which subdomains and lookalikes appear.

**Quiz:** What is 'pivoting' in threat intel?  
_Answer:_ Using one known indicator to discover related indicators, for example from a domain to its IP to other domains on that IP.

**Word of the day: RaaS** · Ransomware as a Service. Gangs rent their ransomware to 'affiliates' who carry out attacks for a cut.

### Review (spaced repetition)

- **.uk domains, Nominet and WHOIS** (1d ago): Why is domain age a useful enrichment field? _Answer: Newly registered domains are much more likely to be used for phishing or malware._
- **Companies House as an enrichment source** (3d ago): What does a SIC code tell you about a company? _Answer: Its industry or type of business activity._
- **Traffic Light Protocol (TLP 2.0)** (7d ago): Which TLP label means 'share with anyone, publicly'? _Answer: TLP:CLEAR._

### Enrichment drill: SonicWall Patches Exploited SonicOS Vulnerability That Weakens VPN Logins

1. Open nvd.nist.gov/vuln/detail/CVE-2026-19868. Note the CVSS score and affected product.
2. Check CVE-2026-19868 on the CISA KEV list and its EPSS score at first.org/epss. Severity vs likelihood vs reality?
3. Find the vendor's own advisory. Is there a patch or only a workaround?
4. Search Shodan or Censys for the product with country:GB. How exposed is the UK?
5. Write a BLUF: which clients, what action, by when (Cyber Essentials allows 14 days, KEV says sooner).

---
Sources healthy: 14/17 (failed: ICO enforcement (UK regulator), URLhaus, ThreatFox)
