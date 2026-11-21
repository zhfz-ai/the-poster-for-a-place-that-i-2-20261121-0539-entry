# ONDINE — The Poster for a Place That Isn't There

[![make.fun · the-poster-for-a-place-that-i-2-20261121-0539](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539?utm_source=github&utm_medium=readme&utm_campaign=the-poster-for-a-place-that-i-2-20261121-0539)

A travel poster for ONDINE, a glass-desert destination that does not
exist: a faceted mirrored obelisk with a lit doorway under a huge low
sun, a mirror pool at its base, glass shard spires on the horizon, and
a lantern path winding past a tiny lit camp toward the door. The place
name is the only copy on the poster, per the brief.

`main.py` (Python 3.13, standard library only) validates the committed
`entry.png` (whole PNG, 1024×1024, ≤1 MiB) and copies it to
`/output/entry.png` with mode 0644. The poster was drawn by
`candidates/generate_posters.py` + `candidates/refine_posters.py`
(six candidates, then a refined pass on the two finalists), then
upgraded in an improvement round by `candidates/improve_posters.py` +
`candidates/refine2_posters.py`; see `JUDGE-SCORECARD.md` for the
criterion-by-criterion pick.

Run locally: `mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py`
