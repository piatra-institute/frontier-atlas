# 32. Harmonious labeling of an open graph family member

**Target.** For a graph family whose harmoniousness Gallian's survey lists as open (or conjectured), exhibit a harmonious labeling of a specific member (found-object), or a small member proven to have none (counterexample). A graph with m edges is harmonious if its vertices can be labeled with distinct elements of Z_m (Z_{m+1} with one repeat for trees) so that the edge sums f(u)+f(v) mod m are all distinct.

**What counts as a win.** A harmonious labeling of a specific open member settles that case (one-sided YES). For a member small enough to exhaust, a certified "no harmonious labeling" refutes a stated claim (one-sided NO).

**Checker (seconds).** Graph has m edges. Read vertex labels in Z_m (injective, per the family's convention). Verify the m edge sums (f(u)+f(v)) mod m are all distinct (a permutation of Z_m). O(m). For nonexistence, exhaust labelings only when m is small.

**Search plan.** Backtracking with the distinct-edge-sum constraint; SAT/CP with all-different over vertex labels and edge sums modulo m; rotational / algebraic labelings over Z_m; local search penalizing edge-sum collisions.

**Prior art (verify).** J.A. Gallian, "A Dynamic Survey of Graph Labeling," EJC DS6, catalogues open harmonious-labeling cases (specific products, generalized Petersen graphs, disjoint unions, etc.). Re-verify the chosen family/member is still open.

**Openness:** verify. **Win-type:** found-object / counterexample.
