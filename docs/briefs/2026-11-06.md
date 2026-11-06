# Threat Intel Field Brief: Friday 06 November 2026

_TLP:CLEAR · generated 13:01 UK time · last 36 hours_

## Your morning in 30 seconds

- Read first: Vulnerability Scans for Older Cisco IOS Vulnerability / Opt-Out Headers, (Thu, Nov 5th) (priority 65).
- 2 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 3 stories with strong UK relevance.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [Vulnerability Scans for Older Cisco IOS Vulnerability / Opt-Out Headers, (Thu, Nov 5th)](https://isc.sans.edu/diary/rss/33492)
**Priority 65** · SANS Internet Storm Center · KEV · EPSS 100% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 2. [Hackers Exploit Patched Apple Flaw to Deliver Info-Stealing Malware, CISA Says](https://thehackernews.com/2026/11/hackers-exploit-patched-apple-flaw-to.html)
**Priority 43** · The Hacker News · KEV · EPSS 1% · _Exploited vuln, Malware_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 3. [UK ministers seek powers to investigate when AI agents are let off the leash](https://www.theregister.com/ai-and-ml/2026/11/06/uk-ministers-seek-powers-to-investigate-when-ai-agents-are-let-off-the-leash/5307889)
**Priority 38** · The Register Security · UK relevant

**In plain English:** General security news worth knowing.

**Do this:** Skim it and note whether any client uses the vendor or product mentioned.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

### 4. [AI agents are a 'bane' for some website operators, says Cloudflare](https://www.theregister.com/networks/2026/11/06/ai-agents-are-a-bane-for-some-website-operators-says-cloudflare/5308022)
**Priority 37** · The Register Security · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** Treat as patch-now: check the CISA KEV due date and the EPSS score. Search client external attack surface for the affected product and version.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

### 5. [CVE-2026-119977: WordPress WordPress Core Time-of-check Time-of-use (TOCTOU) Race Condition Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-119977)
**Priority 35** · CISA KEV · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-11-06): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 6. [Zurich uncovers £19m of fraud with Quantexa data analytics](https://www.computerweekly.com/news/366653717/Zurich-uncovers-19m-of-fraud-with-Quantexa-data-analytics)
**Priority 33** · Computer Weekly Security · UK relevant · _Fraud / Scam, Finance_

**In plain English:** Tricks aimed at stealing money, often by pretending to be a trusted brand or person.

**Do this:** Watch for lookalike domains of client brands (typosquats). UK victims report to Action Fraud (England, Wales, NI) or Police Scotland.

**Enrich next:** Sector (Finance) → tag every client in that sector and send them a short heads-up

### 7. [NATS Air Traffic Control Failure Cost UK Economy £33m](https://www.infosecurity-magazine.com/news/nats-air-traffic-control-fail-cost/)
**Priority 33** · Infosecurity Magazine · UK relevant

**In plain English:** General security news worth knowing.

**Do this:** Skim it and note whether any client uses the vendor or product mentioned.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

### 8. [ARTEX Offensive AI Tool Activity Far Exceeds Reported Campaigns, Censys Finds](https://www.infosecurity-magazine.com/news/artex-activity-exceeds-reported/)
**Priority 27** · Infosecurity Magazine

**In plain English:** General security news worth knowing.

**Do this:** Skim it and note whether any client uses the vendor or product mentioned.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

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

### Lesson 310: .uk domains, Nominet and WHOIS

Nominet runs the .uk domain registry. WHOIS shows registration data such as registrar, creation date and name servers. Since GDPR most personal details are hidden, but creation date, registrar and name servers are still very useful.

> **Think of it like this:** WHOIS is the land registry for domains: you may not see the owner's name, but you see when the plot was bought and who sold it.

**UK angle:** A lookalike .co.uk domain registered yesterday that imitates a client's brand is a strong phishing signal. New domain + brand name = high priority.

**Enrichment tip:** Add 'domain age in days' to every domain indicator. Domains under 30 days old deserve extra suspicion.

**Try it today:** Run a WHOIS lookup on any .co.uk domain and find its creation date and registrar.

**Quiz:** Why is domain age a useful enrichment field?  
_Answer:_ Newly registered domains are much more likely to be used for phishing or malware.

**Word of the day: Ransomware** · Malware that encrypts or steals data and demands payment.

### Review (spaced repetition)

- **IPs, ASNs and RIPE** (1d ago): Which regional registry covers UK IP addresses? _Answer: RIPE NCC._
- **Priority Intelligence Requirements (PIRs)** (3d ago): Why do PIRs make enrichment faster? _Answer: They tell you which context matters, so you only enrich what answers the client's questions._
- **The Admiralty Code: grading sources** (7d ago): In the grade 'B2', what does the B describe and what does the 2 describe? _Answer: B is source reliability (usually reliable). 2 is information credibility (probably true)._

### Enrichment drill: Vulnerability Scans for Older Cisco IOS Vulnerability / Opt-Out Headers, (Thu, Nov 5th)

1. Open nvd.nist.gov/vuln/detail/CVE-2023-20198. Note the CVSS score and affected product.
2. Check CVE-2023-20198 on the CISA KEV list and its EPSS score at first.org/epss. Severity vs likelihood vs reality?
3. Find the vendor's own advisory. Is there a patch or only a workaround?
4. Search Shodan or Censys for the product with country:GB. How exposed is the UK?
5. Write a BLUF: which clients, what action, by when (Cyber Essentials allows 14 days, KEV says sooner).

---
Sources healthy: 14/17 (failed: ICO enforcement (UK regulator), URLhaus, ThreatFox)
