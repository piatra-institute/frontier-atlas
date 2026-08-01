# 02. Strongly regular graph srg(88,27,6,9)

**Target.** Construct a strongly regular graph with parameters (88, 27, 6, 9), or prove none exists. Existence is currently unknown.

**What counts as a win.** A single adjacency matrix on 88 vertices meeting the parameters settles existence (one-sided YES). Feasible eigenvalues are 3 (mult. 55) and -6 (mult. 32); complement is srg(88,60,41,40).

**Checker (seconds).** Read the 88x88 symmetric 0/1 matrix A. Verify diag(A)=0, all row sums = 27, and A*A = 27*I + 6*A + 9*(J - I - A). Milliseconds.

**Search plan.** Orbit-restricted search under a prescribed automorphism (Z_88, Z_44 x Z_2, or a group leaving a nice partition invariant); Kramer-Mesner style incidence system solved by SAT/ILP; regular two-graph / descendant constructions; Cayley graphs over abelian groups of order 88 screened by the character-sum (partial difference set) condition.

**Prior art (verify).** Marked existence "?" in A.E. Brouwer's SRG parameter table (aeb.win.tue.nl/graphs/srg/). This is a long-standing open feasible parameter set; confirm it is still unresolved before starting.

**Openness:** documented-open. **Win-type:** existence.
