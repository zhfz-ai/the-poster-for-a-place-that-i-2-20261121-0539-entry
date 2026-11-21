# Judge scorecard — The Poster for a Place That Isn't There

Brief (from kit RULES.txt, judge criteria in order):
1. Travel poster for a place that does not exist, invented place name set into the picture (no other copy: no quotes, ratings, taglines).
2. Makes you want to go: weather, light, one landmark = clear promise of a stay.
3. Distinct identity: name, landmark, atmosphere specific to this poster.
4. Type with intent: name legible, well placed, carries the mood.
5. Colour/composition sell the place: palette + layout leads eye name → landmark → horizon.
Clutter for its own sake does not count. Gate: /output/entry.png whole PNG/JPEG ≤1 MiB, 1024×1024.

Scores 0–2 per criterion, judged in brief order (lexicographic, not averaged).

| Candidate | 1 On-brief+name | 2 Want to go | 3 Distinct identity | 4 Type | 5 Colour/composition | Verdict |
|---|---|---|---|---|---|---|
| C1 VELMARA (floating isle lighthouse) | 2 | 1 — sun hidden behind isle, beams render grey, clouds read as eggs | 2 — floating isle is specific | 2 | 1 — horizon line cuts the isle, eye stalls mid-poster | Out: landmark scene muddled |
| C2 ONDINE v1 (glass desert obelisk) | 2 | 2 — huge low sun + warm dunes, instant heat promise | 2 — glass dunes + mirrored obelisk | 2 | 2 — name → sun → obelisk → dune horizon | Finalist, refined |
| C3 MIRALUNE (moon bay tower) | 2 | 1 — calm but cold; crescent finial collides with moon disc, reads as a bite/error | 1 — moon-over-bay is a familiar poster | 2 | 1 — landmark off-centre, moon dominates it | Out: landmark loses to moon |
| C4 SOLVANE v1 (terraced shell-mountain) | 2 | 2 — golden hour, lit houses promise a stay | 2 — spiral terraces specific | 2 | 1 — mountain reads slightly as a decorated tree | Finalist, refined |
| C5 AERTHOS (ring city) | 2 | 1 — pretty sky, but ring reads as crown/candles, gardens as lollipops | 2 — ring city is fresh | 2 | 1 — landmark ambiguous at a glance | Out: landmark unclear |
| C6 NULHAVEN (aurora lighthouse-tree) | 2 | 1 — aurora lovely, landmark reads as antenna | 1 — aurora shore is borrowed scenery | 1 — tower pole crosses the name, H/A split | 1 — name fights landmark | Out: type + landmark fail |
| C7 ONDINE v2 (refined) | 2 | 2 | 2 | 2 | 2 — faceted obelisk, sun halo, sparse sparkle, dune rim lines | **WINNER** |
| C8 SOLVANE v2 (refined) | 2 | 2 | 2 | 2 | 1 — still tree-like silhouette | Runner-up |

## Pick: C7/C9 ONDINE (final bytes = candidate-9-ondine-final.png)

- Criterion 1: invented name ONDINE set into the sky band; no other copy anywhere.
- Criterion 2: one landmark (mirrored obelisk), one light (huge low sun), one weather (glass-desert heat) — the stay promise reads in under a second.
- Criterion 3: glass dunes with sparse sparkle + a faceted mirror obelisk is not a real destination or a stock poster.
- Criterion 4: tracked-out bold sans, cream on deep teal, double rule in sun-gold; legible at 300px (checked).
- Criterion 5: teal/amber complementary palette; eye path name → sun disc → obelisk → dune horizon; sparkle kept sparse (clutter does not count).

300px downscale check: passed (name, obelisk, sun, dunes all instantly clear).
File: 416,283 bytes, 1024×1024 PNG — inside the 1 MiB gate.

## Improvement round (rank 342/610 → resubmit)

The flat v1 poster read as generic at judging size. Three richer
candidates (`candidates/improve_posters.py`), then one refinement
(`candidates/refine2_posters.py`):

| Candidate | 1 On-brief+name | 2 Want to go | 3 Distinct identity | 4 Type | 5 Colour/composition | Verdict |
|---|---|---|---|---|---|---|
| C10 golden v1 | 2 | 2 — warm sun, lantern path, travellers | 2 — mirror pool, lit door | 2 — serif display | 1 — mesas read as houses, clouds caterpillar-like | Refined |
| C11 dusk | 2 | 1 — moody, less warmth | 2 — glowing path at dusk | 2 | 2 | Runner-up |
| C12 dawn | 2 | 1 — washed out, low contrast | 1 — pale = generic | 2 | 1 | Out |
| C13 golden v2 | 2 | 2 — sun + lit camp + lantern path = stay promise | 2 — glass shard spires echo the obelisk, mirror pool, lit doorway | 2 — letterspaced serif, diamond rules, poster frame | 2 — name → sun → obelisk → pool → path → camp | **WINNER** |

Final bytes = `candidate-13-ondine-golden-v2.png` (803,394 bytes,
1024×1024). 300px check (`check-300px-v2.png`): name, sun, obelisk,
pool and path all instantly clear.
