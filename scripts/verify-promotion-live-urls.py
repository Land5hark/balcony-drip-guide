#!/usr/bin/env python3
"""Verify that promotion URLs serve the matching locally rendered page."""

import argparse
import html
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse, urlunparse
from urllib.request import Request, urlopen


SITE_HOST = "balcony-drip-guide.pages.dev"
URL_PATTERN = re.compile(r"https://balcony-drip-guide\.pages\.dev[^\s)`>\"]+")


class TitleParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_title = False
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "title":
            self.in_title = True

    def handle_endtag(self, tag):
        if tag.lower() == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.parts.append(data)

    def title(self):
        return " ".join(html.unescape("".join(self.parts)).split())


def parse_title(body):
    parser = TitleParser()
    parser.feed(body)
    return parser.title()


def canonical_url(raw_url):
    if "..." in raw_url:
        return None
    parsed = urlparse(raw_url.rstrip(".,;:"))
    if parsed.netloc != SITE_HOST or "..." in parsed.path:
        return None
    path = parsed.path or "/"
    if not path.endswith("/") and not Path(path).suffix:
        path += "/"
    return urlunparse(("https", SITE_HOST, path, "", "", ""))


def local_page(public_dir, url):
    path = urlparse(url).path.lstrip("/")
    if not path:
        return public_dir / "index.html"
    if Path(path).suffix:
        return public_dir / path
    return public_dir / path / "index.html"


def collect_urls(asset_dirs):
    urls = set()
    for asset_dir in asset_dirs:
        for markdown_file in sorted(asset_dir.glob("*.md")):
            for raw_url in URL_PATTERN.findall(markdown_file.read_text(errors="ignore")):
                url = canonical_url(raw_url)
                if url:
                    urls.add(url)
    return sorted(urls)


def fetch_title(url, timeout):
    request = Request(url, headers={"User-Agent": "balcony-drip-promotion-preflight/1.0"})
    try:
        with urlopen(request, timeout=timeout) as response:
            status = response.status
            body = response.read().decode("utf-8", errors="ignore")
    except HTTPError as error:
        return error.code, "", str(error)
    except URLError as error:
        return 0, "", str(error.reason)
    return status, parse_title(body), ""


def verify(public_dir, asset_dirs, timeout):
    checks = []
    for url in collect_urls(asset_dirs):
        local_file = local_page(public_dir, url)
        local_title = ""
        if local_file.exists():
            local_title = parse_title(local_file.read_text(errors="ignore"))

        status, live_title, error = fetch_title(url, timeout)
        problems = []
        if not local_file.exists():
            problems.append("local rendered page missing")
        if status != 200:
            problems.append(f"live HTTP status is {status or 'fetch-error'}")
        if local_title and live_title != local_title:
            problems.append("live title does not match local rendered title")

        checks.append(
            {
                "url": url,
                "local_file": str(local_file),
                "local_title": local_title,
                "http_status": status,
                "live_title": live_title,
                "error": error,
                "status": "pass" if not problems else "fail",
                "problems": problems,
            }
        )
    return checks


def main():
    parser = argparse.ArgumentParser(
        description="Title-aware live preflight for Markdown promotion URLs."
    )
    parser.add_argument("--public-dir", default="public")
    parser.add_argument(
        "--asset-dir",
        action="append",
        dest="asset_dirs",
        default=[],
        help="Markdown asset directory. Repeat for multiple directories.",
    )
    parser.add_argument("--report", default="")
    parser.add_argument("--timeout", type=float, default=10.0)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    asset_dirs = [Path(path) for path in (args.asset_dirs or ["promotion-assets", "promotion"])]
    checks = verify(Path(args.public_dir), asset_dirs, args.timeout)
    failures = [check for check in checks if check["status"] == "fail"]
    result = {
        "urls_checked": len(checks),
        "passed": len(checks) - len(failures),
        "failed": len(failures),
        "status": "pass" if not failures else "fail",
        "checks": checks,
    }

    if args.report:
        Path(args.report).write_text(json.dumps(result, indent=2) + "\n")

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Promotion URLs checked: {result['urls_checked']}")
        print(f"Title-aware live checks passed: {result['passed']}")
        print(f"Title-aware live checks failed: {result['failed']}")
        for check in failures:
            print(f"- FAIL: {check['url']}")
            for problem in check["problems"]:
                print(f"  - {problem}")
            print(f"  - local title: {check['local_title'] or 'missing'}")
            print(f"  - live title: {check['live_title'] or 'missing'}")
        if args.report:
            print(f"Report saved to: {args.report}")

    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
