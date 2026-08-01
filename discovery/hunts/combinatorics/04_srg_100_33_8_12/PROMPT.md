# 04. Strongly regular graph srg(100,33,8,12)

**Target.** Construct a strongly regular graph with parameters (100, 33, 8, 12), or prove none exists. Existence is currently unknown. (Note: srg(100,22,0,6), the Higman-Sims graph, exists; this is a different, open row on 100 vertices.)

**What counts as a win.** A single 100-vertex adjacency matrix meeting the parameters proves existence (one-sided). Feasible eigenvalues 3 and -7; complement srg(100,66,44,42).

**Checker (seconds).** Read the 100x100 symmetric 0/1 A. Verify diag = 0, all row sums = 33, and A*A = 33*I + 8*A + 12*(J - I - A). Milliseconds.

**Search plan.** Orbit-restricted SAT/ILP under a prescribed automorphism (Z_100, Z_10 x Z_10, or a group with orbits of manageable size); Cayley / partial-difference-set search over abelian groups of order 100; combinatorial constructions from resolvable designs or Latin-square graphs on 100 points; local search with the SRG matrix identity as objective.

**Prior art (verify).** Marked "?" for existence in A.E. Brouwer's SRG table (aeb.win.tue.nl/graphs/srg/). Confirm still open; several 100-vertex rows are settled, this one is not.

**Openness:** documented-open. **Win-type:** existence.
