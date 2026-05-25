# Lane Prompts

Reusable invocation prompts for the passive-income machine's execution lanes.

## Files
- `niche-scout.md`
- `affiliate-validator.md`
- `content-planner.md`
- `drafting-worker.md`
- `publishing-prep.md`
- `reporting-review.md`

## How Spike should use them
1. decide which lane owns the work
2. pass the relevant prompt plus niche/topic/project context into a delegated run
3. require artifacts to be written to deterministic files
4. review the returned status:
   - PASS
   - FAIL
   - BLOCKED
   - NEEDS_OWNER
5. route the next handoff based on the result

## Immediate reality
Until a dedicated Hermes agent is configured, these prompts are the reusable orchestration cartridges for delegated subagent runs.
