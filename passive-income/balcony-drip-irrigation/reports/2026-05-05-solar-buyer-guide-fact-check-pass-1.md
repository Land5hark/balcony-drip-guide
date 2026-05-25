- Lane: fact review / trust hardening
- Status: pass completed
- Page: `site/content/posts/best-solar-drip-irrigation-kits-for-patios-and-balconies.md`
- Scope: verify the two named RainPoint solar-kit branches and their governed placeholder fit on the solar buyer guide
- Timestamp: 2026-05-05 02:30 EDT

## Sources checked
- `https://www.rainpointonline.com/products/rainpoint-compact-programmable-solar-automatic-drip-irrigation-pump-kits-support-up-to-20-plants`
- `https://www.rainpointonline.com/products/rainpoint-smart-wifi-solar-automatic-plant-watering-system-for-house-potted-plants-gen-2`
- `site/data/link-registry.yaml`

## Verified clean
### Compact solar primary path
Confirmed from the live RainPoint page:
- title/product path still maps to **RAINPOINT Compact Programmable Solar Automatic Drip Irrigation Pump Kits Support Up to 20 Plants**
- copy still positions it for **sunny balcony setups**
- copy still supports the article's solar / reservoir / low-water-shutoff framing
- the article's warning that plant-count claims are an upper bound still looks sane, because the live page keeps leaning on `20+ plants` style marketing language

### Premium smart solar path
Confirmed from the live RainPoint page:
- title/product path still maps to **RAINPOINT Smart WiFi Solar Automatic Plant Watering System for House Potted Plants Gen 2**
- live copy still supports the article's cited feature shape:
  - **16.4 ft / 5 m** lift
  - **6 schedules**
  - low-water / clog alerts
  - safe pump shutoff
  - balcony / fence / windowsill mounting language
- that keeps the article's premium-control framing materially aligned with the seller page

### Governed destination fit
Confirmed in `site/data/link-registry.yaml`:
- `bdi-solar-rainpoint-compact-primary` points at the compact solar product path
- `bdi-solar-rainpoint-smart-primary` points at the smart solar Gen 2 path
- `bdi-solar-rainpoint-primary` currently duplicates the compact solar path, which is acceptable as a general solar fallback and not obviously misleading

## No immediate article correction required
The named-product claims checked in this pass are still materially aligned with live seller copy.

## Minor caution
The smart-solar page extract included some noisy extra storefront text below the relevant product block, so this pass trusts the clearly matching title/feature section and not the whole scraped tail. Annoying, but not enough to break the verification.

## Outcome
The solar buyer guide is in decent shape on its named-product branch:
- compact solar path verified
- premium smart solar path verified
- governed destinations still match the article's buyer logic

It still is not affiliate-ready, but this page no longer looks like the weak link in the no-faucet solar lane.