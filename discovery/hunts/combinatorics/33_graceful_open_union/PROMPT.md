# 33. Graceful labeling of a disjoint union listed open

**Target.** For a disjoint union of named graphs whose gracefulness Gallian's survey lists as open (unions of cycles, of complete graphs, of wheels, etc.), exhibit a graceful labeling of a specific such union (found-object), or a small member with no graceful labeling (counterexample). Disjoint unions are a rich source of open labeling cases because gracefulness is not preserved under union.

**What counts as a win.** A graceful labeling of a specific open union settles that case (one-sided YES). For a union small enough to exhaust, a certified nonexistence refutes a stated gracefulness claim (one-sided NO).

**Checker (seconds).** The union has m edges total. Read vertex labels f: V -> {0..m}, injective across the whole (disconnected) graph. Verify the multiset { |f(u)-f(v)| : uv an edge } equals exactly {1,...,m}. O(m). For nonexistence, exhaust only for small m.

**Search plan.** Backtracking with distinct-edge-difference pruning across components; CP/SAT with a single all-different over all vertex labels and over edge differences; combine per-component graceful/alpha-labelings with shifting (alpha-labelings compose well under union); local search on the global labeling.

**Prior art (verify).** J.A. Gallian, "A Dynamic Survey of Graph Labeling," EJC DS6, lists open gracefulness results for disjoint unions of specific families. Re-verify the chosen union is still open.

**Openness:** verify. **Win-type:** found-object / counterexample.
