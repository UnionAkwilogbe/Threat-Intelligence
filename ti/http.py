"""Tiny HTTP helper built on the standard library.

Every feed goes through `fetch()`. When the environment variable
TI_FIXTURES points at a folder, `fetch()` reads `<folder>/<key>` instead
of calling the internet. That is how the tests and `--demo` mode work.
"""

import json
import os
import time
import urllib.error
import urllib.request

USER_AGENT = "ThreatIntelFieldDashboard/1.0 (+https://github.com/UnionAkwilogbe/Threat-Intelligence)"


class FetchError(Exception):
    pass


def fetch(key, url, headers=None, timeout=30, retries=2):
    """Return the raw bytes for `url`. `key` names the fixture file in offline mode."""
    fixtures = os.environ.get("TI_FIXTURES")
    if fixtures:
        path = os.path.join(fixtures, key)
        if not os.path.exists(path):
            raise FetchError(f"no fixture for {key}")
        with open(path, "rb") as fh:
            return fh.read()

    req_headers = {"User-Agent": USER_AGENT, "Accept": "*/*"}
    req_headers.update(headers or {})
    last_err = None
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers=req_headers)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except (urllib.error.URLError, TimeoutError, ConnectionError) as err:
            last_err = err
            if attempt < retries:
                time.sleep(2 ** (attempt + 1))
    raise FetchError(f"{url}: {last_err}")


def fetch_json(key, url, headers=None, timeout=30):
    return json.loads(fetch(key, url, headers=headers, timeout=timeout).decode("utf-8", "replace"))
