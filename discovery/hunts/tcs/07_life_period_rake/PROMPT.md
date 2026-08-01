# 07. Life rake of an open period

**Find.** A rake in Conway's Life (a spaceship that periodically emits other spaceships, usually gliders) whose period p is one for which no rake is currently known, or a rake of an open velocity. Rakes exist for many periods but small-p and unusual-velocity rakes remain gaps on LifeWiki's rake tables (verify the specific target).

**What counts as a win.** One RLE of a pattern that (a) translates by a fixed nonzero (dx, dy) every p generations and (b) emits at least one glider/ship per period that escapes without disrupting the rake. One-sided: existence only.

**Checker (seconds).** Simulate; verify the rake body returns to itself shifted by (dx, dy) at t=p (true period p), and count outbound gliders crossing a downstream line to confirm periodic emission. Verify the body's population stays bounded (nothing accumulates). Integer-exact.

**Search plan.** Structured engineering: attach a glider-emitting reaction to a known period-p spaceship or puffer; convert an existing puffer's debris trail into clean gliders; use backend reflectors. gfind/ikpx2 for the carrier ship, then component assembly. SAT (LLS) for compact emitters.

**Prior art (verify).** LifeWiki, "Rake" and "Puffer" (period tables); ConwayLife.com rake collections. Confirm the target period/velocity still lacks a rake.
