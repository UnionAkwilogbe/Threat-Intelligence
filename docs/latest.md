# Threat Intel Field Brief: Sunday 18 October 2026

_TLP:CLEAR · generated 10:41 UK time · last 36 hours_

## Your morning in 30 seconds

- Read first: CVE-2026-104935: Ivanti Connect Secure Authentication Bypass by Spoofing Vulnerability (priority 40).
- 9 vulnerabilities added to CISA KEV this week. Check clients run none of them.
- 1 botnet C2 servers tracked on UK networks. Block and hunt for them.

## Top 8 for your UK clients

### 1. [CVE-2026-104935: Ivanti Connect Secure Authentication Bypass by Spoofing Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-104935)
**Priority 40** · CISA KEV · KEV · EPSS 26% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-16): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 2. [CVE-2026-21589: Atlassian Multiple Products Files or Directories Accessible to External Parties Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-21589)
**Priority 38** · CISA KEV · KEV · EPSS 13% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-18): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 3. [CVE-2026-105134: Ahsay AhsayCBS Command Injection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-105134)
**Priority 36** · CISA KEV · KEV · EPSS 5% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-17): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 4. [CVE-2026-102764: BeyondTrust Remote Support Authentication Bypass by Spoofing Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-102764)
**Priority 35** · CISA KEV · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-19): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 5. [CVE-2025-61624: Fortinet Multiple Products Path Traversal Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2025-61624)
**Priority 35** · CISA KEV · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-19): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 6. [CVE-2026-76519: Cisco Secure Email Gateway Relative Path Traversal Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-76519)
**Priority 35** · CISA KEV · KEV · EPSS 2% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-17): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 7. [CVE-2026-0322: Palo Alto Networks PAN-OS Code Injection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-0322)
**Priority 35** · CISA KEV · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-17): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 8. [CVE-2026-96951: Microsoft Windows Command Injection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-96951)
**Priority 35** · CISA KEV · KEV · EPSS 2% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-16): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

## Client request RFI-001: Okta vulnerabilities (Client A)

**Status:** In progress, re-checked today.

**Bottom line:** No Okta or Auth0 vulnerability is known to be exploited. The real risk to Okta customers is social engineering: phone-call phishing (vishing) that tricks staff or the help desk into handing over sign-ins and MFA.

- On CISA KEV today: none
- Matching stories today: 0
- New CVEs not yet covered: none
- Themed indicators in today's malware feeds: 1 (e.g. hxxps://raw[.]githubusercontent[.]com/fdaloiapp/okta-terraform-demo-template/HEAD/scripts/archive/okta-terraform-demo-template-grossularia[.]zip)

## Daily knowledge pack

### Lesson 291: Help desk social engineering

Groups like Scattered Spider phone IT help desks pretending to be staff and ask for password or MFA resets. No malware needed: they talk their way in, then add their own devices and move to ransomware or data theft.

> **Think of it like this:** Ringing the hotel reception, claiming you lost your room key, and being handed a new one.

**UK angle:** Major UK retail attacks in 2025 were linked to this style of social engineering. It is a top concern for UK retail, finance and anyone with an outsourced help desk.

**Enrichment tip:** For identity attack stories, enrich with the targeted help desk provider or outsourcer. Clients sharing that supplier face higher risk.

**Try it today:** Write three questions a help desk should ask before resetting MFA.

**Quiz:** What does the attacker usually ask the help desk for?  
_Answer:_ A password reset or to register a new MFA device.

**Word of the day: Defanging** · Changing an indicator so it cannot be clicked by accident, for example evil[.]com or hxxp://.

### Review (spaced repetition)

- **Infostealers and stolen sessions** (1d ago): Why can a stolen session cookie bypass MFA? _Answer: It proves a login that already passed MFA, so the attacker does not have to log in again._
- **UK GDPR, the ICO and the 72-hour rule** (3d ago): How long does a UK organisation have to report a qualifying personal data breach to the ICO? _Answer: 72 hours from becoming aware of it._
- **Indicators go stale: ageing and decay** (7d ago): Why should IP indicators expire faster than hashes? _Answer: IPs get reassigned to new, often innocent, owners, while a hash always identifies the same file._

### Enrichment drill: CVE-2026-104935: Ivanti Connect Secure Authentication Bypass by Spoofing Vulnerability

1. Open nvd.nist.gov/vuln/detail/CVE-2026-104935. Note the CVSS score and affected product.
2. Check CVE-2026-104935 on the CISA KEV list and its EPSS score at first.org/epss. Severity vs likelihood vs reality?
3. Find the vendor's own advisory. Is there a patch or only a workaround?
4. Search Shodan or Censys for the product with country:GB. How exposed is the UK?
5. Write a BLUF: which clients, what action, by when (Cyber Essentials allows 14 days, KEV says sooner).

---
Sources healthy: 16/17 (failed: ICO enforcement (UK regulator))
