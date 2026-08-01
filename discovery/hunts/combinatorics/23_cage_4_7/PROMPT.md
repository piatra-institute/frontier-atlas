# 23. Smaller (4,7)-cage graph

**Target.** Construct a 4-regular graph of girth exactly 7 on fewer vertices than the current best-known record. The (4,7)-cage number n(4,7) is open, bracketed between a lower bound (above the Moore bound 53) and the best-known construction.

**What counts as a win.** One explicit 4-regular graph of girth exactly 7 on m vertices with m strictly below the best-known record improves the upper bound (one-sided). If it also meets the current lower bound it determines n(4,7) exactly.

**Checker (seconds).** Read adjacency (graph6). Verify every degree = 4, and girth = 7 exactly via per-vertex truncated BFS to depth 4 (shortest cycle length must be exactly 7). O(v * (v + edges)).

**Search plan.** Cayley graphs over groups of the target order with connection set screened for girth 7; voltage-graph lifts of small quartic base graphs; incidence / biaffine-plane amalgams; excess pruning plus isomorph-free augmentation for small orders; simulated annealing on 4-regular adjacency maximizing girth.

**Prior art (verify).** Best-known record and bounds are in G. Exoo and R. Jajcay, "Dynamic Cage Survey," EJC dynamic survey DS16. Re-verify the current (4,7) record order before starting; confirm the pair is still open (some small (r,g) once thought open have been settled).

**Openness:** documented-open. **Win-type:** found-object.
