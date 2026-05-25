# FindQuestions fetcher

Local utility for pulling the full JSON topic payload from FindQuestions.com's public API without depending on the email/PDF gate.

## Script
- `passive-income/ops/findquestions_fetch.py`

## What it saves
For each query, the script writes:
- `autocomplete.json`
- `result.json`
- `poll-history.json`
- `summary.md`

It also writes a run-level:
- `manifest.csv`
- `manifest.json`

Default output root:
- `passive-income/reports/findquestions/`

## Example
```bash
passive-income/ops/findquestions_fetch.py \
  --query 'cheap diy watering for balcony plants' \
  --query 'renter friendly balcony watering system' \
  --label balcony-drip-smoke-test
```

## Ranking / shortlist generation
After a fetch run, turn the saved results into a ranked theme/topic shortlist:

```bash
passive-income/ops/findquestions_rank.py \
  passive-income/reports/findquestions/2026-05-03_162558_balcony-drip-smoke-test
```

That writes:
- `ranked/ranked_topics.md`
- `ranked/ranked_topics.csv`
- `ranked/ranked_topics.json`
- `ranked/ranked_themes.csv`

## Article queue generation
Turn ranked outputs into a draft queue with content level, buyer stage, monetization fit, and overlap detection:

```bash
passive-income/ops/findquestions_queue.py \
  passive-income/reports/findquestions/2026-05-03_172152_balcony-drip-batch-1/ranked \
  --existing-topics passive-income/balcony-drip-irrigation/topics.csv
```

That writes:
- `ranked/queue/article_queue.md`
- `ranked/queue/article_queue.csv`
- `ranked/queue/article_queue.json`

## End-to-end runner
Use one command to run fetch → rank → queue:

```bash
passive-income/ops/findquestions_pipeline.py \
  --query-file passive-income/balcony-drip-irrigation/findquestions-seed-queries.txt \
  --label balcony-drip-batch-2 \
  --existing-topics passive-income/balcony-drip-irrigation/topics.csv
```

## Query strategy
Use narrow, problem-first inputs instead of broad category terms.

Good patterns:
- budget / DIY
- renter / no faucet / no tap
- vacation / while away
- balcony containers / patio pots
- comparison phrases for buyer intent

## Best use in our workflow
1. Harvest multiple narrow queries for a niche.
2. Archive raw results under `passive-income/reports/findquestions/`.
3. Compare repeated questions across runs.
4. Run the ranker to surface repeated themes and clustered questions.
5. Run the queue generator to produce publishable candidate articles.
6. Promote repeated intents into:
   - topic maps
   - drafts
   - internal-link plans
   - affiliate roundups

## Note
This is based on public frontend/API behavior only. It is a research capture tool, not a guarantee of backend internals.
