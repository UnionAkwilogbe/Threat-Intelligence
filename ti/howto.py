"""The 'How it works' page: a plain English tour of the logic behind the brief.

Source lists, sectors and threat types are read straight from the code, so
this page stays accurate when you add feeds or keywords. If you change the
scoring in enrich.py, update SCORING below to match.
"""

from . import enrich, nuggets, sources
from .render import e, page

# Mirrors the points system in enrich.enrich_story(), dedupe() and match_clients().
SCORING = [
    ("UK relevance", "UK score × 0.35", "up to 35",
     "The UK score (0-100) starts at 35 for a UK source, or 90 for a UK ransomware victim, "
     "then adds points for UK words such as NHS (+35), NCSC (+30), UK (+30), London (+20), council (+10)."),
    ("Actively exploited (KEV)", "+25", "25", "A CVE in the story is on CISA's Known Exploited Vulnerabilities list."),
    ("EPSS", "EPSS × 20", "up to 20", "A 94% chance of exploitation adds 19 points."),
    ("CVSS", "(CVSS − 7) × 3", "up to 9", "Only for scores of 7 and above. A 9.8 adds 8 points."),
    ("Used by ransomware", "+10", "10", "CISA says ransomware gangs use this bug."),
    ("Serious threat type", "+10", "10", "Ransomware, zero-day, exploited bug, supply chain, or nation-state."),
    ("Official advisory", "+8", "8", "From an official advisory feed such as NCSC or CISA."),
    ("UK victim named", "+15", "15", "A UK organisation appeared on a ransomware leak site."),
    ("Fresh", "+15 / +10 / +5 / 0", "up to 15", "Under 12 hours old +15, under 24h +10, under 48h +5. No date +5."),
    ("Corroborated", "+3 per extra source", "up to 9", "Other outlets reported the same headline or the same CVE."),
    ("Matches your clients", "+20 or +10", "up to 20",
     "+20 when a client's vendor or keyword appears, +10 for a sector-only match."),
]


def _li(items):
    return "".join(f"<li>{x}</li>" for x in items)


def render_how(dashboard_url=""):
    feeds = "".join(
        f"<tr><td>{e(f['name'])}</td><td>{e(f['kind'])}</td><td>{'Yes' if f['uk'] else ''}</td></tr>"
        for f in sources.RSS_FEEDS)
    other = [
        ("CISA KEV", "Bugs attackers are exploiting now (looks back 7 days)"),
        ("NVD", "New critical bugs, CVSS 9.0 and above"),
        ("FIRST EPSS", "Chance of exploitation for every CVE the brief mentions"),
        ("ransomware.live", "Leak-site victims. Only UK victims become stories; the rest feed the gang league table"),
        ("Feodo Tracker", "Botnet control servers. UK-hosted ones are listed"),
        ("URLhaus", "Malware download links. .uk ones are listed"),
        ("ThreatFox", "Fresh indicators, counted by malware family"),
    ]
    other_rows = "".join(f"<tr><td>{e(n)}</td><td colspan='2'>{e(d)}</td></tr>" for n, d in other)
    scoring = "".join(
        f"<tr><td>{e(a)}</td><td class='mono'>{e(b)}</td><td class='num'>{e(c)}</td><td class='sub'>{e(d)}</td></tr>"
        for a, b, c, d in SCORING)
    playbook = "".join(f"<tr><td><b>{e(k)}</b></td><td>{e(v[0])}</td></tr>" for k, v in enrich.PLAYBOOK.items())
    sectors = ", ".join(e(s) for s in enrich.SECTORS)
    lessons = len(nuggets._load("nuggets.json"))
    words = len(nuggets._load("glossary.json"))
    step = ("<div style='flex:1 1 150px;border:1px solid var(--line);border-radius:10px;padding:12px'>"
            "<div class='sub'>Step {n}</div><b>{t}</b><div class='sub'>{d}</div></div>")
    flow = "".join(step.format(n=i, t=t, d=d) for i, (t, d) in enumerate([
        ("Collect", f"{len(sources.RSS_FEEDS) + len(other) - 1} public sources"),
        ("Clean", "Strip HTML, fix dates, drop old items, merge duplicates"),
        ("Enrich", "Add CVE, KEV, EPSS, IOCs, ATT&amp;CK, sectors, UK score"),
        ("Score", "Points system, 0 to 100, highest first"),
        ("Publish", "Web page, email, saved archive"),
    ], 1))
    link = (f"<a href='{e(dashboard_url)}'>{e(dashboard_url)}</a>" if dashboard_url
            else "<code>https://&lt;your-username&gt;.github.io/Threat-Intelligence/</code>")
    body = f"""
<section class="bluf"><h2>The short version</h2>
<p>Every morning a robot (a GitHub Action) wakes up, reads {len(sources.RSS_FEEDS) + 6} public threat sources, throws away old and duplicate items,
adds context to each story, gives it a score out of 100, and publishes the result here and to your email. Then it adds a daily lesson.</p>
<div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:12px">{flow}</div></section>

<section id="where"><h2>Where to find everything</h2>
<table><tbody>
<tr><td><b>Live dashboard</b></td><td>{link}<div class="sub">Bookmark it or add it to your phone's home screen. It updates each morning.</div></td></tr>
<tr><td><b>Email</b></td><td>The same brief arrives in your inbox, with the dashboard attached and a link back here.</td></tr>
<tr><td><b>Past briefs</b></td><td>Linked at the bottom of the dashboard, and saved in the repo under <code>docs/briefs/</code>.</td></tr>
<tr><td><b>Raw data</b></td><td><code>docs/data/&lt;date&gt;.json</code> holds every story with all its enrichment fields.</td></tr>
<tr><td><b>Run it now</b></td><td>GitHub repo → Actions tab → <i>Daily threat intel brief</i> → Run workflow.</td></tr>
</tbody></table></section>

<section id="when"><h2>When it runs</h2>
<ul>{_li([
    "Every day at 05:17 UTC. That is 06:17 UK time in summer (BST) and 05:17 in winter (GMT).",
    "Normally it looks back 36 hours, so nothing slips through the gap between runs.",
    "On Mondays it looks back 72 hours to cover the weekend.",
    "It takes about a minute. Then GitHub Pages republishes the site, which takes another minute or two.",
])}</ul></section>

<section id="collect"><h2>Step 1: Collect</h2>
<p>Each source has its own small collector in <code>ti/sources.py</code>. If one source is down, the rest still work,
and the <b>Source health</b> table at the bottom of the dashboard shows what failed.</p>
<div class="scroll"><table><thead><tr><th>Source</th><th>Type</th><th>UK source?</th></tr></thead>
<tbody>{feeds}{other_rows}</tbody></table></div>
<p class="sub">UK sources get a head start on the UK score, because what they choose to cover is already filtered for UK readers.</p></section>

<section id="clean"><h2>Step 2: Clean</h2>
<ul>{_li([
    "<b>Strip formatting:</b> HTML tags are removed so summaries read as plain text.",
    "<b>Fix dates:</b> every feed writes dates differently, so all of them are converted to one format (UTC).",
    "<b>Time window:</b> items older than the look-back window are dropped. KEV looks back 7 days because it updates less often.",
    "<b>Duplicates:</b> the same link, or the same headline from two outlets, becomes one story. The other outlets are listed as <i>also reported by</i>.",
    "<b>Same bug, different stories:</b> if two stories mention the same CVE, each counts as confirmation (corroboration) for the other.",
])}</ul></section>

<section id="enrich"><h2>Step 3: Enrich</h2>
<p>This is where a headline becomes intelligence. Each story gets these extra fields:</p>
<div class="scroll"><table><thead><tr><th>Field</th><th>How it is worked out</th><th>Why it helps</th></tr></thead><tbody>
<tr><td>CVEs</td><td>Pattern match for IDs like CVE-2026-12345 in the title and summary</td><td>Lets us look the bug up everywhere else</td></tr>
<tr><td>KEV</td><td>Checks each CVE against CISA's exploited list</td><td>Tells you it is being used in real attacks</td></tr>
<tr><td>EPSS</td><td>Asks FIRST.org for each CVE's exploitation probability</td><td>Helps you choose which patch goes first</td></tr>
<tr><td>Indicators (IOCs)</td><td>Pattern match for IPs, domains and file hashes, then made safe to share (<code>evil[.]com</code>)</td><td>Ready to block or search for</td></tr>
<tr><td>ATT&amp;CK</td><td>Pattern match for technique IDs such as T1566</td><td>Links to how the attack works and how to detect it</td></tr>
<tr><td>Threat type</td><td>Keyword groups: ransomware, phishing, data breach, zero-day and more</td><td>Picks the plain English explainer and the advice</td></tr>
<tr><td>Sectors</td><td>Keyword groups for: {sectors}</td><td>Shows which clients should care</td></tr>
<tr><td>UK score</td><td>UK source or UK victim start, plus weighted UK words (0-100)</td><td>Filters out US-only noise</td></tr>
<tr><td>Client match</td><td>Your watchlist's vendors, keywords and sectors</td><td>Makes the brief about <i>your</i> clients</td></tr>
</tbody></table></div>
<p>Each threat type comes with a plain English meaning and next steps:</p>
<div class="scroll"><table><tbody>{playbook}</tbody></table></div>
<p class="sub">Honest limits: this is keyword matching, not a human reading every article. It can miss things or tag them
wrongly, for example a story about "BT" the company versus the letters BT. Leak-site claims come from the criminals, so
treat them as unconfirmed. Always check the source before acting.</p></section>

<section id="score"><h2>Step 4: Score and rank</h2>
<p>Every story earns points. The total, capped at 100, is its <b>priority</b>. Click <i>Why this score?</i> on any card to see its points.</p>
<div class="scroll"><table><thead><tr><th>Reason</th><th>Points</th><th>Max</th><th>Explained</th></tr></thead>
<tbody>{scoring}</tbody></table></div>
<p><b>Levels:</b> <span class="pill s-hi"><span class="dot"></span>HIGH 60+</span> read today ·
<span class="pill s-med"><span class="dot"></span>MED 35-59</span> worth a look ·
<span class="pill s-lo"><span class="dot"></span>LOW under 35</span> background.</p>
<div class="card"><h3>Worked example</h3>
<p>NCSC warns UK organisations about an exploited VPN bug, posted 5 hours ago, also reported by BleepingComputer:</p>
<ul>{_li([
    "UK score: UK source 35 + NCSC 30 + UK 30 = 95 → 95 × 0.35 = <b>33</b>",
    "On KEV: <b>25</b>",
    "EPSS 94% → <b>19</b>",
    "Exploited bug is a serious threat type: <b>10</b>",
    "Official advisory: <b>8</b>",
    "5 hours old: <b>15</b>",
    "One other outlet: <b>3</b>",
    "Total 113, capped at <b>100</b>. It goes to the top.",
])}</ul></div>
<p>The top 8 stories get full cards. If two stories are about the same CVE, only the higher one gets a card, so the
list is not repetitive. Everything else goes into the searchable <i>Everything else</i> table.</p></section>

<section id="publish"><h2>Step 5: Publish</h2>
<ul>{_li([
    "<code>docs/index.html</code>: the dashboard you are using (replaced each day).",
    "<code>docs/briefs/&lt;date&gt;.md</code> and <code>docs/latest.md</code>: the short text brief.",
    "<code>docs/data/&lt;date&gt;.json</code>: all the data, for your own tools.",
    "The robot saves these files to the repo, GitHub Pages republishes the site, and the email goes out.",
])}</ul></section>

<section id="pack"><h2>The knowledge pack</h2>
<ul>{_li([
    f"<b>Lesson:</b> {lessons} lessons, one a day in a fixed order, starting again after {lessons} days. Repetition is on purpose.",
    "<b>Reviews:</b> lessons from 1, 3 and 7 days ago come back as quizzes. This is called spaced repetition: you see "
    "something again just as you would start to forget it, which makes it stick.",
    f"<b>Word of the day:</b> {words} terms, rotating the same way.",
    "<b>Drill:</b> takes the highest-ranked story that has something to look up (a CVE, an indicator, or a UK ransomware "
    "victim) and turns it into a 15-minute step-by-step enrichment exercise.",
])}</ul></section>

<section id="tune"><h2>How to tune it</h2>
<div class="scroll"><table><thead><tr><th>You want to…</th><th>Edit this</th></tr></thead><tbody>
<tr><td>Add or remove a news feed</td><td><code>ti/sources.py</code>, the <code>RSS_FEEDS</code> list</td></tr>
<tr><td>Add UK keywords or change their weight</td><td><code>ti/enrich.py</code>, <code>UK_TERMS</code></td></tr>
<tr><td>Add a sector or threat type</td><td><code>ti/enrich.py</code>, <code>SECTORS</code> / <code>THREAT_TYPES</code> / <code>PLAYBOOK</code></td></tr>
<tr><td>Track your clients</td><td>The <code>CLIENTS_JSON</code> secret (see the README). Use codenames, because this site is public.</td></tr>
<tr><td>Log a client question (RFI) and have it re-checked daily</td><td><code>ti/data/rfis.json</code>. Use codenames such as Client A, because this site is public.</td></tr>
<tr><td>Add lessons or glossary words</td><td><code>ti/data/nuggets.json</code>, <code>ti/data/glossary.json</code></td></tr>
<tr><td>Change the time it runs</td><td><code>.github/workflows/daily-brief.yml</code>, the <code>cron</code> line (times are UTC)</td></tr>
</tbody></table></div></section>"""
    nav = [("where", "Where to find it"), ("when", "When it runs"), ("collect", "1 Collect"),
           ("clean", "2 Clean"), ("enrich", "3 Enrich"), ("score", "4 Score"), ("publish", "5 Publish"),
           ("pack", "Knowledge pack"), ("tune", "Tune it")]
    return page("How the Brief Works",
                "Plain English guide to how the daily threat intel brief collects, enriches and ranks stories",
                "How the brief works", "A plain English tour of the logic behind your morning brief",
                body, nav=nav, links=[("./", "Back to today's brief")])
