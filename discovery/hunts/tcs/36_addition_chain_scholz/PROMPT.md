# 36. A short addition chain at an open Scholz-Brauer value

**Find.** An addition chain for a specific integer whose shortest-chain length l(n) is not known, that is shorter than the best published chain, or a chain settling a Scholz-Brauer equality case. An addition chain for n is 1 = a_0 < a_1 < ... < a_r = n with each a_k = a_i + a_j (i, j < k). Values such as l(2^n - 1) and specific large n where l(n) is uncertain are tracked; the Scholz-Brauer inequality l(2^n - 1) <= n - 1 + l(n) is open in general.

**What counts as a win.** One explicit chain for the target integer of length shorter than the recorded best (an upper-bound improvement), or a chain demonstrating l(2^n - 1) = n - 1 + l(n) at a value where this was not previously exhibited. One-sided: a shorter chain beats the record.

**Checker (seconds).** Verify the chain: each element is a sum of two earlier ones, the sequence is increasing, and it ends at the target; report its length. O(r^2) membership checks, microseconds. (A shortest-length *claim* additionally needs an exhaustive/branch-and-bound minimality search.)

**Search plan.** Structured: branch-and-bound / iterative deepening over addition chains with the standard bounds (Knuth, Thurber pruning); meet-in-the-middle for the tail; reuse chains for factors and for 2^n - 1 via the Brauer/Hansen constructions, then locally shorten.

**Prior art (verify).** Knuth TAOCP vol. 2 (addition chains); OEIS A003313 (l(n)) and A003064 (Scholz-Brauer); Thurber, Clift computations; Scholz-Brauer conjecture open. Verify the target value's current best/known status.
