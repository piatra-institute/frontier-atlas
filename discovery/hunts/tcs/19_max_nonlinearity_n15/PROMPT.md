# 19. A Boolean function beating the best known nonlinearity in an odd dimension

**Find.** A Boolean function f: F_2^n -> F_2 in an odd dimension (n = 15, or n = 13) whose nonlinearity exceeds the current record. Equivalently, a codeword improving the covering radius bound of the first-order Reed-Muller code RM(1,n). Patterson-Wiedemann (1983) broke the "bent-concatenation" barrier 2^{n-1} - 2^{(n-1)/2} for n=15; the exact maximum nonlinearity for n=15 and other odd n is still unknown, so any improvement is a genuine advance.

**What counts as a win.** One explicit truth table (2^n bits) whose nonlinearity is strictly greater than the best published value for that n. One-sided: a single better function wins; no matching upper bound is required.

**Checker (seconds).** Compute the Walsh-Hadamard transform of (-1)^{f} via the fast transform (n=15: 32768-point, microseconds). Nonlinearity = 2^{n-1} - (1/2) max|W_f|. Assert it exceeds the recorded best. Exact integer arithmetic.

**Search plan.** Structured: exploit idempotent / rotation-symmetric / bent-concatenation-plus-perturbation constructions (the Patterson-Wiedemann and Kavut-Yucel orbit approaches); steepest-descent / simulated annealing on the truth table maximizing nonlinearity; algebraic constructions over subfield decompositions.

**Prior art (verify).** Patterson & Wiedemann (1983); Kavut, Maitra, Yucel on 9-variable and 15-variable records; covering radius of RM(1,n) surveys (verify current best nonlinearity for the chosen n). Exact maxima open for odd n >= 9 in several cases.
