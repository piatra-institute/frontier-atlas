# 27. Three mutually orthogonal Latin squares of order 10

**Target.** Construct three mutually orthogonal Latin squares of order 10 (equivalently show N(10) >= 3), or contribute new nonexistence structure. Only two MOLS of order 10 are known; whether a third exists is a long-standing open question. This is the canonical small MOLS case (flagged: famous and heavily attacked, a genuine long shot).

**What counts as a win.** One explicit set of three pairwise-orthogonal 10 x 10 Latin squares settles N(10) >= 3 outright (one-sided YES). Given the history, honest partial products (large orthogonal-triple fragments, structural obstructions) are worth reporting but are not the win.

**Checker (seconds).** Read three 10 x 10 arrays over {0..9}. Verify each is Latin, and each of the three pairs is orthogonal (superimposition yields all 100 ordered pairs). O(n^2), microseconds.

**Search plan.** Search for a common mate to a fixed orthogonal pair via exact-cover / SAT on the third square's cells; prescribed-automorphism restriction to cut the space; transversal-design TD(4,10) formulation (a TD(4,10) is equivalent to 2 MOLS with a common transversal structure yielding a third); large-neighborhood local search. Note: exhaustive resolution is out of scope; target a witness only.

**Prior art (verify).** N(10) = 2 is the best known lower bound; the existence of 3 MOLS(10) is open. See Colbourn-Dinitz "Handbook of Combinatorial Designs" (MOLS chapter) and the extensive order-10 literature (Parker, Bose-Shrikhande-Parker context; later computational studies). Re-verify status.

**Openness:** documented-open (famous). **Win-type:** existence.
