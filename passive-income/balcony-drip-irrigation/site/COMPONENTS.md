# Components — author's guide

Cheat sheet for every shortcode and partial. Copy, paste, edit the values, ship.

---

## In article markdown

### Affiliate disclosure

The disclosure box auto-appears on every article. To **hide** it on a specific
article (e.g. About, Disclosure pages, free-content explainers), set in
frontmatter:

```toml
disclosure = false
```

To drop it manually somewhere mid-article:

```
{{< disclosure >}}
```

---

### Editor's Pick — the affiliate signature

Use **once per article** as the primary product recommendation moment.

```
{{< editors-pick
    name="Raindrip R560DP Universal Kit"
    url="https://amzn.to/your-affiliate-link"
    price="$42"
    rating="4.7"
    reviews="2,148"
    retailer="Amazon"
    image="/images/raindrip-r560dp.jpg"
    blurb="The only starter kit that ships with the right parts for an indoor faucet setup. Three Brooklyn summers, no failures."
>}}
```

| Param      | Required | Notes |
|------------|----------|-------|
| `name`     | ✓        | Product name |
| `url`      | ✓        | Affiliate URL — auto-tagged `rel="sponsored nofollow noopener"` |
| `price`    | —        | e.g. `"$42"`. Shown in the CTA. |
| `rating`   | —        | 1–5 number, e.g. `"4.7"` |
| `reviews`  | —        | Display string, e.g. `"2,148"` |
| `retailer` | —        | Default `"Amazon"`. Used in the CTA. |
| `image`    | —        | Product photo. Falls back to a striped placeholder. |
| `blurb`    | —        | One-paragraph why-we-picked-it. |
| `why`      | —        | CTA secondary link text. Default `"Why we picked it"`. |

---

### Full product card

For roundups with 3–6 picks (e.g. "Best timers"), or when you want pros + cons.

```
{{< affiliate-card
    name="Raindrip R560DP Universal Kit"
    url="https://amzn.to/your-affiliate-link"
    rank="The pick · since 2023"
    price="$42 at Amazon"
    rating="4.7"
    reviews="2,148"
    image="/images/raindrip-r560dp.jpg"
    retailer="Amazon"
    blurb="The only kit that ships with the right parts for indoor-faucet setups."
    pros="Working 25 PSI pressure regulator|Tubing supple enough for tight railings|20 emitters covers most balconies|Three Brooklyn summers, no failures"
    cons="Timer face hard to read in direct sun|Sink-thread adapter not included"
    alt_url="https://www.dripworks.com/your-link"
    alt_retailer="DripWorks"
>}}
```

`pros` and `cons` are **pipe-separated** (`|`) lists.

---

### Inline affiliate mention

Use mid-paragraph when you want to name-drop a product without breaking flow.

```markdown
The kit I recommend is the
{{< aff name="Raindrip R560DP" price="$42" url="https://amzn.to/..." retailer="Amazon" >}};
the rest of this guide tells you how to adapt it.
```

| Param      | Notes |
|------------|-------|
| `name`     | Required |
| `url`      | Required — `rel="sponsored nofollow noopener"` applied automatically |
| `price`    | Optional |
| `retailer` | Default `"Amazon"` |

Renders as a small bordered chip inline with the text.

---

### Comparison table

```
{{< comparison-table >}}
[[rows]]
name      = "Raindrip R560DP"
url       = "https://amzn.to/..."
best_for  = "Renters, beginners"
emitters  = "20 × 2 GPH"
timer     = true
price     = "$42"
pick      = true       # marks this row with an Editor's Pick badge

[[rows]]
name      = "Orbit 69500 Micro"
url       = "https://amzn.to/..."
best_for  = "Big-box availability"
emitters  = "15 × 1 GPH"
timer     = false
price     = "$28"
{{< /comparison-table >}}
```

The shortcode body is TOML. Each `[[rows]]` block is one product row.

**Default columns:** Product · Best for · Emitters · Timer · Price · (link)

**Custom columns:** pass `columns="name,best_for,price"` (comma-separated). Recognised keys also become column headings (snake_case → "Title Case"); unknown keys render as plain text from the row data.

Rows with `pick = true` get a small "Editor's Pick" badge. The Timer column renders ✓ / — based on the boolean. The link column auto-appears when a row has `url`.

The table scrolls horizontally on screens narrower than 640px — no layout shift.

---

### Callouts

Use the markdown-paired form (`{{% %}}`) so you can put bullets / links inside.

#### Tip (sage / green)

```
{{% tip title="Renter tip" %}}
If your sink threads are non-standard (older NYC buildings often are),
a $4 universal-thread adapter solves it. Don't try to force a fit.
{{% /tip %}}
```

#### Warning (clay / amber) — most-common-mistake

```
{{% warning title="The most common mistake" %}}
The pressure regulator goes _after_ the timer, not before.
Backwards, it'll either underwater or burst a fitting.
{{% /warning %}}
```

#### Note (neutral)

```
{{% note %}}
All prices verified May 2026. We re-check quarterly.
{{% /note %}}
```

`title=` is optional. Defaults: "Tip", "Heads up", "Note".

---

## Frontmatter knobs (per-article)

```toml
+++
title         = "How to Build a Self-Watering Balcony Drip System"
date          = 2026-05-10
description   = "A complete, parts-list-included walkthrough for renters."
image         = "/images/setup/balcony-drip-hero.jpg"
image_alt     = "Drip irrigation installed along a Brooklyn balcony railing"
image_caption = "The system in question, photographed in Carroll Gardens, May 2026."
author        = "Maya Chen"
categories    = ["setup-guides"]
tags          = ["drip irrigation", "renters", "setup", "beginner"]

# Optional overrides ↓
toc           = true        # default true; set false to hide TOC entirely
toc_position  = "left"      # "left" | "floating" | "inline"
disclosure    = true        # default true; set false for non-affiliate pages
kicker        = "Setup Guide · The Essentials"   # overrides the auto-derived kicker
+++
```

---

## Site-level config (`config.toml`)

### Add or remove a category

```toml
[[params.categories]]
  slug  = "winter-prep"     # matches /content/winter-prep/
  name  = "Winter Prep"
  blurb = "Draining, storing, and what to leave outside when the freeze comes."
  icon  = "winter"          # references partials/ill/winter.svg
```

To add a new icon, drop an SVG into `layouts/partials/ill/your-icon.svg`
(56×56 viewBox, 64×64 outer, sage strokes). Reference it via `icon = "your-icon"`.

### Edit the "Start here" 3-step path

```toml
[[params.start_here]]
  number = "01"
  title  = "Do you actually need drip?"
  blurb  = "A four-question test."
  time   = "4 min read"
  url    = "/setup-guides/do-you-need-drip/"
```

The numbered path is fully editorial — change titles, URLs, even how many
steps (the grid handles 1–4 cleanly).

---

## When to use which affiliate pattern

| Article type                       | Pattern               |
|------------------------------------|-----------------------|
| Setup guide with one recommended product | **Editor's Pick** once, mid-article |
| Buying guide / "Best X of 2026"    | **Comparison table** at top, **Affiliate cards** for top 3 picks |
| Troubleshooting / how-to with peripheral mentions | **Inline `{{< aff >}}`** within prose |
| Single-product deep review         | **Affiliate card** at top with pros/cons |

Rule of thumb: **one prominent affiliate moment per article, anchored to
specific lived experience.** That's what makes the recommendation feel
trustworthy rather than spammy.

---

## Files you'll edit most

| Job                                  | File |
|--------------------------------------|------|
| Change a color                       | `static/css/tokens.css` |
| Change a font                        | `static/css/tokens.css` + `partials/head.html` (CDN URL) |
| Change nav links                     | `config.toml` → `[[params.categories]]` |
| Change footer links                  | `partials/footer.html` |
| Change the hero copy                 | `partials/hero.html` |
| Change "Start here" steps            | `config.toml` → `[[params.start_here]]` |
| Tune the article layout              | `static/css/site.css` → `.article-layout`, `.article`, `.prose` |

Almost everything else should be left alone. If you find yourself touching
templates more than three times in a week, the site's design system has
drifted — file an issue, don't keep patching.
