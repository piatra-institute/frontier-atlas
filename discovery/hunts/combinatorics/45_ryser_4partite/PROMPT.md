# 45. Counterexample to Ryser's Conjecture for r = 4 or 5

**Target.** Find an r-partite r-uniform hypergraph H (r = 4 or r = 5) with cover number tau(H) > (r-1) * nu(H), where nu is the maximum matching and tau the minimum vertex cover. Ryser's Conjecture asserts tau <= (r-1) * nu for every r-partite r-uniform hypergraph. It is a theorem for r <= 3 (r = 3 is Aharoni's theorem via the Aharoni-Haxell machinery); r >= 4 is open. A single hypergraph violating the bound refutes it for that r.

**What counts as a win.** One explicit r-partite r-uniform hypergraph with tau > (r-1) * nu refutes Ryser for that r (one-sided NO). Both parameters are exactly computable for a small hypergraph.

**Checker (seconds).** Read H: the r parts and the list of edges (each edge one vertex per part). Compute nu (maximum matching) and tau (minimum vertex cover) exactly by ILP or exhaustive search; keep the number of edges/vertices small enough that both integer programs solve in seconds. Assert tau > (r-1) * nu.

**Search plan.** Look for tightness-breaking constructions near the known extremal families that meet tau = (r-1) * nu (truncated projective planes give the conjectured extremal ratio); local search / ILP-in-the-loop that adds edges to push tau up while holding nu fixed; algebraic (affine/projective-plane-based) hypergraphs for small prime-power orders; SAT over an edge-presence model encoding "tau >= k and nu <= m".

**Prior art (verify).** Ryser's Conjecture is open for r >= 4 (surveys and the Aharoni-Berger-Ziv line of work). Extremal examples meeting equality exist for r a prime power plus one (truncated projective planes); no violation is known. Re-verify status before starting.

**Openness:** documented-open. **Win-type:** counterexample.
