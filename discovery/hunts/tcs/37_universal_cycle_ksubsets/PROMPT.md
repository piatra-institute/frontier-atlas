# 37. A universal cycle of k-subsets at an open parameter

**Find.** A universal cycle (Ucycle) for the k-subsets of an n-set at a specific (n, k) where existence is open or unverified. A Ucycle for k-subsets is a cyclic sequence a_0 a_1 ... a_{m-1} over {1..n} (m = C(n,k)) such that the m windows of k consecutive symbols are exactly the C(n,k) distinct k-subsets, each once. Chung-Diaconis-Graham conjectured these exist whenever the obvious divisibility conditions hold and n is large enough; specific small (n, k) cases remain unresolved (verify the target).

**What counts as a win.** One explicit cyclic sequence over {1..n} of length C(n,k) whose consecutive-k windows are all distinct as sets and cover every k-subset. One-sided: a single Ucycle settles existence for that (n, k).

**Checker (seconds).** Slide a length-k window cyclically; for each window take the *set* of its symbols; assert (a) each window's k symbols are distinct, (b) the collection of C(n,k) window-sets equals all k-subsets of {1..n}, each exactly once. Hash sets; O(C(n,k) * k), fast for the small parameters at issue.

**Search plan.** Structured: model as an Eulerian/Hamiltonian problem on the transition graph of (k-1)-prefixes; search for a Hamiltonian cycle covering all k-subsets with backtracking + pruning, or SAT/CP; use known constructions (Hurlbert, Jackson) as scaffolding and repair.

**Prior art (verify).** Chung, Diaconis, Graham, "Universal cycles for combinatorial structures" (1992); Hurlbert on Ucycles of k-subsets; Jackson. Verify which small (n, k) cells are still open.
