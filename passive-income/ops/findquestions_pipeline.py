#!/usr/bin/env python3
"""Run the full FindQuestions pipeline: fetch -> rank -> queue."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

ROOT = Path("/home/linuxlite/.openclaw/workspace/passive-income/ops")
FETCH = ROOT / "findquestions_fetch.py"
RANK = ROOT / "findquestions_rank.py"
QUEUE = ROOT / "findquestions_queue.py"
DEFAULT_REPORT_ROOT = Path("/home/linuxlite/.openclaw/workspace/passive-income/reports/findquestions")


def run(cmd: list[str]) -> None:
    print("$", " ".join(cmd))
    subprocess.run(cmd, check=True)


def newest_run(report_root: Path, label_fragment: str) -> Path:
    matches = sorted(
        [p for p in report_root.iterdir() if p.is_dir() and label_fragment in p.name],
        key=lambda p: p.name,
    )
    if not matches:
        raise FileNotFoundError(f"No run directory found in {report_root} matching {label_fragment!r}")
    return matches[-1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query", action="append", help="Query to fetch. Repeat for multiple.")
    parser.add_argument("--query-file", help="File containing queries.")
    parser.add_argument("--label", required=True, help="Short label for this pipeline run.")
    parser.add_argument("--delay", type=int, default=2)
    parser.add_argument("--timeout", type=int, default=90)
    parser.add_argument("--report-root", default=str(DEFAULT_REPORT_ROOT))
    parser.add_argument("--existing-topics", help="topics.csv for overlap detection in queue generation.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    report_root = Path(args.report_root).expanduser().resolve()

    fetch_cmd = [str(FETCH), "--label", args.label, "--delay", str(args.delay), "--timeout", str(args.timeout), "--output-dir", str(report_root)]
    if args.query_file:
        fetch_cmd += ["--query-file", args.query_file]
    for q in args.query or []:
        fetch_cmd += ["--query", q]
    if not args.query and not args.query_file:
        raise SystemExit("Provide at least one --query or a --query-file.")

    run(fetch_cmd)
    run_dir = newest_run(report_root, args.label.replace(" ", "-"))

    rank_cmd = [str(RANK), str(run_dir)]
    run(rank_cmd)

    ranked_dir = run_dir / "ranked"
    queue_cmd = [str(QUEUE), str(ranked_dir)]
    if args.existing_topics:
        queue_cmd += ["--existing-topics", args.existing_topics]
    run(queue_cmd)

    print(f"\nPipeline complete. Run dir: {run_dir}")
    print(f"Ranked dir: {ranked_dir}")
    print(f"Queue dir: {ranked_dir / 'queue'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
