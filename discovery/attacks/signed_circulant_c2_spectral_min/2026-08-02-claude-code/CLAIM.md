# Claim

**Claim.** No new mathematical result. B1 (independent verification + finite-range
extension). Conjecture 3 of arXiv:2607.18334 (Suvagiya, posted 2026-07-19) states that for
the 4-regular circulant `C_n(1,2)` the minimum spectral radius over all edge-signings equals
`rho_-(n) = 2*sqrt(cos(pi/n)^2 + cos(2*pi/n)^2)` for every even `n >= 8`; the source reports
exhaustive verification through `n=18`. This run (a) independently re-derived the `n=8..18`
verification with a from-scratch enumerator (different bit indexing and batched spectral
computation than the scout checker), matching `rho_-(n)` to `<= 1e-15`; and (b) extended the
exhaustive check to `n=20`, `n=22`, and `n=24`, where the conjecture continues to hold with
min spectral radius equal to `rho_-(n)` to `<= 2e-15` and no counterexample. The conjecture
(all even `n`) remains **OPEN**: this extends the verified finite range from 18 to 24, it does
not prove or refute the statement.

**Checker.** `verify_extend.py`. For each of the `2^(n+1)` switching classes (spanning-tree
gauge fixes the `n-1` step-1 path edges `+1`; the wrap edge and the `n` step-2 edges carry the
free signs), build the signed adjacency matrix, compute all eigenvalues
(`numpy.linalg.eigvalsh`, batched), take `max|lambda|`, and compare the global minimum to
`rho_-(n)`. Any class with spectral radius below `rho_-(n) - 1e-9` is flagged as a
counterexample; none was found. This checker is independent of the scout's
`check_signed_circulant.py` (separate file, reversed bit indexing, batched build) and is
cross-validated against it on the full `n=8..18` overlap.

**Trust base.** Double precision. Two independent implementations agree to `~1e-15` on the
entire `n=8..18` overlap, and each reproduces the source closed form. Enumeration is exhaustive
over switching classes (complete, not sampled). The count `2^(n+1)` is the correct gauge-fixed
number of switching classes (`2n` edges, `n-1` fixed by a spanning tree). Residual risk:
floating-point spectral radius. A counterexample with gap `< ~1e-9` would require an exact
re-check; none appeared, and every confirmation sits at machine-precision equality (gap
`~1e-15`, far above the flag tolerance in the safe direction).

**Encoding fidelity.** Statement, graph `C_n(1,2)`, signing model, objective (spectral radius
of the signed adjacency matrix), and closed form `rho_-(n)` are taken directly from the source
Conjecture 3. The switching-class reduction is exact: switching (vertex sign flips) preserves
the signed-adjacency spectrum, so minimizing over classes equals minimizing over all signings.

**Review level.** self + agent. ChatGPT Pro scouted the target and supplied a baseline checker;
Claude Code re-implemented independently, cross-checked on the overlap, and extended the range.
Not human-refereed. Not yet sent to the author.

**Provenance.** Scout: ChatGPT Pro (GPT-5.6 Pro), 2026-08-02. Verification and extension: Claude
Code (Opus), 2026-08-02. Source: arXiv:2607.18334v1, Conjecture 3.

**Cost and attempts.** One deterministic exhaustive pass per order, no search or tuning:
`n=20` (2,097,152 classes, 18.8 s), `n=22` (8,388,608, 87.1 s), `n=24` (33,554,432, 416.5 s)
on a single workstation core with batched eigensolves. Outcome: the conjecture holds at every
order checked; no counterexample; the open all-`n` problem is not resolved. Realistic brute-force
ceiling on this host is around `n=26-28`; settling the all-`n` statement needs a proof
(transfer-matrix / bandwidth-2 recurrence), not enumeration. Each confirmed order lowers the
prior on a counterexample at reachable size.
