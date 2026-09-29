"""Render the dashboard (HTML) and the morning brief (Markdown).

All feed text is untrusted, so everything goes through `e()` (HTML escape)
and links go through `safe_url()` (http/https only).
"""

import html
import os
from urllib.parse import quote

TOP_N = 8


def e(value):
    return html.escape(str(value if value is not None else ""), quote=True)


def safe_url(url):
    url = (url or "").strip()
    return url if url.lower().startswith(("https://", "http://")) else "#"


def pct(x):
    return "" if x is None else f"{x * 100:.0f}%"


def _when(iso):
    return iso[:16].replace("T", " ") if iso else ""


def pick_top(stories, n=TOP_N):
    """Top stories, skipping ones whose CVEs are already covered by a higher story."""
    top, seen = [], set()
    for s in stories:
        cves = set(s.get("cves", []))
        if cves and cves <= seen:
            continue
        seen |= cves
        top.append(s)
        if len(top) == n:
            break
    return top


def bluf_lines(stories, stats):
    """The 'morning in 30 seconds' summary."""
    kev_new = [s for s in stories if s.get("source_id") == "kev"]
    kev_rw = [s for s in kev_new if s.get("extra", {}).get("ransomware_use")]
    uk_rw = [s for s in stories if s.get("kind") == "ransomware"]
    uk_news = [s for s in stories if s["uk_score"] >= 50 and s.get("kind") != "ransomware"]
    lines = []
    if stories:
        lines.append(f"Read first: {stories[0]['title']} (priority {stories[0]['priority']}).")
    if kev_new:
        lines.append(f"{len(kev_new)} vulnerabilities added to CISA KEV this week"
                     f"{f', {len(kev_rw)} linked to ransomware' if kev_rw else ''}. Check clients run none of them.")
    if uk_rw:
        sectors = sorted({s.get('extra', {}).get('sector') or 'unknown' for s in uk_rw})
        lines.append(f"{len(uk_rw)} UK organisations named on ransomware leak sites "
                     f"(sectors: {', '.join(sectors[:4])}).")
    if uk_news:
        lines.append(f"{len(uk_news)} stories with strong UK relevance.")
    uk_c2 = stats.get("c2_uk") or []
    if uk_c2:
        lines.append(f"{len(uk_c2)} botnet C2 servers tracked on UK networks. Block and hunt for them.")
    if not lines:
        lines.append("Quiet morning. Use the time for the knowledge pack below.")
    return lines


# ---------------------------------------------------------------------------
# HTML
# ---------------------------------------------------------------------------

CSS = """
:root{--bg:#f6f7f9;--panel:#fff;--ink:#14171c;--muted:#5b6472;--line:#e3e6eb;--accent:#1d4ed8;
--accent-soft:#e6edfd;--hi:#b42318;--hi-soft:#fdecea;--med:#b54708;--med-soft:#fef4e6;--lo:#067647;
--lo-soft:#e7f6ee;--chip:#eef0f3;--code:#f1f3f5}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#0e1116;--panel:#161a21;
--ink:#e7eaee;--muted:#9aa3af;--line:#262c36;--accent:#7aa2ff;--accent-soft:#1b2540;--hi:#ff8a80;
--hi-soft:#3a1d1b;--med:#ffb86b;--med-soft:#3a2a17;--lo:#6fd6a0;--lo-soft:#15301f;--chip:#222833;--code:#1d222b}}
:root[data-theme="dark"]{--bg:#0e1116;--panel:#161a21;--ink:#e7eaee;--muted:#9aa3af;--line:#262c36;
--accent:#7aa2ff;--accent-soft:#1b2540;--hi:#ff8a80;--hi-soft:#3a1d1b;--med:#ffb86b;--med-soft:#3a2a17;
--lo:#6fd6a0;--lo-soft:#15301f;--chip:#222833;--code:#1d222b}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.55 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
.wrap{max-width:1180px;margin:0 auto;padding:24px 16px 64px}
header{display:flex;flex-wrap:wrap;gap:12px;align-items:flex-end;justify-content:space-between;margin-bottom:20px}
h1{font-size:26px;margin:0;letter-spacing:-.01em}h2{font-size:19px;margin:0 0 12px}
h3{font-size:16px;margin:0 0 6px}
.sub{color:var(--muted);font-size:13px}
.tlp{font:600 12px/1 ui-monospace,monospace;background:#000;color:#fff;padding:5px 8px;border-radius:4px}
section{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:18px;margin:0 0 18px}
.bluf{border-left:4px solid var(--accent)}
.bluf ul{margin:0;padding-left:20px}.bluf li{margin:4px 0}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin:0 0 18px}
.tile{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:14px}
.tile b{display:block;font-size:26px;line-height:1.1;font-variant-numeric:tabular-nums}
.tile span{color:var(--muted);font-size:13px}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:18px}
@media (max-width:820px){.grid2{grid-template-columns:1fr}}
.grid2>*{min-width:0}section,.card{min-width:0;overflow-wrap:anywhere}
.card{border:1px solid var(--line);border-radius:10px;padding:14px;margin:0 0 12px}
.card-head{display:flex;gap:12px;align-items:flex-start}
.score{flex:0 0 auto;min-width:44px;text-align:center;font:700 16px/1 ui-monospace,monospace;padding:9px 6px;border-radius:8px}
.s-hi{background:var(--hi-soft);color:var(--hi)}.s-med{background:var(--med-soft);color:var(--med)}.s-lo{background:var(--lo-soft);color:var(--lo)}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin:6px 0}
.chip{background:var(--chip);border-radius:999px;padding:2px 9px;font-size:12px;color:var(--muted)}
.chip.uk{background:var(--accent-soft);color:var(--accent)}.chip.kev{background:var(--hi-soft);color:var(--hi)}
.rookie{background:var(--accent-soft);border-radius:8px;padding:8px 10px;margin:8px 0;font-size:14px}
.card ul{margin:4px 0 0;padding-left:20px}.card li{margin:2px 0}
.label{font-size:12px;font-weight:600;text-transform:uppercase;letter-spacing:.04em;color:var(--muted);margin-top:8px}
details summary{cursor:pointer;color:var(--muted);font-size:13px;margin-top:8px}
table{width:100%;border-collapse:collapse;font-size:14px}
th,td{text-align:left;padding:7px 8px;border-bottom:1px solid var(--line);vertical-align:top}
th{font-size:12px;color:var(--muted);font-weight:600;text-transform:uppercase;letter-spacing:.04em}
td.num{font-variant-numeric:tabular-nums;white-space:nowrap}
.scroll{overflow-x:auto}
code,.mono{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:13px;background:var(--code);padding:1px 5px;border-radius:4px;word-break:break-all}
.ok{color:var(--lo)}.bad{color:var(--hi)}
.lesson{border-left:4px solid var(--lo)}
.quiz{background:var(--code);border-radius:8px;padding:8px 10px;margin-top:8px}
.word{font-size:18px;font-weight:700}
input[type=search]{width:100%;padding:9px 12px;border:1px solid var(--line);border-radius:8px;background:var(--bg);color:var(--ink);font:inherit;margin-bottom:10px}
.muted{color:var(--muted)}
.toggle{background:var(--panel);border:1px solid var(--line);color:var(--ink);border-radius:8px;padding:6px 10px;cursor:pointer;font:inherit;font-size:13px}
"""

JS = """
(function(){
  var q=document.getElementById('filter');
  if(q){q.addEventListener('input',function(){var v=q.value.toLowerCase();
    document.querySelectorAll('#all tbody tr').forEach(function(r){
      r.style.display=r.textContent.toLowerCase().indexOf(v)>-1?'':'none';});});}
  var t=document.getElementById('theme');
  if(t){t.addEventListener('click',function(){var d=document.documentElement;
    var cur=d.getAttribute('data-theme')||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');
    d.setAttribute('data-theme',cur==='dark'?'light':'dark');});}
})();
"""


def _score_class(p):
    return "s-hi" if p >= 60 else "s-med" if p >= 35 else "s-lo"


def _chips(s):
    out = [f'<span class="chip kev">Client: {e(c["client"])}</span>' for c in s.get("clients", [])]
    if s["uk_score"] >= 50:
        out.append('<span class="chip uk">UK relevant</span>')
    for c in s.get("kev", []):
        out.append(f'<span class="chip kev">KEV {e(c)}</span>')
    if s.get("epss") is not None:
        out.append(f'<span class="chip">EPSS {pct(s["epss"])}</span>')
    for t in s.get("threat_types", [])[:4]:
        out.append(f'<span class="chip">{e(t)}</span>')
    for t in s.get("sectors", [])[:3]:
        out.append(f'<span class="chip">{e(t)}</span>')
    return f'<div class="chips">{"".join(out)}</div>' if out else ""


def _story_card(s):
    why = ", ".join(f"{k} +{v}" for k, v in s["priority_why"].items() if v)
    also = (f' · also reported by {e(", ".join(s["also_reported_by"]))}'
            if s.get("also_reported_by") else "")
    iocs = ""
    if s.get("iocs"):
        iocs = "<div class='label'>Indicators (defanged)</div>" + " ".join(
            f"<code>{e(v)}</code>" for vals in s["iocs"].values() for v in vals[:4])
    attack = ""
    if s.get("attack"):
        attack = " ".join(f'<a class="mono" href="https://attack.mitre.org/techniques/{e(t.replace(".", "/"))}/">{e(t)}</a>'
                          for t in s["attack"])
        attack = f"<div class='label'>ATT&amp;CK</div>{attack}"
    return f"""
<div class="card">
  <div class="card-head">
    <div class="score {_score_class(s['priority'])}" title="Priority score out of 100">{s['priority']}</div>
    <div>
      <h3><a href="{e(safe_url(s.get('url')))}" rel="noopener noreferrer" target="_blank">{e(s['title'])}</a></h3>
      <div class="sub">{e(s['source'])} · {e(_when(s.get('published')))}{also}</div>
      {_chips(s)}
    </div>
  </div>
  <div class="rookie"><b>In plain English:</b> {e(s['rookie'])}</div>
  {f'<div class="muted">{e(s["summary"])}</div>' if s.get("summary") else ""}
  <div class="label">Do this for UK clients</div>
  <ul>{"".join(f"<li>{e(a)}</li>" for a in s["actions"])}</ul>
  <div class="label">Enrich it further</div>
  <ul>{"".join(f"<li>{e(a)}</li>" for a in s["enrich_steps"])}</ul>
  {iocs}{attack}
  <details><summary>Why this score?</summary><div class="sub">{e(why)}</div></details>
</div>"""


def _vuln_table(stories):
    vulns = [s for s in stories if s.get("cves") and s.get("kind") == "vuln"]
    if not vulns:
        return "<p class='muted'>No new exploited or critical vulnerabilities in this window.</p>"
    rows = []
    for s in sorted(vulns, key=lambda x: (bool(x.get("kev")), x.get("epss") or 0), reverse=True)[:25]:
        x = s.get("extra", {})
        product = f"{x.get('vendor', '')} {x.get('product', '')}".strip() or e(s.get("summary", "")[:80])
        rows.append(
            f"<tr><td><a class='mono' href='{e(safe_url(s['url']))}' target='_blank' rel='noopener noreferrer'>{e(s['cves'][0])}</a></td>"
            f"<td>{e(product)}</td>"
            f"<td>{'<b class=bad>Yes</b>' if s.get('kev') else 'No'}</td>"
            f"<td class='num'>{pct(s.get('epss')) or '-'}</td>"
            f"<td class='num'>{e(x.get('cvss') or '-')}</td>"
            f"<td>{'Yes' if x.get('ransomware_use') else '-'}</td>"
            f"<td class='num'>{e(x.get('due_date') or '-')}</td></tr>")
    return ("<div class='scroll'><table><thead><tr><th>CVE</th><th>Product</th><th>Exploited (KEV)</th>"
            "<th>EPSS</th><th>CVSS</th><th>Ransomware</th><th>KEV due</th></tr></thead><tbody>"
            + "".join(rows) + "</tbody></table></div>")


def _ransomware_table(stories, stats):
    uk = [s for s in stories if s.get("kind") == "ransomware"]
    top = stats.get("top_groups") or []
    head = ""
    if stats.get("victims_total") is not None:
        head = (f"<p class='sub'>{stats.get('victims_total', 0)} victims posted worldwide in this window, "
                f"{stats.get('victims_uk', 0)} in the UK. Most active: "
                f"{e(', '.join(f'{g} ({n})' for g, n in top[:5]) or 'n/a')}.</p>")
    if not uk:
        return head + "<p class='muted'>No UK victims posted in this window.</p>"
    rows = "".join(
        f"<tr><td>{e(s['extra'].get('victim'))}</td><td>{e(s['extra'].get('group'))}</td>"
        f"<td>{e(s['extra'].get('sector'))}</td><td class='num'>{e(_when(s.get('published')))}</td>"
        f"<td><a href='https://find-and-update.company-information.service.gov.uk/search?q={e(quote(str(s['extra'].get('victim') or '')))}' "
        f"target='_blank' rel='noopener noreferrer'>Companies House</a></td></tr>" for s in uk)
    return (head + "<div class='scroll'><table><thead><tr><th>Victim</th><th>Group</th><th>Sector</th>"
            "<th>Posted</th><th>Enrich</th></tr></thead><tbody>" + rows + "</tbody></table></div>"
            "<p class='sub'>Leak-site claims are the gang's word, not confirmed facts. Admiralty grade them C3 until verified.</p>")


def _infra(stats):
    parts = []
    c2 = stats.get("c2_uk") or []
    if stats.get("c2_total") is not None:
        fams = ", ".join(f"{f} ({n})" for f, n in stats.get("c2_families", []))
        parts.append(f"<h3>Botnet C2 servers (Feodo Tracker)</h3><p class='sub'>{stats['c2_total']} tracked, "
                     f"{stats.get('c2_online', 0)} online. Families: {e(fams)}</p>")
        if c2:
            parts.append("<div class='scroll'><table><thead><tr><th>IP (defanged)</th><th>Port</th><th>Malware</th>"
                         "<th>Network (ASN)</th><th>Status</th><th>Last online</th></tr></thead><tbody>" + "".join(
                             f"<tr><td class='mono'>{e(str(c['ip']).replace('.', '[.]'))}</td><td class='num'>{e(c['port'])}</td>"
                             f"<td>{e(c['malware'])}</td><td>{e(c.get('as_name'))} (AS{e(c.get('asn'))})</td>"
                             f"<td>{e(c.get('status'))}</td><td class='num'>{e(c.get('last_online'))}</td></tr>" for c in c2)
                         + "</tbody></table></div>")
        else:
            parts.append("<p class='muted'>No C2 servers on UK networks right now.</p>")
    if stats.get("urls_total") is not None:
        tags = ", ".join(f"{t} ({n})" for t, n in stats.get("url_tags", []))
        parts.append(f"<h3>Malware URLs (URLhaus)</h3><p class='sub'>{stats['urls_total']} recent URLs. Top tags: {e(tags)}</p>")
        for u in stats.get("urls_uk") or []:
            parts.append(f"<div><code>{e(u['url'].replace('http', 'hxxp', 1).replace('.', '[.]'))}</code> "
                         f"<span class='sub'>{e(u['threat'])} {e(u['tags'])}</span></div>")
    if stats.get("iocs_total") is not None:
        fams = ", ".join(f"{f} ({n})" for f, n in stats.get("ioc_families", []))
        parts.append(f"<h3>Fresh IOCs (ThreatFox)</h3><p class='sub'>{stats['iocs_total']} indicators. Top families: {e(fams)}</p>")
    return "".join(parts) or "<p class='muted'>Infrastructure feeds unavailable today.</p>"


def _all_table(stories):
    rows = "".join(
        f"<tr><td class='num'><span class='score {_score_class(s['priority'])}' style='padding:3px 6px'>{s['priority']}</span></td>"
        f"<td><a href='{e(safe_url(s.get('url')))}' target='_blank' rel='noopener noreferrer'>{e(s['title'])}</a>"
        f"<div class='sub'>{e(', '.join(s.get('threat_types', [])[:3] + s.get('sectors', [])[:2]))}</div></td>"
        f"<td>{e(s['source'])}</td><td class='num'>{s['uk_score']}</td></tr>" for s in stories)
    return ("<input id='filter' type='search' placeholder='Filter: try NHS, ransomware, Fortinet, phishing…'>"
            "<div class='scroll'><table id='all'><thead><tr><th>Priority</th><th>Story</th><th>Source</th>"
            "<th>UK score</th></tr></thead><tbody>" + rows + "</tbody></table></div>")


def _pack(pack):
    L = pack["lesson"]
    reviews = "".join(
        f"<div class='card'><div class='sub'>Review · first seen {r['gap']} day{'s' if r['gap'] > 1 else ''} ago</div>"
        f"<h3>{e(r['title'])}</h3><p>{e(r['explain'])}</p>"
        f"<div class='quiz'><b>Quick quiz:</b> {e(r['quiz_q'])}"
        f"<details><summary>Show answer</summary>{e(r['quiz_a'])}</details></div></div>" for r in pack["reviews"])
    drill = ""
    if pack.get("drill"):
        d = pack["drill"]
        drill = (f"<div class='card'><h3>Today's enrichment drill (15 minutes)</h3>"
                 f"<div class='sub'>Using a real story: <a href='{e(safe_url(d['story_url']))}' target='_blank' "
                 f"rel='noopener noreferrer'>{e(d['story_title'])}</a></div><ol>"
                 + "".join(f"<li>{e(x)}</li>" for x in d["steps"]) + "</ol></div>")
    return f"""
<div class="card lesson">
  <div class="sub">Lesson {pack['day_number']} · {e(L['category'])} · cycle of {pack['total_lessons']}, repeats on purpose</div>
  <h3>{e(L['title'])}</h3>
  <p>{e(L['explain'])}</p>
  <div class="rookie"><b>Think of it like this:</b> {e(L['analogy'])}</div>
  <div class="label">Why it matters for UK clients</div><p>{e(L['uk_angle'])}</p>
  <div class="label">Enrichment tip</div><p>{e(L['enrichment_tip'])}</p>
  <div class="label">Try it today</div><p>{e(L['try_today'])}</p>
  <div class="quiz"><b>Quiz:</b> {e(L['quiz_q'])}<details><summary>Show answer</summary>{e(L['quiz_a'])}</details></div>
</div>
<div class="grid2">
  <div><div class="card"><div class="sub">Word of the day</div><div class="word">{e(pack['word']['term'])}</div>
  <p>{e(pack['word']['meaning'])}</p></div>{drill}</div>
  <div>{reviews}</div>
</div>"""


def _health(health):
    rows = "".join(
        f"<tr><td>{e(h['name'])}</td><td class='{'ok' if h['ok'] else 'bad'}'>{'OK' if h['ok'] else 'Failed'}</td>"
        f"<td class='num'>{h['count']}</td><td class='sub'>{e(h['error'])}</td></tr>" for h in health)
    return ("<div class='scroll'><table><thead><tr><th>Source</th><th>Status</th><th>Stories</th><th>Note</th>"
            "</tr></thead><tbody>" + rows + "</tbody></table></div>")


def render_html(ctx):
    stories, stats, pack, health = ctx["stories"], ctx["stats"], ctx["pack"], ctx["health"]
    ok = sum(1 for h in health if h["ok"])
    uk_rw = sum(1 for s in stories if s.get("kind") == "ransomware")
    kev_new = sum(1 for s in stories if s.get("source_id") == "kev")
    uk_rel = sum(1 for s in stories if s["uk_score"] >= 50)
    top = pick_top(stories)
    rest = [s for s in stories if s not in top]
    archive = "".join(f"<a href='briefs/{e(d)}.md'>{e(d)}</a> · " for d in ctx.get("archive", [])[:14])
    demo = ("<section style='border-color:var(--med)'><b>Demo mode:</b> built from sample data in tests/fixtures, "
            "not live feeds.</section>" if ctx.get("demo") else "")
    tiles = [
        (len(stories), "stories after de-duplication"),
        (uk_rel, "UK-relevant stories"),
        (kev_new, "new KEVs (7 days)"),
        (uk_rw, "UK ransomware victims"),
        (len(stats.get("c2_uk") or []), "botnet C2s on UK networks"),
        (f"{ok}/{len(health)}", "sources healthy"),
    ]
    return f"""<!doctype html>
<html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Threat Intel Field Brief</title>
<meta name="description" content="Daily UK-focused cyber threat intelligence brief and knowledge pack for {e(ctx['date'])}">
<style>{CSS}</style></head><body><div class="wrap">
<header>
  <div><h1>Threat Intel Field Brief</h1>
  <div class="sub">{e(ctx['date_long'])} · generated {e(ctx['generated'])} UK time · {ctx['window']}</div></div>
  <div style="display:flex;gap:8px;align-items:center"><a class="toggle" href="how-it-works.html">How it works</a>
  <span class="tlp">TLP:CLEAR</span>
  <button class="toggle" id="theme" type="button">Light / dark</button></div>
</header>
{demo}
<section class="bluf"><h2>Your morning in 30 seconds</h2><ul>{"".join(f"<li>{e(l)}</li>" for l in bluf_lines(stories, stats))}</ul>
<details><summary>New here? How to read this page (full guide: <a href="how-it-works.html">How it works</a>)</summary><p class="sub">Every story gets a <b>priority score</b> (0-100): higher means read it first.
Red is 60 and above, amber 35-59, green below 35. <b>UK relevant</b> means UK words, UK sources or UK victims were found.
<b>KEV</b> means attackers are already exploiting the bug. <b>EPSS</b> is the chance it gets exploited in the next 30 days.
Each card tells you what it means in plain English, what to do for clients, and which lookups (enrichment) would make it more useful.</p></details></section>
<div class="tiles">{"".join(f"<div class='tile'><b>{e(v)}</b><span>{e(k)}</span></div>" for v, k in tiles)}</div>
<section><h2>Top {len(top)} for your UK clients</h2>{"".join(_story_card(s) for s in top) or "<p class='muted'>No stories today.</p>"}</section>
<section><h2>Patch watch: vulnerabilities</h2>{_vuln_table(stories)}</section>
<section><h2>UK ransomware watch</h2>{_ransomware_table(stories, stats)}</section>
<section><h2>Attacker infrastructure</h2>{_infra(stats)}</section>
<section><h2>Daily knowledge pack</h2>{_pack(pack)}</section>
<section><h2>Everything else</h2>{_all_table(rest)}</section>
<section><h2>Source health</h2>{_health(health)}</section>
<p class="sub">Past briefs: {archive or 'none yet'} Data: <a href="data/{e(ctx['date'])}.json">today's JSON</a>.
Built from public sources: CISA, NCSC, NVD, FIRST EPSS, abuse.ch, ransomware.live and security news RSS. Always verify before acting.</p>
</div><script>{JS}</script></body></html>
"""


# ---------------------------------------------------------------------------
# Markdown (for email, GitHub, or reading on a phone)
# ---------------------------------------------------------------------------

def render_markdown(ctx):
    stories, stats, pack = ctx["stories"], ctx["stats"], ctx["pack"]
    out = [f"# Threat Intel Field Brief: {ctx['date_long']}", "",
           f"_TLP:CLEAR · generated {ctx['generated']} UK time · {ctx['window']}_", "",
           "## Your morning in 30 seconds", ""]
    out += [f"- {l}" for l in bluf_lines(stories, stats)]
    top = pick_top(stories)
    out += ["", f"## Top {len(top)} for your UK clients", ""]
    for i, s in enumerate(top, 1):
        tags = ", ".join(s.get("threat_types", [])[:3] + s.get("sectors", [])[:2])
        extra = []
        if s.get("kev"):
            extra.append("KEV")
        if s.get("epss") is not None:
            extra.append(f"EPSS {pct(s['epss'])}")
        if s["uk_score"] >= 50:
            extra.append("UK relevant")
        extra += [f"CLIENT: {c['client']}" for c in s.get("clients", [])]
        out += [f"### {i}. [{s['title']}]({safe_url(s.get('url'))})",
                f"**Priority {s['priority']}** · {s['source']}"
                + (f" · {' · '.join(extra)}" if extra else "") + (f" · _{tags}_" if tags else ""), "",
                f"**In plain English:** {s['rookie']}", "",
                "**Do this:** " + " ".join(s["actions"][:2]), "",
                "**Enrich next:** " + s["enrich_steps"][0], ""]
    L = pack["lesson"]
    out += ["## Daily knowledge pack", "",
            f"### Lesson {pack['day_number']}: {L['title']}", "", L["explain"], "",
            f"> **Think of it like this:** {L['analogy']}", "",
            f"**UK angle:** {L['uk_angle']}", "",
            f"**Enrichment tip:** {L['enrichment_tip']}", "",
            f"**Try it today:** {L['try_today']}", "",
            f"**Quiz:** {L['quiz_q']}  ", f"_Answer:_ {L['quiz_a']}", "",
            f"**Word of the day: {pack['word']['term']}** · {pack['word']['meaning']}", ""]
    if pack["reviews"]:
        out += ["### Review (spaced repetition)", ""]
        out += [f"- **{r['title']}** ({r['gap']}d ago): {r['quiz_q']} _Answer: {r['quiz_a']}_" for r in pack["reviews"]]
        out.append("")
    if pack.get("drill"):
        out += [f"### Enrichment drill: {pack['drill']['story_title']}", ""]
        out += [f"{i}. {x}" for i, x in enumerate(pack["drill"]["steps"], 1)]
        out.append("")
    failed = [h["name"] for h in ctx["health"] if not h["ok"]]
    out += ["---", f"Sources healthy: {len(ctx['health']) - len(failed)}/{len(ctx['health'])}"
            + (f" (failed: {', '.join(failed)})" if failed else ""), ""]
    return "\n".join(out)


def list_archive(briefs_dir):
    if not os.path.isdir(briefs_dir):
        return []
    return sorted((f[:-3] for f in os.listdir(briefs_dir) if f.endswith(".md")), reverse=True)
