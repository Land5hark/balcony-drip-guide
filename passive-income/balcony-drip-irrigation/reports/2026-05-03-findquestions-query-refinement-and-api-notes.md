# FindQuestions query refinement and API notes

Date: 2026-05-03

## Purpose
Capture what the public FindQuestions.com frontend exposes, how the report pipeline appears to work from query to deliverable, and which query variants produce cleaner balcony/patio/container topic sets than the broad seed `balcony drip irrigation`.

## Public flow reconstructed from frontend + live API testing

### Frontend endpoints
- `GET /api/autocomplete?q=...`
- `POST /api/search` with JSON body `{ "business": "..." }`
- `POST /api/search-status` with JSON body `{ "business": "..." }`
- `POST /api/capture-email` with JSON body `{ "email": "...", "query": "..." }`

### Observed behavior
1. User enters a business/query phrase.
2. Frontend asks `autocomplete` for suggestions.
3. Frontend submits `search`.
4. Backend either returns full results immediately if cached or returns `status: queued`.
5. Frontend polls `search-status` until complete.
6. Once complete, backend returns the full JSON result set, including all questions and metadata.
7. Frontend only reveals a preview in the UI and uses the email gate for the PDF/lead-capture step.
8. `capture-email` accepts a valid email and query and returns success.

### Important implication
The full report payload is retrievable from the public API response once processing finishes. The email gate appears to be mainly for lead capture and PDF delivery, not for protecting the underlying topic data.

## Evidence from public terms/privacy page
The public terms/privacy page states or strongly implies:
- Hosting: Railway
- AI processing: Anthropic
- Email delivery: Resend
- CRM / lead management: GoHighLevel
- Search-result cache retention: 7 days
- Data source framing: public Reddit discussions

## Likely backend pipeline (inferred, not source-confirmed)
1. Receive query string.
2. Fetch or reuse cached Reddit-source material.
3. Run AI synthesis (likely Anthropic) to produce:
   - title/question list
   - search-intent summaries
   - bonus topics
   - subreddit recommendations
   - sources
4. Cache results for reuse.
5. On email capture, render/send PDF via email provider and push lead info to CRM.

## Constraint
This is reconstructed from public frontend code, live endpoint behavior, and public policy pages only. The private backend source, prompts, Reddit retrieval logic, PDF generator, and exact prompt chain were not exposed.

## Query testing summary

### Broad seed tested
#### `balcony drip irrigation`
Returned too much generic yard/contractor/hardscape intent:
- install cost
- hire a pro
- patio concrete routing
- buried-line issues
- large-yard framing

This is too category-broad for the target niche.

## Refined queries that produced cleaner topic sets

### 1. `cheap diy watering for balcony plants`
Best for budget + DIY + beginner + affiliate angles.

Top observed questions:
- How to Water Balcony Plants on a Budget
- DIY Drip Irrigation System for Balcony Plants
- Cheapest Way to Keep Balcony Plants Watered
- How to Water Plants While Away on Vacation
- Best Budget Drip Irrigation Kits for Apartment Balconies
- DIY Watering System Using 5-Gallon Buckets
- Can I Automate Balcony Plant Watering Without Spending Much?

Observed subreddit mix:
- r/gardening
- r/lifehacks
- r/houseplants
- r/containergardening
- r/UrbanGardening
- r/Apartmentliving
- r/homeassistant
- r/BudgetGardening
- r/IndoorGarden
- r/balconygardening

### 2. `renter friendly balcony watering system`
Best for apartment/rental friction and no-permanent-installation angles.

Top observed questions:
- How to Water Plants on Your Balcony Without a Tap
- Best Watering Systems for Apartment Balconies
- Can You Use a Garden Hose Inside an Apartment?
- How to Stop Water from Pooling on Your Balcony
- Automatic Watering System for Rental Apartments
- DIY Balcony Watering System for Renters
- Drip Irrigation for Balcony Plants: Complete Guide

Observed subreddit mix:
- r/UrbanGardening
- r/ApartmentHacks
- r/gardening
- r/houseplants
- r/TenantRights
- r/SmallSpaces
- r/BalconyGarden

### 3. `balcony container watering system`
Best for system-design content, buyer guides, and multi-container setups.

Top observed questions:
- How to Water Balcony Plants When You're Away on Vacation
- Best Automatic Watering System for Balcony Containers
- DIY Balcony Watering System on a Budget
- Can You Use Drip Irrigation on a Balcony?
- How to Set Up a Gravity-Fed Watering System for Balcony Plants
- What Size Water Reservoir Do Balcony Plants Need?
- How Often Should You Water Balcony Container Plants?

Observed subreddit mix:
- r/houseplants
- r/containergardening
- r/balconygardening
- r/gardening
- r/lifehacks
- r/apartmentgardening
- r/urbangardening

### 4. `watering balcony plants while away`
Best for travel/vacation problem framing.

Top observed questions:
- How to Keep Balcony Plants Alive While You're Away
- Best DIY Plant Watering System for Your Balcony
- How Long Can Potted Plants Survive Without Water?
- Bathtub Plant Watering Trick: Does It Really Work?
- String Watering System for Plants: Step-by-Step Guide

### 5. `automatic watering for potted patio plants`
Best for generic automation/comparison content.

Top observed questions:
- Can You Automate Watering for Outdoor Potted Plants?
- Best Automatic Watering Systems for Potted Patio Plants
- How Much Does an Automatic Plant Watering System Cost?
- Do Self-Watering Pots Actually Work?
- How to Water Potted Plants While on Vacation

### 6. `balcony drip irrigation for container plants`
Cleaner than the original seed and still drip-specific.

Top observed themes:
- potted plants compatibility
- low-cost balcony watering
- automatic watering systems for balcony gardens
- vacation care
- system components
- gravity-fed vs pump
- timer selection
- scale to 20+ containers
- flow-rate / spacing guidance
- clogging prevention

## Recommended query lanes for future harvesting

### Lane A: buyer / affiliate intent
Use for product-comparison and kit-roundup article seeds.
- `best automatic watering system for balcony containers`
- `best budget drip irrigation kits for apartment balconies`
- `best hose timers for balcony drip irrigation systems`

### Lane B: pain-point / top-of-funnel
Use for broad traffic and entry pages.
- `watering balcony plants while away`
- `how to water balcony plants without a tap`
- `how to stop water from pooling on your balcony`

### Lane C: DIY / budget intent
Use for high-click practical guides that can bridge into product picks.
- `cheap diy watering for balcony plants`
- `diy balcony watering system on a budget`
- `gravity fed watering system for balcony plants`

### Lane D: container-specific technical intent
Use for problem-solving and internal-link support pieces.
- `how often should you water balcony container plants`
- `what size water reservoir do balcony plants need`
- `drip irrigation spacing and flow rate for containers`

## Content implications
Strongest repeated intents across refined queries:
- vacation watering
- no-tap / renter constraints
- budget DIY setups
- best automatic systems for small spaces
- balcony containers specifically
- gravity-fed vs timer/pump setups
- drainage / neighbor-drip / pooling concerns

These are materially more on-niche than the generic `drip irrigation` seed and should drive the next content-map pass.

## Suggested next build step
Create a small local tool that:
1. accepts a list of candidate queries
2. hits `search`
3. polls `search-status`
4. saves raw JSON outputs per query
5. clusters repeated intents across queries
6. emits a merged topic shortlist for the balcony-drip site

This avoids dependence on the email/PDF layer and makes future query iteration cheap.
