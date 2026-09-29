# Threat Intel Field Brief: Tuesday 29 September 2026

_TLP:CLEAR · generated 13:53 UK time · last 36 hours_

## Your morning in 30 seconds

- Read first: Precision Facades Ltd listed by N0n ransomware (priority 75).
- 7 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 3 UK organisations named on ransomware leak sites (sectors: Manufacturing, Technology).
- 2 stories with strong UK relevance.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [Precision Facades Ltd listed by N0n ransomware](https://www.ransomware.live/id/UHJlY2lzaW9uIEZhY2FkZXMgTHRkQE4wbg==)
**Priority 75** · ransomware.live · UK relevant · _Ransomware, Finance, Manufacturing_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 2. [safescaffolding.net listed by threeam ransomware](https://www.ransomware.live/id/c2FmZXNjYWZmb2xkaW5nLm5ldEB0aHJlZWFt)
**Priority 66** · ransomware.live · UK relevant · _Ransomware, Manufacturing_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Domain → WHOIS / Nominet for .uk, passive DNS, certificate transparency (crt.sh)

### 3. [Dediserve Ltd listed by N0n ransomware](https://www.ransomware.live/id/RGVkaXNlcnZlIEx0ZEBOMG4=)
**Priority 61** · ransomware.live · UK relevant · _Ransomware, Finance, Technology_

**In plain English:** Criminals lock (encrypt) or steal a company's files, then demand money.

**Do this:** Check whether any client shares the victim's sector, suppliers or software. Confirm clients have offline or immutable backups and have tested a restore.

**Enrich next:** Victim → Companies House (sector SIC code, size, directors) → which clients share suppliers or sector

### 4. [Exploitation of vulnerabilities affecting Citrix NetScaler ADC and Citrix NetScaler Gateway](https://www.ncsc.gov.uk/news/exploitation-of-vulnerabilities-affecting-citrix-netscaler-adc-and-citrix-netscaler-gateway)
**Priority 56** · NCSC UK · UK relevant · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** Treat as patch-now: check the CISA KEV due date and the EPSS score. Search client external attack surface for the affected product and version.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

### 5. [CISA Says Attackers Are Exploiting Two Critical Citrix NetScaler Flaws Globally](https://thehackernews.com/2026/09/cisa-says-attackers-are-exploiting-two.html)
**Priority 43** · The Hacker News · KEV · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV: patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 6. [Ukraine’s tech industry still stands strong](https://www.computerweekly.com/feature/Ukraines-tech-industry-still-stands-strong)
**Priority 38** · Computer Weekly Security · UK relevant

**In plain English:** General security news worth knowing.

**Do this:** Skim it and note whether any client uses the vendor or product mentioned.

**Enrich next:** Add a TLP label and an Admiralty rating (source reliability + credibility) before sharing

### 7. [CVE-2026-88772: Citrix NetScaler Citrix NetScaler Improper Restriction of Operations within the Bounds of a Memory Buffer Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-88772)
**Priority 35** · CISA KEV · KEV · _Exploited vuln, DDoS_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-09-30): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 8. [CVE-2026-67279: MikroTik RouterOS Mikrotik RouterOS Improper Enforcement of Behavioral Workflow Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-67279)
**Priority 35** · CISA KEV · KEV · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-09-28): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

## Daily knowledge pack

### Lesson 272: The PHIA probability yardstick

The UK Professional Head of Intelligence Assessment (PHIA) yardstick links words to probability ranges so 'likely' means the same thing to everyone. Roughly: remote chance (under 5%), highly unlikely (10-20%), unlikely (25-35%), realistic possibility (40-50%), likely (55-75%), highly likely (80-90%), almost certain (95% and above).

> **Think of it like this:** Like a weather forecast saying '70% chance of rain' instead of 'it might rain'. Everyone knows how seriously to take it.

**UK angle:** The NCSC and UK government assessments use this language. Using it in client reports makes your intel sound professional and makes it hard to misread.

**Enrichment tip:** After enriching a story, write one assessment sentence with a yardstick term, for example: 'It is likely (55-75%) that UK retailers will be targeted with this technique this quarter.'

**Try it today:** Rewrite one headline from today's brief as a PHIA-style assessment sentence.

**Quiz:** Which yardstick term covers roughly 55-75%?  
_Answer:_ Likely (or probable).

**Word of the day: SIC code** · Standard Industrial Classification. The UK code describing what business a company does.

### Review (spaced repetition)

- **Traffic Light Protocol (TLP 2.0)** (1d ago): Which TLP label means 'share with anyone, publicly'? _Answer: TLP:CLEAR._
- **NCSC Early Warning: free enrichment for UK clients** (3d ago): What two kinds of asset does an organisation register with Early Warning? _Answer: IP addresses and domain names._
- **What is data enrichment?** (7d ago): In one sentence, what is the goal of enrichment? _Answer: To add enough context to a raw indicator that someone can make a decision with it._

### Enrichment drill: Precision Facades Ltd listed by N0n ransomware

1. Search Companies House for 'Precision Facades Ltd'. Note its SIC code, size and registered region.
2. Look up N0n on ransomware.live. How many UK victims has it listed this year?
3. Search 'N0n initial access' to find how they usually break in (ATT&CK tactic TA0001).
4. Which of your clients share this sector or region? Write a two-line BLUF heads-up for them.
5. Grade your sources with the Admiralty Code, for example C3 for a leak-site claim.

---
Sources healthy: 16/17 (failed: ICO enforcement (UK regulator))
