# 13. Perfect 1-factorization of K_{2n} at the smallest open order

**Target.** Construct a perfect 1-factorization (P1F) of the complete graph K_{2n} for the smallest order 2n at which existence is open. A P1F partitions the edges of K_{2n} into 2n-1 perfect matchings such that the union of every pair of matchings is a single Hamilton cycle. It is conjectured every K_{2n} has one; the known constructions cover 2n = p+1 and 2n = 2p (p prime).

**What counts as a win.** One explicit P1F at an open order 2n settles that order (one-sided YES).

**Checker (seconds).** Read 2n-1 perfect matchings on vertices {0..2n-1}. Verify each is a perfect matching, the matchings partition all C(2n,2) edges, and for every pair of matchings the union graph (2-regular) is one Hamilton cycle (single connected component of length 2n). O(n^3), milliseconds.

**Search plan.** Starter-adder and rotational (Z_{2n-1}) constructions; prescribed-automorphism SAT/ILP; hill-climbing that swaps edges between matchings to break short cycles in pairwise unions.

**Prior art (verify).** Existence is open for infinitely many orders; consult the perfect-1-factorization entry in Colbourn and Dinitz (eds.), "Handbook of Combinatorial Designs," 2nd ed., and Wanless's surveys for the current smallest undecided 2n. Re-verify the target order is still open (small orders have been settled by computer over time).

**Openness:** verify. **Win-type:** existence.
