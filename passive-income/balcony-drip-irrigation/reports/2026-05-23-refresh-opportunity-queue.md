# Balcony Drip Refresh Opportunity Queue - 2026-05-23

## Purpose

Cloudflare deployment and public promotion are owner-gated, so the useful internal move is to improve the pages most likely to receive, retain, and route traffic once promotion starts.

## Quick Corpus Read

- Current `site-deploy/content/posts/` corpus: 40 markdown posts/pages.
- Strongest depth is in buyer and troubleshooting content: several pieces are ~1,700-2,500 words.
- Weakest visible entry points are the hub/overview pages:
  - `balcony-watering-systems-hub.md` - ~652 words
  - `balcony-watering-systems.md` - ~620 words
  - `best-drip-irrigation-kits-for-apartment-balconies.md` - ~1,161 words
  - `how-much-water-do-balcony-plants-really-need.md` - ~1,172 words
  - `how-much-does-a-basic-balcony-watering-system-cost.md` - ~1,222 words

## Priority Queue

### P1 - Strengthen the Main Hub Entry - drafted 2026-05-23

Target: `balcony-watering-systems-hub.md`

Why: This should be the broad routing page for new visitors, but it is currently one of the thinnest pages in the corpus. If promotion traffic lands anywhere near the homepage/hub path, this page should quickly route readers into the best setup, no-faucet, timer, cost, and troubleshooting content.

Refresh package:

- Add a balcony-condition decision table:
  - has outdoor faucet
  - no faucet
  - railing planters/hanging baskets
  - herbs/vegetables
  - frequent travel
  - hot south/west exposure
- Add "start here" sections linking to the highest-intent guides:
  - setup guide
  - no-faucet guide
  - hose timer buyer guide
  - apartment balcony kit guide
  - hot weather adjustment guide
- Add a short "what not to buy first" section to reduce buyer regret and keep trust high.

Status: Draft refresh applied. Word count increased from ~652 to ~1,174. Local Hugo build and static QA passed:

- Missing internal targets: `0`
- Sitemap duplicate URLs: `0`

### P2 - Upgrade the Apartment Kit Buyer Page - drafted 2026-05-23

Target: `best-drip-irrigation-kits-for-apartment-balconies.md`

Why: Apartment balcony searches have cleaner buyer intent than generic balcony watering searches, and this page is thin compared with the broader kit guide.

Refresh package:

- Add apartment constraints:
  - no permanent plumbing
  - landlord/renter limits
  - no hose bib
  - storage limits
  - quiet pump/timer concerns
- Add a kit-matching table by balcony size:
  - 3-5 pots
  - 6-10 pots
  - 10-20 pots
  - railing planters
  - mixed herbs and vegetables
- Route readers to Drip Depot/RainPoint slots already governed in `data/link-registry.yaml`.

Status: Draft refresh applied. Word count increased from ~1,161 to 1,599. Added apartment constraint table, balcony-size kit matching table, and buying guidance for railing planters plus mixed herb/vegetable setups. Local Hugo build and static QA passed:

- Missing internal targets: `0`
- Sitemap duplicate URLs: `0`

### P3 - Turn Water-Amount Page Into a Support Hub - drafted 2026-05-23

Target: `how-much-water-do-balcony-plants-really-need.md`

Why: Water amount is a natural bridge between plant-care searches and irrigation hardware. It can support the hot-weather, frequency, emitter-count, overwatering, and tomato/herb pages.

Refresh package:

- Add water-per-pot ranges by container size and exposure.
- Add plant-specific notes:
  - tomatoes
  - peppers
  - basil/mint/herbs
  - hanging baskets
- Add "adjust your drip system" links to emitter count, hot weather, overwatering, and watering frequency pages.

Status: Draft refresh applied. Word count increased from ~1,172 to 1,813. Added quick water ranges by container size/exposure, plant-specific notes for tomatoes, peppers, herbs, and hanging baskets/rail planters, plus a drip-system adjustment table that routes to frequency, emitter count, overwatering, hot-weather, and uneven-flow guides. Local Hugo build and static QA passed:

- Missing internal targets: `0`
- Sitemap duplicate URLs: `0`

## Execution Notes

- Do not publish or promote until Cloudflare Pages serves the corrected homepage/category counts.
- Keep refreshes editorial-first; affiliate links should support specific decisions, not lead the page.
- After each refresh, run:

```bash
cd /home/linuxlite/.openclaw/workspace/passive-income/balcony-drip-irrigation/site-deploy
hugo --minify
python3 scripts/qa_static_build.py
```

Expected QA:

- Missing internal targets: `0`
- Sitemap duplicate URLs: `0`
