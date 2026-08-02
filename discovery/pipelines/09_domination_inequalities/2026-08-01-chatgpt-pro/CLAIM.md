# Claim

**Claim.** No refutation of a currently-open domination conjecture. No new result.
Details:
1. **Open conjectures survived.** Product domination `gamma_t(G box H) >= gamma(G tensor H)` held across 10,255 exact factor pairs (factors to order 6, 0 violations, 766 equalities); independently corroborated here on 7 small pairs (all satisfy, 6 tight). Regular `i(G) <= mu*(G)` held on all reachable graphs (54 regular through n=9; 5,000 constructed order-60 cubics, best i=17 < mu*=18). A public post claims an order-60 girth-5 cubic counterexample to `i <= mu*` but exposed no graph, so it is unverified, neither confirmed nor refuted.
2. **Status audit (the useful part).** The "4 open" TxGraffiti conjectures from the 2025 paper are mostly already resolved: annihilation-residue proved, saturation-harmonic false (friendship graph F4), zero-forcing refuted (July 2026). The engine re-verified these rather than wasting the run.
3. **The two graph6 "counterexamples" are NOT open-problem results.** `3*gamma <= n+Delta` (witness `G?\`DE_`) and `2i <= 3*gamma` (witness `G??F?{`) are refutations of the model's own auto-fitted candidates, not conjectures. Verified here (my independent gamma/i match exactly: 8-vertex trees, gamma=4 and gamma=2/i=4), but explicitly not novel.

**Checker.** Independent recompute (Claude Code): exhaustive gamma and independent-domination on both witnesses (match); gamma_t of Cartesian product vs gamma of tensor product on 7 small pairs (all satisfy). The run's own two-method audit: 1,196 full-panel graphs, 0 mismatches, 0 invalid certificates. Toolchain: Python 3.12 + networkx (verification); the run used C++ bit-mask + ILP cross-check.

**Trust base.** Exact domination by ILP / cardinality-ordered exhaustive search with "no smaller feasible set" certificates; two independent methods. Witnesses self-certifying. The hardening is evidence, not proof: product tested only to factor order 6, regular only to n=9 plus a sampled order-60 subclass. Enumeration counts match A001349 through n=9.

**Review level.** self + agent. ChatGPT Pro generated; Claude Code independently verified the witnesses and the product-domination claim. Not human-refereed.

**Provenance.** ChatGPT Pro, 2026-08-01, 96m26s. Verification: Claude Code (Opus), 2026-08-02.

**Cost and attempts.** Wall-clock 96m26s. 273,193 graphs enumerated (n<=9); 59 auto-fit candidates (37 broke, all non-novel); 10,255 product pairs; 5,000 order-60 cubics. No open-problem refutation; value is a hardened open conjecture plus a status audit.
