# Cost Page Refresh - 2026-05-23

## Target

`site-deploy/content/posts/how-much-does-a-basic-balcony-watering-system-cost.md`

## Why

The cost page is buyer-intent and close to affiliate decisions, but it was still mostly organized by generic price tiers. It needed stronger routing by balcony situation, water source, and failure risk.

## Changes

- Added "choose your budget by balcony situation" table:
  - small herb pots near faucet
  - 6-10 mixed containers near faucet
  - no faucet access
  - frequent travel
  - hot south/west exposure
  - 20+ containers / mixed zones
- Added "cost by balcony size" table:
  - 3-5 pots
  - 6-10 pots
  - 10-20 pots
  - railing planters / hanging baskets
  - mixed herbs and vegetables
- Added best-fit internal routes for faucet, no-faucet, and gravity-fed setups.
- Added "where the cheap kits usually fail" section to improve trust and buying clarity.

## Result

- Word count increased from ~1,222 to 1,674.
- Hugo build passed.
- Static QA passed:
  - Missing internal targets: `0`
  - Sitemap duplicate URLs: `0`

## Publishing Note

Do not promote externally until Cloudflare Pages serves the corrected homepage/category-count build.
