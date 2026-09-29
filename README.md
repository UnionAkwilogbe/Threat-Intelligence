# Threat Intel Field Brief

A daily cyber threat intelligence dashboard for people who look after **UK clients**.
Every morning it:

1. **Pulls** threats from public sources (government, researchers, news).
2. **Enriches** each one: adds the context that turns a headline into a decision.
3. **Ranks** everything by how much it matters to UK organisations (and to *your* clients).
4. **Briefs** you: a web dashboard, a short Markdown brief, and optionally an email.
5. **Teaches** you: a daily knowledge pack with a lesson, review quizzes, a word of the day and a hands-on drill.

## Your links

| What | Where |
|---|---|
| **Live dashboard** | https://unionakwilogbe.github.io/Threat-Intelligence/ |
| **How it works** (the logic, in plain English) | https://unionakwilogbe.github.io/Threat-Intelligence/how-it-works.html |
| Today's text brief | [`docs/latest.md`](docs/latest.md) |
| Past briefs | [`docs/briefs/`](docs/briefs/) |
| Run it now | Actions tab → *Daily threat intel brief* → *Run workflow* |

The site uses GitHub Pages: *Settings → Pages* should say *Deploy from a branch*, `main`, `/docs`.
(If it is set to `/ (root)` the link still works, it just redirects to `/docs`.)

No paid tools, no API keys needed to start, and no libraries to install (plain Python 3.11+).

---

## Explain it like I'm a rookie

**Threat intelligence** is information about who is attacking, how, and with what, so you can defend before it hits you.

**Data enrichment** is adding context. A raw clue like `203.0.113.45` means nothing on its own.
Enriched, it becomes: *"a botnet control server, hosted on a UK network, seen online yesterday, also reported by two other sources."* Now you can act.

This tool does the first layer of enrichment automatically and tells you which lookups to do next.

### What each score means

| Thing on the page | What it means | Why you care |
|---|---|---|
| **Priority (0-100)** | Read-this-first score. Red 60+, amber 35-59, green under 35 | Tells you where to spend your first 10 minutes |
| **UK relevant** | UK words, UK sources or UK victims were found | Filters out US-only noise |
| **KEV** | On the CISA list of bugs *already* being exploited | Patch now, not next month |
| **EPSS** | Chance (%) a bug gets exploited in the next 30 days | Helps choose which patches go first |
| **CVSS** | How bad a bug *could* be (0-10) | Severity, not likelihood |
| **Client: X** | Matches your client watchlist | This one is personal |
| **Why this score?** | The breakdown of every point | So you can explain it to a client |

---

## Where the data comes from

| Source | What it gives | UK? |
|---|---|---|
| NCSC UK | Official UK advisories and news | Yes |
| ICO | UK data protection enforcement and news | Yes |
| Computer Weekly, The Register, Infosecurity Magazine | UK-based security news | Yes |
| CISA KEV | Vulnerabilities attackers are actively using | |
| NVD | Newly published critical vulnerabilities | |
| FIRST EPSS | Exploitation likelihood for every CVE we see | |
| ransomware.live | Ransomware leak-site victims (we keep UK ones) | Filtered |
| Feodo Tracker (abuse.ch) | Live botnet control servers (we highlight UK-hosted ones) | Filtered |
| URLhaus (abuse.ch) | Web addresses spreading malware (we highlight .uk ones) | Filtered |
| ThreatFox (abuse.ch) | Fresh indicators of compromise | |
| BleepingComputer, The Record, The Hacker News, Krebs, SANS ISC, SecurityWeek, CISA advisories | Global news and research | |

If a source is down, the brief still builds. The **Source health** table at the bottom shows what worked.
Add or remove feeds in `ti/sources.py` (the `RSS_FEEDS` list).

---

## Setup (about 10 minutes, once)

The brief arrives **by email every morning**: a readable summary in the email, with the full
interactive dashboard attached as an `.html` file (tap it to open, works on a phone).
This works with a **private** repo. No GitHub Pages needed.

1. **Make a Gmail app password.** Google blocks your normal password for apps like this, so you create a special one.
   - Turn on 2-Step Verification: [myaccount.google.com/security](https://myaccount.google.com/security).
   - Then go to [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords), name it `threat brief`, and copy the 16-letter password.
2. **Add two secrets in GitHub.** Repo → *Settings → Secrets and variables → Actions → New repository secret*:
   - `SMTP_USER` = your Gmail address
   - `SMTP_PASSWORD` = the 16-letter app password (spaces are fine)

   The brief is sent from and to that address. To send it to someone else too, add `BRIEF_TO`
   (comma-separated addresses).
3. **Merge into `main`.** GitHub only runs scheduled workflows from the main branch.
4. **Test it now.** *Actions tab → Daily threat intel brief → Run workflow.* The email lands within a few minutes.
   After that it runs by itself every morning at about 06:17 UK time (05:17 in winter), and looks back 72 hours on Mondays to cover the weekend.
   If no email arrives, open the run in the Actions tab: a yellow warning explains what went wrong.
5. **(Optional) Better data.** A free `NVD_API_KEY` (from nvd.nist.gov) avoids NVD rate limits. A free `ABUSECH_AUTH_KEY` (from auth.abuse.ch) keeps abuse.ch feeds working if they require one.

Every brief is also saved in the repo under `docs/` (`docs/latest.md` is always today's), so you can read past ones on GitHub.

> **Want a web page instead?** GitHub Pages needs a public repo on the free plan. If you ever make the repo public:
> *Settings → Pages → Deploy from a branch → `main` / `/docs`*, then add a repository variable `DASHBOARD_URL`
> with the page address so the email links to it. Keep real client names out of a public repo (see below).

---

## Make it about your clients

Copy `clients.example.json` to `clients.json` and list each client's sector, key vendors/products, and keywords:

```json
{"clients": [
  {"name": "Client A", "sectors": ["Legal"], "vendors": ["Fortinet", "Citrix"], "keywords": ["law firm"]}
]}
```

**Private option (recommended):** instead of committing `clients.json`, paste its contents into a GitHub
secret called `CLIENTS_JSON`. The daily run uses it and the names never appear in the code.
(`clients.json` is in `.gitignore` so it is not committed by accident.)
Client tags do still show on the published dashboard, so use codenames if the dashboard is public.

Any story mentioning a client's vendor gets **+20 priority** and a **Client: A** tag. A sector match gets **+10**.
This is the single biggest step up in enrichment quality: the brief goes from "news" to "news about *your* estate".

Sector names you can use: `Health / NHS`, `Finance`, `Retail`, `Public sector`, `Education`, `Legal`,
`Manufacturing`, `Energy / Utilities`, `Telecoms`, `Tech / MSP`, `Charity`, `Transport / Logistics`.

---

## The daily knowledge pack

Every brief includes:

- **Lesson of the day**: 33 lessons on enrichment and UK threat intel (Pyramid of Pain, EPSS vs KEV, Admiralty Code, TLP, Companies House, RIPE, NCSC Early Warning, UK GDPR, and more). Each has a plain English explanation, an analogy, the UK angle, an enrichment tip, a try-it-today task and a quiz.
- **Review cards**: lessons from 1, 3 and 7 days ago come back as quizzes. This is *spaced repetition*: things return just as you would forget them. Repetition is on purpose.
- **Word of the day** from a 40-term glossary.
- **Enrichment drill**: a 15-minute guided exercise built from a real story in today's brief.

Add your own lessons to `ti/data/nuggets.json` and terms to `ti/data/glossary.json`.

---

## Run it on your own computer

```bash
python -m ti --demo          # sample data, no internet needed → writes demo_output/index.html
python -m ti                 # live feeds → docs/index.html and docs/briefs/<date>.md
python -m ti --hours 72      # look back further
python -m unittest discover -s tests   # run the tests
```

## How the code is organised

```
ti/sources.py    collectors: one small function per feed
ti/enrich.py     enrichment: CVEs, KEV, EPSS, IOCs, ATT&CK, UK score, sectors, client matching, priority
ti/nuggets.py    daily knowledge pack and drill
ti/render.py     dashboard HTML and Markdown brief
ti/notify.py     optional email
ti/data/         lessons and glossary (edit freely)
docs/            the published dashboard, daily briefs and JSON archive
tests/           tests and fictional sample data
```

## Ideas for next steps

- Add paid or keyed enrichment (VirusTotal, AbuseIPDB, Shodan, GreyNoise) in `ti/enrich.py`.
- Look up UK ransomware victims automatically in the Companies House API (free key) to add SIC codes.
- Export the day's indicators as STIX 2.1 for clients' tools, or push them into MISP.
