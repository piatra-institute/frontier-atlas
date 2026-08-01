# Batch sweep: refute independence/matching/cover inequalities

**Mode:** one ChatGPT Pro session, code sandbox, batch throughput.
**Goal:** an explicit graph violating a stated independence/matching/cover bound, or hardened survivors. Refutation is the clean win.

**Family + panel.** Connected graphs; independence α, matching ν, vertex cover τ, fractional α_f and ν_f, the residue (Havel-Hakimi residue, a lower bound on α), the annihilation number, and the Caro-Wei bound Σ1/(d(v)+1). Track n, m, Δ, δ.

**Enumerate.** nauty `geng`, connected graphs to n=9 (A001349: 1,1,2,6,21,112,853,11117,261080); n=10 if the exact α solver keeps up.

**Conjecture generation.** Harvest from the Graffiti conjectures (Fajtlowicz, "Written on the Wall"), many relating α to residue, matching, and degree sequences, several historically refuted; and from TxGraffiti's independence/annihilation-number conjectures (Davila-Pepper). Auto-fit α-vs-(residue, ν, annihilation) and ratio bounds on n≤7.

**Adversarial families.** Complements of sparse graphs, kneser graphs (large α), line graphs (matching becomes independence), coronas, block graphs, and random regular graphs; graphs with prescribed degree sequences targeting residue-based bounds.

**Checker (exact).** Compute α and ν exactly (max independent set by ILP/branch-and-bound; ν by blossom algorithm), and residue/annihilation exactly from the sorted degree sequence. Verify witnessing sets independently. Emit violators in graph6.

**Verification discipline.** Generator is not verifier: recompute α with a second exact solver; recompute the degree-sequence invariants from scratch; use König's theorem (τ=ν on bipartite) as an internal audit. Cite each tested bound or mark "could not verify." Report candidates generated / broken / survived, graph6 witnesses.
