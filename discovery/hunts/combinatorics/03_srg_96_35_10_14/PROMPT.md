# 03. Strongly regular graph srg(96,35,10,14)

**Target.** Construct a strongly regular graph with parameters (96, 35, 10, 14), or prove none exists. Existence is currently unknown.

**What counts as a win.** One adjacency matrix on 96 vertices with these parameters is a full existence proof (one-sided). Feasible eigenvalues 3 and -7; complement srg(96,60,38,36).

**Checker (seconds).** Read the 96x96 symmetric 0/1 A. Verify diag = 0, row sums = 35, and A*A = 35*I + 10*A + 14*(J - I - A). O(v^3), milliseconds.

**Search plan.** Prescribed-automorphism orbit search (groups of order dividing 96 = 2^5 * 3, e.g. Z_96, Z_48 x Z_2, or an elementary-abelian action) with the resulting linear/incidence constraints handed to SAT or ILP; Cayley / partial-difference-set search over abelian groups of order 96; gluing / substructure amalgamation from known srg(35,...) or srg(96,...)-adjacent graphs; simulated annealing on adjacency with the SRG identity residual as energy.

**Prior art (verify).** Existence "?" in A.E. Brouwer's SRG table (aeb.win.tue.nl/graphs/srg/). Re-verify openness against the current table.

**Openness:** documented-open. **Win-type:** existence.
