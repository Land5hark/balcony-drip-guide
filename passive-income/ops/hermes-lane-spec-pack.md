# Hermes Lane Spec Pack

Purpose: define the reusable worker lanes for the passive-income machine so Spike can orchestrate and Hermes-style agents can execute.

## Control model
- **Spike** owns routing, approvals, memory, process evolution, and final go/no-go decisions.
- **Lane workers** own bounded execution tasks.
- **Sharky** only touches identity, payment, legal, risky external actions, and explicit owner approvals.

## Global lane rules
1. Stay inside the lane scope.
2. Write outputs to deterministic files, not chat-only vapor.
3. Escalate instead of guessing when identity, payment, account approval, or ambiguous evidence blocks progress.
4. Prefer rejection over rationalizing weak niches or weak monetization.
5. Every lane must return one of:
   - PASS
   - FAIL
   - BLOCKED
   - NEEDS_OWNER

---

## Lane 1 — Niche Scout
### Mission
Generate and pressure-test candidate niches.

### Inputs
- machine constraints
- target business model
- previous niche history
- any user preference or exclusion

### Process
1. generate candidate niches
2. filter for hyper-specific long-tail opportunities
3. reject giant-incumbent sludge
4. assess content depth and credibility risk
5. shortlist primary + backups

### Outputs
- ranked niche shortlist
- rejection reasons for discarded niches
- suggested next niche for validation

### Pass condition
At least one niche is shortlist-worthy.

### Fail condition
No credible candidate niche survives initial filtering.

---

## Lane 2 — Affiliate Validator
### Mission
Validate whether a niche has a real, worthwhile affiliate stack.

### Inputs
- shortlisted niche
- merchant/program candidates
- `passive-income/ops/affiliate-program-scorecard.md`

### Process
1. identify 3-5 merchant/program candidates
2. verify affiliate path existence
3. score each program
4. rank primary / secondary / fallback
5. reject thin monetization stacks

### Outputs
- `affiliate-programs.csv` in the niche folder when it exists
- or a decision-ready markdown report if the niche folder does not exist yet

### Pass condition
- 1 primary candidate scores 70+
- at least 1 backup path scores 55+ or a credible fallback exists

### Fail condition
No merchant stack clears the threshold.

### Escalate when
- owner must create/apply for account
- payout setup needs owner action
- evidence is ambiguous

---

## Lane 3 — Content Planner
### Mission
Turn a validated niche into a structured publication backlog.

### Inputs
- approved niche
- monetization constraints
- search intent map
- product/merchant context

### Process
1. generate first 10-20 article ideas
2. cluster by intent
3. prioritize by usefulness + buyer/problem intensity
4. define internal linking and update order
5. mark which pieces can carry monetization naturally

### Outputs
- `topics.csv`
- topic clusters
- publication order
- notes on monetization fit by topic

### Pass condition
Backlog supports the first 30+ useful article path.

### Fail condition
Topic depth is weak or too repetitive.

---

## Lane 4 — Drafting Worker
### Mission
Produce useful, credible draft packages from approved topics.

### Inputs
- approved topic brief
- template
- niche rules
- monetization guardrails

### Process
1. research topic
2. draft article
3. structure for intent match
4. flag claims needing verification
5. note monetization insertion points without forcing them

### Outputs
- draft article package
- verification checklist
- metadata for publish readiness

### Pass condition
Draft is useful, specific, credible, and structured.

### Fail condition
Draft is generic, weak, or unsupported.

---

## Lane 5 — Publishing Prep
### Mission
Prepare drafts for safe publication.

### Inputs
- approved draft
- affiliate-link governance
- site structure
- disclosure rules

### Process
1. finalize formatting
2. insert governed links
3. confirm disclosure placement
4. check internal links and taxonomy
5. verify static-site readiness

### Outputs
- publication-ready content file
- link placement log
- publish checklist result

### Pass condition
Content is ready to publish with no missing structural pieces.

### Fail condition
Missing links, disclosure, taxonomy, or build-readiness.

---

## Lane 6 — Reporting / Review
### Mission
Review performance, friction, and next actions.

### Inputs
- analytics/search data
- publication log
- affiliate status
- workflow notes

### Process
1. summarize what shipped
2. summarize traffic/indexing signals
3. summarize monetization state
4. surface blockers
5. recommend next actions

### Outputs
- recurring report in `reports/`
- operator summary for Spike
- explicit refresh / expand / pivot recommendations

### Pass condition
Report produces clear next actions.

### Fail condition
Data is too incomplete to say anything useful.

---

## Handoffs
- Niche Scout -> Affiliate Validator
- Affiliate Validator -> Content Planner
- Content Planner -> Drafting Worker
- Drafting Worker -> Publishing Prep
- Publishing Prep -> live site / publish action
- live site + data -> Reporting / Review
- Reporting / Review -> Spike for iteration routing

## Critical path
1. Niche Scout must not pass junk
2. Affiliate Validator must not bless weak economics
3. Content Planner must produce a deep, usable queue
4. Drafting must create genuinely useful assets
5. Publishing Prep must enforce structure and disclosure
6. Reporting must tell the truth about traction

## Routing rules for Spike
- If a niche is merely interesting -> send to Niche Scout
- If a niche survives filtering -> send to Affiliate Validator
- If monetization passes -> send to Content Planner
- If a topic is approved -> send to Drafting Worker
- If a draft is approved -> send to Publishing Prep
- If a reporting interval hits or a batch ships -> send to Reporting / Review

## Immediate implementation note
Current surface/tooling does not yet support a dedicated persistent Hermes thread on this Telegram route.
Until Hermes is formally configured, these lane specs act as the durable contract for delegated subagent runs and future Hermes integration.
