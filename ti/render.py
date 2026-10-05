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
:root{color-scheme:light;
--bg:#f4f3ef;--panel:#fcfcfb;--panel-2:#f7f6f2;--ink:#0b0b0b;--muted:#52514e;--faint:#77756f;--line:#e4e2dc;
--accent:#1c5cab;--accent-soft:#e8f0fa;--bar:#2a78d6;--top:#0f1b2d;--top-ink:#f4f3ef;--top-muted:#a9b3c2;
--crit:#d03b3b;--crit-soft:#fbeeee;--warn:#ec835a;--low:#a3a19b;--good:#0ca30c;--code:#efeee9;--c0:#8a8984;--c1:#2a78d6;--c2:#eb6834;--c3:#1baf7a;--c4:#eda100;--c5:#e87ba4;--c6:#008300;--c7:#4a3aa7;--c8:#e34948}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){color-scheme:dark;
--bg:#121211;--panel:#1a1a19;--panel-2:#1f1f1d;--ink:#ffffff;--muted:#c3c2b7;--faint:#9a998f;--line:#2e2e2b;
--accent:#6da7ec;--accent-soft:#17263b;--bar:#3987e5;--top:#0b1320;--top-ink:#f4f3ef;--top-muted:#8c97a8;
--crit:#e06060;--crit-soft:#341c1c;--warn:#ec835a;--low:#6f6e68;--good:#0ca30c;--code:#242422;--c0:#77766f;--c1:#3987e5;--c2:#d95926;--c3:#199e70;--c4:#c98500;--c5:#d55181;--c6:#008300;--c7:#9085e9;--c8:#e66767}}
:root[data-theme="dark"]{color-scheme:dark;
--bg:#121211;--panel:#1a1a19;--panel-2:#1f1f1d;--ink:#ffffff;--muted:#c3c2b7;--faint:#9a998f;--line:#2e2e2b;
--accent:#6da7ec;--accent-soft:#17263b;--bar:#3987e5;--top:#0b1320;--top-ink:#f4f3ef;--top-muted:#8c97a8;
--crit:#e06060;--crit-soft:#341c1c;--warn:#ec835a;--low:#6f6e68;--good:#0ca30c;--code:#242422;--c0:#77766f;--c1:#3987e5;--c2:#d95926;--c3:#199e70;--c4:#c98500;--c5:#d55181;--c6:#008300;--c7:#9085e9;--c8:#e66767}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:64px}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.6 Inter,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;-webkit-font-smoothing:antialiased}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
.topbar{background:linear-gradient(120deg,var(--top) 0%,var(--top) 55%,color-mix(in srgb,var(--top) 70%,var(--c1)) 100%);color:var(--top-ink)}
.topbar .in{max-width:1180px;margin:0 auto;padding:22px 16px 18px;display:flex;flex-wrap:wrap;gap:14px;align-items:flex-end;justify-content:space-between}
.eyebrow{font:600 11px/1 Inter,system-ui,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--top-muted)}
h1{font-size:28px;margin:6px 0 4px;letter-spacing:-.02em;font-weight:700}
.topbar .sub{color:var(--top-muted)}
.actions{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
.nav{position:sticky;top:0;z-index:5;background:color-mix(in srgb,var(--bg) 92%,transparent);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.nav .in{max-width:1180px;margin:0 auto;padding:0 16px;display:flex;gap:4px;overflow-x:auto;scrollbar-width:none}
.nav a{color:var(--muted);font-size:13px;font-weight:500;padding:12px 10px;white-space:nowrap;border-bottom:2px solid transparent}
.nav a:hover{color:var(--ink);text-decoration:none;border-bottom-color:var(--accent)}
.wrap{max-width:1180px;margin:0 auto;padding:24px 16px 64px}
h2{font-size:18px;margin:0 0 4px;letter-spacing:-.01em}h3{font-size:16px;margin:0 0 4px;line-height:1.4}
.h-note{color:var(--faint);font-size:13px;margin:0 0 14px}
.sub{color:var(--muted);font-size:13px}
.tlp{font:600 11px/1 ui-monospace,SFMono-Regular,Menlo,monospace;background:#000;color:#fff;padding:6px 8px;border-radius:4px;border:1px solid #444;letter-spacing:.04em}
section{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:22px;margin:0 0 20px}
.bluf{border-left:4px solid var(--accent)}
.bluf ul{margin:8px 0 0;padding-left:20px}.bluf li{margin:6px 0}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:12px;margin:0 0 20px}
.tile{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:16px}
.tile b{display:block;font-size:30px;line-height:1.1;font-weight:700;letter-spacing:-.02em;font-variant-numeric:tabular-nums}
.tile span{color:var(--muted);font-size:13px}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:20px}
@media (max-width:820px){.grid2{grid-template-columns:1fr}}
.grid2>*{min-width:0}section,.card{min-width:0;overflow-wrap:anywhere}
.card{border:1px solid var(--line);border-left:4px solid var(--low);border-radius:10px;padding:16px 18px;margin:0 0 14px;background:var(--panel)}
.card.r-hi{border-left-color:var(--crit)}.card.r-med{border-left-color:var(--warn)}
.card-head{display:flex;gap:14px;align-items:flex-start}
.card h3 a{color:var(--ink)}.card h3 a:hover{color:var(--accent)}
.score{flex:0 0 auto;min-width:58px;text-align:center;border:1px solid var(--line);border-radius:10px;padding:6px 6px 5px;background:var(--panel-2)}
.score b{display:block;font:700 20px/1.1 Inter,system-ui,sans-serif;font-variant-numeric:tabular-nums}
.score i{display:flex;gap:5px;align-items:center;justify-content:center;font:600 10px/1 Inter,system-ui,sans-serif;letter-spacing:.08em;font-style:normal;color:var(--muted);margin-top:3px}
.dot{width:8px;height:8px;border-radius:50%;background:var(--low);display:inline-block;flex:0 0 auto}
.s-hi .dot{background:var(--crit)}.s-med .dot{background:var(--warn)}
.pill{display:inline-flex;gap:6px;align-items:center;border:1px solid var(--line);border-radius:999px;padding:2px 9px 2px 7px;font-size:12px;font-weight:600;background:var(--panel-2);font-variant-numeric:tabular-nums}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0 2px}
.chip{background:var(--panel-2);border:1px solid var(--line);border-radius:999px;padding:1px 9px;font-size:12px;color:var(--muted)}
.chip.uk{background:var(--accent-soft);border-color:transparent;color:var(--accent);font-weight:600}
.chip.kev{background:var(--crit-soft);border-color:transparent;color:var(--ink);font-weight:600}
.chip.kev::before{content:"";display:inline-block;width:6px;height:6px;border-radius:50%;background:var(--crit);margin-right:6px;vertical-align:1px}
.rookie{background:var(--accent-soft);border-radius:8px;padding:10px 12px;margin:12px 0 8px;font-size:14px}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:6px}
@media (max-width:720px){.cols{grid-template-columns:1fr}}
.card ul,.card ol{margin:4px 0 0;padding-left:20px}.card li{margin:3px 0}
.label{font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.08em;color:var(--faint);margin-top:12px}
details summary{cursor:pointer;color:var(--muted);font-size:13px;margin-top:10px}
table{width:100%;border-collapse:collapse;font-size:14px}
th,td{text-align:left;padding:9px 10px;border-bottom:1px solid var(--line);vertical-align:top}
tbody tr:hover{background:var(--panel-2)}
th{font-size:11px;color:var(--faint);font-weight:600;text-transform:uppercase;letter-spacing:.08em}
td.num{font-variant-numeric:tabular-nums;white-space:nowrap}
.scroll{overflow-x:auto}
code,.mono{font-family:"JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12.5px;background:var(--code);padding:1px 6px;border-radius:4px;word-break:break-all}
.ok{color:var(--ink)}.ok::before{content:"";display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--good);margin-right:7px}
.bad{color:var(--ink);font-weight:600}.bad::before{content:"";display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--crit);margin-right:7px}
.lesson{border-left-color:var(--accent)}
.quiz{background:var(--panel-2);border:1px solid var(--line);border-radius:8px;padding:10px 12px;margin-top:10px}
.word{font-size:22px;font-weight:700;letter-spacing:-.01em}
input[type=search]{width:100%;padding:10px 12px;border:1px solid var(--line);border-radius:10px;background:var(--panel-2);color:var(--ink);font:inherit;margin-bottom:12px}
input[type=search]:focus{outline:2px solid var(--accent);outline-offset:1px}
.muted{color:var(--muted)}
.toggle{display:inline-block;background:transparent;border:1px solid color-mix(in srgb,currentColor 30%,transparent);color:inherit;border-radius:8px;padding:6px 11px;cursor:pointer;font:inherit;font-size:13px;font-weight:500}
.toggle:hover{text-decoration:none;border-color:currentColor}
.bars{display:grid;gap:9px}
.bar-row{display:grid;grid-template-columns:minmax(110px,38%) 1fr 32px;gap:10px;align-items:center;font-size:13px;padding:2px 0;border-radius:6px}
.bar-row:hover{background:var(--panel-2)}
.bar-track{height:10px}
.bar-fill{height:10px;background:var(--bar);border-radius:0 4px 4px 0;min-width:4px}
.bar-row .v{text-align:right;font-variant-numeric:tabular-nums;color:var(--muted)}
footer{color:var(--faint);font-size:13px;padding:8px 2px}
.tt{--c:var(--c0);background:color-mix(in srgb,var(--c) 12%,var(--panel));border-color:color-mix(in srgb,var(--c) 35%,transparent);color:var(--ink)}
.tt::before{content:"";display:inline-block;width:7px;height:7px;border-radius:50%;background:var(--c);margin-right:6px;vertical-align:1px}
.t-1{--c:var(--c1)}.t-2{--c:var(--c2)}.t-3{--c:var(--c3)}.t-4{--c:var(--c4)}.t-5{--c:var(--c5)}.t-6{--c:var(--c6)}.t-7{--c:var(--c7)}.t-8{--c:var(--c8)}
.bar-fill.tt-bar{background:var(--c)}
.tile{position:relative;overflow:hidden}
.tile::before{content:"";position:absolute;left:0;top:0;right:0;height:4px;background:var(--c,var(--c1))}
.tile .ico{display:inline-grid;place-items:center;width:26px;height:26px;border-radius:8px;background:color-mix(in srgb,var(--c,var(--c1)) 16%,var(--panel));color:var(--c,var(--c1));font-size:14px;margin-bottom:8px}
section>h2::before{content:"";display:inline-block;width:10px;height:10px;border-radius:3px;background:var(--hc,var(--accent));margin-right:9px;vertical-align:1px}
.headline{font-size:19px;font-weight:600;line-height:1.45;margin:6px 0 2px}
.oneliner{margin:10px 0 2px;font-size:14.5px}
.oneliner b{color:var(--ink)}
.rfi{border:1px solid var(--line);border-radius:12px;overflow:hidden;margin:0 0 14px}
.rfi-head{display:flex;flex-wrap:wrap;gap:10px;align-items:center;justify-content:space-between;padding:14px 18px;background:color-mix(in srgb,var(--c7) 10%,var(--panel))}
.rfi-body{padding:16px 18px}
.status{display:inline-flex;align-items:center;gap:6px;font-size:12px;font-weight:600;border-radius:999px;padding:3px 10px;border:1px solid var(--line);background:var(--panel)}
.status::before{content:"";width:8px;height:8px;border-radius:50%;background:var(--good)}
.status.upd::before{background:var(--crit)}
.finding{border-left:4px solid var(--c0);padding:8px 12px;margin:10px 0;background:var(--panel-2);border-radius:0 8px 8px 0}
.finding.f-high{border-left-color:var(--crit)}.finding.f-medium{border-left-color:var(--warn)}
.checks{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:10px;margin:12px 0}
.check{border:1px solid var(--line);border-radius:10px;padding:10px 12px;background:var(--panel)}
.check b{display:block;font-size:22px;font-variant-numeric:tabular-nums}
.sev{display:inline-flex;align-items:center;gap:6px;font-variant-numeric:tabular-nums;font-weight:600}
.sev::before{content:"";width:8px;height:8px;border-radius:50%;background:var(--c0)}
.sev.crit::before{background:var(--crit)}.sev.high::before{background:var(--warn)}.sev.med::before{background:var(--c4)}
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


# Each threat type keeps one fixed colour slot everywhere (colour follows the entity).
THREAT_SLOT = {"Nation-state / APT": 1, "Phishing": 2, "Supply chain": 3, "Exploited vuln": 4,
               "Data breach": 5, "Identity / MFA": 6, "Ransomware": 7, "Zero-day": 8}


def _tt(name):
    return f"t-{THREAT_SLOT.get(name, 0)}"


def _score_class(p):
    return "s-hi" if p >= 60 else "s-med" if p >= 35 else "s-lo"


def _level(p):
    return "HIGH" if p >= 60 else "MED" if p >= 35 else "LOW"


def _badge(p):
    """Priority badge: number + dot + word, so meaning never relies on colour alone."""
    return (f'<div class="score {_score_class(p)}" title="Priority score out of 100">'
            f'<b>{p}</b><i><span class="dot"></span>{_level(p)}</i></div>')


def _pill(p):
    return f'<span class="pill {_score_class(p)}"><span class="dot"></span>{p}</span>'


def _bars(counts, title_suffix="stories", colour=False):
    """Horizontal bar list: one hue, labels and values as text, hover shows the count."""
    counts = [(k, v) for k, v in counts if v]
    if not counts:
        return "<p class='muted'>Nothing to chart today.</p>"
    top = max(v for _, v in counts)
    return "<div class='bars'>" + "".join(
        f"<div class='bar-row' title='{e(k)}: {v} {title_suffix}'><span>{e(k)}</span>"
        f"<div class='bar-track'><div class='bar-fill{' tt-bar ' + _tt(k) if colour else ''}' style='width:{v / top * 100:.0f}%'></div></div>"
        f"<span class='v'>{v}</span></div>" for k, v in counts) + "</div>"


def _mix(stories, field):
    counts = {}
    for s in stories:
        for t in s.get(field, []):
            counts[t] = counts.get(t, 0) + 1
    return sorted(counts.items(), key=lambda kv: -kv[1])[:8]


def _chips(s):
    out = [f'<span class="chip kev">Client: {e(c["client"])}</span>' for c in s.get("clients", [])]
    if s["uk_score"] >= 50:
        out.append('<span class="chip uk">UK relevant</span>')
    for c in s.get("kev", []):
        out.append(f'<span class="chip kev">KEV {e(c)}</span>')
    if s.get("epss") is not None:
        out.append(f'<span class="chip">EPSS {pct(s["epss"])}</span>')
    for t in s.get("threat_types", [])[:4]:
        out.append(f'<span class="chip tt {_tt(t)}">{e(t)}</span>')
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
        attack = f"<div class='label'>ATT&amp;CK techniques</div>{attack}"
    rail = {"s-hi": "r-hi", "s-med": "r-med"}.get(_score_class(s["priority"]), "")
    return f"""
<article class="card {rail}">
  <div class="card-head">
    {_badge(s['priority'])}
    <div style="min-width:0">
      <h3><a href="{e(safe_url(s.get('url')))}" rel="noopener noreferrer" target="_blank">{e(s['title'])}</a></h3>
      <div class="sub">{e(s['source'])} · {e(_when(s.get('published')))}{also}</div>
      {_chips(s)}
    </div>
  </div>
  <div class="oneliner"><b>What it means:</b> {e(s['rookie'])}</div>
  <div class="oneliner"><b>Do first:</b> {e(s['actions'][0])}</div>
  <details><summary>Details, actions and enrichment</summary>
  {f'<div class="muted" style="font-size:14px;margin-top:8px">{e(_short(s["summary"]))}</div>' if s.get("summary") else ""}
  <div class="cols">
    <div><div class="label">Do this for UK clients</div>
    <ul>{"".join(f"<li>{e(a)}</li>" for a in s["actions"])}</ul></div>
    <div><div class="label">Enrich it further</div>
    <ul>{"".join(f"<li>{e(a)}</li>" for a in s["enrich_steps"])}</ul></div>
  </div>
  {iocs}{attack}
  <div class="label">Why this score</div><div class="sub">{e(why)}</div>
  </details>
</article>"""


def _short(text, limit=320):
    return text if len(text) <= limit else text[:limit].rsplit(" ", 1)[0] + "…"


def _sev(cvss):
    cls = "crit" if cvss >= 9 else "high" if cvss >= 7 else "med" if cvss >= 4 else ""
    word = "Critical" if cvss >= 9 else "High" if cvss >= 7 else "Medium" if cvss >= 4 else "Low"
    return f"<span class='sev {cls}'>{cvss:.1f} {word}</span>"


def _rfi_card(r):
    status = ("<span class='status upd'>Needs update: new evidence today</span>" if r.get("needs_update")
              else f"<span class='status'>{e(r.get('status', 'Open'))} · re-checked today</span>")
    findings = "".join(
        f"<div class='finding f-{e(f.get('level', '').lower())}'><b>{e(f['title'])}</b> "
        f"<span class='chip'>{e(f.get('level', ''))} concern</span><div style='font-size:14px;margin-top:4px'>{e(f['text'])}</div></div>"
        for f in r.get("findings", []))
    kev = r.get("kev_hits", [])
    kev_text = ("Not checked today (KEV feed unavailable)" if not r.get("kev_checked")
                else ", ".join(k["id"] for k in kev) if kev else "None on the exploited list")
    checks = (f"<div class='checks'>"
              f"<div class='check' style='border-top:4px solid var({'--crit' if kev else '--good'})'><b>{len(kev)}</b>"
              f"<span class='sub'>on CISA KEV today: {e(kev_text)}</span></div>"
              f"<div class='check' style='border-top:4px solid var(--c1)'><b>{len(r.get('matches', []))}</b>"
              f"<span class='sub'>matching stories in today's feeds</span></div>"
              f"<div class='check' style='border-top:4px solid var({'--crit' if r.get('new_cves') else '--c3'})'>"
              f"<b>{len(r.get('new_cves', []))}</b><span class='sub'>new CVEs not yet in the answer"
              f"{': ' + e(', '.join(r['new_cves'])) if r.get('new_cves') else ''}</span></div></div>")
    cves = "".join(
        f"<tr><td><a class='mono' href='https://www.cve.org/CVERecord?id={e(c['id'])}' target='_blank' rel='noopener noreferrer'>{e(c['id'])}</a></td>"
        f"<td>{e(c['product'])}</td><td>{e(c['issue'])}</td><td class='num'>{_sev(float(c['cvss']))}</td><td>{e(c['fixed'])}</td></tr>"
        for c in sorted(r.get("cves", []), key=lambda c: -float(c["cvss"])))
    cve_table = ("<div class='label'>Vulnerabilities covered</div><div class='scroll'><table><thead><tr><th>CVE</th><th>Product</th>"
                 "<th>Issue</th><th>CVSS</th><th>Fixed in</th></tr></thead><tbody>" + cves + "</tbody></table></div>") if cves else ""
    matches = "".join(f"<li><a href='{e(safe_url(m.get('url')))}' target='_blank' rel='noopener noreferrer'>{e(m['title'])}</a> "
                      f"<span class='sub'>{e(m['source'])}</span></li>" for m in r.get("matches", []))
    sources = "".join(f"<li><a href='{e(safe_url(x['url']))}' target='_blank' rel='noopener noreferrer'>{e(x['name'])}</a></li>"
                      for x in r.get("sources", []))
    return f"""
<div class="rfi">
  <div class="rfi-head"><div><span class="sub">{e(r['id'])} · {e(r.get('client', ''))} · opened {e(r.get('opened', ''))}</span>
  <h3 style="margin:2px 0 0">{e(r['topic'])}</h3></div>{status}</div>
  <div class="rfi-body">
    <div class="rookie"><b>Bottom line:</b> {e(r.get('bluf', ''))}</div>
    {checks}
    {findings}
    <div class="label">Assessment</div><p style="margin:4px 0">{e(r.get('assessment', ''))}</p>
    <p class="sub" style="margin:0">{e(r.get('confidence', ''))}</p>
    <details open><summary>Recommended actions</summary><ol>{"".join(f"<li>{e(a)}</li>" for a in r.get('actions', []))}</ol></details>
    <details><summary>Vulnerability detail ({len(r.get('cves', []))} CVEs)</summary>{cve_table}</details>
    {f"<details open><summary>In today's feeds</summary><ul>{matches}</ul></details>" if matches else ""}
    <details><summary>Sources</summary><ul>{sources}</ul></details>
  </div>
</div>"""


def _rfi_section(rfis):
    if not rfis:
        return ""
    return ("<section id='rfi' style='--hc:var(--c7)'><h2>Client requests</h2>"
            "<p class='h-note'>Questions clients have asked. Each one is re-checked against CISA KEV and today's feeds every morning.</p>"
            + "".join(_rfi_card(r) for r in rfis) + "</section>")


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
        f"<tr><td class='num'>{_pill(s['priority'])}</td>"
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
    demo = ("<section style='border-left:4px solid var(--warn)'><b>Demo mode:</b> built from sample data in tests/fixtures, "
            "not live feeds.</section>" if ctx.get("demo") else "")
    tiles = [  # value, label, icon, colour slot
        (len(stories), "stories after de-duplication", "≡", 1),
        (uk_rel, "UK-relevant stories", "◆", 3),
        (kev_new, "new KEVs (7 days)", "!", 8),
        (uk_rw, "UK ransomware victims", "▲", 7),
        (len(stats.get("c2_uk") or []), "botnet C2s on UK networks", "◎", 2),
        (f"{ok}/{len(health)}", "sources healthy", "✓", 6),
    ]
    rfis = ctx.get("rfis") or []
    high = sum(1 for x in stories if x["priority"] >= 60)
    if not top:
        headline = "Quiet day: nothing new in the feeds."
    elif high:
        headline = f"{high} high-priority item{'s' if high != 1 else ''} today. Start with: {top[0]['title']}"
    else:
        headline = f"No high-priority items today. Top story: {top[0]['title']}"
    nav = ([("rfi", "Client requests")] if rfis else []) + [("top", "Top stories"),("mix", "Threat mix"), ("patch", "Patch watch"), ("ransomware", "Ransomware"),
           ("infra", "Infrastructure"), ("learn", "Knowledge pack"), ("all", "All stories"), ("sources", "Sources")]
    body = f"""
{demo}
<section class="bluf"><h2>Your morning in 30 seconds</h2><div class="headline">{e(headline)}</div><ul>{"".join(f"<li>{e(l)}</li>" for l in bluf_lines(stories, stats))}</ul>
<details><summary>New here? How to read this page</summary><p class="sub">Every story gets a <b>priority score</b> out of 100: the higher, the sooner you should read it.
<b>HIGH</b> is 60 and above, <b>MED</b> 35-59, <b>LOW</b> under 35. <b>UK relevant</b> means UK words, UK sources or UK victims were found.
<b>KEV</b> means attackers are already exploiting the bug. <b>EPSS</b> is the chance it gets exploited in the next 30 days.
Each card tells you what it means in plain English, what to do for clients, and which lookups (enrichment) would add more context.
The full guide is on the <a href="how-it-works.html">How it works</a> page.</p></details></section>
<div class="tiles">{"".join(f"<div class='tile' style='--c:var(--c{c})'><div class='ico' aria-hidden='true'>{i}</div><b>{e(v)}</b><span>{e(k)}</span></div>" for v, k, i, c in tiles)}</div>
{_rfi_section(rfis)}
<section id="top" style="--hc:var(--crit)"><h2>Top {len(top)} for your UK clients</h2><p class="h-note">Ranked by priority. The coloured edge and badge show the level.</p>
{"".join(_story_card(s) for s in top) or "<p class='muted'>No stories today.</p>"}</section>
<div class="grid2" id="mix">
<section style="--hc:var(--c8)"><h2>Threat mix</h2><p class="h-note">How many of today's stories involve each threat type</p>{_bars(_mix(stories, "threat_types"), colour=True)}</section>
<section style="--hc:var(--c3)"><h2>Sectors in the news</h2><p class="h-note">Which UK sectors today's stories touch</p>{_bars(_mix(stories, "sectors"))}</section>
</div>
<section id="patch" style="--hc:var(--c4)"><h2>Patch watch</h2><p class="h-note">Exploited (KEV) and critical vulnerabilities, most urgent first</p>{_vuln_table(stories)}</section>
<section id="ransomware" style="--hc:var(--c7)"><h2>UK ransomware watch</h2>{_ransomware_table(stories, stats)}</section>
<section id="infra" style="--hc:var(--c2)"><h2>Attacker infrastructure</h2>{_infra(stats)}</section>
<section id="learn" style="--hc:var(--c3)"><h2>Daily knowledge pack</h2><p class="h-note">A new lesson each day, plus quick reviews of earlier ones</p>{_pack(pack)}</section>
<section id="all" style="--hc:var(--c1)"><h2>Everything else</h2>{_all_table(rest)}</section>
<section id="sources" style="--hc:var(--c6)"><h2>Source health</h2>{_health(health)}</section>
<footer>Past briefs: {archive or 'none yet'} Data: <a href="data/{e(ctx['date'])}.json">today's JSON</a>.
Built from public sources: CISA, NCSC, NVD, FIRST EPSS, abuse.ch, ransomware.live and security news RSS. Always verify before acting.</footer>"""
    return page("Threat Intel Field Brief",
                f"Daily UK-focused cyber threat intelligence brief and knowledge pack for {ctx['date']}",
                "Threat Intel Field Brief",
                f"{ctx['date_long']} · generated {ctx['generated']} UK time · {ctx['window']}",
                body, nav=nav, links=[("how-it-works.html", "How it works")])


def page(title, description, heading, subtitle, body, nav=None, links=None):
    """Shared page shell: dark top bar, optional sticky section nav, content, theme toggle."""
    nav_html = ""
    if nav:
        nav_html = ("<nav class='nav'><div class='in'>"
                    + "".join(f"<a href='#{e(i)}'>{e(t)}</a>" for i, t in nav) + "</div></nav>")
    link_html = "".join(f"<a class='toggle' href='{e(h)}'>{e(t)}</a>" for h, t in (links or []))
    return f"""<!doctype html>
<html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(description)}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<header class="topbar"><div class="in">
  <div><div class="eyebrow">UK cyber threat intelligence · daily</div><h1>{e(heading)}</h1>
  <div class="sub">{e(subtitle)}</div></div>
  <div class="actions">{link_html}<span class="tlp">TLP:CLEAR</span>
  <button class="toggle" id="theme" type="button">Light / dark</button></div>
</div></header>
{nav_html}
<main class="wrap">{body}</main>
<script>{JS}</script></body></html>
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
    for r in ctx.get("rfis") or []:
        kev = r.get("kev_hits", [])
        out += [f"## Client request {r['id']}: {r['topic']} ({r.get('client', '')})", "",
                ("**Status: needs update, new evidence today.**" if r.get("needs_update")
                 else f"**Status:** {r.get('status', 'Open')}, re-checked today."), "",
                f"**Bottom line:** {r.get('bluf', '')}", "",
                f"- On CISA KEV today: {', '.join(k['id'] for k in kev) if kev else 'none'}",
                f"- Matching stories today: {len(r.get('matches', []))}",
                f"- New CVEs not yet covered: {', '.join(r.get('new_cves', [])) or 'none'}", ""]
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
