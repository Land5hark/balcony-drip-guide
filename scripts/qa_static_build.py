#!/usr/bin/env python3
"""Static build QA for the Balcony Drip Hugo deploy tree."""

import argparse
import json
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag != "a":
            return
        href = dict(attrs).get("href")
        if href:
            self.links.append(href)


def resolve_internal_target(public_dir, href):
    parsed = urlparse(href)
    if parsed.scheme or parsed.netloc:
        return None
    if href.startswith(("#", "mailto:", "tel:", "javascript:")):
        return None

    path = unquote(parsed.path)
    if not path or path.startswith("//"):
        return None

    relative = path.lstrip("/")
    if path.endswith("/") or not Path(path).suffix:
        return public_dir / relative / "index.html"
    return public_dir / relative


def audit_internal_links(public_dir):
    checked = 0
    missing = []
    html_files = sorted(public_dir.rglob("*.html"))

    for html_file in html_files:
        parser = LinkParser()
        parser.feed(html_file.read_text(errors="ignore"))
        for href in parser.links:
            target = resolve_internal_target(public_dir, href)
            if target is None:
                continue
            checked += 1
            if not target.exists():
                missing.append(
                    {
                        "source": str(html_file.relative_to(public_dir)),
                        "href": href,
                        "expected": str(target.relative_to(public_dir)),
                    }
                )

    return {
        "html_files": len(html_files),
        "internal_links_checked": checked,
        "missing_count": len(missing),
        "missing": missing,
    }


def audit_sitemap(public_dir):
    sitemap = public_dir / "sitemap.xml"
    if not sitemap.exists():
        return {
            "exists": False,
            "total_urls": 0,
            "unique_urls": 0,
            "duplicate_count": 0,
            "duplicates": {},
        }

    namespace = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    root = ET.parse(sitemap).getroot()
    locs = [el.text for el in root.findall("s:url/s:loc", namespace) if el.text]
    duplicates = {loc: count for loc, count in Counter(locs).items() if count > 1}
    return {
        "exists": True,
        "total_urls": len(locs),
        "unique_urls": len(set(locs)),
        "duplicate_count": len(duplicates),
        "duplicates": duplicates,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--public-dir",
        default="public",
        help="Path to Hugo public output directory. Default: public",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable JSON only.",
    )
    args = parser.parse_args()

    public_dir = Path(args.public_dir).resolve()
    if not public_dir.is_dir():
        print(f"ERROR: public directory not found: {public_dir}", file=sys.stderr)
        return 2

    result = {
        "public_dir": str(public_dir),
        "internal_links": audit_internal_links(public_dir),
        "sitemap": audit_sitemap(public_dir),
    }
    result["ok"] = (
        result["internal_links"]["missing_count"] == 0
        and result["sitemap"]["exists"]
        and result["sitemap"]["duplicate_count"] == 0
    )

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        links = result["internal_links"]
        sitemap = result["sitemap"]
        print(f"HTML files: {links['html_files']}")
        print(f"Internal links checked: {links['internal_links_checked']}")
        print(f"Missing internal targets: {links['missing_count']}")
        print(f"Sitemap URLs: {sitemap['total_urls']}")
        print(f"Sitemap unique URLs: {sitemap['unique_urls']}")
        print(f"Sitemap duplicate URLs: {sitemap['duplicate_count']}")
        if links["missing"]:
            print("\nMissing links:")
            for item in links["missing"][:50]:
                print(f"- {item['source']}: {item['href']} -> {item['expected']}")
        if sitemap["duplicates"]:
            print("\nDuplicate sitemap URLs:")
            for loc, count in sitemap["duplicates"].items():
                print(f"- {count}x {loc}")

    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
