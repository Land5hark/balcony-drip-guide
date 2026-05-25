# Hanging baskets and rail planters fact check — pass 1

- Lane: passive-income / buyer-intent content hardening
- Status: pass completed
- Scope: tighten the live hanging-baskets / rail-planters guide with source-backed specifics instead of leaving it entirely on heuristic advice
- Timestamp: 2026-05-07 16:18 EDT

## Article reviewed
- `passive-income/balcony-drip-irrigation/site/content/posts/best-drip-setup-for-hanging-baskets-and-rail-planters.md`

## Sources checked
1. Drip Depot support — `https://help.dripdepot.com/support/solutions/articles/11000043229-dripper-buying-guide`
   - Hanging-basket guidance explicitly warns that micro-tubing can curl and move the emitter off-center.
   - Recommends a rigid riser and threaded dripper approach when centered basket placement matters.
2. Rain Bird homeowners guide — `https://www.rainbird.com/homeowners/blog/how-to-plan-an-automatic-drip-watering-system-for-container-plants`
   - Says larger containers often need more than one dripper.
   - Calls out `1/4 in. emitter tubing` with emission points every 6 inches as ideal for long window boxes.
3. Orbit planter kit page — `https://www.orbitonline.com/products/hose-end-planter-watering-kit`
   - Product packaging reinforces that small planter kits are often framed around one large planter box or two smaller containers, supporting the article's anti-"one dripper solves everything" positioning.

## Changes made
Added two source-backed hardening details to the live article:

1. **Hanging baskets**
   - Added a concrete caution that centered emitter placement matters.
   - Added source-backed explanation that curled micro-tubing can push a basket emitter off to the side.
   - Added rigid-riser / threaded-dripper language as a cleaner stabilization path.

2. **Rail planters / window-box style containers**
   - Strengthened the multi-point watering section to explicitly include emitter tubing or closely spaced devices for long planters.
   - Added a supporting line that Rain Bird specifically recommends 1/4-inch emitter tubing with emission points every 6 inches for long planters and window boxes.

## Verification
Checks run:
- `hugo --minify` in `passive-income/balcony-drip-irrigation/site`
- grep of built output for the new `rigid riser` and `every 6 inches` phrases

Observed result:
- Hugo build completed cleanly
- built page contains the new fact-backed basket and rail-planter language

## Outcome
This article is now less hand-wavy in two places that matter for buyer trust:
- why basket emitters drift and how to stabilize them
- why long rail planters often need distributed watering rather than one dripper at one end

That is a better pre-monetization state for a problem-aware page that will eventually map into emitter, stake, and connector affiliate slots.
