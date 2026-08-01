# 21. Beat a best-known lotto design L(n,k,p,t)

**Target.** Find a lotto design L(n,k,p,t) with fewer tickets than the current best-known upper bound in the La Jolla repository, for a cell above the lower bound. An L(n,k,p,t) is a set of k-subsets (tickets) of an n-set such that every p-subset (a "draw") meets at least one ticket in >= t elements; the lotto number L(n,k,p,t) is the minimum number of tickets.

**What counts as a win.** One explicit ticket list of size strictly below the tabulated best-known, still guaranteeing a >= t match for every p-subset, improves the upper bound (one-sided). Pick a specific (n,k,p,t) with a gap.

**Checker (seconds).** Read b tickets (k-subsets of {0..n-1}). For every p-subset S of {0..n-1}, verify some ticket T has |S intersect T| >= t; and b < best-known. Enumerate the C(n,p) draws; keep n,p modest so this runs in seconds. O(C(n,p) * b).

**Search plan.** Randomized greedy + restarts; simulated annealing swapping ticket elements; covering-design-based constructions (a lotto design generalizes coverings: L(n,k,t,t) is a covering); cyclic base-block search; ILP for small instances.

**Prior art (verify).** Best-known lotto designs and bounds are tabulated in the La Jolla Covering Repository (lotto tables, D. Gordon, ljcr.dmgordon.org) and the lotto-design literature (Li, van Rees). A cell with upper > lower is open. Re-verify the current best-known before claiming.

**Openness:** documented-open. **Win-type:** found-object.
