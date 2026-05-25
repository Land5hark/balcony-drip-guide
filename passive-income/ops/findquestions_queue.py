#!/usr/bin/env python3
"""Turn ranked FindQuestions outputs into a draft/article queue."""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


@dataclass
class Candidate:
    title: str
    slug: str
    content_level: str
    content_type: str
    buyer_stage: str
    monetization_fit: str
    priority_score: float
    priority_band: str
    source_theme: str
    source_cluster: str
    repeated_across_queries: int
    evidence_hits: int
    keyword_hint: str
    angle: str
    recommended_cta: str
    existing_overlap: str
    status: str


BUYER_KEYWORDS = {"best", "kit", "kits", "timer", "timers", "system", "systems", "vs", "worth", "cost", "price"}
COMPARISON_KEYWORDS = {"vs", "compare", "comparison", "better"}
PROBLEM_KEYWORDS = {"how", "why", "fix", "prevent", "without", "away", "vacation", "pooling", "clogged", "uneven"}
TECH_KEYWORDS = {"size", "schedule", "frequency", "pressure", "reservoir", "connect", "expand", "winterize"}

THEME_TO_PILLAR = {
    "Buyer guide: kits / systems": "Balcony watering systems",
    "Drip setup and expansion": "Balcony drip setup",
    "Budget DIY watering": "DIY balcony watering",
    "Timers and automation": "Balcony watering automation",
    "No tap / renter constraints": "Renter-friendly balcony watering",
    "Vacation / away watering": "Vacation watering for balcony plants",
    "Hose / soaker options": "Balcony hose and soaker options",
    "Watering frequency and schedules": "Balcony watering schedules",
}


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    slug = re.sub(r"-+", "-", slug)
    return slug[:90].rstrip("-")


def normalize(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9\s]", " ", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def load_existing_titles(path: Path | None) -> tuple[set[str], set[str]]:
    if not path or not path.exists():
        return set(), set()
    titles: set[str] = set()
    slugs: set[str] = set()
    with path.open(encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            keyword = (row.get("primary_keyword") or "").strip()
            slug = (row.get("slug") or "").strip()
            angle = (row.get("angle") or "").strip()
            if keyword:
                titles.add(normalize(keyword))
            if angle:
                titles.add(normalize(angle))
            if slug:
                slugs.add(slug)
    return titles, slugs


def buyer_stage(title: str) -> str:
    t = normalize(title)
    tokens = set(t.split())
    if tokens & COMPARISON_KEYWORDS or tokens & BUYER_KEYWORDS:
        return "buyer"
    if tokens & PROBLEM_KEYWORDS:
        return "problem-aware"
    return "solution-aware"


def content_type(title: str) -> str:
    t = normalize(title)
    tokens = set(t.split())
    if tokens & COMPARISON_KEYWORDS:
        return "comparison"
    if any(x in t for x in ["best ", " top ", " worth", " cost"]):
        return "buyer-guide"
    if tokens & TECH_KEYWORDS:
        return "technical-guide"
    if tokens & PROBLEM_KEYWORDS:
        return "problem-solver"
    return "guide"


def monetization_fit(title: str, theme: str) -> str:
    t = normalize(title)
    if any(x in t for x in ["best", "kit", "timer", "system", "hose", "soaker", "pump", "reservoir"]):
        return "high"
    if theme in {"Buyer guide: kits / systems", "Timers and automation", "Hose / soaker options", "Drip setup and expansion"}:
        return "high"
    if theme in {"Budget DIY watering", "Vacation / away watering", "No tap / renter constraints"}:
        return "medium"
    return "low"


def content_level(title: str, theme: str) -> str:
    t = normalize(title)
    if any(x in t for x in ["best", "systems", "kits", "guide", "cost", "worth"]):
        return "L2 money page"
    if any(x in t for x in ["how to", "without", "vacation", "prevent", "fix", "when", "often"]):
        return "L3 support / problem solver"
    if theme in {"Buyer guide: kits / systems", "Drip setup and expansion", "Timers and automation"}:
        return "L2 money page"
    return "L3 support / problem solver"


def angle_for(theme: str, title: str) -> str:
    t = normalize(title)
    if "without a tap" in t:
        return "Renter-first guide for balconies with no outdoor faucet."
    if "vacation" in t or "away" in t:
        return "Problem-first travel guide with timer/reservoir/backup options."
    if "cost" in t:
        return "Pricing explainer anchored to realistic small-space setups."
    if "best" in t:
        return "Buyer guide focused on small-space fit, reliability, and ease of setup."
    if theme == "Budget DIY watering":
        return "Show the cheapest setups that still work without making the page junky."
    if theme == "Drip setup and expansion":
        return "Technical setup guide with clear parts, limits, and troubleshooting notes."
    return "Search-led practical guide tied to container, balcony, and renter constraints."


def cta_for(theme: str, title: str) -> str:
    t = normalize(title)
    if any(x in t for x in ["best", "timer", "kit", "system", "hose", "soaker"]):
        return "Link to recommended products and core buyer guides."
    if any(x in t for x in ["vacation", "away", "without a tap"]):
        return "Bridge into reservoir, timer, and no-faucet setup product pages."
    if theme == "Drip setup and expansion":
        return "Bridge into fittings, emitters, filters, and expansion parts."
    return "Link to the nearest setup guide plus 1-2 relevant product pages."


def priority_band(score: float) -> str:
    if score >= 28:
        return "P1"
    if score >= 20:
        return "P2"
    if score >= 14:
        return "P3"
    return "P4"


def theme_priority_boost(theme: str) -> float:
    boosts = {
        "Buyer guide: kits / systems": 4.0,
        "Drip setup and expansion": 3.5,
        "Budget DIY watering": 3.0,
        "Timers and automation": 3.0,
        "No tap / renter constraints": 2.5,
        "Vacation / away watering": 2.5,
        "Hose / soaker options": 2.0,
        "Watering frequency and schedules": 1.5,
    }
    return boosts.get(theme, 1.0)


def build_pillar_candidates(theme_rows: list[dict[str, str]], existing_titles: set[str], existing_slugs: set[str]) -> list[Candidate]:
    candidates: list[Candidate] = []
    for row in theme_rows:
        label = row["theme_label"]
        if label == "General balcony/container watering":
            continue
        pillar = THEME_TO_PILLAR.get(label)
        if not pillar:
            continue
        slug = slugify(pillar)
        overlap = "existing-ish" if normalize(pillar) in existing_titles or slug in existing_slugs else "new"
        base_score = float(row["score"])
        score = round(base_score + 6.0, 2)
        candidates.append(Candidate(
            title=pillar,
            slug=slug,
            content_level="L1 pillar / hub",
            content_type="pillar",
            buyer_stage="mixed",
            monetization_fit="high" if label in {"Buyer guide: kits / systems", "Timers and automation", "Drip setup and expansion"} else "medium",
            priority_score=score,
            priority_band=priority_band(score),
            source_theme=label,
            source_cluster="theme-derived",
            repeated_across_queries=int(row["unique_query_count"]),
            evidence_hits=int(row["question_count"]),
            keyword_hint=label,
            angle=f"Hub page that organizes the {label.lower()} lane for balcony/patio/container setups.",
            recommended_cta="Link out to best-fit setup guides, buyer guides, and troubleshooting articles.",
            existing_overlap=overlap,
            status="candidate",
        ))
    return candidates


def build_cluster_candidates(topic_rows: list[dict[str, str]], existing_titles: set[str], existing_slugs: set[str]) -> list[Candidate]:
    candidates: list[Candidate] = []
    for row in topic_rows:
        title = row["label"].strip()
        theme_guess = row.get("theme_guess", "")
        slug = slugify(title)
        overlap = "existing-ish" if normalize(title) in existing_titles or slug in existing_slugs else "new"
        base = float(row["score"])
        uq = int(row["unique_query_count"])
        qh = int(row["question_count"])
        theme = theme_guess or row.get("lane", "")
        score = round(base + theme_priority_boost(theme_guess), 2)
        candidates.append(Candidate(
            title=title,
            slug=slug,
            content_level=content_level(title, theme_guess),
            content_type=content_type(title),
            buyer_stage=buyer_stage(title),
            monetization_fit=monetization_fit(title, theme_guess),
            priority_score=score,
            priority_band=priority_band(score),
            source_theme=theme_guess,
            source_cluster=title,
            repeated_across_queries=uq,
            evidence_hits=qh,
            keyword_hint=row.get("keyword_signature", ""),
            angle=angle_for(theme_guess, title),
            recommended_cta=cta_for(theme_guess, title),
            existing_overlap=overlap,
            status="candidate",
        ))
    return candidates


def assign_theme(topic_rows: list[dict[str, str]], theme_rows: list[dict[str, str]]) -> None:
    theme_lookup = [(row["theme_label"], set(normalize(row["examples"]).split(" | ")) if False else None) for row in theme_rows]
    theme_keywords: dict[str, set[str]] = {}
    for row in theme_rows:
        examples = row.get("examples", "")
        tokens = set()
        for part in examples.split(" | "):
            tokens |= set(normalize(part).split())
        theme_keywords[row["theme_label"]] = tokens

    for row in topic_rows:
        label_tokens = set(normalize(row["label"]).split()) | set(normalize(row.get("keyword_signature", "")).split())
        best_theme = ""
        best_score = -1
        for theme_label, tokens in theme_keywords.items():
            score = len(label_tokens & tokens)
            if score > best_score:
                best_score = score
                best_theme = theme_label
        row["theme_guess"] = best_theme


def dedupe_candidates(candidates: list[Candidate]) -> list[Candidate]:
    best_by_slug: dict[str, Candidate] = {}
    for cand in candidates:
        existing = best_by_slug.get(cand.slug)
        if existing is None or cand.priority_score > existing.priority_score:
            best_by_slug[cand.slug] = cand
    rows = list(best_by_slug.values())
    rows.sort(key=lambda c: (c.existing_overlap == "existing-ish", -c.priority_score, c.title.lower()))
    return rows


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def write_outputs(out_dir: Path, candidates: list[Candidate]) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    rows = [c.__dict__ for c in candidates]
    with (out_dir / "article_queue.csv").open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    (out_dir / "article_queue.json").write_text(json.dumps(rows, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    sections = [
        "# FindQuestions article queue",
        "",
        f"- generated_at: {datetime.utcnow().isoformat()}Z",
        f"- candidate_count: {len(candidates)}",
        "",
        "## Top priorities",
        "",
    ]
    for idx, c in enumerate(candidates[:25], start=1):
        sections += [
            f"### {idx}. {c.title}",
            f"- priority_band: {c.priority_band}",
            f"- priority_score: {c.priority_score}",
            f"- content_level: {c.content_level}",
            f"- content_type: {c.content_type}",
            f"- buyer_stage: {c.buyer_stage}",
            f"- monetization_fit: {c.monetization_fit}",
            f"- source_theme: {c.source_theme}",
            f"- repeated_across_queries: {c.repeated_across_queries}",
            f"- evidence_hits: {c.evidence_hits}",
            f"- existing_overlap: {c.existing_overlap}",
            f"- keyword_hint: {c.keyword_hint}",
            f"- angle: {c.angle}",
            f"- recommended_cta: {c.recommended_cta}",
            "",
        ]
    (out_dir / "article_queue.md").write_text("\n".join(sections), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ranked_dir", help="Directory containing ranked_topics.csv and ranked_themes.csv")
    parser.add_argument("--existing-topics", help="Existing topics.csv to use for overlap detection")
    parser.add_argument("--output-dir", help="Output dir. Defaults to <ranked_dir>/queue")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    ranked_dir = Path(args.ranked_dir).expanduser().resolve()
    topics_path = ranked_dir / "ranked_topics.csv"
    themes_path = ranked_dir / "ranked_themes.csv"
    if not topics_path.exists() or not themes_path.exists():
        raise SystemExit("ranked_topics.csv and ranked_themes.csv are required in ranked_dir")

    topic_rows = read_csv_rows(topics_path)
    theme_rows = read_csv_rows(themes_path)
    assign_theme(topic_rows, theme_rows)

    existing_titles, existing_slugs = load_existing_titles(Path(args.existing_topics).expanduser().resolve() if args.existing_topics else None)

    candidates = []
    candidates.extend(build_pillar_candidates(theme_rows, existing_titles, existing_slugs))
    candidates.extend(build_cluster_candidates(topic_rows, existing_titles, existing_slugs))
    candidates = dedupe_candidates(candidates)

    out_dir = Path(args.output_dir).expanduser().resolve() if args.output_dir else ranked_dir / "queue"
    write_outputs(out_dir, candidates)
    print(f"Wrote queue outputs to: {out_dir}")
    print(f"Candidates: {len(candidates)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
