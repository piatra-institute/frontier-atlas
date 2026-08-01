# Batch sweep: refute connectivity-type index inequalities (Randic, ABC, GA)

> **Status: SETTLED (validation-only).** These bounds are known true or known false, so a sweep only reproduces known results (the first run confirmed this). See `../INDEX.md` re-triage. Aim the engine at open/unproven conjectures instead.

**Mode:** one ChatGPT Pro session, code sandbox, batch throughput.
**Goal:** an explicit graph or tree violating a stated Randic / atom-bond-connectivity / geometric-arithmetic bound, or hardened survivors. Refutation is the clean win.

**Family + panel.** Connected graphs and trees; edge-weighted "bond-incident-degree" indices: Randic R=Σ_{uv}(d(u)d(v))^{-1/2}, general Randic R_a, sum-connectivity Σ(d(u)+d(v))^{-1/2}, harmonic Σ2/(d(u)+d(v)), geometric-arithmetic GA=Σ 2√(d(u)d(v))/(d(u)+d(v)), atom-bond-connectivity ABC=Σ√((d(u)+d(v)-2)/(d(u)d(v))). Track n, m, Δ, δ.

**Enumerate.** nauty `geng`, connected graphs to n=9 (A001349: 1,1,2,6,21,112,853,11117,261080). Trees to n=15 separately (A000055), since the ABC-minimal-tree structure problem lives there.

**Conjecture generation.** Harvest bounds from: Randic 1975; Estrada et al. ABC 1998; Vukicevic-Furtula GA 2009; Bollobas-Erdos general Randic; the long-open ABC-minimal-tree structure question (Gan-Liu-You and later MATCH papers, several partial claims refuted by search). Auto-fit index-vs-index and index-vs-(n,m,Δ) bounds on n≤7.

**Adversarial families.** Trees that shift ABC/Randic extremes: balanced vs unbalanced double-brooms, spiders, caterpillars, Bethe/complete d-ary trees, path-plus-pendants; plus complete bipartite and kite graphs for the general-graph bounds.

**Checker (exact).** Recompute each index as a high-precision sum with exact per-edge terms (keep √ under interval arithmetic so a claimed strict inequality is never decided by float error); emit violators in graph6 with the exact margin.

**Verification discipline.** Generator is not verifier: second independent index implementation; interval arithmetic for all radicals. Cite each tested bound's source or mark "could not verify." Report candidates generated / broken / survived, with graph6 witnesses and margins.
