# Batch sweep: refute domination-family inequalities

**Mode:** one ChatGPT Pro session, code sandbox, batch throughput.
**Goal:** an explicit graph violating a stated domination bound, or hardened survivors. Refutation is the clean win.

**Family + panel.** Connected graphs; domination variants: domination γ, total domination γ_t, independent domination i, connected domination γ_c, Roman domination γ_R, paired domination, and the classical partners α (independence), τ (vertex cover), and n, Δ, δ.

**Enumerate.** nauty `geng`, connected graphs to n=9 (A001349: 1,1,2,6,21,112,853,11117,261080); n=10 if the ILP/exact domination solver keeps up.

**Conjecture generation.** Harvest from the domination literature (Haynes-Hedetniemi-Slater "Fundamentals of Domination" 1998; Chellali-Haynes-Hedetniemi surveys) and from TxGraffiti's machine-generated domination conjectures (Davila, arXiv), a live source of unproven, small-graph-fitted bounds. Auto-fit γ-vs-invariant and ratio bounds (e.g. γ_t/γ, i/γ) on n≤7.

**Adversarial families.** Coronas G∘K1 (extremal for many domination ratios), spiders, complete multipartite, generalized Petersen graphs, kneser graphs, grid/torus products, and random cubic graphs; caterpillars for tree-restricted claims.

**Checker (exact).** Compute each domination number exactly by ILP or exhaustive minimum set cover (small n), not by a greedy heuristic; verify the reported dominating set actually dominates and is minimum by certificate (a smaller set is absent). Emit violators in graph6 plus the optimal set.

**Verification discipline.** Generator is not verifier: recompute each domination number with a second exact method (ILP vs branch-and-bound) and confirm the witnessing set independently. Cite each tested bound or mark "could not verify." Report candidates generated / broken / survived, graph6 witnesses with optimal sets.
