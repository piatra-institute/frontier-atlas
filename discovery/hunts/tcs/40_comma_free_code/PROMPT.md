# 40. A comma-free code beating the best known size

**Find.** A comma-free code over a q-letter alphabet with block length k containing more codewords than the best known example, at a specific (q, k) where the maximum size is open. A code C of length-k words is comma-free if no proper "overlap" of two codewords is itself a codeword: for all u, v, w in C, no cyclic concatenation window uv (positions 2..k, k+1..2k-1) equals a codeword. The maximum comma-free code size W_q(k) is known only for small cases; general k is open.

**What counts as a win.** One explicit set C of length-k words over {0..q-1} that is comma-free and has size exceeding the recorded best for that (q, k). One-sided: a larger comma-free code is a new lower-bound record; the exact maximum need not be proven.

**Checker (seconds).** For every ordered pair (u, v) in C and every offset d = 1..k-1, assert the length-k window straddling the junction of uv is not in C; also assert no codeword is a cyclic rotation of another. O(|C|^2 * k), fast.

**Search plan.** Structured: extend Eastman's odd-k construction (optimal for prime k) into open k; model maximum comma-free code as a maximum independent set in the overlap-conflict graph, run exact/heuristic MIS; SAT/CP with the comma-free constraints.

**Prior art (verify).** Golomb, Gordon, Welch (comma-free codes, 1958); Eastman (1965, optimal for odd word length); the Golomb-Gordon-Welch bound and W_q(k) tables (verify open (q, k) cells). Maximum size open for general even k.
