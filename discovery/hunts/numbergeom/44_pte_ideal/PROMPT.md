# Ideal Prouhet-Tarry-Escott solution at an open size

**Find.** An ideal Prouhet-Tarry-Escott (PTE) solution of size n at a value of n where none is known: two distinct multisets of integers {a_1, ..., a_n} and {b_1, ..., b_n} with equal power sums for every exponent k = 1, 2, ..., n-1 (and unequal at k = n).

**What counts as a win (one-sided).** One pair of integer multisets with matching power sums through exponent n-1. A single ideal solution settles that size; failure proves nothing.

**Checker (seconds).** For k = 1..n-1 assert sum a_i^k = sum b_i^k, and assert sum a_i^n != sum b_i^n and the multisets differ. Exact big-integer arithmetic; constant work per exponent.

**Search plan.** Equivalent to finding a polynomial identity prod(x - a_i) - prod(x - b_i) = constant; search via the symmetric-function constraints (equal elementary symmetric functions e_1..e_{n-1}) as a Diophantine system; use lattice reduction (LLL) on the power-sum conditions, and known parametric families as seeds; algebraic-geometry search for rational points on the associated variety. Evolutionary search over integer tuples scored by the number of matched power sums.

**Prior art (verify).** Ideal PTE solutions are known for many sizes but the smallest sizes with no known ideal solution remain open (historically the frontier has sat around sizes 12 and above). See Peter Borwein, "Computational Excursions in Analysis and Number Theory," the PTE chapter, and the ideal-PTE tables (Borwein-Lisonek-Percival; Shuwen's PTE pages). Confirm the smallest open size before starting (verify).
