#!/usr/bin/env python3
import re
import subprocess
import sys
from pathlib import Path
from urllib.request import Request, urlopen

SITE_DIR = Path("/home/linuxlite/.openclaw/workspace/passive-income/aquarium-ato/site")
LOCAL_INDEX = SITE_DIR / "public" / "index.html"
LIVE_URL = "https://nano-tank-ato-reliability.pages.dev/"
CHECKS = [
    "data-cf-beacon",
    "How to Stop False ATO Alarms in Small Tanks",
    "Float Switch vs Optical Sensor ATOs for Nano Tanks",
]


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def fetch_live(url: str) -> str:
    req = Request(url, headers={"User-Agent": "Mozilla/5.0 SpikeLiveCheck/1.0"})
    with urlopen(req, timeout=20) as resp:
        return resp.read().decode("utf-8", errors="replace")


def branch_tip(branch: str) -> str:
    return subprocess.check_output([
        "git", "-C", str(SITE_DIR), "rev-parse", branch
    ], text=True).strip()


def remote_heads() -> str:
    return subprocess.check_output([
        "git", "-C", str(SITE_DIR), "ls-remote", "--heads", "origin"
    ], text=True)


def main() -> int:
    local_html = load_text(LOCAL_INDEX)
    live_html = fetch_live(LIVE_URL)

    print(f"Live URL: {LIVE_URL}")
    print(f"Local file: {LOCAL_INDEX}")
    print(f"main tip: {branch_tip('main')}")
    try:
        print(f"origin/master tip: {branch_tip('origin/master')}")
    except subprocess.CalledProcessError:
        print("origin/master tip: [not fetched]")
    print("---")

    any_diff = False
    for needle in CHECKS:
        local_has = needle in local_html
        live_has = needle in live_html
        status = "MATCH" if local_has == live_has else "DIFF"
        if status == "DIFF":
            any_diff = True
        print(f"{status:5} | local={str(local_has):5} | live={str(live_has):5} | {needle}")

    print("---")
    if any_diff:
        print("Result: live site does not match the local generated homepage on key checks.")
    else:
        print("Result: live site matches the local generated homepage on key checks.")

    return 1 if any_diff else 0


if __name__ == "__main__":
    sys.exit(main())
