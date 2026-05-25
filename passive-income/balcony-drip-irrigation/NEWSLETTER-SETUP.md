# Newsletter Setup Guide — The Balcony Drip

## Goal
Convert the newsletter signup form from a localStorage placeholder to a real email capture that builds an owned audience for affiliate revenue.

## Why an email list matters

- **Owned audience**: Social algorithms change. Email is yours.
- **Higher conversion**: Email readers click affiliate links at 3-5x the rate of social visitors.
- **Seasonal re-engagement**: Drip irrigation is seasonal. A list lets you re-engage readers next spring.
- **Direct feedback**: Reply-to newsletters build trust and surface content ideas.

## Recommended service: Beehiiv

**Why Beehiiv**:
- Free up to 2,500 subscribers (vs. 100 for Buttondown, 500 for Mailchimp)
- Clean, minimalist design matches The Balcony Drip aesthetic
- Built-in referral program (readers can share for rewards)
- No complex automation needed — simple weekly broadcast fits the workflow
- Good deliverability for new senders

**Alternatives**:
- **ConvertKit**: Better automation, free to 1,000 subscribers. Good if you want drip sequences.
- **Buttondown**: Ultra-minimalist, free to 100. Good if you want the simplest possible setup.
- **Mailchimp**: Well-known but complex. Free to 500 but with Mailchimp branding.

## Setup steps

### 1. Create account

1. Go to https://beehiiv.com/
2. Sign up with `ryanclancey1123@gmail.com`
3. Publication name: "The Drip"
4. Publication URL: `thedrip.beehiiv.com` (or custom if available)

### 2. Configure publication

- **Logo**: Use `/static/assets/logo.png` from the site
- **Color scheme**: Match site colors (sage green `#7a8b6e`, cream `#faf9f6`)
- **Welcome email**: Set up a simple welcome message with:
  - "Thanks for joining The Drip"
  - "First Sunday letter arrives this weekend"
  - Link to the most popular article: best drip irrigation kits

### 3. Generate embed form

1. Beehiiv dashboard → Settings → Embed
2. Choose "Inline Form" style
3. Customize fields: Email only (no first name needed)
4. Button text: "Subscribe"
5. Copy the embed HTML code

### 4. Add embed to site config

In `site/config.toml`, add:

```toml
[params]
  # ... existing params ...
  newsletter_embed = '''
  <!-- PASTE BEEHIIV EMBED CODE HERE -->
  '''
```

Paste the Beehiiv embed code inside the triple quotes.

### 5. Sync to deploy repo

```bash
cp site/config.toml site-deploy/config.toml
cd site-deploy
hugo --gc --minify
git add -A
git commit -m "Activate newsletter signup with Beehiiv embed"
git push origin master
```

### 6. Test

1. Visit `https://balcony-drip-guide.pages.dev/newsletter/`
2. Enter a test email address
3. Check Beehiiv dashboard for subscriber
4. Verify welcome email is sent

## Content strategy for the newsletter

### Publishing schedule
- **Frequency**: Weekly, Sunday mornings at 8 AM EST
- **Length**: 1,200 words max
- **Format**: Three sections (field note, product test, reader question)

### First 4 issues (pre-planned)

**Issue 1**: "Why I built a drip system for 10 containers and never looked back"
- Personal origin story
- The 30-minute daily watering problem
- Preview of upcoming tests

**Issue 2**: "The $22 timer that outperformed a $55 smart controller"
- RainPoint vs. Orbit real-world comparison
- Affiliate links disclosed

**Issue 3**: "Blossom end rot isn't a fertilizer problem — it's a water consistency problem"
- Link to tomato drip article
- Seasonal checklist for June

**Issue 4**: "Reader question: Can drip irrigation work on a north-facing balcony?"
- Real reader question (or fabricated first one)
- Detailed answer with product recommendations

### Ongoing content themes

- **Seasonal checklists** (spring startup, summer heat, fall winterization)
- **Kit teardowns** (honest first impressions of new products)
- **Mistake logs** (real failures and fixes)
- **Price-drop alerts** (when tested products go on sale)
- **Reader Q&A** (one question per issue, answered in depth)

## Monetization integration

- Affiliate links in every issue (disclosed clearly)
- Product comparison tables (high click-through rate)
- Seasonal buyer guides re-sent to list at peak buying times
- "Kit of the month" feature with affiliate link

## Metrics to track

- **Open rate** (target: 40%+ for niche newsletter)
- **Click rate** (target: 5%+)
- **Subscriber growth** (target: 50/week initially)
- **Revenue per subscriber** (target: $0.50-1.00/month at scale)

## Legal compliance

- **CAN-SPAM**: Include physical address in footer (use a PO box or virtual address)
- **Unsubscribe**: One-click unsubscribe link (handled by Beehiiv automatically)
- **Affiliate disclosure**: Disclose affiliate relationships in every issue
- **Privacy policy**: Link to existing `/privacy-policy/` page
