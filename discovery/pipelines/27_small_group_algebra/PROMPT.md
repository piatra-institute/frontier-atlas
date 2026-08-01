# Batch sweep: refute inequalities among finite-group invariants

**Mode:** one ChatGPT Pro session, code sandbox, batch throughput.
**Goal:** an explicit small group violating a stated invariant inequality, or hardened survivors. Refutation is the clean win.

**Family + panel.** Finite groups; invariants: order |G|, number of conjugacy classes k(G), commuting probability cp(G)=k(G)/|G|, number of subgroups, derived length dl(G), nilpotency class, number of distinct character degrees |cd(G)|, largest character degree, and number of maximal subgroups.

**Enumerate.** The GAP SmallGroups library (Besche-Eick-O'Brien), complete for all orders up to 2000 except 1024, and many larger orders. Sweep all groups up to order ~512 exhaustively; sanity-check group counts per order against the library's SmallGroupsInformation.

**Conjecture generation.** Anchor on real statements: cp(G) ≤ 5/8 for nonabelian G (Gustafson — a theorem, use as self-check) and the structure of the cp value-spectrum (gaps studied by Eberhard 2015, some open); Isaacs-type bounds dl(G) ≤ |cd(G)| for solvable groups (open in general); and Taketa/Berkovich inequalities. Auto-fit inequalities among the panel (e.g. k(G) vs number of subgroups, dl vs |cd|) over the library, then adversarially test.

**Adversarial families.** p-groups (extremal for many class/subgroup-count bounds), extraspecial groups, groups of order p^a q^b, Frobenius groups, and the Sylow-structured groups near each conjecture's boundary.

**Checker (exact).** Recompute each invariant directly in GAP (conjugacy classes, subgroup lattice, character table, derived series) — all exact, integer/algebraic. A refutation is a specific SmallGroup ID violating the inequality. Emit the [order, id] identifier.

**Verification discipline.** Generator is not verifier: recompute at least one invariant per hit by an independent construction (e.g. class count from the character table vs from conjugacy-class enumeration); confirm cp ≤ 5/8 as an internal audit. Cite each inequality, noting proven vs open. Report candidates generated / broken / survived, with SmallGroup IDs.
