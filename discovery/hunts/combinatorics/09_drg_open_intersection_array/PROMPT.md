# 09. Distance-regular graph for an open feasible intersection array

**Target.** Construct a distance-regular graph (DRG) realizing one intersection array that is currently listed as feasible (passes all known integrality, Krein, and absolute-bound conditions) but for which no graph is known and no nonexistence proof exists. Pick a specific open array from the table (below) and confirm it is still unresolved.

**What counts as a win.** A single graph whose distance partition matches the chosen array settles that array's existence (one-sided YES). Choose a small-diameter array so the graph fits on a workstation.

**Checker (seconds).** Read adjacency A (graph6). Compute, for a base vertex, the distance-i neighborhoods; verify for every vertex and every i that b_i (neighbors at distance i+1 from a distance-i vertex) and c_i (neighbors at distance i-1) are constant and equal the array. Confirm a_i = k - b_i - c_i. O(v^2 * diam). Re-check from several base vertices.

**Search plan.** Prescribed-automorphism orbit search (SAT/ILP), Cayley graphs over small groups screened by girth and diameter, antipodal/bipartite covers and lifts of known small DRGs, coset geometries.

**Prior art (verify).** Open feasible arrays are tabulated in A.E. Brouwer's distance-regular graph tables (aeb.win.tue.nl/drg/) and E. van Dam, J. Koolen, H. Tanaka, "Distance-regular graphs," Electronic Journal of Combinatorics, dynamic survey DS22. Re-verify the chosen array is still open.

**Openness:** verify. **Win-type:** existence.
