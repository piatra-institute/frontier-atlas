# 12. Spaceship of an open speed in a Larger-than-Life rule

**Find.** A "bug" (spaceship) of an unrealized velocity in a specified Larger-than-Life (LtL) rule, a totalistic Life-like rule on a large radius-r neighbourhood with birth/survival intervals, for example Bosco's Rule (R5, birth [34,45], survival [34,58]). LtL bugs are studied but their velocity spectra are far from mapped (verify rule and gap).

**What counts as a win.** One RLE valid under the chosen LtL rule that is a spaceship of a velocity absent from the known set for that rule. One-sided: existence only.

**Checker (seconds).** Simulate the LtL transition: for each cell, count live cells in the radius-r box (Moore or specified) and apply the birth/survival intervals. Verify true period and translation vector. Integer-exact; validate the neighbour-count and interval logic against a reference LtL engine.

**Search plan.** Structured/evolutionary: LtL bugs are typically found by soup search plus manual glider-style extraction; run randomized-seed searches at the target rule, cluster surviving translating blobs by velocity, then clean up. Adapt gfind-style row extension where the neighbourhood permits.

**Prior art (verify).** Evans, "Larger than Life" (2001) and follow-ups; LifeWiki, "Larger than Life"; Bosco's Rule and Golly's LtL algo. Verify which velocities remain unrealized in the chosen rule before starting.
