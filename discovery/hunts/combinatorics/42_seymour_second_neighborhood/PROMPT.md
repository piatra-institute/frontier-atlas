# 42. Counterexample to Seymour's Second Neighborhood Conjecture

**Target.** Find an oriented graph (a digraph with no loops and no 2-cycles) in which every vertex v has |N++(v)| < |N+(v)|, where N+(v) is the out-neighborhood and N++(v) the set of vertices reachable by exactly two forward steps but not one. Seymour's Second Neighborhood Conjecture asserts every oriented graph has at least one vertex with |N++(v)| >= |N+(v)|. A digraph where all vertices fail this refutes it.

**What counts as a win.** One explicit oriented graph in which |N++(v)| < |N+(v)| for every vertex refutes the conjecture (one-sided NO).

**Checker (seconds).** Read the digraph as an adjacency matrix A (no i with A[i][i], no pair with both A[i][j] and A[j][i]). For each v compute N+(v) = out-neighbors, N++(v) = {w != v : w not in N+(v) and exists u in N+(v) with edge u->w}. Assert |N++(v)| < |N+(v)| for all v. O(n^3).

**Search plan.** Tournaments are known to satisfy the conjecture (Fisher; Havet-Thomasse for tournaments), so search sparse and unbalanced oriented graphs; local search / tabu on orientations minimizing the count of "good" vertices; prescribed-automorphism / Cayley digraphs; SAT over edge-orientation variables encoding the all-vertices-fail condition.

**Prior art (verify).** Seymour's Second Neighborhood Conjecture is open in general (proven for tournaments and some classes). No counterexample is known; small cases have been checked. Re-verify the current status and any computational bounds before starting.

**Openness:** documented-open. **Win-type:** counterexample.
