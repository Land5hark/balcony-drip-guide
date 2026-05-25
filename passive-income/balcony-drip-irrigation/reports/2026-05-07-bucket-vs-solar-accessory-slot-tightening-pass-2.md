# Bucket-vs-solar accessory slot tightening — pass 2

- Lane: passive-income / governed affiliate readiness
- Status: pass completed
- Scope: remove the accidental generic-selector regression from the bucket-vs-solar accessory lane and replace it with a more specific bucket-fed DIY component path
- Timestamp: 2026-05-07 12:18 EDT

## Problem
The prior bucket-vs-solar accessory-slot cleanup fixed the merchant mismatch, but it still left one soft problem behind:
- `bdi-bucket-vs-solar-reservoir-accessories-primary` was pointed at `https://www.dripdepot.com/irrigation-kit-selector`

That reintroduced the same broad-selector pattern that the earlier governed selector audit had already cleaned out everywhere except the one intentional build-your-own kit page.

For this comparison page, the third lane is not a custom faucet-fed kit builder. It is a **bucket-fed DIY component** path for apartment growers who want the simplest no-faucet build route.

## Change made
Updated the slot in `site/data/link-registry.yaml` from the generic selector path to:
- `https://www.dripdepot.com/category/polyethylene-irrigation-tubing`

Also tightened the notes so the slot now explicitly describes a bucket-fed DIY path built around basic tubing runs instead of a packaged solar or reservoir kit.

## Verification
Ran a registry audit after the edit.

Observed result:
- the bucket-vs-solar accessory slot now resolves to Drip Depot's polyethylene irrigation tubing category
- `https://www.dripdepot.com/irrigation-kit-selector` is back to appearing only once in the registry, on the intentional `bdi-kit-dripdepot-selector-primary` slot for the main balcony kit guide

## Why this matters
This fixes a subtle governance regression:
- less placeholder sprawl
- better alignment between article intent and destination shape
- preserves the earlier selector-audit cleanup instead of undoing it by accident

## Outcome
The bucket-vs-solar governed placeholder set is now cleaner in a more durable way:
- solar kit lane -> packaged solar path
- simpler reservoir lane -> packaged reservoir kit path
- bucket-fed lane -> specific DIY tubing/component path

That is a better setup for later affiliate insertion than a loose selector fallback pretending to be a bucket-fed accessory lane.
