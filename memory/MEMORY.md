# betmaker-lucky-slip

Prototype **3 · Odds field — "Lucky Slip"** extracted from
`~/Downloads/BetMaker Direct (standalone) (2).html` (a Claude Design
self-extracting bundle) and rebuilt as a fluid full-viewport page for Maze.

Live: https://jimpawa.github.io/betmaker-lucky-slip/
Repo: https://github.com/jimpawa/betmaker-lucky-slip (public, Pages =
"deploy from branch", main / root — no Actions workflow because the `gh`
token lacks the `workflow` scope). Deploy = `git push`.

## The key finding
Option 3 is NOT a new design. In the bundle it is literally
`["optLucky", () => <OptSlider title="Lucky Slip" />]` — the same component
as option 2, with the section heading changed. Everything else (odds field,
generator, betslip) is identical to [[betmaker-odds-field]].

## Pipeline
Same as betmaker-odds-field — see that project's memory for the Claude
Design "(standalone)" bundle format. Only the asset UUIDs change between
exports, so `src/build.py` is that script with the UUIDs swapped.
