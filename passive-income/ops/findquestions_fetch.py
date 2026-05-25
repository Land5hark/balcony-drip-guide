#!/usr/bin/env python3
"""Fetch topic-report data from FindQuestions.com's public API.

This is meant for research use inside the passive-income workflow.
It pulls the full JSON payload that backs the site's gated preview flow,
so we can archive query results without depending on PDF/email delivery.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

BASE_URL = "https://findquestions.com"
USER_AGENT = "SpikeFindQuestionsFetcher/1.0"
DEFAULT_DELAY_SECONDS = 8
DEFAULT_TIMEOUT_SECONDS = 240


class FetchError(RuntimeError):
    pass


def slugify(value: str, max_len: int = 80) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    slug = re.sub(r"-+", "-", slug)
    return (slug[:max_len].rstrip("-")) or "query"


def request_json(method: str, path: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
    data = None
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json",
    }
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"

    req = Request(BASE_URL + path, data=data, headers=headers, method=method)
    try:
        with urlopen(req, timeout=30) as resp:
            text = resp.read().decode("utf-8", errors="replace")
    except HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise FetchError(f"HTTP {exc.code} for {path}: {body[:400]}") from exc
    except URLError as exc:
        raise FetchError(f"Network error for {path}: {exc}") from exc

    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise FetchError(f"Non-JSON response for {path}: {text[:400]}") from exc


def fetch_autocomplete(query: str) -> list[str]:
    req = Request(
        f"{BASE_URL}/api/autocomplete?q={quote(query)}",
        headers={"User-Agent": USER_AGENT, "Accept": "application/json"},
        method="GET",
    )
    try:
        with urlopen(req, timeout=30) as resp:
            text = resp.read().decode("utf-8", errors="replace")
        data = json.loads(text)
    except Exception as exc:  # best-effort only
        print(f"warn: autocomplete failed for {query!r}: {exc}", file=sys.stderr)
        return []
    suggestions = data.get("suggestions")
    return suggestions if isinstance(suggestions, list) else []


def start_search(query: str) -> dict[str, Any]:
    return request_json("POST", "/api/search", {"business": query})


def check_status(query: str) -> dict[str, Any]:
    return request_json("POST", "/api/search-status", {"business": query})


def resolve_result(query: str, delay_seconds: int, timeout_seconds: int) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    started = time.time()
    history: list[dict[str, Any]] = []

    initial = start_search(query)
    history.append({
        "ts": datetime.now(timezone.utc).isoformat(),
        "stage": "search",
        "response": initial,
    })

    if initial.get("questions"):
        return initial, history

    while True:
        if time.time() - started > timeout_seconds:
            raise FetchError(f"Timed out waiting for query {query!r}")

        time.sleep(delay_seconds)
        status = check_status(query)
        history.append({
            "ts": datetime.now(timezone.utc).isoformat(),
            "stage": "status",
            "response": status,
        })

        if status.get("questions") or status.get("status") == "complete":
            return status, history
        if status.get("status") == "failed":
            raise FetchError(f"Backend marked query failed: {query!r}")


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def write_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def build_markdown(query: str, autocomplete: list[str], result: dict[str, Any]) -> str:
    questions = result.get("questions") or []
    bonus = result.get("bonus_topics") or []
    subreddits = result.get("subreddits") or []
    sources = result.get("sources") or []

    lines = [
        f"# FindQuestions result: {query}",
        "",
        f"- fetched_at_utc: {datetime.now(timezone.utc).isoformat()}",
        f"- cached: {result.get('cached')}",
        f"- question_count: {len(questions)}",
        f"- autocomplete_suggestions: {len(autocomplete)}",
        "",
    ]

    if autocomplete:
        lines += ["## Autocomplete suggestions", ""]
        lines += [f"- {item}" for item in autocomplete]
        lines += [""]

    if questions:
        lines += ["## Questions", ""]
        for idx, item in enumerate(questions, start=1):
            q = item.get("question", "").strip()
            intent = item.get("search_intent", "").strip()
            if intent:
                lines.append(f"{idx}. {q} — {intent}")
            else:
                lines.append(f"{idx}. {q}")
        lines += [""]

    if bonus:
        lines += ["## Bonus topics", ""]
        lines += [f"- {item}" for item in bonus]
        lines += [""]

    if subreddits:
        lines += ["## Subreddits", ""]
        lines += [f"- r/{item}" if not str(item).startswith("r/") else f"- {item}" for item in subreddits]
        lines += [""]

    if sources:
        lines += ["## Sources", ""]
        for item in sources:
            subreddit = item.get("subreddit", "")
            url = item.get("url", "")
            if subreddit or url:
                lines.append(f"- {subreddit}: {url}")
        lines += [""]

    return "\n".join(lines).rstrip() + "\n"


def load_queries(args: argparse.Namespace) -> list[str]:
    queries: list[str] = []
    if args.query:
        queries.extend(args.query)
    if args.query_file:
        for line in Path(args.query_file).read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                queries.append(line)
    deduped: list[str] = []
    seen: set[str] = set()
    for item in queries:
        key = item.strip()
        if key and key not in seen:
            seen.add(key)
            deduped.append(key)
    return deduped


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query", action="append", help="Query phrase to fetch. Repeat for multiple.")
    parser.add_argument("--query-file", help="Path to a newline-delimited file of queries.")
    parser.add_argument(
        "--output-dir",
        default="/home/linuxlite/.openclaw/workspace/passive-income/reports/findquestions",
        help="Directory where timestamped results should be written.",
    )
    parser.add_argument("--label", default="run", help="Short label for this run directory.")
    parser.add_argument("--delay", type=int, default=DEFAULT_DELAY_SECONDS, help="Poll interval in seconds.")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT_SECONDS, help="Per-query timeout in seconds.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    queries = load_queries(args)
    if not queries:
        print("error: provide at least one --query or a --query-file", file=sys.stderr)
        return 2

    stamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    run_dir = Path(args.output_dir) / f"{stamp}_{slugify(args.label, 40)}"
    ensure_dir(run_dir)

    manifest_rows: list[dict[str, Any]] = []

    for query in queries:
        slug = slugify(query)
        print(f"==> {query}")
        query_dir = run_dir / slug
        ensure_dir(query_dir)

        autocomplete = fetch_autocomplete(query)
        try:
            result, history = resolve_result(query, args.delay, args.timeout)
            status = "ok"
            error = ""
        except Exception as exc:
            result = {"business": query}
            history = []
            status = "error"
            error = str(exc)
            print(f"error: {query}: {exc}", file=sys.stderr)

        write_json(query_dir / "autocomplete.json", {"query": query, "suggestions": autocomplete})
        write_json(query_dir / "result.json", result)
        write_json(query_dir / "poll-history.json", history)
        (query_dir / "summary.md").write_text(build_markdown(query, autocomplete, result), encoding="utf-8")

        manifest_rows.append({
            "query": query,
            "slug": slug,
            "status": status,
            "error": error,
            "cached": result.get("cached"),
            "question_count": len(result.get("questions") or []),
            "subreddit_count": len(result.get("subreddits") or []),
            "suggestion_count": len(autocomplete),
            "dir": str(query_dir),
        })

    manifest_path = run_dir / "manifest.csv"
    with manifest_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=["query", "slug", "status", "error", "cached", "question_count", "subreddit_count", "suggestion_count", "dir"],
        )
        writer.writeheader()
        writer.writerows(manifest_rows)

    write_json(run_dir / "manifest.json", manifest_rows)

    print(f"\nSaved run to: {run_dir}")
    print(f"Manifest: {manifest_path}")
    return 0 if all(row["status"] == "ok" for row in manifest_rows) else 1


if __name__ == "__main__":
    raise SystemExit(main())
