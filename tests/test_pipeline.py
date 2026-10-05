import os
import tempfile
import unittest
from datetime import date, datetime, timezone

from ti import enrich, nuggets, render, sources

FIXTURES = os.path.join(os.path.dirname(__file__), "fixtures")


class PipelineTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        os.environ["TI_FIXTURES"] = FIXTURES
        items, cls.stats, cls.health = sources.collect_all(lookback_hours=24 * 365 * 10)
        cls.stories, _ = enrich.enrich_all(items, cls.stats, clients=[])

    @classmethod
    def tearDownClass(cls):
        os.environ.pop("TI_FIXTURES", None)

    def test_missing_feeds_fail_gracefully(self):
        failed = [h for h in self.health if not h["ok"]]
        self.assertTrue(failed, "fixtures deliberately omit some feeds")
        self.assertTrue(any(h["ok"] for h in self.health))

    def test_kev_and_epss_enrichment(self):
        vpn = next(s for s in self.stories if s["source"] == "NCSC UK" and "ExampleVPN" in s["title"])
        self.assertEqual(vpn["kev"], ["CVE-2026-10001"])
        self.assertAlmostEqual(vpn["epss"], 0.94)
        self.assertIn("T1190", vpn["attack"])
        self.assertGreaterEqual(vpn["uk_score"], 50)

    def test_duplicate_headline_merged(self):
        titles = [s["title"] for s in self.stories]
        self.assertEqual(sum("patch ExampleVPN" in t for t in titles), 1)
        vpn = next(s for s in self.stories if "patch ExampleVPN" in s["title"])
        self.assertIn("BleepingComputer", vpn["also_reported_by"])

    def test_only_uk_ransomware_victims_kept(self):
        victims = [s["extra"]["victim"] for s in self.stories if s["kind"] == "ransomware"]
        self.assertCountEqual(victims, ["Example Widgets Ltd", "Demo Solicitors LLP"])
        self.assertEqual(self.stats["victims_total"], 3)

    def test_iocs_are_defanged(self):
        stealer = next(s for s in self.stories if "infostealer" in s["title"].lower())
        self.assertIn("198[.]51[.]100[.]23", stealer["iocs"]["ips"])
        self.assertIn("sha256", stealer["iocs"])

    def test_uk_c2_filtered(self):
        self.assertEqual([c["ip"] for c in self.stats["c2_uk"]], ["192.0.2.10"])

    def test_sorted_by_priority(self):
        prios = [s["priority"] for s in self.stories]
        self.assertEqual(prios, sorted(prios, reverse=True))

    def test_render_escapes_untrusted_text(self):
        evil = dict(self.stories[0], title='<script>alert(1)</script>', url="javascript:alert(1)")
        ctx = {"date": "2026-09-29", "date_long": "Tuesday", "generated": "06:00", "window": "test",
               "stories": [evil] + self.stories[1:], "stats": self.stats, "health": self.health,
               "pack": nuggets.build_pack(date(2026, 9, 29), self.stories), "archive": []}
        out = render.render_html(ctx)
        self.assertNotIn("<script>alert(1)", out)
        self.assertNotIn('href="javascript:', out)
        self.assertIn("Daily knowledge pack", render.render_markdown(ctx))


class ClientMatchTest(unittest.TestCase):
    def test_vendor_and_sector_match(self):
        clients = [{"name": "A", "vendors": ["ExampleVPN"], "sectors": [], "keywords": []},
                   {"name": "B", "vendors": [], "sectors": ["Legal"], "keywords": []}]
        os.environ["TI_FIXTURES"] = FIXTURES
        try:
            items, stats, _ = sources.collect_all(lookback_hours=24 * 365 * 10)
            stories, _ = enrich.enrich_all(items, stats, clients=clients)
        finally:
            os.environ.pop("TI_FIXTURES", None)
        vpn = next(s for s in stories if "patch ExampleVPN" in s["title"])
        self.assertEqual([c["client"] for c in vpn["clients"]], ["A"])
        self.assertEqual(vpn["priority_why"]["Matches your clients"], 20)
        law = next(s for s in stories if "Solicitors" in s["title"])
        self.assertEqual([c["client"] for c in law["clients"]], ["B"])


class EmailTest(unittest.TestCase):
    def test_markdown_to_html_escapes_and_links(self):
        from ti import notify
        out = notify.markdown_to_html("# Hi\n- **bold** <b>x</b>\n1. [link](https://example.com)\n")
        self.assertIn("<h1>Hi</h1>", out)
        self.assertIn("<b>bold</b> &lt;b&gt;x&lt;/b&gt;", out)
        self.assertIn('<a href="https://example.com">link</a>', out)
        self.assertNotIn("href", notify.markdown_to_html("[x](javascript:alert(1))"))


class NuggetTest(unittest.TestCase):
    def test_every_nugget_complete(self):
        fields = {"id", "title", "category", "explain", "analogy", "uk_angle",
                  "enrichment_tip", "try_today", "quiz_q", "quiz_a"}
        data = nuggets._load("nuggets.json")
        self.assertEqual(len({n["id"] for n in data}), len(data))
        for n in data:
            self.assertEqual(set(n), fields, n.get("id"))

    def test_rotation_and_reviews(self):
        a = nuggets.build_pack(date(2026, 9, 29), [])
        b = nuggets.build_pack(date(2026, 9, 30), [])
        self.assertNotEqual(a["lesson"]["id"], b["lesson"]["id"])
        # yesterday's lesson comes back as today's first review
        self.assertEqual(b["reviews"][0]["id"], a["lesson"]["id"])


class ParsingTest(unittest.TestCase):
    def test_dates(self):
        self.assertEqual(sources.parse_date("Mon, 28 Sep 2026 08:00:00 +0000"),
                         datetime(2026, 9, 28, 8, tzinfo=timezone.utc))
        self.assertEqual(sources.parse_date("2026-09-27").day, 27)
        self.assertIsNone(sources.parse_date("not a date"))

    def test_uk_terms_case(self):
        self.assertGreater(enrich.uk_relevance({"title": "NHS trust hit", "summary": ""}), 0)
        self.assertEqual(enrich.uk_relevance({"title": "Duke of york", "summary": "we are ok"}), 0)



class RfiTest(unittest.TestCase):
    def test_tracking_flags_new_evidence(self):
        from ti import rfi
        rfis = [{"id": "RFI-X", "topic": "Okta", "keywords": ["okta"], "cves": [{"id": "CVE-2026-1", "cvss": 5}]}]
        stories = [{"title": "Okta bug CVE-2026-2 exploited", "summary": "", "cves": ["CVE-2026-2"], "source": "x"},
                   {"title": "Unrelated", "summary": "", "cves": [], "source": "y"}]
        quiet = rfi.track(rfis, stories[1:], {"CVE-2020-1": {"vendorProject": "Microsoft", "product": "Windows"}})[0]
        self.assertFalse(quiet["needs_update"])
        self.assertTrue(quiet["kev_checked"])
        busy = rfi.track(rfis, stories, {"CVE-2026-2": {"vendorProject": "Okta", "product": "Gateway"}})[0]
        self.assertTrue(busy["needs_update"])
        self.assertEqual([k["id"] for k in busy["kev_hits"]], ["CVE-2026-2"])
        self.assertEqual(busy["new_cves"], ["CVE-2026-2"])

    def test_shipped_rfis_render(self):
        from ti import rfi
        tracked = rfi.track(rfi.load_rfis(), [], {})
        self.assertTrue(tracked)
        html = render._rfi_section(tracked)
        self.assertIn("Client requests", html)
        self.assertIn("Not checked today", html)
        for r in tracked:  # public site: no real names, only codenames
            self.assertTrue(r["client"].startswith("Client "))


class HowItWorksTest(unittest.TestCase):
    def test_page_renders_with_link(self):
        from ti import howto
        page = howto.render_how("https://example.github.io/Threat-Intelligence/")
        self.assertIn("https://example.github.io/Threat-Intelligence/", page)
        self.assertIn("Worked example", page)
        for f in sources.RSS_FEEDS:
            self.assertIn(f["name"], page)


if __name__ == "__main__":
    unittest.main()
