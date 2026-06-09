#!/usr/bin/env python3
"""Prune noisy short-term recall entries while preserving useful recall state."""

from __future__ import annotations

import json
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent.parent
RECALL_FILE = WORKSPACE / "memory" / ".dreams" / "short-term-recall.json"
LOG_FILE = WORKSPACE / "reports" / "short-term-recall-cleanup.log"

DAILY_MEMORY_TTL = timedelta(days=3)
SESSION_CORPUS_TTL = timedelta(days=2)
MAX_ENTRIES_PER_FILE = 5
MAX_ENTRIES = 200
SOFT_ZERO_TARGET = 150


def parse_time(value: str | None) -> datetime:
    if not value:
        return datetime.fromtimestamp(0, timezone.utc)
    normalized = value.replace("Z", "+00:00")
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return datetime.fromtimestamp(0, timezone.utc)
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def source_class(entry: dict) -> str:
    path = str(entry.get("path") or entry.get("key") or "")
    if "memory/.dreams/session-corpus/" in path:
        return "session_corpus"
    return "daily_memory"


def effective_recall_count(entry: dict) -> int:
    """Return the best-available recall count, falling back to recallDays length."""
    rc = int(entry.get("recallCount") or 0)
    if rc > 0:
        return rc
    rd = len(entry.get("recallDays") or [])
    return rd


def score(entry: dict) -> tuple:
    return (
        effective_recall_count(entry),
        float(entry.get("maxScore") or 0),
        parse_time(entry.get("lastRecalledAt")).timestamp(),
    )


def log(message: str) -> None:
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with LOG_FILE.open("a", encoding="utf-8") as handle:
        handle.write(message.rstrip() + "\n")


def main() -> int:
    if not RECALL_FILE.exists():
        log(f"[{datetime.now(timezone.utc).isoformat()}] No recall file found.")
        print("No recall file found.")
        return 0

    payload = json.loads(RECALL_FILE.read_text(encoding="utf-8"))
    entries = payload.get("entries", {})
    if not isinstance(entries, dict):
        raise SystemExit("short-term recall payload has no entries object")

    now = datetime.now(timezone.utc)
    kept: dict[str, dict] = {}
    age_removed_by_source = {"session_corpus": 0, "daily_memory": 0}
    per_file_removed_by_source = {"session_corpus": 0, "daily_memory": 0}
    cap_removed_by_source = {"session_corpus": 0, "daily_memory": 0}
    ratio_removed_by_source = {"session_corpus": 0, "daily_memory": 0}

    for key, entry in entries.items():
        cls = source_class(entry)
        ttl = SESSION_CORPUS_TTL if cls == "session_corpus" else DAILY_MEMORY_TTL
        first_seen = parse_time(entry.get("firstRecalledAt"))
        if effective_recall_count(entry) == 0 and now - first_seen > ttl:
            age_removed_by_source[cls] += 1
            continue
        kept[key] = entry

    grouped: dict[str, list[tuple[str, dict]]] = defaultdict(list)
    for key, entry in kept.items():
        grouped[str(entry.get("path") or key)].append((key, entry))

    per_file_kept: dict[str, dict] = {}
    for group_entries in grouped.values():
        ordered = sorted(group_entries, key=lambda item: score(item[1]), reverse=True)
        for index, (key, entry) in enumerate(ordered):
            if index < MAX_ENTRIES_PER_FILE:
                per_file_kept[key] = entry
            else:
                per_file_removed_by_source[source_class(entry)] += 1

    kept = per_file_kept
    if len(kept) > MAX_ENTRIES:
        ordered = sorted(kept.items(), key=lambda item: score(item[1]), reverse=True)
        keep_keys = {key for key, _ in ordered[:MAX_ENTRIES]}
        for key, entry in kept.items():
            if key not in keep_keys:
                cap_removed_by_source[source_class(entry)] += 1
        kept = {key: entry for key, entry in ordered[:MAX_ENTRIES]}

    # Fix entries where recallCount is 0 but recallDays is populated.
    # This is a data-quality repair: the memory system should increment both
    # fields when an entry is recalled, but currently only recallDays is set.
    fixed_count = 0
    for key, entry in kept.items():
        rc = int(entry.get("recallCount") or 0)
        rd = len(entry.get("recallDays") or [])
        if rc == 0 and rd > 0:
            entry["recallCount"] = rd
            fixed_count += 1

    zero_recall = [(key, entry) for key, entry in kept.items() if effective_recall_count(entry) == 0]
    if len(zero_recall) > SOFT_ZERO_TARGET:
        zero_ordered = sorted(zero_recall, key=lambda item: score(item[1]))
        remove_count = len(zero_recall) - SOFT_ZERO_TARGET
        remove_keys = {key for key, _ in zero_ordered[:remove_count]}
        for key in remove_keys:
            ratio_removed_by_source[source_class(kept[key])] += 1
            kept.pop(key, None)

    recall_count_zero = sum(1 for entry in kept.values() if int(entry.get("recallCount") or 0) == 0)
    recall_days_only = sum(
        1
        for entry in kept.values()
        if int(entry.get("recallCount") or 0) == 0 and len(entry.get("recallDays") or []) > 0
    )
    effective_zero = sum(1 for entry in kept.values() if effective_recall_count(entry) == 0)

    payload["entries"] = kept
    payload["updatedAt"] = now.isoformat().replace("+00:00", "Z")
    RECALL_FILE.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    age_removed = sum(age_removed_by_source.values())
    per_file_removed = sum(per_file_removed_by_source.values())
    cap_removed = sum(cap_removed_by_source.values())
    ratio_removed = sum(ratio_removed_by_source.values())
    message = (
        f"[{now.isoformat()}] Removed {age_removed + per_file_removed + cap_removed + ratio_removed} entries "
        f"({age_removed} age-based, {per_file_removed} per-file, {cap_removed} cap-enforced, "
        f"{ratio_removed} ratio-pruned). Fixed {fixed_count} recallCount=0 entries. "
        f"Age removed by source: {age_removed_by_source}. "
        f"Per-file removed by source: {per_file_removed_by_source}. "
        f"Cap removed by source: {cap_removed_by_source}. Ratio removed by source: {ratio_removed_by_source}. "
        f"Thresholds: daily=3d, session_corpus=2d, per_file={MAX_ENTRIES_PER_FILE}, "
        f"cap={MAX_ENTRIES}, soft_target={SOFT_ZERO_TARGET}. Kept {len(kept)} entries. "
        f"Recall audit: recallCount_zero={recall_count_zero}, "
        f"recallDays_only={recall_days_only}, effective_zero={effective_zero}."
    )
    log(message)
    print(message)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
