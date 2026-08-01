# 18. Beat a best-known triple-covering design C(v,k,3)

**Target.** Find a covering design C(v,k,3) with fewer blocks than the current best-known upper bound in the La Jolla Covering Repository, for a cell where best-known exceeds the Schoenheim lower bound. A C(v,k,3) covers every 3-subset of a v-set with at least one of its k-subset blocks.

**What counts as a win.** One explicit block list of size strictly below the tabulated best-known strictly improves the upper bound (one-sided). Choose a specific (v,k) with a gap; t=3 cells are less picked-over than t=2.

**Checker (seconds).** Read b blocks (k-subsets of {0..v-1}). Verify each block size k, every one of the C(v,3) triples is covered by some block, and b < best-known. Enumerate triples per block (C(k,3) each) into a covered-set; assert |covered| = C(v,3). O(b*C(k,3) + C(v,3)).

**Search plan.** Randomized greedy with restarts; simulated annealing removing redundant blocks; inflation from smaller coverings and group-divisible designs; cyclic/prescribed-automorphism base-block search; SAT/ILP set-cover with symmetry breaking for small v.

**Prior art (verify).** Best-known C(v,k,3) coverings and lower bounds are in the La Jolla Covering Repository (ljcr.dmgordon.org). A cell with a gap is open. Re-verify the current best-known for the chosen cell before claiming.

**Openness:** documented-open. **Win-type:** found-object.
