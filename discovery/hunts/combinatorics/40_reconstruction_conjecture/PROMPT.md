# 40. Counterexample to the Reconstruction Conjecture

**Target.** Find two non-isomorphic graphs G, H on n >= 12 vertices with the same deck: the multiset of vertex-deleted subgraphs { G - v : v in V(G) } equals { H - w : w in V(H) } up to isomorphism. The Reconstruction Conjecture (Kelly, Ulam) asserts no such pair exists for n >= 3. A single pair refutes it. All graphs on up to 11 vertices are known reconstructible (McKay).

**What counts as a win.** One explicit pair (G, H), non-isomorphic, with identical decks, refutes the conjecture (one-sided NO).

**Checker (seconds).** Read G, H (graph6). Verify same n and same degree sequence. Compute nauty canonical forms of G and H; assert they differ (non-isomorphic). Compute each deck as a sorted multiset of canonical forms of the n vertex-deleted subgraphs; assert the two multisets are equal. O(n) canonicalizations, fast for n around 12-14.

**Search plan.** Search among graphs with the same degree sequence and matching subdeck statistics; use the known constraints (number of edges and degree sequence are reconstructible) to prune; hunt near-reconstruction pairs (graphs sharing all but one card) and try to close the last card; regular graphs and highly symmetric graphs are natural candidates.

**Prior art (verify).** Reconstruction is verified for all graphs on <= 11 vertices (B. McKay, computational). The conjecture is open in general. Re-verify no counterexample and the current computational frontier before starting.

**Openness:** documented-open. **Win-type:** counterexample.
