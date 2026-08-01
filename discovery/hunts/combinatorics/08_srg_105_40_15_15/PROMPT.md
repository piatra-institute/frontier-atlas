# 08. Strongly regular graph srg(105,40,15,15)

**Target.** Construct a strongly regular graph with parameters (105, 40, 15, 15), or prove none exists. Existence is currently unknown. Here lambda = mu = 15, so the graph is a (105,40;15,15) "pseudo-geometric" type.

**What counts as a win.** One 105-vertex adjacency matrix with these parameters proves existence (one-sided). Feasible eigenvalues 5 (mult. 48) and -5 (mult. 56); complement srg(105,64,38,40).

**Checker (seconds).** Read the 105x105 symmetric 0/1 A. Verify diag = 0, all row sums = 40, and A*A = 40*I + 15*A + 15*(J - I - A). Note lambda = mu collapses the last term to 15*(J - I). Milliseconds.

**Search plan.** 105 = 3 * 5 * 7; prescribe an automorphism with orbits over Z_105 or a subgroup and reduce to an orbit-incidence SAT/ILP system; regular-two-graph and descendant constructions (lambda = mu graphs relate to regular two-graphs); Cayley / partial-difference-set search; local search on adjacency with the SRG identity residual.

**Prior art (verify).** Existence "?" in A.E. Brouwer's SRG table (aeb.win.tue.nl/graphs/srg/). Re-verify openness.

**Openness:** documented-open. **Win-type:** existence.
