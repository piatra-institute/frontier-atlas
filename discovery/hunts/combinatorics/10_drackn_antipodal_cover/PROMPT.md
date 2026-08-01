# 10. Distance-regular antipodal cover of a complete graph (open parameters)

**Target.** Construct a distance-regular antipodal r-fold cover of a complete graph K_n (a "DRACKN"), i.e. a distance-regular graph of diameter 3 with intersection array {n-1, (r-1)c, 1; 1, c, n-1}, for a parameter triple (n, r, c) currently listed as feasible but with no known graph. Pick a specific open triple from the tables and confirm it is unresolved.

**What counts as a win.** One graph realizing the array settles that (n,r,c) (one-sided YES). These objects are equivalent to certain resolvable designs / equiangular-line systems, so a hit has downstream value.

**Checker (seconds).** Read adjacency A. Verify: r*n vertices; regular of degree n-1; the "antipodal" relation (distance 3) partitions vertices into n classes of size r; intersection numbers match {n-1, (r-1)c, 1; 1, c, n-1} from several base vertices via distance-partition counts. O(v^2).

**Search plan.** Voltage-graph / regular-cover constructions over small groups on top of K_n; prescribed-automorphism SAT/ILP on the cover; generalized-Hadamard-matrix and mixed-difference constructions (covers of K_n correspond to certain generalized Hadamard / difference matrices).

**Prior art (verify).** Feasibility and known cases are catalogued in A.E. Brouwer's DRG tables (aeb.win.tue.nl/drg/) and the van Dam-Koolen-Tanaka survey DS22; antipodal covers of complete graphs are surveyed by Godsil-Hensel and later authors. Re-verify the chosen triple is open.

**Openness:** verify. **Win-type:** existence.
