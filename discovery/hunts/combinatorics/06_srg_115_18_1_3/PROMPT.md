# 06. Strongly regular graph srg(115,18,1,3)

**Target.** Construct a strongly regular graph with parameters (115, 18, 1, 3), or prove none exists. Existence is currently unknown. This is a sparse, girth-constrained case: lambda = 1 forces every edge into exactly one triangle, mu = 3 is small.

**What counts as a win.** A single 115-vertex adjacency matrix with these parameters proves existence (one-sided). Feasible eigenvalues 3 (mult. 69) and -5 (mult. 45).

**Checker (seconds).** Read the 115x115 symmetric 0/1 A. Verify diag = 0, all row sums = 18, and A*A = 18*I + 1*A + 3*(J - I - A). Milliseconds.

**Search plan.** The small lambda,mu make orbit search attractive: prescribe Z_115 = Z_5 x Z_23 or Z_23 automorphism, build the difference-pattern constraints (each nonzero group element appears with a fixed neighbor-count profile), solve by SAT/ILP; Cayley / partial-difference-set search over Z_115; orderly / canonical-augmentation growth exploiting lambda = 1 local structure to prune hard.

**Prior art (verify).** Existence "?" in A.E. Brouwer's SRG table (aeb.win.tue.nl/graphs/srg/). Re-verify openness; sparse SRG rows are attractive but persistently open.

**Openness:** documented-open. **Win-type:** existence.
