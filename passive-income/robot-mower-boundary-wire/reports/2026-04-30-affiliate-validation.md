- Lane: Affiliate Validator
- Status: FAIL
- Niche: robot lawn mower boundary-wire setup, troubleshooting, and accessories
- Topic / Program / Scope: affiliate-program viability for this niche only
- Trigger: follow-up from 2026-04-30 niche scout primary recommendation
- Timestamp: 2026-04-30 15:46 EDT

## Inputs received
- `passive-income/ops/lane-prompts/affiliate-validator.md`
- `passive-income/ops/hermes-lane-run-template.md`
- `passive-income/ops/affiliate-program-scorecard.md`
- `passive-income/ops/passive-income-machine-process.md`
- `passive-income/reports/2026-04-30-niche-scout-fresh-start.md`

## Work performed
1. Pulled the lane rules and scorecard, then constrained the run to affiliate validation only.
2. Checked 5 merchant/program candidates that were plausible for the niche: Husqvarna direct, Worx direct, Amazon Associates, Walmart Creator, and eBay Partner Network.
3. Verified public program existence where possible, scored each candidate, updated `affiliate-programs.csv`, and made a niche-level pass/fail call.

## Evidence / artifacts updated
- `passive-income/robot-mower-boundary-wire/reports/2026-04-30-affiliate-validation.md`
- `passive-income/robot-mower-boundary-wire/affiliate-programs.csv`

## Findings
- The direct-brand paths that would make this niche truly attractive were not defensibly verifiable in this run. Husqvarna robotic-mower product pages are real, but a public affiliate URL was not found; a guessed affiliate page returned 404 and sitemap/homepage checks did not surface a public program. Worx/Landroid had the same problem.
- The only clearly verified monetization stack came from broad marketplaces, not niche-leading merchants:
  - **Amazon Associates** is real and supports the category. Public program page: `https://affiliate-program.amazon.com/`. A robot lawn mower boundary wire search page also exists, confirming product coverage.
  - **Walmart Creator** is real and supports affiliate links/storefronts. Public page: `https://creator.walmart.com/`. A Walmart search page exists for robot lawn mower boundary wire.
  - **eBay Partner Network** is real and supports item/landing-page linking. Public page: `https://partnernetwork.ebay.com/`.
- Economics are usable but thin for an accessories-heavy niche:
  - boundary wire, connectors, pegs, splice kits, testers, and small repair parts are mostly low-to-moderate AOV
  - the strongest verified paths have either short attribution windows, unclear/variable commissions, or marketplace-style margin compression
  - this makes the stack workable as a supplement, but weak as the anchor for a new site

## Scorecard summary
| Candidate | Affiliate path | Weighted score | Verdict |
|---|---|---:|---|
| Amazon Associates | Verified | 68 | Best fallback / best converter, but not strong enough primary |
| Walmart Creator | Verified | 58 | Backup only |
| eBay Partner Network | Verified | 56 | Backup only |
| Husqvarna direct | Not verified | 47 | Reject as primary until program is proven |
| Worx direct | Not verified | 43 | Reject as primary until program is proven |

## Ranking
- **Primary:** None approved
- **Secondary:** Amazon Associates
- **Fallbacks:** eBay Partner Network, Walmart Creator

## Decision
- **FAIL**
- Reason: no merchant stack cleared the required primary threshold with defensible evidence. The best verified option (Amazon Associates at 68) is close but still below a confident primary for this accessory-led niche. Backups exist, but they do not fix the missing strong primary merchant.
- Operational read: this is exactly the kind of niche that can look promising on content/search intent while still underperforming on monetization quality.

## Escalations / owner actions needed
- None for this decision.
- If the niche is revived later, owner signup/approval/payout setup would still be required for Amazon/Walmart/eBay, but that does not change the current fail call.

## Recommended next handoff
- Next lane: Niche Scout
- Why: the niche has real buyer intent, but the merchant stack is too marketplace-dependent and too weakly anchored by verified direct programs. Move to the next backup niche rather than rationalize thin economics.
