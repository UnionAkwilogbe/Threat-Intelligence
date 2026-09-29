"""Run the daily brief.

    python -m ti                 # live feeds, writes into docs/
    python -m ti --demo          # sample data from tests/fixtures, no internet needed
    python -m ti --hours 72      # look further back (for example after a weekend)
    python -m ti --email         # also email the brief if SMTP secrets are set
"""

import argparse
import json
import os
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

from . import enrich, nuggets, notify, render, sources

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UK = ZoneInfo("Europe/London")


def main(argv=None):
    ap = argparse.ArgumentParser(description="Daily UK threat intel field brief")
    ap.add_argument("--out", default=None, help="output folder (default docs/, or demo_output/ with --demo)")
    ap.add_argument("--hours", type=int, default=36, help="how far back to look for news (default 36)")
    ap.add_argument("--demo", action="store_true", help="use sample data from tests/fixtures")
    ap.add_argument("--email", action="store_true", help="email the brief if SMTP secrets are set")
    args = ap.parse_args(argv)

    if args.out is None:
        args.out = os.path.join(ROOT, "demo_output" if args.demo else "docs")
    if args.demo:
        os.environ["TI_FIXTURES"] = os.path.join(ROOT, "tests", "fixtures")
        args.hours = 24 * 365 * 10  # fixtures are frozen in time, so accept any date

    now = datetime.now(UK)
    print(f"Collecting feeds (last {args.hours}h)…")
    items, stats, health = sources.collect_all(lookback_hours=args.hours)
    print(f"  {len(items)} raw items, {sum(h['ok'] for h in health)}/{len(health)} sources OK")

    stories, epss = enrich.enrich_all(items, stats)
    stats.pop("kev_index", None)  # large, not needed in the output
    pack = nuggets.build_pack(now.date(), stories)

    briefs = os.path.join(args.out, "briefs")
    data = os.path.join(args.out, "data")
    os.makedirs(briefs, exist_ok=True)
    os.makedirs(data, exist_ok=True)
    day = now.strftime("%Y-%m-%d")
    ctx = {
        "date": day,
        "date_long": now.strftime("%A %d %B %Y"),
        "generated": now.strftime("%H:%M"),
        "window": "sample data" if args.demo else f"last {args.hours} hours",
        "stories": stories,
        "stats": stats,
        "health": health,
        "pack": pack,
        "demo": args.demo,
    }

    md = render.render_markdown(ctx)
    with open(os.path.join(briefs, f"{day}.md"), "w", encoding="utf-8") as fh:
        fh.write(md)
    with open(os.path.join(args.out, "latest.md"), "w", encoding="utf-8") as fh:
        fh.write(md)
    ctx["archive"] = render.list_archive(briefs)
    page = render.render_html(ctx)
    with open(os.path.join(args.out, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(page)
    with open(os.path.join(data, f"{day}.json"), "w", encoding="utf-8") as fh:
        json.dump({"date": day, "stories": stories, "stats": stats, "health": health,
                   "lesson": pack["lesson"]["id"]}, fh, indent=1, default=str)

    print(f"Wrote {args.out}/index.html and briefs/{day}.md ({len(stories)} stories)")
    if stories:
        print(f"Top story: [{stories[0]['priority']}] {stories[0]['title']}")

    if args.email:
        url = os.environ.get("DASHBOARD_URL", "")
        try:
            sent = notify.send_brief(f"Threat Intel Field Brief · {ctx['date_long']}", md,
                                     dashboard_html=page, attachment_name=f"threat-brief-{day}.html",
                                     dashboard_url=url)
            print("Emailed brief." if sent else
                  "::warning::Email not configured: add SMTP_USER and SMTP_PASSWORD secrets.")
        except Exception as err:  # noqa: BLE001 - email failure must not stop the brief being saved
            print(f"::warning::Email failed: {err}", file=sys.stderr)

    if not any(h["ok"] for h in health):
        print("Every source failed. Check network access.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
