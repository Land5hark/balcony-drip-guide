#!/usr/bin/env python3
from __future__ import annotations

import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POSTS_DIR = ROOT / "content" / "posts"
PUBLIC_POSTS_DIR = ROOT / "public" / "posts"

DATE_RE = re.compile(r'^date\s*=\s*"?([^"\n]+)"?\s*$', re.MULTILINE)
DRAFT_RE = re.compile(r'^draft\s*=\s*(true|false)\s*$', re.MULTILINE)
SLUG_RE = re.compile(r'^slug\s*=\s*"([^"]+)"\s*$', re.MULTILINE)


@dataclass
class CheckResult:
    name: str
    ok: bool
    detail: str


def run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)


def parse_post(path: Path) -> tuple[str, datetime | None, bool]:
    text = path.read_text()
    slug_match = SLUG_RE.search(text)
    slug = slug_match.group(1) if slug_match else path.stem

    date_match = DATE_RE.search(text)
    parsed_date = None
    if date_match:
        raw = date_match.group(1).strip()
        parsed_date = datetime.fromisoformat(raw)
        if parsed_date.tzinfo is None:
            parsed_date = parsed_date.replace(tzinfo=timezone.utc)

    draft_match = DRAFT_RE.search(text)
    draft = draft_match.group(1) == "true" if draft_match else False
    return slug, parsed_date, draft


def check_git_status() -> CheckResult:
    proc = run(["git", "status", "--short", "--branch"])
    if proc.returncode != 0:
        return CheckResult("git status", False, proc.stderr.strip() or "git status failed")
    lines = [line for line in proc.stdout.splitlines() if line.strip()]
    branch = lines[0] if lines else "unknown branch"
    changed = max(len(lines) - 1, 0)
    return CheckResult("git status", True, f"{branch}; {changed} changed/untracked path(s)")


def check_future_dates(now: datetime) -> CheckResult:
    future = []
    live_count = 0
    for path in sorted(POSTS_DIR.glob("*.md")):
        slug, parsed_date, draft = parse_post(path)
        if draft:
            continue
        live_count += 1
        if parsed_date and parsed_date.astimezone(timezone.utc) > now.astimezone(timezone.utc):
            future.append(f"{slug} -> {parsed_date.isoformat()}")
    if future:
        return CheckResult("future-dated posts", False, "; ".join(future))
    return CheckResult("future-dated posts", True, f"0 future-dated live posts across {live_count} live post file(s)")


def check_hugo_build() -> CheckResult:
    proc = run(["hugo", "--minify"])
    if proc.returncode != 0:
        detail = (proc.stdout + "\n" + proc.stderr).strip()
        return CheckResult("hugo build", False, detail[-1200:])
    summary = []
    for line in proc.stdout.splitlines():
        if "Pages" in line or line.startswith("Total in"):
            summary.append(line.strip())
    detail = " | ".join(summary) if summary else "hugo --minify passed"
    return CheckResult("hugo build", True, detail)


def check_public_posts() -> CheckResult:
    if not PUBLIC_POSTS_DIR.exists():
        return CheckResult("public post count", False, "public/posts does not exist")
    count = sum(1 for p in PUBLIC_POSTS_DIR.iterdir() if p.is_dir())
    if count == 0:
        return CheckResult("public post count", False, "0 built post directories found")
    return CheckResult("public post count", True, f"{count} built post directories in public/posts")


def main() -> int:
    now = datetime.now(timezone.utc)
    checks = [
        check_git_status(),
        check_future_dates(now),
        check_hugo_build(),
        check_public_posts(),
    ]

    print("Balcony drip deployment preflight")
    print(f"Root: {ROOT}")
    print(f"Checked at: {now.isoformat()}")
    print()

    failed = False
    for check in checks:
        status = "PASS" if check.ok else "FAIL"
        print(f"[{status}] {check.name}: {check.detail}")
        if not check.ok:
            failed = True

    print()
    print("Result:", "READY FOR MANUAL REVIEW" if not failed else "FIX FAILURES BEFORE PUSH")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
