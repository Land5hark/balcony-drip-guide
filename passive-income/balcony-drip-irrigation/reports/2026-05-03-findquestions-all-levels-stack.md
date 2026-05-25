# FindQuestions all-levels stack

Date: 2026-05-03

## Built layers

### 1. Raw capture
- Script: `passive-income/ops/findquestions_fetch.py`
- Purpose: fetch autocomplete + full result JSON + poll history for arbitrary queries.

### 2. Theme and cluster ranking
- Script: `passive-income/ops/findquestions_rank.py`
- Purpose: dedupe overlapping question variants and surface repeated themes + question clusters.

### 3. Article queue generation
- Script: `passive-income/ops/findquestions_queue.py`
- Purpose: convert ranked outputs into candidate articles with:
  - content level
  - content type
  - buyer stage
  - monetization fit
  - priority score / band
  - overlap check against existing `topics.csv`

### 4. End-to-end runner
- Script: `passive-income/ops/findquestions_pipeline.py`
- Purpose: run fetch -> rank -> queue in one command.

### 5. Docs + query seeds
- `passive-income/ops/findquestions-README.md`
- `passive-income/balcony-drip-irrigation/findquestions-seed-queries.txt`

## Verified runs

### Full balcony batch
- raw run: `passive-income/reports/findquestions/2026-05-03_172152_balcony-drip-batch-1/`
- ranked: `passive-income/reports/findquestions/2026-05-03_172152_balcony-drip-batch-1/ranked/`
- queue: `passive-income/reports/findquestions/2026-05-03_172152_balcony-drip-batch-1/ranked/queue/`

Batch stats:
- queries: 12
- raw question rows: 480
- clustered topic rows: 389
- queued candidates: 397

### Pipeline smoke test
- run: `passive-income/reports/findquestions/2026-05-03_173405_pipeline-smoke/`

Verified that the one-command pipeline produced:
- fetch outputs
- ranked outputs
- queue outputs

## Operational result
FindQuestions is now usable as a standing research/content primitive for:
- random niche validation
- balcony drip irrigation content expansion
- future niche topic mining
- queue generation for drafts and buyer guides

## Most useful next layer
Add a promotion step that converts the queue into:
- shortlist by publication window
- article brief stubs
- internal-link targets
- affiliate target set per article

That would make the stack go from research pipeline to near-direct publishing queue.
