# 15. A new glider or collision product in a 1D elementary CA

**Find.** In a specified elementary (1D, 2-state, 3-neighbour) cellular automaton with rich glider dynamics, most famously Rule 110 (also Rule 54, Rule 62, Rule 184-variants), either (a) a glider of a period/velocity not in the published glider catalogue, or (b) a two-glider collision whose product is not yet catalogued. The Rule 110 glider tables (Cook; Martinez et al.) are extensive but not proven complete (verify the target catalogue).

**What counts as a win.** For a new glider: a background (ether) plus a localized structure that translates by (dx, p) unlisted in the catalogue. For a new collision: two catalogued gliders whose collision yields a product not previously recorded. One-sided: exhibiting the pattern settles it.

**Checker (seconds).** Simulate the elementary rule on a wide finite strip (or torus) with the standard ether background. Verify: (a) the candidate glider recurs shifted by (dx, p) against the ether; (b) the collision product's identity by matching against the known-glider/still-structure library. Integer-exact.

**Search plan.** Structured/exhaustive: run all small perturbations of the ether phase (finite alphabet of gaps between gliders) to enumerate collisions; scan for un-catalogued survivors. De Bruijn-diagram analysis of the rule to seed candidate localized structures.

**Prior art (verify).** Cook, "Universality in elementary cellular automata" (2004); Martinez, McIntosh, Mora, glider/collision catalogues for Rule 110 and Rule 54. Verify which structures the catalogue omits.
