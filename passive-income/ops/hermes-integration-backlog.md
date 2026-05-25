# Hermes Integration Backlog

## Objective
Move from Spike-does-too-much to Spike-orchestrates-lanes.

## Immediate backlog
1. Define dedicated Hermes agent configuration
2. Bind Hermes to passive-income execution lanes
3. Create lane invocation prompts for:
   - Niche Scout
   - Affiliate Validator
   - Content Planner
   - Drafting Worker
   - Publishing Prep
   - Reporting / Review
4. Add deterministic output file conventions per lane
5. Add lane-trigger rules to the passive-income machine control docs
6. Test one delegated run per lane on the aquarium ATO pilot
7. Record failure modes and tighten prompts/specs

## Blocking constraints right now
- Telegram route does not expose persistent thread-bound subagent spawning hooks
- allowed subagent ids currently only expose `main`
- dedicated Hermes worker is not yet configured as an allowed subagent target

## Short-term workaround
Use delegated isolated subagent runs against the lane specs, with Spike routing and reviewing outputs.

## Long-term target
Dedicated Hermes execution workers running each lane with stable routing contracts and minimal owner involvement.
