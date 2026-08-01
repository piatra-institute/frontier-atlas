# 19. Beat a best-known packing design D(v,k,t)

**Target.** Find a packing design D(v,k,t) with MORE blocks than the current best-known lower bound (largest known packing) in the La Jolla repository, for a cell where the best-known packing is below the upper (Johnson-type) bound. A packing is a family of k-subsets of a v-set in which every t-subset lies in at most one block; the packing number is the maximum block count.

**What counts as a win.** One explicit block list with strictly more blocks than the tabulated best-known, still a valid packing, improves the lower bound (one-sided). Pick a specific (v,k,t), typically t=2.

**Checker (seconds).** Read b blocks (k-subsets of {0..v-1}). Verify each block size k, every t-subset is covered at most once (t-subset counter, assert max <= 1), and b > best-known. O(b*C(k,t) + C(v,t)).

**Search plan.** Maximal-packing greedy with randomized restarts; local search adding blocks after removing conflicts; cyclic base-block (difference-family) constructions; leave-graph analysis to squeeze in extra blocks; ILP maximizing block count for small v.

**Prior art (verify).** Best-known packings and upper bounds are in the La Jolla Covering Repository (packing tables, D. Gordon, ljcr.dmgordon.org). A cell where the packing number is not pinned down is open. Re-verify the current best-known before claiming an improvement.

**Openness:** documented-open. **Win-type:** found-object.
