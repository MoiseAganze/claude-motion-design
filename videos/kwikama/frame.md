# frame.md — KWIKAMA

Brand truth taken from the prototype's own CSS variables (kwikama.vercel.app, `:root`). Strict: hex values, fonts, weights.

## Palette

| Role            | Token        | Hex       |
| --------------- | ------------ | --------- |
| Background      | navy-700     | `#052649` |
| Wall / panel    | navy-600     | `#0a3360` |
| Deep navy       | navy-900     | `#031829` |
| Navy mid        | navy-500     | `#13487f` |
| Navy muted text | navy-200     | `#afc5d8` |
| Accent (gold)   | or-400       | `#d8a828` |
| Gold light      | or-300       | `#e7c266` |
| Gold deep       | or-500       | `#a98310` |
| Paper (cards)   | ivoire       | `#fbf9f5` |
| Paper 2         | craie        | `#f4f1ea` |
| Ink (on paper)  | encre        | `#13181e` |
| Ink 2           | ardoise      | `#495867` |
| Critical        | critique     | `#9b2c24` |
| Success         | succes       | `#1e6b4f` |

One accent: gold. Every motion-designed frame sits on `#052649`. Gold is a hairline / node / signature color, never a fill behind text.

## Typography

- Display: **Fraunces** (serif), 500–600, tight leading 1.15 — headlines, the word KWIKAMA, chapter titles.
- UI / body / labels: **Inter**, 400–600; small caps labels in Inter 600 with +0.08em tracking (as the site does).
- Fonts are local woff2 files in `assets/fonts/` (latin subset — é à ç).

## Motion personality

Institutional, calm, exact. Eases: `power2.out` / `power3.out` for arrivals, `power2.inOut` for camera moves,
the script's `cubic-bezier(0.2, 0.7, 0.3, 1)` for the convergence. No bounce, no elastic, no blur, no rotation, no shake,
no particles, no flares, no halos. `transform` and `opacity` only.

## Screen captures

Real prototype states captured at 3840×2160 (1920×1080 @2x) and shown full-bleed, scale ≥ 1.0 — never shrunk (text must never get
smaller than the real UI). Cursor is a drawn SVG pointer, slow, with a 1.5 s hold after each click.

## Do / Don't

- Do: hairline gold rules, generous navy space, real data from the prototype, small Inter caps labels.
- Don't: gradients on text, neon, glow, emoji, invented screens or invented numbers.
