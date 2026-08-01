# 22. Smaller (3,13)-cage graph

**Target.** Construct a 3-regular graph of girth exactly 13 on fewer vertices than the current best-known record. The (3,13)-cage number n(3,13) is open: it is the first unknown cubic cage (all n(3,g) are known for g <= 12). The Moore bound is 190; the true value lies strictly above it, bracketed by a lower bound and the best-known construction.

**What counts as a win.** One explicit cubic graph of girth exactly 13 on m vertices with m below the best-known record strictly improves the upper bound (one-sided). Any improvement is a contribution to the cage survey.

**Checker (seconds).** Read adjacency (graph6). Verify every degree = 3, and girth = 13 exactly: per-vertex truncated BFS to depth 7 finds a shortest cycle of length exactly 13 (a shorter cycle disqualifies; girth > 13 also disqualifies). O(v * (v + edges)).

**Search plan.** Cayley graphs over small groups screened algebraically for girth; voltage-graph / regular-cover lifts of small base graphs with girth controlled by the voltage assignment; excess/spectral pruning to seed an isomorph-rejection tree; tabu / evolutionary edge-swap search maintaining 3-regularity and pushing girth to 13.

**Prior art (verify).** Best-known record and bounds are in G. Exoo and R. Jajcay, "Dynamic Cage Survey," Electronic Journal of Combinatorics, dynamic survey DS16 (periodically updated). Re-verify the current record order for (3,13) before committing; records drift.

**Openness:** documented-open. **Win-type:** found-object.
