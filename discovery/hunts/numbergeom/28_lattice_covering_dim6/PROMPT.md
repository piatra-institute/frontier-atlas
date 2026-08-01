# Lattice covering beating the best known density in dimension 6

**Find.** A lattice in dimension 6 (or another small dimension where the optimum is unknown) whose covering density (thickness) is strictly below the best published lattice covering for that dimension.

**What counts as a win (one-sided).** One lattice (given by an exact Gram matrix) with covering density below the current record. A single better lattice improves the bound; failure proves nothing.

**Checker (seconds).** From the Gram matrix compute the covering radius exactly (the deep-hole / farthest Delaunay point, via the Delaunay decomposition or a covering-radius computation) and the determinant; form the covering density and compare to the record. Exact / certified arithmetic; independent recomputation of the covering radius.

**Search plan.** Local optimization over positive-definite quadratic forms minimizing the covering density (the Delone / secondary-cone framework of Schuermann-Vallentin); gradient / subgradient descent within a Delone cone; perturb the best known lattices (A_6^*, laminated, and their relatives). Certify the final covering radius exactly.

**Prior art (verify).** Least dense lattice coverings are proven optimal only through dimension 5 (Ryshkov-Baranovskii and the Schuermann-Vallentin computations); dimension 6 and up have only best-known lattices that may be beatable. See Schuermann and Vallentin on computational lattice covering, and Conway-Sloane, SPLAG. Confirm the current record for the target dimension (verify).
