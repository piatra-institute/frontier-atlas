# 21. A rotation-symmetric or homogeneous bent function at an open parameter

**Find.** A bent function f: F_2^n -> F_2 (n even) inside a structurally-constrained class where existence is open: for example a rotation-symmetric bent function in a dimension n where none is catalogued, or a homogeneous bent function of degree 3 for an n where the existence question is unresolved. Bent functions (maximum nonlinearity 2^{n-1} - 2^{n/2 - 1}) are fully understood generically, but existence within these symmetry/homogeneity classes has documented gaps.

**What counts as a win.** One explicit truth table (or ANF) meeting the class constraint (rotation symmetry, or homogeneity of the stated degree) that is bent. One-sided: a single witness settles the class-existence question for that n.

**Checker (seconds).** Compute the Walsh-Hadamard transform; assert |W_f(a)| = 2^{n/2} for every a (the bent criterion). Separately verify the structural constraint: rotation-symmetry by checking f is constant on cyclic-shift orbits, or homogeneity by checking the ANF has monomials of exactly the stated degree. Exact integer, fast transform.

**Search plan.** Structured: search over orbit-representative truth tables (rotation-symmetric functions are determined by one bit per necklace, shrinking the space dramatically); algebraic constructions (Maiorana-McFarland restricted to symmetric layouts, cubic homogeneous forms). SAT on the reduced orbit variables plus bent constraints.

**Prior art (verify).** Rothaus (1976, bent functions); Stanica-Maitra on rotation-symmetric bent functions; Charnes/Rotteler/Beth and Qu-Seberry-Pieprzyk on homogeneous bent functions of degree 3. Verify which n remain open for the chosen class.
