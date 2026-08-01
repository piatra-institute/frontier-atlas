# 26. Atomic Latin square at an open composite order

**Target.** Construct an atomic Latin square of a composite order n for which none is currently known. A Latin square is atomic if it is pan-Hamiltonian in a strong sense: every one of its 2 x n and n x 2 (and conjugate) cycle structures is a single n-cycle, equivalently it has no proper Latin subrectangle in any conjugate. Atomic squares are known for prime orders (from the cyclic group) and some composite orders; several small composite orders are open.

**What counts as a win.** One explicit atomic Latin square at an open order n settles that order (one-sided YES).

**Checker (seconds).** Read the n x n array over {0..n-1}. Verify Latin. Then verify atomicity: for every ordered pair of rows (r,s), the permutation mapping symbol positions of row r to row s is a single n-cycle; repeat for the row/column/symbol conjugates. Equivalently check every pair of rows, of columns, and of symbol-layers gives one n-cycle. O(n^3).

**Search plan.** Cyclotomic and group-based constructions; search over Latin squares with a prescribed cyclic autotopism; hill-climbing / tabu that penalizes any short cycle between row pairs; build from perfect 1-factorizations (atomic squares connect to pan-Hamiltonian structures).

**Prior art (verify).** Atomic Latin squares are introduced and tabulated by I.M. Wanless, "Atomic Latin squares based on cyclotomic orthomorphisms," Electronic Journal of Combinatorics (mid-2000s). Re-verify which composite orders remain open before starting.

**Openness:** verify. **Win-type:** existence.
