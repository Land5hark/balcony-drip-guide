# Affiliate Governance Setup — 2026-04-22

## What was created
To keep the pilot moving without overbuilding the money layer too early, the site now has lightweight affiliate/disclosure governance scaffolding:

- `site/content/disclosure.md`
- `affiliate-programs.csv`
- `link-registry.csv`

## Purpose of each file
### `site/content/disclosure.md`
Sitewide disclosure draft explaining:
- commissions may exist later
- usefulness comes before commission
- recommendation quality standards
- why the site is trying not to become gear-hype sludge

### `affiliate-programs.csv`
A small tracker for:
- priority retailer program
- possible brand-direct program
- Amazon fallback only if needed

### `link-registry.csv`
Central place to govern product links so pages do not end up full of unmanaged raw merchant URLs.

## Why this was the right next move
The first publish-ready draft existed, so disclosure and link-governance became the next bottleneck. This setup keeps the monetization layer inspectable and reversible without pretending the full affiliate program stack is already selected.

## Current limitation
This is governance scaffolding, not a live affiliate system yet.

Still missing before real monetized publication:
- chosen affiliate programs
- approved accounts
- payout destination setup
- actual affiliate URLs
- final decision on the first page to flip from draft to live
