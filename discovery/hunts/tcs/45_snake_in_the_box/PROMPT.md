# 45. A longer snake or coil in the hypercube

**Find.** An induced (chordless) path (a "snake") or induced cycle (a "coil") in the n-dimensional hypercube graph Q_n that is longer than the best known for a specific open dimension (records are open from roughly n = 9 upward, and for many variants: coils, symmetric coils, higher "spread" k). The snake-in-the-box problem asks for the longest such path/cycle; exact maxima are unknown beyond small n, and lower bounds are improved by construction.

**What counts as a win.** One explicit vertex sequence in {0,1}^n that is a valid snake (or coil) longer than the recorded best for that n and variant. One-sided: a longer valid snake is a new lower-bound record; the exact maximum need not be proven.

**Checker (seconds).** Verify: consecutive vertices differ in exactly one bit (a hypercube edge); all vertices are distinct; and the induced-subgraph condition holds, i.e. no two non-consecutive vertices of the path are at Hamming distance 1 (for a coil, also the wrap-around pair must be adjacent and no other cross-adjacencies). O(length^2) Hamming checks, fast. Exact.

**Search plan.** Structured/evolutionary: the state of the art uses genetic algorithms, stochastic beam / Monte-Carlo tree search, and constraint solvers over the transition-sequence ("coil" encodings); seed from known long snakes and extend via backtracking with strong induced-path pruning; exploit symmetry (canonical transition sequences).

**Prior art (verify).** Kautz (1958); Singleton; the snake-in-the-box records tracked by Kinny, Wynn, Allison, Palombo and others (verify the current best length for the target n and variant). Exact maxima open for n >= 9 (verify).
