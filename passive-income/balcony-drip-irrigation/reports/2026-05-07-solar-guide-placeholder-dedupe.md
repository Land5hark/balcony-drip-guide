# Solar guide placeholder dedupe

- Lane: passive-income / governed affiliate readiness
- Status: pass completed
- Scope: remove alias-style governed placeholder duplication from the solar buyer guide so later affiliate insertion works from one clean canonical slot set instead of multiple names for the same compact product path
- Timestamp: 2026-05-07 14:19 EDT

## Problem
The solar buyer guide was carrying extra placeholder noise in both the registry and article copy.

These slots all pointed at the same compact RainPoint destination or otherwise duplicated the same lane:
- `bdi-solar-rainpoint-compact-primary`
- `bdi-solar-rainpoint-primary`
- `bdi-solar-compact-primary`

That made the governed inventory messier than it needed to be:
- more than one slot name for the same compact solar product path
- article placeholder lists longer than the actual buyer logic required
- extra ambiguity for later affiliate URL insertion and slot-by-slot QA

## Change made
Removed the two alias-style registry rows:
- `bdi-solar-rainpoint-primary`
- `bdi-solar-compact-primary`

Kept the clean canonical set for the live solar guide:
- `bdi-solar-rainpoint-compact-primary`
- `bdi-solar-rainpoint-smart-primary`

Also updated:
- `site/content/posts/best-solar-drip-irrigation-kits-for-patios-and-balconies.md`
- `drafts/best-solar-drip-irrigation-kits-for-patios-and-balconies.md`
- `drafts/best-solar-drip-irrigation-kits-for-patios-and-balconies.publish.md`

so the placeholder references now match the canonical slot set instead of the retired aliases.

## Verification
Checks run:
- grep for the retired alias slot names across site content, public output, and drafts
- `hugo --minify` in `passive-income/balcony-drip-irrigation/site`

Observed result:
- no remaining references to `bdi-solar-rainpoint-primary` or `bdi-solar-compact-primary` in live content, built output, or drafts
- Hugo build completed cleanly

## Why this matters
This is small but valuable governed-link hygiene:
- fewer duplicate slot names for the same merchant path
- cleaner future affiliate activation on one buyer-intent page
- less chance of inserting or reviewing the same compact solar destination under multiple labels

## Outcome
The solar buyer guide now has a cleaner governed placeholder set that matches its real decision structure:
- compact solar primary path
- premium smart solar path

That is a better handoff state for later owner-approved monetization than a registry padded with legacy alias slots.
