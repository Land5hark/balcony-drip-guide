#!/usr/bin/env python3
"""Aggregate FindQuestions runs into a deduped ranked topic shortlist."""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from dataclasses import dataclass, field
from datetime import datetime
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

COMMON_STOPWORDS = {
    "a", "an", "and", "are", "at", "be", "best", "better", "can", "cost", "could",
    "do", "does", "for", "from", "get", "how", "i", "if", "in", "is", "it", "its",
    "my", "need", "of", "on", "or", "really", "should", "so", "system", "that", "the",
    "their", "this", "to", "use", "what", "when", "while", "with", "without", "you", "your",
    "balcony", "balconies", "plant", "plants", "watering", "water", "garden", "gardens",
    "container", "containers", "apartment", "apartments",
}

BUYER_WORDS = {
    "best", "kit", "kits", "timer", "timers", "system", "systems", "cost", "worth", "vs",
    "compare", "comparison", "hose", "pump", "solar", "budget", "price", "setup",
}

PAIN_WORDS = {
    "away", "vacation", "without", "clogged", "problem", "problems", "fix", "prevent", "stop",
    "pooling", "neighbors", "drying", "dry", "uneven", "leak", "leaky", "overwatering",
}

DIY_WORDS = {"diy", "cheap", "budget", "bucket", "gravity", "make", "build"}
RENTER_WORDS = {"apartment", "balcony", "renters", "renter", "rental", "tap", "faucet", "neighbors"}
TECH_WORDS = {"flow", "pressure", "reservoir", "emitters", "drip", "lines", "schedule", "frequency"}

THEME_RULES: list[tuple[str, str, set[str]]] = [
    ("vacation-watering", "Vacation / away watering", {"vacation", "away", "traveling", "alive"}),
    ("budget-diy", "Budget DIY watering", {"budget", "cheap", "diy", "bucket", "gravity"}),
    ("no-tap-renter", "No tap / renter constraints", {"tap", "faucet", "renters", "rental", "neighbors", "pooling"}),
    ("kit-buyer", "Buyer guide: kits / systems", {"best", "kit", "kits", "systems", "worth"}),
    ("hose-soaker", "Hose / soaker options", {"hose", "soaker", "adapters"}),
    ("drip-setup", "Drip setup and expansion", {"drip", "irrigation", "lines", "emitters", "reservoir"}),
    ("timers-automation", "Timers and automation", {"timer", "timers", "smart", "automate", "automation", "plug"}),
    ("watering-frequency", "Watering frequency and schedules", {"often", "schedule", "frequency"}),
]


@dataclass
class QuestionItem:
    query: str
    question: str
    intent: str
    source_path: str
    question_norm: str
    token_set: set[str]


@dataclass
class TopicCluster:
    items: list[QuestionItem] = field(default_factory=list)
    token_counter: Counter = field(default_factory=Counter)

    def add(self, item: QuestionItem) -> None:
        self.items.append(item)
        self.token_counter.update(item.token_set)

    @property
    def question_count(self) -> int:
        return len(self.items)

    @property
    def unique_queries(self) -> list[str]:
        return sorted({item.query for item in self.items})

    @property
    def unique_query_count(self) -> int:
        return len(self.unique_queries)

    @property
    def intents(self) -> list[str]:
        return [item.intent for item in self.items if item.intent]

    @property
    def label(self) -> str:
        counts = Counter(item.question for item in self.items)
        ranked = sorted(counts.items(), key=lambda kv: (-kv[1], len(kv[0]), kv[0].lower()))
        return ranked[0][0]

    @property
    def keyword_signature(self) -> str:
        tokens = [token for token, _ in self.token_counter.most_common(6)]
        return ", ".join(tokens)

    def lane(self) -> str:
        tokens = set(self.token_counter)
        if tokens & BUYER_WORDS:
            return "buyer"
        if tokens & PAIN_WORDS:
            return "pain-point"
        if tokens & DIY_WORDS:
            return "diy-budget"
        if tokens & RENTER_WORDS:
            return "renter-small-space"
        if tokens & TECH_WORDS:
            return "technical-setup"
        return "general"

    def score(self) -> float:
        tokens = set(self.token_counter)
        score = 0.0
        score += self.unique_query_count * 4.0
        score += self.question_count * 1.5
        if tokens & BUYER_WORDS:
            score += 2.5
        if tokens & PAIN_WORDS:
            score += 2.0
        if tokens & DIY_WORDS:
            score += 1.5
        if tokens & RENTER_WORDS:
            score += 1.0
        if any(word in self.label.lower() for word in ["best", "how to", "how do", "what", "can i"]):
            score += 0.5
        return round(score, 2)

    def representative_intent(self) -> str:
        intents = Counter(self.intents)
        return intents.most_common(1)[0][0] if intents else ""

    def related_questions(self, limit: int = 5) -> list[str]:
        counts = Counter(item.question for item in self.items)
        return [q for q, _ in counts.most_common(limit)]


def slugify(value: str, max_len: int = 80) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    slug = re.sub(r"-+", "-", slug)
    return (slug[:max_len].rstrip("-")) or "run"


def normalize_text(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def token_set(text: str) -> set[str]:
    words = normalize_text(text).split()
    return {w for w in words if len(w) > 2 and w not in COMMON_STOPWORDS}


def similarity(a: QuestionItem, b: QuestionItem) -> float:
    if not a.token_set or not b.token_set:
        return 0.0
    jaccard = len(a.token_set & b.token_set) / len(a.token_set | b.token_set)
    seq = SequenceMatcher(None, a.question_norm, b.question_norm).ratio()
    contains = 1.0 if a.question_norm in b.question_norm or b.question_norm in a.question_norm else 0.0
    same_query_family = 1.0 if any(tok in a.token_set and tok in b.token_set for tok in {"vacation", "away", "budget", "diy", "hose", "tap", "faucet", "drip", "timer", "soaker", "gravity", "renters", "rental", "pooling"}) else 0.0
    return max(jaccard, seq * 0.82, contains * 0.72, (jaccard * 0.8) + (same_query_family * 0.2))


def cluster_items(items: list[QuestionItem], threshold: float = 0.62) -> list[TopicCluster]:
    clusters: list[TopicCluster] = []
    for item in items:
        best_cluster = None
        best_score = 0.0
        for cluster in clusters:
            rep = cluster.items[0]
            score = similarity(item, rep)
            if score > best_score:
                best_score = score
                best_cluster = cluster
        if best_cluster is not None and best_score >= threshold:
            best_cluster.add(item)
        else:
            cluster = TopicCluster()
            cluster.add(item)
            clusters.append(cluster)
    return clusters


def discover_result_files(run_dirs: list[Path]) -> list[Path]:
    files: list[Path] = []
    for run_dir in run_dirs:
        if (run_dir / "manifest.json").exists():
            files.extend(sorted(run_dir.glob("*/result.json")))
        elif run_dir.name == "result.json":
            files.append(run_dir)
        else:
            files.extend(sorted(run_dir.rglob("result.json")))
    return sorted(set(files))


def detect_themes(item: QuestionItem) -> list[tuple[str, str]]:
    text_tokens = item.token_set | set(normalize_text(item.question).split()) | set(normalize_text(item.intent).split())
    found: list[tuple[str, str]] = []
    for slug, label, keywords in THEME_RULES:
        if text_tokens & keywords:
            found.append((slug, label))
    if not found:
        found.append(("general", "General balcony/container watering"))
    return found


def load_items(result_files: list[Path]) -> tuple[list[QuestionItem], list[str]]:
    items: list[QuestionItem] = []
    bonus_topics: list[str] = []
    for path in result_files:
        data = json.loads(path.read_text(encoding="utf-8"))
        query = data.get("business") or path.parent.name
        for bonus in data.get("bonus_topics") or []:
            if isinstance(bonus, str):
                bonus_topics.append(bonus)
        for raw in data.get("questions") or []:
            question = (raw.get("question") or "").strip()
            intent = (raw.get("search_intent") or raw.get("search_Intent") or "").strip()
            if not question:
                continue
            items.append(QuestionItem(
                query=query,
                question=question,
                intent=intent,
                source_path=str(path),
                question_norm=normalize_text(question),
                token_set=token_set(question + " " + intent),
            ))
    return items, bonus_topics


def build_theme_rows(items: list[QuestionItem]) -> list[dict[str, Any]]:
    theme_map: dict[str, dict[str, Any]] = {}
    for item in items:
        for slug, label in detect_themes(item):
            row = theme_map.setdefault(slug, {
                "theme_slug": slug,
                "theme_label": label,
                "query_set": set(),
                "question_count": 0,
                "examples": [],
            })
            row["query_set"].add(item.query)
            row["question_count"] += 1
            if len(row["examples"]) < 5 and item.question not in row["examples"]:
                row["examples"].append(item.question)

    rows: list[dict[str, Any]] = []
    for row in theme_map.values():
        unique_query_count = len(row["query_set"])
        score = round(unique_query_count * 4 + row["question_count"] * 1.2, 2)
        rows.append({
            "theme_slug": row["theme_slug"],
            "theme_label": row["theme_label"],
            "unique_query_count": unique_query_count,
            "question_count": row["question_count"],
            "score": score,
            "queries": sorted(row["query_set"]),
            "examples": row["examples"],
        })
    rows.sort(key=lambda r: (r["theme_slug"] == "general", -r["score"], -r["unique_query_count"], -r["question_count"], r["theme_label"].lower()))
    return rows


def build_markdown(run_dirs: list[Path], clusters: list[TopicCluster], bonus_topics: list[str], limit: int, theme_rows: list[dict[str, Any]]) -> str:
    lines = [
        "# FindQuestions ranked topic shortlist",
        "",
        f"- generated_at: {datetime.utcnow().isoformat()}Z",
        f"- run_count: {len(run_dirs)}",
        f"- cluster_count: {len(clusters)}",
        f"- question_count: {sum(c.question_count for c in clusters)}",
        "",
        "## Top themes",
        "",
    ]
    for idx, row in enumerate(theme_rows[:12], start=1):
        lines += [
            f"### {idx}. {row['theme_label']}",
            f"- score: {row['score']}",
            f"- repeated_across_queries: {row['unique_query_count']}",
            f"- total_hits: {row['question_count']}",
            "- queries:",
        ]
        lines += [f"  - {q}" for q in row["queries"]]
        lines.append("- example_questions:")
        lines += [f"  - {q}" for q in row["examples"]]
        lines.append("")

    lines += ["## Top question clusters", ""]
    for idx, cluster in enumerate(clusters[:limit], start=1):
        lines += [
            f"### {idx}. {cluster.label}",
            f"- score: {cluster.score()}",
            f"- lane: {cluster.lane()}",
            f"- repeated_across_queries: {cluster.unique_query_count}",
            f"- total_hits: {cluster.question_count}",
            f"- representative_intent: {cluster.representative_intent()}",
            f"- keyword_signature: {cluster.keyword_signature}",
            "- queries:",
        ]
        lines += [f"  - {q}" for q in cluster.unique_queries]
        related = cluster.related_questions(5)
        if related:
            lines.append("- related_questions:")
            lines += [f"  - {q}" for q in related]
        lines.append("")

    if bonus_topics:
        bonus_counts = Counter(bonus_topics)
        lines += ["## Repeated bonus topics", ""]
        for topic, count in bonus_counts.most_common(15):
            lines.append(f"- {topic} ({count})")
        lines.append("")

    return "\n".join(lines)


def write_outputs(out_dir: Path, clusters: list[TopicCluster], bonus_topics: list[str], run_dirs: list[Path], limit: int, theme_rows: list[dict[str, Any]]) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)

    rows = []
    for cluster in clusters:
        rows.append({
            "label": cluster.label,
            "score": cluster.score(),
            "lane": cluster.lane(),
            "unique_query_count": cluster.unique_query_count,
            "question_count": cluster.question_count,
            "representative_intent": cluster.representative_intent(),
            "keyword_signature": cluster.keyword_signature,
            "queries": " | ".join(cluster.unique_queries),
            "related_questions": " | ".join(cluster.related_questions(5)),
        })

    with (out_dir / "ranked_topics.csv").open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "label", "score", "lane", "unique_query_count", "question_count",
                "representative_intent", "keyword_signature", "queries", "related_questions",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    with (out_dir / "ranked_themes.csv").open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=["theme_slug", "theme_label", "score", "unique_query_count", "question_count", "queries", "examples"],
        )
        writer.writeheader()
        writer.writerows({
            **row,
            "queries": " | ".join(row["queries"]),
            "examples": " | ".join(row["examples"]),
        } for row in theme_rows)

    payload = {
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "run_dirs": [str(p) for p in run_dirs],
        "themes": theme_rows,
        "clusters": rows,
        "bonus_topics": Counter(bonus_topics).most_common(),
    }
    (out_dir / "ranked_topics.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (out_dir / "ranked_topics.md").write_text(build_markdown(run_dirs, clusters, bonus_topics, limit, theme_rows), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dirs", nargs="+", help="One or more FindQuestions run directories or result.json paths.")
    parser.add_argument(
        "--output-dir",
        help="Where to write ranked outputs. Defaults to <first_run>/ranked/",
    )
    parser.add_argument("--limit", type=int, default=20, help="Top clusters to include in markdown summary.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    run_dirs = [Path(p).expanduser().resolve() for p in args.run_dirs]
    result_files = discover_result_files(run_dirs)
    if not result_files:
        raise SystemExit("No result.json files found in the provided paths.")

    items, bonus_topics = load_items(result_files)
    if not items:
        raise SystemExit("No questions found in the provided result files.")

    theme_rows = build_theme_rows(items)
    clusters = cluster_items(items)
    clusters.sort(key=lambda c: (-c.score(), -c.unique_query_count, -c.question_count, c.label.lower()))

    if args.output_dir:
        out_dir = Path(args.output_dir).expanduser().resolve()
    else:
        base = run_dirs[0] if run_dirs[0].is_dir() else run_dirs[0].parent
        out_dir = base / "ranked"

    write_outputs(out_dir, clusters, bonus_topics, run_dirs, args.limit, theme_rows)
    print(f"Wrote ranked outputs to: {out_dir}")
    print(f"Clusters: {len(clusters)} | Questions: {len(items)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
