# 05. Strongly regular graph srg(111,30,5,9)

**Target.** Construct a strongly regular graph with parameters (111, 30, 5, 9), or prove none exists. Existence is currently unknown.

**What counts as a win.** One 111-vertex adjacency matrix with these parameters proves existence (one-sided). Feasible eigenvalues 3 (mult. 74) and -6 (mult. 36); complement srg(111,80,55,60).

**Checker (seconds).** Read the 111x111 symmetric 0/1 A. Verify diag = 0, row sums = 30, and A*A = 30*I + 5*A + 9*(J - I - A). O(v^3), milliseconds.

**Search plan.** 111 = 3 * 37; prescribe a Z_111 or Z_37-acting automorphism and reduce to an orbit-incidence system for SAT/ILP; Cayley / partial-difference-set search over Z_111 using cyclotomic classes mod 37; substructure from geometries on 111 points (note 111 = number of points of PG(2,10)-sized objects, screen geometric constructions); annealing on adjacency.

**Prior art (verify).** Existence "?" in A.E. Brouwer's SRG table (aeb.win.tue.nl/graphs/srg/). Re-verify the row is still open.

**Openness:** documented-open. **Win-type:** existence.
