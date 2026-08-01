# Empty lattice simplex with larger width than known

**Find.** An empty lattice simplex in dimension d (a simplex with integer vertices whose only lattice points are its d+1 vertices) whose lattice width exceeds the largest published width for empty simplices in that dimension, for a small d where the maximum width is open.

**What counts as a win (one-sided).** One empty lattice d-simplex with lattice width above the current record. A single wider empty simplex beats the record; failure proves nothing.

**Checker (seconds).** Emptiness: verify the simplex contains no lattice points other than its vertices (Ehrhart / enumerate the fundamental parallelepiped, or a direct bounded lattice-point scan). Width: minimize over nonzero integer functionals w of (max - min) of w over the vertices (a finite reduced search). Exact integer arithmetic.

**Search plan.** Parameterize simplices by their Hermite normal form / a determinant and residue vector; enumerate small-determinant empty simplices and compute widths; local search on the defining lattice to raise width while preserving emptiness. Focus on d = 4, 5 where the maximum width is not settled.

**Prior art (verify).** The maximum lattice width of empty (hollow) lattice simplices is known in dimension 3 but open in higher dimensions, with only bounds and record examples. See Haase-Ziegler on empty simplices and subsequent work on hollow lattice simplices (Averkov, Nill, and others). Confirm the record width for the target d (verify).
