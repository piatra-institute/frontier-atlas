# 43. A counterexample to a greedy shortest-superstring ratio

**Find.** A finite set of strings S (over a small alphabet) that refutes a stated performance bound of the GREEDY shortest-common-superstring heuristic, i.e. an instance where GREEDY's output length divided by the optimal superstring length exceeds a target ratio r. The Greedy Conjecture asserts GREEDY is 2-approximate; it is open. Sub-conjectures and stronger claimed ratios (e.g. for specific tie-breaking rules, or claimed bounds below 2 on structured inputs) are refutable by an explicit instance.

**What counts as a win.** One explicit multiset S plus (a) GREEDY's output under the stated tie-break rule and (b) a shorter valid superstring, with greedy_len / opt_len > r (ratio > 2 for the main conjecture would be a landmark refutation). One-sided: an instance violating the claimed ratio refutes it.

**Checker (seconds).** Simulate GREEDY (repeatedly merge the pair with maximum overlap per the fixed rule) to get its superstring length; verify the exhibited shorter superstring actually contains every string of S as a substring and measure its length; compute the ratio and assert it exceeds r. For a *true* optimum (needed only for exact-ratio claims) run exact shortest-superstring by held-Karp/ILP on small S. Exact.

**Search plan.** Structured: small-instance exhaustive/SAT search over string sets with bounded length and alphabet, maximizing greedy/opt; evolutionary search seeded by known hard families (e.g. the c(ab)^k patterns from lower-bound constructions).

**Prior art (verify).** Blum, Jiang, Li, Tromp, Yannakakis (superstring approximation, 1994); the Greedy Conjecture (Tarhio-Ukkonen / Turner), still open; recent bounds (e.g. Kaplan-Shafrir, Englert et al.). Verify the exact ratio claim being targeted.
