# 09. Open spaceship in HighLife (B36/S23)

**Find.** A spaceship of an open velocity, or an oscillator/gun of an open period, in the Life-like rule HighLife (B36/S23). HighLife is famous for its replicator; its zoo of ships and oscillators is far less complete than Life's, and Catagolue's HighLife census still shows velocities/periods with no known example (verify current gaps).

**What counts as a win.** One RLE valid under B36/S23 that is a spaceship of a velocity (or an oscillator/gun of a period) currently absent from the HighLife census. One-sided: existence only. Reproducing a catalogued object does not count.

**Checker (seconds).** Simulate under the B36/S23 transition (birth on 3 or 6 neighbours, survival on 2 or 3). Verify the true period and translation vector as in the Life ship/oscillator checkers. Integer-exact; the only change from Life is the rule table.

**Search plan.** Structured: run gfind/zfind and LLS with the rule set to B36/S23; mine Catagolue's HighLife haul (apgsearch soup census) for tagged unknown-velocity objects and refine. Evolutionary soup-search then symmetry cleanup.

**Prior art (verify).** LifeWiki, "HighLife"; Catagolue census for rule b36s23 (object/velocity tables). Confirm the specific target velocity or period is still unrealized.
