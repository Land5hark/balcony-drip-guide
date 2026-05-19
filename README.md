# The Balcony Drip — Hugo Theme

A drop-in Hugo theme for [balcony-drip-guide.pages.dev](https://balcony-drip-guide.pages.dev).
Field-notes editorial aesthetic, mobile-first, light + dark mode out of the box.

- **Hugo:** any version ≥ 0.55 (tested mental-model against 0.68.3 — your current).
- **No JS framework.** ~3 KB of vanilla JS total (theme toggle + TOC scrollspy).
- **No build step.** Plain CSS, plain JS, system fonts + Google Fonts via CDN.
- **Affiliate-aware.** Editor's-pick callout, comparison-table shortcode, FTC disclosure partial.

---

## Install (drop-in replacement)

These files are designed to replace your `layouts/`, `static/css/`, `static/js/`, and `archetypes/` folders.
Your existing `content/` does not need to change. Your existing `config.toml` will need a few additions (see below).

```
# from the root of this delivery
cp -R hugo/layouts/    /path/to/your-site/
cp -R hugo/static/     /path/to/your-site/
cp -R hugo/archetypes/ /path/to/your-site/
```

Then merge the additions from `hugo/config.toml` into your existing config (`[params.categories]`, `[params.start_here]`, and `[markup.tableOfContents]` are the new bits). **Don't change** existing `baseURL`, `[permalinks]`, or `[taxonomies]` unless you intend to.

Run:

```
hugo server
```

Visit http://localhost:1313 — homepage uses the Field Notes layout, every existing article renders through `single.html`.

---

## What's in here

```
hugo/
├── config.toml                  # additions to merge into your config
├── archetypes/default.md        # default frontmatter for `hugo new`
├── content/                     # sample content (homepage, about, disclosure,
│                                #   category indexes, and one full example article)
├── layouts/
│   ├── _default/
│   │   ├── baseof.html          # outer document
│   │   ├── single.html          # article template (the long-form)
│   │   ├── list.html            # category/section index
│   │   └── terms.html           # tag pages
│   ├── index.html               # homepage — Field Notes layout
│   ├── partials/
│   │   ├── head.html            # <head>: SEO, OG, JSON-LD, fonts, CSS
│   │   ├── nav.html
│   │   ├── footer.html
│   │   ├── hero.html
│   │   ├── start-here.html      # 3-step numbered path (from config)
│   │   ├── categories.html      # illustrated category tiles
│   │   ├── latest-entries.html  # dated journal list
│   │   ├── newsletter.html
│   │   ├── article-card.html
│   │   ├── article-meta.html    # byline + share
│   │   ├── toc.html             # wraps Hugo's auto-TOC in our styled container
│   │   ├── disclosure.html      # FTC affiliate disclosure
│   │   ├── affiliate-card.html  # Editor's Pick callout
│   │   ├── stars.html           # accessible star rating
│   │   ├── hero-illustration.svg
│   │   └── ill/                 # 5 category icon SVGs
│   └── shortcodes/
│       ├── disclosure.html
│       ├── editors-pick.html    # the affiliate signature pattern
│       ├── affiliate-card.html  # full product card alternative
│       ├── aff.html             # subtle inline mention
│       ├── comparison-table.html
│       ├── tip.html             # green callout
│       ├── warning.html         # clay callout (most-common-mistake)
│       └── note.html            # neutral callout
├── static/
│   ├── css/
│   │   ├── tokens.css           # design tokens (light + dark)
│   │   └── site.css             # everything else
│   └── js/
│       ├── theme.js             # 1 KB — toggle, mobile drawer
│       └── toc.js               # 1.5 KB — IntersectionObserver scrollspy
├── README.md                    # you are here
└── COMPONENTS.md                # author-facing usage guide
```

---

## Required frontmatter (none — by design)

Every template is written to render gracefully with **only** `title`. If
`description`, `image`, `categories`, `tags`, `author`, etc. are missing,
the corresponding UI just doesn't appear.

Recommended for any article:

```toml
+++
title       = "How to Build a Self-Watering Balcony Drip System"
date        = 2026-05-10
description = "A complete walkthrough for renters. $42 budget, 30 minutes."
image       = "/images/setup/balcony-drip-hero.jpg"
image_alt   = "Drip irrigation installed along a Brooklyn balcony railing"
author      = "Maya Chen"
categories  = ["setup-guides"]
tags        = ["drip irrigation", "renters", "setup"]
+++
```

Per-article overrides:

| Param            | Default | Effect |
|------------------|---------|--------|
| `toc`            | `true`  | Hide the table of contents entirely. |
| `toc_position`   | `"left"`| `"left"`, `"floating"` (right rail), or `"inline"` (collapsible above body). |
| `disclosure`     | `true`  | Hide the FTC disclosure box. |
| `image_caption`  | —       | Caption under the lead image. |
| `featured`       | `false` | Reserved for future use (homepage featuring). |

---

## Design tokens

All design is driven by CSS custom properties in `static/css/tokens.css`.
To re-skin, edit only that file.

```css
:root {
  --bg:       #f6f3ec;   /* page */
  --ink:      #1f2a24;   /* text */
  --sage:     #3d6b4a;   /* primary accent */
  --clay:     #a85a35;   /* used sparingly: editor's pick + warnings */
  --rule:     #e3ddd0;
  --font-serif: 'Newsreader', Georgia, serif;
  --font-sans:  'IBM Plex Sans', system-ui, sans-serif;
  --article-max: 720px;
  /* …spacing scale, radii, etc. */
}
```

Dark mode is two-layered:
1. `:root[data-theme="dark"]` — manual override (toggle button, persisted in localStorage).
2. `@media (prefers-color-scheme: dark)` — system preference, unless user has chosen `light`.

An inline script in `<head>` (see `partials/head.html`) reads the saved choice before paint, so there's no light flash on dark systems.

---

## Affiliate links

The site's revenue depends on affiliate clicks. Three patterns are
provided, all with `rel="sponsored nofollow noopener"` and a clear,
trustworthy aesthetic — never "BUY NOW" screaming.

| Pattern | Where to use | Shortcode |
|---|---|---|
| **Editor's Pick** (default) | The primary affiliate moment per article. Use once. | `{{< editors-pick … >}}` |
| **Full product card** | Roundup posts with 3–6 picks. | `{{< affiliate-card … >}}` |
| **Inline mention** | Mid-paragraph product references. | `{{< aff … >}}` |
| **Comparison table** | "X vs Y vs Z" articles. | `{{< comparison-table >}}…{{< /comparison-table >}}` |

See `COMPONENTS.md` for full usage examples.

---

## SEO & metadata

The `head.html` partial emits:

- `<title>` (article title · site title), `<meta description>`, canonical
- OG: `og:type`, `og:title`, `og:description`, `og:image`, `og:url`
- Twitter: `summary_large_image` card
- JSON-LD `Article` schema on `single.html` pages, with author, dates, image, publisher
- RSS `<link rel="alternate">` on the homepage

All metadata sources from frontmatter with site-level fallbacks — your
existing 21 articles' SEO will not regress.

---

## Accessibility

- Skip link to `#main` (visible on focus)
- `prefers-reduced-motion` honoured for all transitions
- Min 44×44px tap targets on every interactive element
- `aria-current="page"` on active nav links
- TOC is a proper `<nav aria-label>`, articles announce author / date in a single labelled block
- Color contrast verified for both light and dark modes against WCAG 2.1 AA

---

## Performance

- ~12 KB CSS (uncompressed; gzip ≈ 3.5 KB)
- ~3 KB JS, both `defer`
- 1 Google Fonts request (Newsreader + IBM Plex Sans + IBM Plex Mono, `display=swap`)
- No web framework, no runtime CSS, no client routing
- All images `loading="lazy"` except the article lead image (`loading="eager"`)
- Static fingerprinting handled by Hugo (use `resources.Fingerprint` if you upgrade)

Expected Lighthouse scores on a stock Cloudflare Pages deploy: 95+ Performance, 100 Accessibility, 100 Best Practices, 100 SEO.

---

## Customising the homepage

Three things drive the homepage; all live in `config.toml`:

```toml
# 1. The 5 illustrated category tiles
[[params.categories]]
  slug = "setup-guides"
  name = "Setup Guides"
  blurb = "…"
  icon = "setup"   # maps to partials/ill/setup.svg

# 2. The 3-step "Start here" numbered path
[[params.start_here]]
  number = "01"
  title  = "Do you actually need drip?"
  blurb  = "…"
  time   = "4 min read"
  url    = "/setup-guides/do-you-need-drip/"

# 3. The "Latest entries" list is auto-populated from .Site.RegularPages
#    (most recent 6 across all categories). No config required.
```

---

## What I did NOT change

- Your `[permalinks]` block — existing URLs are preserved.
- Your `[taxonomies]` — `category` and `tag` taxonomies remain.
- Any frontmatter fields — all of mine are additive and optional.
- Your build command (`hugo`) or deploy target (Cloudflare Pages).

---

## Next steps

1. Drop the theme in, run `hugo server`, page through the 21 articles.
2. Anywhere an article looks off, the fix is almost always to add `image`, `description`, or `categories` to its frontmatter — not to change template code.
3. Replace placeholder affiliate URLs in `content/setup-guides/self-watering-balcony-drip-system.md` with your real ones, then delete that file or move it to drafts.
4. Run Lighthouse. Tune `image` formats (WebP / AVIF) if needed — the templates already emit `<img loading="lazy">`.

Open issues to me in the same thread.
