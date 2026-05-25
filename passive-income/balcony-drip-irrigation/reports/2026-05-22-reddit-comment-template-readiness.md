# Reddit Comment Template Readiness - 2026-05-22

Purpose: make comment-only Reddit participation executable without placeholder cleanup during posting.

## Result

Replaced vague `[here]` placeholders in `promotion/reddit-posts.md` with direct live URLs for the three comment-response templates.

## Updated Templates

| Scenario | Destination | Verification |
| --- | --- | --- |
| Drip recommendations | `https://balcony-drip-guide.pages.dev/posts/balcony-watering-systems-complete-guide/` | 200 OK |
| Vacation watering | `https://balcony-drip-guide.pages.dev/posts/vacation-watering-for-container-gardens-using-drip-irrigation/` | 200 OK |
| Uneven watering | `https://balcony-drip-guide.pages.dev/posts/why-your-container-drip-system-is-watering-unevenly/` | 200 OK |

## Guardrail

`rg` found no remaining `[here]` placeholders in `promotion/reddit-posts.md`.

## Remaining Dependency

Actual Reddit posting or commenting remains owner/identity-gated. Use the templates only after Sharky approves the account identity and the target thread genuinely asks for help.
