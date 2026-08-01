# 05. Glider synthesis of a Life object that has none

**Find.** A glider synthesis (a set of gliders on collision courses that build a target object) for a small Life still life, oscillator, or spaceship that currently has *no known* glider synthesis. Catagolue and the ConwayLife synthesis project track many low-population objects for which no synthesis exists; pick one flagged "no known synthesis" (verify).

**What counts as a win.** One RLE: a finite set of gliders, mutually distant at t=0, whose evolution leaves exactly the target object (plus optional escaping gliders that never return). One-sided: producing any synthesis settles it. Cost-minimality is not required.

**Checker (seconds).** Place the input gliders per the RLE, run until the field stabilizes (bounded, e.g. a few thousand generations), then verify the stabilized region equals the target object (up to translation/phase) and that all other cells are empty or contain only outbound gliders. Integer-exact simulation.

**Search plan.** Structured: seed-and-collide search (e.g. the "seeds"/Bellman-style or Catagolue's apgluxe synthesis tooling), iterative deepening on glider count, and reuse of known component syntheses to build the target in stages. Evolutionary refinement of collision offsets.

**Prior art (verify).** LifeWiki, "Glider synthesis"; Catagolue object pages listing "no known synthesis." ConwayLife.com synthesis threads. Verify the chosen target still lacks a synthesis.
