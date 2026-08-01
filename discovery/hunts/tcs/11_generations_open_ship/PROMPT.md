# 11. Spaceship of an open speed in a Generations rule

**Find.** A spaceship of an unrealized velocity in a named multi-state Generations rule (cells have a birth state, several dying/refractory states, then death), for example StarWars (B2/S345/4) or Brian's Brain (B2/S/3). These rules are dominated by fast ships and have sparse, incomplete velocity coverage on Catagolue (verify the target rule and gap).

**What counts as a win.** One RLE valid under the chosen Generations rule that translates by (dx, dy) every p generations at a velocity absent from that rule's census. One-sided: existence only.

**Checker (seconds).** Simulate the Generations transition: state 0 cells birth per B, state 1 cells survive per S else advance, states >=2 advance deterministically to death. Verify the multi-state pattern (all states) reappears shifted by (dx, dy) at true period p. Integer-exact; validate the state-advance semantics against Golly.

**Search plan.** Structured: gfind supports Generations rules for orthogonal/diagonal ships; LLS handles small boxes. Seed from Catagolue apgsearch hauls for the rule and from ConwayLife "Generations" threads listing partials.

**Prior art (verify).** LifeWiki, "Generations" and the rule pages "StarWars," "Brian's Brain"; Catagolue Generations censuses. Verify the target velocity is still unrealized in the chosen rule.
