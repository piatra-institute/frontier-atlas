# 25. Improve N(n): more MOLS at an under-tested order

**Target.** For a specific order n where the Handbook MOLS table lists a best-known lower bound N(n) = s that is below the upper bound, construct s+1 mutually orthogonal Latin squares of order n. Good under-tested candidates are composite non-prime-power orders (e.g. n = 15, 18, 20, 21, 22, 26, ...) where the tabulated lower bound comes from old product constructions.

**What counts as a win.** One explicit set of s+1 pairwise-orthogonal Latin squares of order n raises the lower bound N(n) >= s+1 (one-sided). Even one extra square beyond the tabulated value is a genuine improvement.

**Checker (seconds).** Read s+1 arrays, each n x n over {0..n-1}. Verify each is Latin (every symbol once per row and per column), and every pair is orthogonal: superimposing squares A,B yields all n^2 ordered pairs (i.e. |{(A[x],B[x])}| = n^2). O((s+1)^2 * n^2), milliseconds.

**Search plan.** Transversal-design / difference-matrix constructions over abelian groups; extend a known set by searching for a common orthogonal mate via exact-cover / SAT on the mate's cells; simulated annealing on one new square constrained orthogonal to all fixed squares; prescribed-automorphism (cyclic) search.

**Prior art (verify).** Best-known N(n) lower bounds are tabulated in Colbourn and Dinitz (eds.), "Handbook of Combinatorial Designs," 2nd ed. (MOLS table). Re-verify the current best N(n) for the chosen n before claiming an improvement.

**Openness:** documented-open. **Win-type:** found-object.
