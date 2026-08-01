# Lattice packing beating the best known density in a fixed dimension

**Find.** A lattice in a dimension d between roughly 10 and 15 whose packing density exceeds the best published lattice packing for that dimension (where the densest lattice is not proven optimal).

**What counts as a win (one-sided).** One lattice (exact Gram matrix) with packing density above the current record. A single denser lattice improves the bound; failure proves nothing. (Flag: these tables are moderately hardened; treat as a long shot.)

**Checker (seconds).** From the Gram matrix compute the minimal squared norm exactly (short-vector enumeration, e.g. Fincke-Pohst) and the determinant; form the center density and compare to the record. Exact arithmetic; independent re-run of the shortest-vector computation.

**Search plan.** Local optimization over quadratic forms maximizing density within a fixed lattice-type / perfect-form domain (Voronoi's algorithm neighborhood); perturb the record lattices (laminated K_d, and the best-known non-lattice-derived forms); gluing / cross-section constructions from good higher-dimensional lattices. Certify minimal norm exactly on finalists.

**Prior art (verify).** Densest lattice packings are proven optimal only through dimension 8 (and 24 for lattices via recent work), so dimensions 9-15 hold best-known lattices that are not proven optimal. See Conway-Sloane, SPLAG, and the online catalogue of lattices (Nebe-Sloane). Confirm the record for the target dimension before starting (verify).
