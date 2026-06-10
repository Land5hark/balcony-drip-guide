#!/usr/bin/env python3
"""Static build QA for the Balcony Drip Hugo deploy tree."""

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


AFFILIATE_PATTERNS = (
    "aff.dripdepot.com",
    "sca_ref=",
    "amazon.com",
)

GOVERNED_AFFILIATE_PATTERNS = (
    "aff.dripdepot.com",
    "sca_ref=",
)


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.link_attrs = []

    def handle_starttag(self, tag, attrs):
        if tag != "a":
            return
        attr_map = dict(attrs)
        href = attr_map.get("href")
        if href:
            self.links.append(href)
            self.link_attrs.append(attr_map)


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


def audit_rendered_affiliate_links(public_dir):
    checked = 0
    violations = []
    html_files = sorted(public_dir.rglob("*.html"))

    for html_file in html_files:
        parser = LinkParser()
        parser.feed(html_file.read_text(errors="ignore"))
        for attrs in parser.link_attrs:
            href = attrs.get("href", "")
            if not any(pattern in href for pattern in AFFILIATE_PATTERNS):
                continue
            checked += 1
            rel_values = set(attrs.get("rel", "").split())
            missing_rel = [
                value
                for value in ("sponsored", "nofollow", "noopener")
                if value not in rel_values
            ]
            target = attrs.get("target")
            if missing_rel or target != "_blank":
                violations.append(
                    {
                        "source": str(html_file.relative_to(public_dir)),
                        "href": href,
                        "target": target,
                        "rel": attrs.get("rel", ""),
                        "missing_rel": missing_rel,
                    }
                )

    return {
        "rendered_affiliate_links_checked": checked,
        "violation_count": len(violations),
        "violations": violations,
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


def read_allowed_categories(config_path):
    if not config_path.exists():
        return []

    slugs = []
    in_category = False
    for line in config_path.read_text(errors="ignore").splitlines():
        stripped = line.strip()
        if stripped == "[[params.categories]]":
            in_category = True
            continue
        if stripped.startswith("[") and stripped != "[[params.categories]]":
            in_category = False
        if not in_category:
            continue

        match = re.match(r'slug\s*=\s*"([^"]+)"', stripped)
        if match:
            slugs.append(match.group(1))
    return slugs


def extract_front_matter_categories(markdown_file):
    front_matter = extract_front_matter(markdown_file)
    if not front_matter:
        return []

    for line in front_matter:
        match = re.match(r"\s*categories\s*[:=]\s*\[(.*?)\]\s*$", line)
        if not match:
            continue
        return re.findall(r'"([^"]+)"', match.group(1))
    return []


def extract_front_matter(markdown_file):
    text = markdown_file.read_text(errors="ignore")
    first_line = text.splitlines()[0] if text else ""
    if first_line not in ("---", "+++"):
        return []

    delimiter = first_line
    front_matter = []
    for line in text.splitlines()[1:]:
        if line == delimiter:
            break
        front_matter.append(line)
    return front_matter


def parse_front_matter_scalar(front_matter, key):
    pattern = re.compile(rf"\s*{re.escape(key)}\s*[:=]\s*(.*?)\s*$")
    for line in front_matter:
        match = pattern.match(line)
        if not match:
            continue
        value = match.group(1).strip().strip('"').strip("'")
        if value.lower() in ("true", "false"):
            return value.lower() == "true"
        return value
    return None


def audit_categories(source_dir, public_dir, config_path):
    allowed = read_allowed_categories(config_path)
    allowed_set = set(allowed)
    unknown = []

    if source_dir.is_dir():
        for markdown_file in sorted(source_dir.rglob("*.md")):
            categories = extract_front_matter_categories(markdown_file)
            for category in categories:
                if category not in allowed_set:
                    unknown.append(
                        {
                            "source": str(markdown_file.relative_to(source_dir)),
                            "category": category,
                        }
                    )

    category_dir = public_dir / "categories"
    generated = []
    if category_dir.is_dir():
        generated = sorted(
            child.name
            for child in category_dir.iterdir()
            if child.is_dir() and child.name != "page"
        )
    stale_generated = [slug for slug in generated if slug not in allowed_set]

    return {
        "allowed": allowed,
        "unknown_source_count": len(unknown),
        "unknown_source_categories": unknown,
        "generated": generated,
        "stale_generated_count": len(stale_generated),
        "stale_generated": stale_generated,
    }


def audit_affiliate_disclosure(source_dir):
    violations = []
    affiliate_pages = 0
    affiliate_ready_pages = 0

    if not source_dir.is_dir():
        return {
            "affiliate_pages": 0,
            "affiliate_ready_pages": 0,
            "violation_count": 0,
            "violations": violations,
        }

    for markdown_file in sorted(source_dir.rglob("*.md")):
        text = markdown_file.read_text(errors="ignore")
        front_matter = extract_front_matter(markdown_file)
        affiliate_ready = parse_front_matter_scalar(front_matter, "affiliate_ready")
        disclosure = parse_front_matter_scalar(front_matter, "disclosure")
        show_disclosure = parse_front_matter_scalar(front_matter, "show_disclosure")
        has_affiliate_link = any(pattern in text for pattern in AFFILIATE_PATTERNS)

        if has_affiliate_link:
            affiliate_pages += 1
        if affiliate_ready is True:
            affiliate_ready_pages += 1

        if (has_affiliate_link or affiliate_ready is True) and (
            disclosure is False or show_disclosure is False
        ):
            violations.append(
                {
                    "source": str(markdown_file.relative_to(source_dir)),
                    "has_affiliate_link": has_affiliate_link,
                    "affiliate_ready": affiliate_ready,
                    "disclosure": disclosure,
                    "show_disclosure": show_disclosure,
                }
            )

    return {
        "affiliate_pages": affiliate_pages,
        "affiliate_ready_pages": affiliate_ready_pages,
        "violation_count": len(violations),
        "violations": violations,
    }


def read_registered_affiliate_urls(registry_path):
    if not registry_path.exists():
        return []

    urls = []
    pattern = re.compile(r"""\s*affiliate_url:\s*["']?([^"'\n]+)""")
    for line in registry_path.read_text(errors="ignore").splitlines():
        match = pattern.match(line)
        if match:
            urls.append(match.group(1).strip())
    return sorted(set(urls))


def extract_markdown_urls(text):
    return re.findall(r"""https?://[^\]\)\s"']+""", text)


def audit_affiliate_registry(source_dir, registry_path):
    registered_urls = read_registered_affiliate_urls(registry_path)
    registered_set = set(registered_urls)
    occurrences = 0
    unregistered = []

    if source_dir.is_dir():
        for markdown_file in sorted(source_dir.rglob("*.md")):
            text = markdown_file.read_text(errors="ignore")
            for url in extract_markdown_urls(text):
                if not any(pattern in url for pattern in GOVERNED_AFFILIATE_PATTERNS):
                    continue
                occurrences += 1
                if url not in registered_set:
                    unregistered.append(
                        {
                            "source": str(markdown_file.relative_to(source_dir)),
                            "url": url,
                        }
                    )

    return {
        "registry_path": str(registry_path),
        "registered_url_count": len(registered_urls),
        "governed_occurrences": occurrences,
        "unregistered_count": len(unregistered),
        "unregistered": unregistered,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--public-dir",
        default="public",
        help="Path to Hugo public output directory. Default: public",
    )
    parser.add_argument(
        "--source-dir",
        default="content",
        help="Path to Hugo content source directory. Default: content",
    )
    parser.add_argument(
        "--config",
        default="config.toml",
        help="Path to Hugo config file. Default: config.toml",
    )
    parser.add_argument(
        "--link-registry",
        default="data/link-registry.yaml",
        help="Path to governed affiliate link registry. Default: data/link-registry.yaml",
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
    source_dir = Path(args.source_dir).resolve()
    config_path = Path(args.config).resolve()
    registry_path = Path(args.link_registry).resolve()

    result = {
        "public_dir": str(public_dir),
        "internal_links": audit_internal_links(public_dir),
        "rendered_affiliate_links": audit_rendered_affiliate_links(public_dir),
        "sitemap": audit_sitemap(public_dir),
        "categories": audit_categories(source_dir, public_dir, config_path),
        "affiliate_disclosure": audit_affiliate_disclosure(source_dir),
        "affiliate_registry": audit_affiliate_registry(source_dir, registry_path),
    }
    result["ok"] = (
        result["internal_links"]["missing_count"] == 0
        and result["rendered_affiliate_links"]["violation_count"] == 0
        and result["sitemap"]["exists"]
        and result["sitemap"]["duplicate_count"] == 0
        and result["categories"]["unknown_source_count"] == 0
        and result["categories"]["stale_generated_count"] == 0
        and result["affiliate_disclosure"]["violation_count"] == 0
        and result["affiliate_registry"]["unregistered_count"] == 0
    )

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        links = result["internal_links"]
        sitemap = result["sitemap"]
        print(f"HTML files: {links['html_files']}")
        print(f"Internal links checked: {links['internal_links_checked']}")
        print(f"Missing internal targets: {links['missing_count']}")
        rendered_affiliate = result["rendered_affiliate_links"]
        print(
            "Rendered affiliate links checked: "
            f"{rendered_affiliate['rendered_affiliate_links_checked']}"
        )
        print(
            "Rendered affiliate link rel/target violations: "
            f"{rendered_affiliate['violation_count']}"
        )
        print(f"Sitemap URLs: {sitemap['total_urls']}")
        print(f"Sitemap unique URLs: {sitemap['unique_urls']}")
        print(f"Sitemap duplicate URLs: {sitemap['duplicate_count']}")
        categories = result["categories"]
        print(f"Allowed categories: {', '.join(categories['allowed'])}")
        print(f"Unknown source categories: {categories['unknown_source_count']}")
        print(f"Stale generated categories: {categories['stale_generated_count']}")
        affiliate = result["affiliate_disclosure"]
        print(f"Affiliate-link source pages: {affiliate['affiliate_pages']}")
        print(f"Affiliate-ready source pages: {affiliate['affiliate_ready_pages']}")
        print(f"Affiliate disclosure violations: {affiliate['violation_count']}")
        registry = result["affiliate_registry"]
        print(f"Registered governed affiliate URLs: {registry['registered_url_count']}")
        print(f"Governed affiliate URL occurrences: {registry['governed_occurrences']}")
        print(f"Unregistered governed affiliate URLs: {registry['unregistered_count']}")
        if links["missing"]:
            print("\nMissing links:")
            for item in links["missing"][:50]:
                print(f"- {item['source']}: {item['href']} -> {item['expected']}")
        if rendered_affiliate["violations"]:
            print("\nRendered affiliate link rel/target violations:")
            for item in rendered_affiliate["violations"][:50]:
                print(
                    "- {source}: {href} target={target} rel={rel} "
                    "missing_rel={missing_rel}".format(**item)
                )
        if sitemap["duplicates"]:
            print("\nDuplicate sitemap URLs:")
            for loc, count in sitemap["duplicates"].items():
                print(f"- {count}x {loc}")
        if categories["unknown_source_categories"]:
            print("\nUnknown source categories:")
            for item in categories["unknown_source_categories"][:50]:
                print(f"- {item['source']}: {item['category']}")
        if categories["stale_generated"]:
            print("\nStale generated categories:")
            for slug in categories["stale_generated"]:
                print(f"- {slug}")
        if affiliate["violations"]:
            print("\nAffiliate disclosure violations:")
            for item in affiliate["violations"][:50]:
                print(
                    "- {source}: has_affiliate_link={has_affiliate_link}, "
                    "affiliate_ready={affiliate_ready}, disclosure={disclosure}, "
                    "show_disclosure={show_disclosure}".format(**item)
                )
        if registry["unregistered"]:
            print("\nUnregistered governed affiliate URLs:")
            for item in registry["unregistered"][:50]:
                print(f"- {item['source']}: {item['url']}")

    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
