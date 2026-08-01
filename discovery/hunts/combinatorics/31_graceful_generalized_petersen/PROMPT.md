# 31. Graceful labeling of a generalized Petersen graph (open case)

**Target.** For a generalized Petersen graph P(n,k) whose gracefulness is listed as open in Gallian's labeling survey, either exhibit a graceful labeling (found-object) or, for a family conjectured graceful, exhibit a small member with no graceful labeling (counterexample). P(n,k) has 2n vertices and 3n edges. Gracefulness of P(n,k) is settled for several k but open for others.

**What counts as a win.** A graceful labeling of a specific open P(n,k) settles that case (one-sided YES). Alternatively, for a member small enough to check exhaustively, a certified "no graceful labeling exists" refutes a stated gracefulness claim for the family (one-sided NO).

**Checker (seconds).** Graph has m = 3n edges. Read vertex labels f: V -> {0..m}, injective. Verify the multiset of |f(u)-f(v)| over edges equals exactly {1,2,...,m}. O(m). For a nonexistence claim on a small graph, exhaust labelings (feasible only for small m) and confirm none is graceful.

**Search plan.** Backtracking with the distinct-edge-difference constraint and strong pruning; SAT/CP model (labels as integer variables, all-different on vertices and on edge differences); constructive rotational labelings; local search minimizing repeated edge differences.

**Prior art (verify).** J.A. Gallian, "A Dynamic Survey of Graph Labeling," Electronic Journal of Combinatorics, DS6 (updated regularly), lists which P(n,k) gracefulness cases are open. Re-verify the chosen (n,k) is still open.

**Openness:** verify. **Win-type:** found-object / counterexample.
