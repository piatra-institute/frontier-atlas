# 17. Beat a best-known pair-covering design C(v,k,2)

**Target.** Find a covering design C(v,k,2) with fewer blocks than the current best-known upper bound in the La Jolla Covering Repository, for a cell where the best-known size still exceeds the Schoenheim lower bound. A C(v,k,2) is a family of k-subsets (blocks) of a v-set covering every pair at least once; the covering number is the minimum block count.

**What counts as a win.** One explicit block list of size strictly below the tabulated best-known is a new record (one-sided: a smaller valid covering strictly improves the upper bound). Pick a specific cell (v,k) where a gap exists.

**Checker (seconds).** Read b blocks (k-subsets of {0..v-1}). Verify each block has size k, every one of the C(v,2) pairs is covered at least once (v x v boolean matrix), and b < best-known. O(b*C(k,2) + v^2).

**Search plan.** Greedy + randomized restarts; simulated annealing / tabu removing redundant blocks; Lovasz-style LP-guided block selection; group-divisible and resolvable constructions; prescribed-automorphism (cyclic) base-block search reducing the block count to orbit representatives.

**Prior art (verify).** Best-known coverings and Schoenheim bounds are tabulated in the La Jolla Covering Repository (D. Gordon, ljcr.dmgordon.org/cover.html). A cell with upper > lower is open. Re-verify the target cell's current best before claiming an improvement (the repository updates continuously).

**Openness:** documented-open. **Win-type:** found-object.
