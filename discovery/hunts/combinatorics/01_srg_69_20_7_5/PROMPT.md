# 01. Strongly regular graph srg(69,20,7,5)

**Target.** Construct a strongly regular graph with parameters (v,k,lambda,mu) = (69, 20, 7, 5), or prove none exists. Existence is currently unknown.

**What counts as a win.** One adjacency matrix on 69 vertices that is strongly regular with these parameters settles existence outright (one-sided: a single valid graph is a full YES). Feasible eigenvalues are 5 (mult. 23) and -3 (mult. 45); the complement is srg(69,48,32,36).

**Checker (seconds).** Read the 69x69 symmetric 0/1 matrix A. Verify diag(A)=0, every row sum = 20, and A*A = 20*I + 7*A + 5*(J - I - A). That single matrix identity certifies strong regularity. O(v^3), milliseconds.

**Search plan.** Prescribe an automorphism group (cyclic Z_69, or a group of order dividing 69 or with small index) and solve the resulting orbit-incidence system with SAT (kissat/CaDiCaL) or ILP; Cayley/partial-difference-set constructions over Z_69 = Z_3 x Z_23; local-search / tabu on adjacency with the SRG identity as the objective.

**Prior art (verify).** Listed with existence status "?" in A.E. Brouwer, "Parameters of strongly regular graphs" (online table, aeb.win.tue.nl/graphs/srg/). Re-verify the row is still open before committing compute; SRG tables update.

**Openness:** documented-open. **Win-type:** existence.
