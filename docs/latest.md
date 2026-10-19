# Threat Intel Field Brief: Monday 19 October 2026

_TLP:CLEAR · generated 11:53 UK time · last 72 hours_

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

### 2. [CVE-2026-105134: Ahsay AhsayCBS Command Injection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-105134)
**Priority 36** · CISA KEV · KEV · EPSS 5% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-17): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 3. [CVE-2026-102764: BeyondTrust Remote Support Authentication Bypass by Spoofing Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-102764)
**Priority 35** · CISA KEV · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-19): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 4. [CVE-2025-61624: Fortinet Multiple Products Path Traversal Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2025-61624)
**Priority 35** · CISA KEV · KEV · EPSS 1% · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-19): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

**Enrich next:** CVE → EPSS + KEV + vendor advisory → which client assets run it (Shodan/Censys query filtered to country:GB)

### 5. [CVE-2026-21589: Atlassian Multiple Products Files or Directories Accessible to External Parties Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-21589)
**Priority 35** · CISA KEV · KEV · _Exploited vuln_

**In plain English:** Attackers are already using this weakness in real attacks, not just in theory.

**Do this:** On CISA KEV (US federal patch deadline 2026-10-18): patch or mitigate for UK clients now, do not wait. Treat as patch-now: check the CISA KEV due date and the EPSS score.

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

### Lesson 292: Typosquatting and brand monitoring

Typosquatting means registering lookalike domains: cl1ent.co.uk, client-login.com, client.co instead of client.co.uk. Tools like dnstwist generate the possible variants and check which ones are registered.

> **Think of it like this:** A fake shop on the high street with a logo almost identical to the real one.

**UK angle:** UK clients are often impersonated across .uk, .co.uk, .com and .org.uk. Monitoring all of these is cheap and catches phishing early.

**Enrichment tip:** For each lookalike: add creation date, whether it has MX records (can send or receive email), whether it has a live website, and certificate data from crt.sh.

**Try it today:** Run dnstwist (pip install dnstwist) against a UK brand domain and count the registered lookalikes.

**Quiz:** Why does an MX record on a lookalike domain matter?  
_Answer:_ It means the domain can handle email, so it can be used for phishing or invoice fraud.

**Word of the day: EDR** · Endpoint Detection and Response. Security software on laptops and servers that watches for attacker behaviour.

### Review (spaced repetition)

- **Help desk social engineering** (1d ago): What does the attacker usually ask the help desk for? _Answer: A password reset or to register a new MFA device._
- **Where UK victims report things** (3d ago): Where do UK users forward suspicious emails? _Answer: report@phishing.gov.uk._
- **False positives and allowlists** (7d ago): What is a MISP warninglist for? _Answer: Flagging indicators that are probably false positives, such as well-known legitimate services._

### Enrichment drill: CVE-2026-104935: Ivanti Connect Secure Authentication Bypass by Spoofing Vulnerability

1. Open nvd.nist.gov/vuln/detail/CVE-2026-104935. Note the CVSS score and affected product.
2. Check CVE-2026-104935 on the CISA KEV list and its EPSS score at first.org/epss. Severity vs likelihood vs reality?
3. Find the vendor's own advisory. Is there a patch or only a workaround?
4. Search Shodan or Censys for the product with country:GB. How exposed is the UK?
5. Write a BLUF: which clients, what action, by when (Cyber Essentials allows 14 days, KEV says sooner).

---
Sources healthy: 16/17 (failed: ICO enforcement (UK regulator))
