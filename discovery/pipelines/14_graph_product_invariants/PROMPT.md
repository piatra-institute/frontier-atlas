# Batch sweep: refute graph-product invariant conjectures

**Mode:** one ChatGPT Pro session, code sandbox, batch throughput.
**Goal:** an explicit pair (G,H) violating a stated product inequality, or hardened survivors. Refutation is the clean win. Precedent: Hedetniemi's conjecture on χ of the tensor product was disproved (Shitov, 2019), so this class demonstrably yields counterexamples.

**Family + panel.** Small graphs G, H and their Cartesian G□H, tensor G×H, strong G⊠H, and lexicographic products; invariants: domination γ, independence α, chromatic χ, clique ω, and fractional relaxations. Track factor invariants for the ratio.

**Enumerate.** nauty `geng`, connected factors to n=7 (A001349 prefix: 1,1,2,6,21,112,853), forming all ordered pairs and their four products; verify product vertex counts equal |V(G)|·|V(H)|.

**Conjecture generation.** Anchor on named statements: Vizing's conjecture γ(G□H) ≥ γ(G)γ(H) (open since 1968); the tensor-product independence/fractional-chromatic relations; and the general multiplicativity/super-multiplicativity claims for α and γ across product types. Auto-fit invariant(G∗H)-vs-invariant(G),invariant(H) bounds on small pairs.

**Adversarial families.** Products where one factor is a cycle, Kneser graph, or Mycielskian (chromatic products misbehave), and repeated products (G□G, G×G×G) to push size; complete-multipartite factors for domination.

**Checker (exact).** Build each product graph explicitly from the correct adjacency rule (Cartesian vs tensor vs strong vs lexicographic — get these exactly right), recompute the invariant on the product by exact solver, and compare to the factor combination. Emit violating (G,H) pairs in graph6.

**Verification discipline.** Generator is not verifier: recompute each product with a second construction and each invariant with a second exact solver; unit-test the four product rules on K2□K2, C5×C5, etc. Cite each conjecture, noting Hedetniemi is refuted. Report candidates generated / broken / survived, graph6 witness pairs.
