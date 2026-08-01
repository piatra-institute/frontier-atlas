# Batch sweep: refute domination-family inequalities

**Mode:** one ChatGPT Pro session, code sandbox, batch throughput.
**Goal:** an explicit graph violating a stated domination bound, or hardened survivors. Refutation is the clean win.

**Family + panel.** Connected graphs; domination variants: domination γ, total domination γ_t, independent domination i, connected domination γ_c, Roman domination γ_R, paired domination, and the classical partners α (independence), τ (vertex cover), and n, Δ, δ.

**Enumerate.** nauty `geng`, connected graphs to n=9 (A001349: 1,1,2,6,21,112,853,11117,261080); n=10 if the ILP/exact domination solver keeps up.

**Conjecture generation.** PRIORITY, and the whole point: TxGraffiti's *currently-open* machine-generated domination conjectures (Davila, the live open-conjecture list / recent arXiv), which are unproven and small-graph-fitted. Refuting any one resolves a real open problem. Cite each open conjecture and confirm it is still open before testing. Do NOT re-test the settled classical bounds (Haynes-Hedetniemi-Slater "Fundamentals of Domination" 1998; Chellali-Haynes-Hedetniemi surveys) except once, to validate the engine - like Zagreb, those are known true or false and only reproduce. Secondary generator: auto-fit fresh γ-vs-invariant and ratio bounds (γ_t/γ, i/γ) on n≤7 that are not in the literature, then push them.

**Adversarial families.** Coronas G∘K1 (extremal for many domination ratios), spiders, complete multipartite, generalized Petersen graphs, kneser graphs, grid/torus products, and random cubic graphs; caterpillars for tree-restricted claims.

**Checker (exact).** Compute each domination number exactly by ILP or exhaustive minimum set cover (small n), not by a greedy heuristic; verify the reported dominating set actually dominates and is minimum by certificate (a smaller set is absent). Emit violators in graph6 plus the optimal set.

**Verification discipline.** Generator is not verifier: recompute each domination number with a second exact method (ILP vs branch-and-bound) and confirm the witnessing set independently. Cite each tested bound or mark "could not verify." Report candidates generated / broken / survived, graph6 witnesses with optimal sets.
