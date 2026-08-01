# 20. Beat a best-known Turan system T(n,k,r)

**Target.** Find a Turan (n,k,r)-system with fewer blocks than the current best-known upper bound in the La Jolla repository, for a cell above the best lower bound. A Turan (n,k,r)-system is a family of r-subsets of an n-set such that every k-subset contains at least one system member; the Turan number T(n,k,r) is the minimum such count. (It is the complement/dual of a covering.)

**What counts as a win.** One explicit family of r-subsets of size strictly below the tabulated best-known, still meeting every k-subset, improves the upper bound (one-sided). Choose a specific (n,k,r) with a documented gap; the classic hard family is r=3.

**Checker (seconds).** Read b blocks (r-subsets of {0..n-1}). Verify each block size r, every one of the C(n,k) k-subsets contains at least one block, and b < best-known. For each k-subset, test membership of some block (index blocks by their elements for speed). O(C(n,k) * (something)) - keep n modest so this runs in seconds.

**Search plan.** Complement to covering search: randomized greedy, simulated annealing, cyclic/prescribed-automorphism base-block search; recursive product constructions of Turan systems (Sidorenko, de Caen).

**Prior art (verify).** Best-known Turan systems and bounds are in the La Jolla Covering Repository (Turan tables) and the Turan-system literature (Sidorenko's survey of the Turan (n,k,r) problem). T(n,k,3) values are largely open. Re-verify the target cell's current best.

**Openness:** documented-open. **Win-type:** found-object.
