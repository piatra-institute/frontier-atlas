# 24. Smaller cage graph for any open (r,g) with a small gap

**Target.** Pick an open (r,g) pair whose cage number n(r,g) has a small lower-upper gap in the current cage survey, and construct an r-regular graph of girth exactly g on fewer vertices than the best-known record. Good candidates include girth-6 cases where r-1 is not a prime power (e.g. (7,6): no projective plane of order 6, so the Moore bound 86 is unattainable) and other small-gap (r,g).

**What counts as a win.** One explicit r-regular graph of girth exactly g on m vertices, m strictly below the best-known record, improves the upper bound for that pair (one-sided). Record ties do not count.

**Checker (seconds).** Read adjacency (graph6) and the claimed (r,g). Verify every degree = r, and girth = g exactly via per-vertex truncated BFS to depth floor(g/2)+1. O(v * (v + edges)).

**Search plan.** Choose the pair to match method: girth-6 non-prime-power cases favor incidence-geometry and excess-guided isomorph-rejection search; other pairs favor Cayley / voltage-lift constructions over small groups screened for girth. Validate the whole pipeline on a solved cage before the open target.

**Prior art (verify).** Current records and bounds for every (r,g) are in G. Exoo and R. Jajcay, "Dynamic Cage Survey," EJC dynamic survey DS16. Re-verify the chosen pair's current record and that it is still open.

**Openness:** documented-open. **Win-type:** found-object.
