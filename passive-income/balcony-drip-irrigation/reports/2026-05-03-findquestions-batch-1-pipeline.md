# FindQuestions batch 1 pipeline

Date: 2026-05-03

## What was built
A reusable local research pipeline for harvesting and ranking FindQuestions topic data.

### Scripts
- `passive-income/ops/findquestions_fetch.py`
- `passive-income/ops/findquestions_rank.py`

### Docs / seed list
- `passive-income/ops/findquestions-README.md`
- `passive-income/balcony-drip-irrigation/findquestions-seed-queries.txt`

## Batch 1 run
Raw fetch run:
- `passive-income/reports/findquestions/2026-05-03_172152_balcony-drip-batch-1/`

Ranked outputs:
- `passive-income/reports/findquestions/2026-05-03_172152_balcony-drip-batch-1/ranked/ranked_topics.md`
- `passive-income/reports/findquestions/2026-05-03_172152_balcony-drip-batch-1/ranked/ranked_themes.csv`
- `passive-income/reports/findquestions/2026-05-03_172152_balcony-drip-batch-1/ranked/ranked_topics.csv`

## Batch 1 scale
- queries: 12
- raw question rows captured: 480
- fuzzy question clusters: 389

## Highest-signal themes from batch 1
1. Buyer guide: kits / systems
2. Drip setup and expansion
3. Budget DIY watering
4. Timers and automation
5. No tap / renter constraints
6. Vacation / away watering
7. Hose / soaker options
8. Watering frequency and schedules

## What this unlocks
This is now usable as a standing research primitive for:
- random niche idea validation
- content planning
- article-brief generation
- internal-link cluster discovery
- buyer-guide / affiliate adjacency research

## Recommended next step
Add one more layer that takes ranked themes + repeated questions and emits:
- proposed article titles
- cluster assignment
- likely intent stage
- monetization fit
- draft priority

That would turn the pipeline from research capture into a direct article-queue generator.
