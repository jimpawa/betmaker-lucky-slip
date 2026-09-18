# BetMaker — Odds field "Lucky Slip" (Maze build)

**Live:** https://jimpawa.github.io/betmaker-lucky-slip/

`index.html` — prototype **3 · Odds field — "Lucky Slip"** from
`BetMaker Direct (standalone) (4).html`, rebuilt as a normal responsive web
page: no device frame, fills the viewport at any size. Single self-contained
file (~1.1 MB) with fonts, icon sprite, React and app code inlined.

## Relationship to `betmaker-odds-field`
In the source bundle option 3 is the **same** `OptSlider` component as option
2, mounted as `<OptSlider title="Lucky Slip" />`. The section heading
("BetMaker" → "Lucky Slip") differs, and — as of bundle (4) — the CTA
("Generate Lucky Slip" / "Generating Lucky Slip…") and the info tooltip,
which now name Lucky Slip. Same odds input, same generator, same betslip.

## What changed vs. the source bundle
- Only `optLucky` is mounted; the review-page shell and the other two
  prototypes are gone.
- JSX precompiled, so Babel-standalone (3.1 MB) is dropped; React/ReactDOM
  are the 18.3.1 production UMD builds.
- Fonts: Roboto 400 + 700 only; variable + italic faces dropped.
- Casino artwork dropped — unused by this screen.
- `src/override.css` turns `.phone` into the page: 100% x 100% of the
  viewport, chrome full-bleed, content column capped at 680 px with `max()`
  gutters, safe-area padding on the bottom nav, betslip sheet on the same
  column.

## Rebuilding
```
cd src && node compile.js && cd .. && python3 src/build.py
```

## Verification
`src/check.mjs` (390x844, 768x1024, 1440x900, 360x640, 740x400) and
`src/flow.mjs` (odds -> Generate Betslip -> betslip sheet) both pass with no
console or page errors and no horizontal overflow.
