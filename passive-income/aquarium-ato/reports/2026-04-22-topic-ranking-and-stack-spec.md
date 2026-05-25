# Aquarium ATO Topic Ranking + Stack Spec — 2026-04-22

## 1) Ranked first-10 execution order

Ranked with the `keyword-validator` logic: intent quality first, then monetization fit, SERP opportunity, cluster value, and how useful each page is as a trust-building support layer.

### 1. Why Your ATO Keeps Overfilling a Nano Tank
- **Verdict:** pursue first
- **Why:** strongest immediate problem-solving intent, high anxiety, high usefulness, and strong natural internal-link power into comparisons, safety pages, and product replacements.
- **Intent type:** troubleshooting / problem-aware
- **Monetization fit:** strong support monetization
- **SERP opportunity:** likely good if current results are forum-heavy or scattered
- **Best angle:** ranked diagnosis + fast triage + safety framing

### 2. Float Switch vs Optical Sensor ATOs for Nano Tanks
- **Verdict:** pursue first wave
- **Why:** clean comparison intent with direct buyer value and strong conversion assist potential.
- **Intent type:** comparison
- **Monetization fit:** strong
- **SERP opportunity:** good if existing pages are feature-heavy instead of failure-mode-heavy
- **Best angle:** compare graceful failure, cleaning burden, and real-world maintenance tradeoffs

### 3. Best ATO Systems for Nano Reef Tanks Under 20 Gallons
- **Verdict:** pursue first wave
- **Why:** strongest direct buyer intent in the set, but should be reinforced by support articles so it does not become generic affiliate sludge.
- **Intent type:** buyer
- **Monetization fit:** very strong
- **SERP opportunity:** moderate, better after cluster support exists
- **Best angle:** reliability-first shortlist, not a hype roundup

### 4. ATO Failure Modes That Can Flood a Nano Tank or Crash Salinity
- **Verdict:** pursue first wave
- **Why:** high trust-builder, strong safety/search utility, and ideal hub for internal links into troubleshooting and buying pages.
- **Intent type:** problem-aware / safety
- **Monetization fit:** medium-strong
- **SERP opportunity:** good if broad aquarium sites under-explain failure chains
- **Best angle:** failure map + prevention guide

### 5. How to Stop False ATO Alarms in Small Tanks
- **Verdict:** pursue first wave
- **Why:** practical troubleshooting demand with strong support value and decent accessory crossover.
- **Intent type:** troubleshooting
- **Monetization fit:** medium
- **SERP opportunity:** likely solid if current answers are mostly forum fragments
- **Best angle:** symptom-led troubleshooting ordered by probable cause

### 6. ATO Maintenance Schedule for Nano Tanks
- **Verdict:** pursue
- **Why:** strong maintenance/search intent, high trust value, and useful for retention + internal links.
- **Intent type:** maintenance
- **Monetization fit:** medium
- **SERP opportunity:** solid if current content is generic
- **Best angle:** realistic maintenance cadence by risk point, not fake precision

### 7. Dual-Sensor vs Single-Sensor ATO Systems
- **Verdict:** pursue
- **Why:** good comparison intent and useful follow-on page after the sensor-type comparison.
- **Intent type:** comparison
- **Monetization fit:** medium-strong
- **SERP opportunity:** decent
- **Best angle:** meaningful redundancy vs marketing theater

### 8. How Big Should Your ATO Reservoir Be for Safety?
- **Verdict:** pursue
- **Why:** strong safety framing and high practical value, though requires careful wording to avoid fake exactness.
- **Intent type:** problem-aware / safety
- **Monetization fit:** medium
- **SERP opportunity:** decent
- **Best angle:** conservative sizing logic + downside limits

### 9. Best ATO Reservoir Options for Open-Top Nano Tanks
- **Verdict:** maybe / second wave
- **Why:** monetizable and useful, but narrower than the first cluster and easier to write once sizing/safety content exists.
- **Intent type:** buyer
- **Monetization fit:** strong
- **SERP opportunity:** moderate
- **Best angle:** sizing, aesthetics, refill friction, and spill-risk tradeoffs

### 10. Useful ATO Accessories That Actually Improve Reliability
- **Verdict:** maybe / second wave
- **Why:** monetizable but easiest to turn into garbage if not grounded in real failure-point logic.
- **Intent type:** buyer
- **Monetization fit:** strong
- **SERP opportunity:** moderate
- **Best angle:** only accessories that solve specific failure modes

## Recommended first 5 production order
1. `why-your-ato-keeps-overfilling-a-nano-tank`
2. `float-switch-vs-optical-sensor-ato-nano-tanks`
3. `best-ato-systems-nano-reef-tanks-under-20-gallons`
4. `ato-failure-modes-flood-salinity-crash`
5. `how-to-stop-false-ato-alarms-small-tanks`

---

## 2) Static-site-publisher stack spec

### Recommended stack
- **Generator:** Hugo
- **Repo model:** one repo rooted at `passive-income/aquarium-ato/site`
- **Host:** Cloudflare Pages as primary recommendation
- **Fallback host:** GitHub Pages
- **Source of truth:** markdown draft packages in workspace, promoted into Hugo content after review

### Why this stack
- Hugo is fast, simple, markdown-first, and easy for future Hermes automation.
- Cloudflare Pages is free, low-friction, and cleaner than trying to bolt fragile nonsense onto the first pilot.
- GitHub remains the control plane for history, review, and deployment triggers.
- The existing site folder already points the project toward a Hugo workflow, so forcing a different stack would be self-sabotaging.

### Recommended repo/deployment structure
- `site/config.toml` -> core site config
- `site/content/posts/` -> article pages
- `site/archetypes/default.md` -> frontmatter defaults
- `site/layouts/` -> lean templates
- `site/static/` -> assets, disclosures, icons, future images
- `site/.github/workflows/` -> build verification for GitHub-side checks
- `drafts/` -> working article packages before promotion into final site content
- `templates/` -> reusable article scaffolds
- `reports/` -> operating reviews and publication logs
- `products.csv` -> verified product facts and affiliate readiness

### Publishing workflow
1. Validate topic priority.
2. Build the draft package in `drafts/`.
3. Verify claims, product facts, and safety framing.
4. Promote the approved package into `site/content/posts/` with proper frontmatter.
5. Run local Hugo build.
6. Commit to GitHub.
7. Auto-deploy via Cloudflare Pages.
8. Log publication in `reports/`.

### Frontmatter recommendation
Add or standardize these fields on post pages:
- `title`
- `date`
- `draft`
- `description`
- `slug`
- `categories`
- `tags`
- `intent`
- `cluster`
- `verification_status`

### Host recommendation
#### Primary: Cloudflare Pages
Choose this if the goal is the cleanest free deployment with minimal babysitting.
- Connect GitHub repo
- Build command: `hugo --minify`
- Output directory: `public`
- Environment: Hugo version pinned
- Custom domain later if the pilot earns it

#### Fallback: GitHub Pages
Use if you want everything GitHub-native and can tolerate slightly more configuration fiddling.

### Immediate implementation notes
- The repo already has a Hugo config and a basic GitHub Actions build workflow.
- That means the actual next step is not “choose a stack from scratch.” It is “tighten the existing Hugo stack and choose Cloudflare Pages as the deploy target.”
- Do not publish externally until disclosure language and product verification flow are defined.

---

## 3) First 5 draft-package status

### Already present
- `best-ato-systems-nano-reef-tanks-under-20-gallons`
- `why-your-ato-keeps-overfilling-a-nano-tank`
- `float-switch-vs-optical-sensor-ato-nano-tanks`

### Still needed to complete the first 5
- `ato-failure-modes-flood-salinity-crash`
- `how-to-stop-false-ato-alarms-small-tanks`
