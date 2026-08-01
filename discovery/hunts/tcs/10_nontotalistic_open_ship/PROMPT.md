# 10. Spaceship of an open speed in an isotropic non-totalistic rule

**Find.** A spaceship (or high-period oscillator) of a currently unrealized velocity in a specified 2-state isotropic non-totalistic (INT) Life-like rule. INT rules (Hensel notation, e.g. tlife/B3-q..., or Just Friends B2-a/S12) have large, actively-searched but very incomplete object zoos on Catagolue, with many velocities marked "no known ship" (verify the rule and gap).

**What counts as a win.** One RLE valid under the chosen INT rule that is a spaceship of a velocity (or oscillator of a period) absent from that rule's census. One-sided: existence only.

**Checker (seconds).** Simulate under the exact INT transition table (the neighbourhood-configuration birth/survival sets). Verify true period and translation vector. Integer-exact; correctness hinges on encoding the rule's isotropic transition table faithfully, so cross-check the table against a reference engine (Golly/lifelib).

**Search plan.** Structured: gfind/zfind and LLS both support INT rules; target a small period at the claimed gap velocity. Seed from Catagolue apgsearch hauls and ConwayLife "rules of interest" threads that flag near-miss partials.

**Prior art (verify).** LifeWiki, "Isotropic non-totalistic rule" and "Hensel notation"; Catagolue rule censuses (e.g. tlife, "Just Friends," "Pedestrian Life"). Verify the target velocity/period is still open in the chosen rule.
