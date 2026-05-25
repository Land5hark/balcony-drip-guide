# Aquarium ATO Pilot Stack Application — 2026-04-22

## 1) Niche-scout view

### Niche verdict
**Pursue**

### Why this niche is worth running
- It targets a narrow but real aquarium sub-problem rather than broad aquarium hobby traffic.
- Searchers are often problem-aware, anxious, and motivated to prevent expensive or annoying failures.
- Content can naturally cover troubleshooting, safety, comparisons, maintenance, and accessories.
- Monetization fit is real because the problem space maps to ATO systems, reservoirs, alarms, tubing, check valves, and related reliability gear.
- It is narrow enough that a specialist site can plausibly outrank generic aquarium listicles and weak broad gear pages.

### Risks / watch-outs
- Product facts must be verified carefully; this niche punishes fake specificity.
- Trust matters more than hype because safety/failure risk is part of the search intent.
- The topic pool is deep enough for a lean niche site, but not infinite; cluster discipline matters.

## 2) Keyword-validator pass on current queue

### Highest-priority topics to pursue first

#### A. `why-your-ato-keeps-overfilling-a-nano-tank`
**Verdict:** pursue
- **Intent:** strong troubleshooting / high-anxiety / immediate problem-solving intent
- **Monetization fit:** good; naturally connects to replacement parts, better systems, sensors, tubing fixes, alarms
- **SERP opportunity:** likely good if current results are generic or scattered across forums/videos
- **Best angle:** calm, ranked diagnosis guide with fast triage and explicit safety notes

#### B. `float-switch-vs-optical-sensor-ato-nano-tanks`
**Verdict:** pursue
- **Intent:** comparison / buyer intent with strong practical decision value
- **Monetization fit:** strong; direct product-category comparison
- **SERP opportunity:** good if existing pages focus on features instead of failure modes and maintenance burden
- **Best angle:** compare reliability tradeoffs, fouling risk, false triggers, maintenance burden, and fail-safe logic

#### C. `best-ato-systems-nano-reef-tanks-under-20-gallons`
**Verdict:** pursue
- **Intent:** buyer / comparison / strong affiliate fit
- **Monetization fit:** very strong
- **SERP opportunity:** moderate; likely more competitive than troubleshooting pieces, so it should be informed by adjacent articles and internal links
- **Best angle:** reliability-first buying guide, not a hype list

#### D. `ato-failure-modes-flood-salinity-crash`
**Verdict:** pursue
- **Intent:** safety / problem-aware / risk-reduction intent
- **Monetization fit:** medium to strong; useful for assisted conversion and trust-building
- **SERP opportunity:** good if current content is generic or incomplete on real failure chains
- **Best angle:** failure-mode map with prevention framing and links into product/comparison pages

#### E. `how-to-stop-false-ato-alarms-small-tanks`
**Verdict:** pursue
- **Intent:** troubleshooting / annoyance reduction / maintenance intent
- **Monetization fit:** medium; good supporting article with accessory/system crossover
- **SERP opportunity:** likely solid if forum-heavy
- **Best angle:** symptom-led troubleshooting with probable causes ranked by frequency

### Second-wave topics
- `ato-maintenance-schedule-nano-tanks`
- `dual-sensor-vs-single-sensor-ato-systems`
- `best-ato-reservoir-options-open-top-nano-tanks`
- `how-big-should-your-ato-reservoir-be-for-safety`
- `useful-ato-accessories-that-actually-improve-reliability`

## 3) Static-site-publisher recommendation for this pilot

### Recommended stack
**Hugo + GitHub repo + Cloudflare Pages or GitHub Pages**

### Why
- Markdown-first and easy to automate
- cheap/free
- simple content folder conventions
- good fit for recurring article publication from agent-generated drafts
- easy Git-based history and deployment

### Recommended repo structure
- `content/` -> article markdown
- `layouts/` -> templates
- `static/` -> assets
- `data/` -> optional product/comparison data later
- `archetypes/` -> article frontmatter defaults
- `docs/` or direct deploy target -> depending on chosen host

### Publishing workflow
1. Draft article package in workspace
2. Verify claims and product facts
3. Convert final approved draft into site markdown/frontmatter
4. Commit to Git repo
5. Auto-deploy on push
6. Record published URLs in weekly report

### Initial publishing recommendation
- Start with **Hugo** unless there is a strong reason not to.
- Start with **Cloudflare Pages** or **GitHub Pages** for lowest-friction free deployment.
- Keep analytics/disclosure partials simple and reusable.

## 4) Recommended next execution actions
1. Draft the first 3 articles from the priority set above.
2. Define the Hugo content model/frontmatter needed for this niche.
3. Stand up the first static site repo and test one build/deploy.
4. Seed verified products into `products.csv` before final buyer-guide publication.
5. Begin a recurring weekly pilot performance review file in this `reports/` folder.
