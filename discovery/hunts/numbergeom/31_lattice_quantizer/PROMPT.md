# Lattice quantizer beating the best known second moment

**Find.** A lattice in a small dimension d (e.g. 9-15) whose normalized second moment (dimensionless quantizer constant G) is strictly below the best published value for that dimension.

**What counts as a win (one-sided).** One lattice (exact Gram matrix) with normalized second moment below the current record. A single better lattice improves the record; failure proves nothing.

**Checker (seconds).** Compute the Voronoi cell of the lattice, integrate the second moment over it exactly (the cell is a rational polytope; use exact volume-weighted moment integration or a certified Delaunay decomposition), normalize by dimension and determinant. Compare to the record. Exact / certified arithmetic on the finalist.

**Search plan.** Gradient descent over quadratic forms minimizing the second moment (the standard quantizer optimization), using the Voronoi-relevant vectors; seed from the best known quantizers (dual laminated lattices and their relatives); local perturbation within the secondary cone. Certify the final second moment exactly.

**Prior art (verify).** Optimal lattice quantizers are proven only in dimensions 1, 2, 3; higher dimensions have best-known lattices with recently improved second moments. See Conway-Sloane, SPLAG, quantizer tables, and recent optimization work (Agrell and collaborators). Confirm the current record for the target dimension (verify).
