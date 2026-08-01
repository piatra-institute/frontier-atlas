# Batch sweep: refute degree-based topological-index inequalities

> **Status: SETTLED (validation-only).** These bounds are known true or known false, so a sweep only reproduces known results (the first run confirmed this). See `../INDEX.md` re-triage. Aim the engine at open/unproven conjectures instead.

**Mode:** one ChatGPT Pro session, code sandbox, batch throughput (not one problem).
**Goal:** an explicit small graph violating a published degree-index inequality, or a set of computationally-hardened survivors. The refutation is the clean win.

**Family + panel.** Connected graphs; degree-based indices: first/second Zagreb M1=Σd(v)^2, M2=Σ_{uv}d(u)d(v), forgotten index F=Σd(v)^3, hyper-Zagreb, Albertson irregularity Σ_{uv}|d(u)-d(v)|, sigma index Σ(d(u)-d(v))^2, and their per-vertex/per-edge normalisations M1/n, M2/m. Also track n, m, Δ, δ, and whether the graph is a tree or chemical (Δ≤4).

**Enumerate.** All connected graphs to n=9 (n=10 if time) via nauty `geng`. Count-check A001349: 1,1,2,6,21,112,853,11117,261080. Add trees (A000055: 1,1,1,2,3,6,11,23,47) and chemical trees separately, since many index conjectures are stated only for trees or chemical graphs.

**Conjecture generation.** Harvest stated bounds from the degree-index literature (Gutman-Trinajstic Zagreb 1972; Furtula-Gutman forgotten index 2015; the M1/n ≤ M2/m comparison of Hansen-Vukicevic, Croat. Chem. Acta 2007, known false for general graphs). Also auto-fit tightest linear/ratio bounds among panel pairs on n≤7, then push.

**Adversarial families.** Bags that break naive degree bounds: complete bipartite K_{a,b} with a≪b, stars, double-stars, brooms, kites, Turan graphs, barbells, subdivided stars, and dense-plus-pendant graphs (extreme degree spread).

**Checker (exact).** Recompute each index as an exact rational/integer sum over the degree sequence and edge list; compare against the claimed inequality; emit any violator in graph6.

**Verification discipline.** Generator is not verifier: recompute every index with a second, independently written function (and cross-check M1=Σd^2 against 2m-based identities). Name the source of each tested bound or mark "could not verify against literature." Report the denominator: candidates generated / broken / survived, with graph6 witnesses.
