# 14. A small Life pattern beating the methuselah longevity record

**Find.** A Conway's Life pattern confined to a small bounding box (e.g. <= n x n) or below a fixed population cap that takes longer to stabilize (become a still life / oscillator set / escaping-ship configuration) than the current record methuselah for that size class. This is a well-defined "busy-beaver for Life": records like Lidka and the small-population champions are tracked and occasionally broken (verify the record for the chosen size cap).

**What counts as a win.** One RLE within the size/population cap whose stabilization time (generation after which population and pattern become eventually periodic, ignoring escaping ships) strictly exceeds the recorded best. One-sided: a longer-lived example wins; no lower bound is claimed.

**Checker (seconds).** Simulate with a hashing/period detector (e.g. lifelib/hashlife or an explicit ash-detector): run until the pattern is provably eventually periodic (all remaining activity is a fixed set of still lifes, oscillators, and escaping ships), record the settling generation. Confirm the start pattern meets the cap. Integer-exact.

**Search plan.** Structured/evolutionary: enumerate or randomly sample patterns within the cap (symmetry-reduced), simulate, keep the longest-lived; hill-climb by single-cell perturbations of champions. Golly/lifelib for speed.

**Prior art (verify).** LifeWiki, "Methuselah" (records: Lidka, and small-box / small-population champions with named lifespans); ConwayLife.com "long-lived" threads. Verify the record for the exact size class before starting.
