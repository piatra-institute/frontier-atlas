# Batch sweep: refute Nordhaus-Gaddum-type relations

**Mode:** one ChatGPT Pro session, code sandbox, batch throughput.
**Goal:** an explicit graph violating a stated Nordhaus-Gaddum bound on f(G) and f(complement), or hardened survivors. Refutation is the clean win.

**Family + panel.** Graphs G and their complements together; for an invariant f, the sum f(G)+f(Ḡ) and product f(G)·f(Ḡ). Panel f: chromatic χ, independence α, domination γ, clique ω, spectral radius λ1, algebraic connectivity, matching ν, diameter, and topological indices (Wiener, Zagreb).

**Enumerate.** nauty `geng`, all graphs to n=9 (use A000088: 1,1,2,4,11,34,156,1044,12346,274668,12005168 for the full set, since complements of disconnected graphs matter here). Compute each invariant on G and on Ḡ.

**Conjecture generation.** Harvest from Aouchiche-Hansen "A survey of Nordhaus-Gaddum type relations" (Discrete Appl. Math. 161, 2013), which collects dozens of such bounds across invariants, several AutoGraphiX-generated and later refuted or left open. Auto-fit tight upper/lower bounds on f(G)+f(Ḡ) and the product as functions of n on n≤7.

**Adversarial families.** Self-complementary graphs (Paley graphs, self-complementary trees), threshold and split graphs (extremal for many NG sums), Turan graphs, and random graphs near the self-complementary regime; push to larger n where invariants are cheap.

**Checker (exact).** Build Ḡ explicitly, recompute f on both graphs with the exact method appropriate to f, and evaluate the sum/product against the claimed bound. Emit violators in graph6.

**Verification discipline.** Generator is not verifier: recompute each invariant with a second implementation on both G and Ḡ; verify complementation is correct (edges of G and Ḡ partition K_n). Cite each tested relation or mark "could not verify." Report candidates generated / broken / survived, graph6 witnesses.
