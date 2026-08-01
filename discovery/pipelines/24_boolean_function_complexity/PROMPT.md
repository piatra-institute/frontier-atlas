# Batch sweep: refute Boolean-function complexity-measure conjectures

**Mode:** one ChatGPT Pro session, code sandbox, batch throughput.
**Goal:** an explicit Boolean function beating a claimed relation between complexity measures, or hardened survivors. A record-beating separation is a small, exactly-checkable witness.

**Family + panel.** Boolean functions f:{0,1}^n→{0,1}; measures: sensitivity s(f), block sensitivity bs(f), certificate complexity C(f), decision-tree depth D(f), degree deg(f) (as a real polynomial), and approximate degree. The open questions are the exact largest gaps between these (the sensitivity conjecture s vs deg is settled — Huang 2019, deg ≤ s^2 — but tight constants and the bs-vs-s and C-vs-bs gaps are open).

**Enumerate.** Small arity exhaustively (all 2^(2^n) functions for n≤4, up to symmetry) and structured/large-arity families for n=5..~12. Count-check: verify measures on known extremal functions (e.g. the Rubinstein bs-vs-s gap function, address/multiplexer functions) reproduce published gap values.

**Conjecture generation.** Target the ratios bs/s, C/bs, D/deg, deg/bs, and approximate-degree gaps; the search is for a function whose ratio exceeds the current best-known separation. Generate candidates by composing gap gadgets (the standard tool for pushing separations) and by local search over truth tables.

**Adversarial families.** Recursive compositions of a base gadget (composition multiplies gaps), the Rubinstein/Ambainis-Sun functions, tribes/address functions, and random monotone functions.

**Checker (exact).** Compute every measure exactly from the truth table (s and bs by scanning neighbourhoods, C by minimal certificates, deg by Mobius/Walsh expansion, D by exact decision-tree DP). A refutation is a function certified to beat the recorded best ratio. Emit the truth table.

**Verification discipline.** Generator is not verifier: recompute each measure with a second independent routine; verify the polynomial degree via exact Walsh coefficients. Cite the current record separation (survey of Buhrman-de Wolf, and Aaronson et al. on degree vs approximate degree) or mark "could not verify." Report candidates generated / broken / survived, with truth tables.
