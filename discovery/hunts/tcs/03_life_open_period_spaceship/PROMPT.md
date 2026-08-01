# 03. Life spaceship of a period with no known example

**Find.** A Conway's Life spaceship whose minimal period p is one for which no spaceship of that exact period is currently known. Unlike oscillators (Life proved omniperiodic in 2023), spaceship periods still have documented gaps: there exist small p with no known moving pattern of period exactly p. Pull the current gap list from LifeWiki before starting (verify).

**What counts as a win.** One RLE that is a spaceship of minimal period exactly p (the target gap period). One-sided: existence only. A ship of a different period, or one whose true period divides p, does not count.

**Checker (seconds).** Simulate p generations; assert the pattern reappears translated by some nonzero (dx, dy) at t=p, and does not reappear translated at any 0<k<p (so p is the true period). Integer-exact simulation, milliseconds.

**Search plan.** Structured: gfind/zfind and ikpx2 constrained to the target period; adapt known high-period ships (via tandem/half-baked reactions) toward the gap period; SAT (LLS) for small bounding boxes. Also assemble from period-p rakes/puffers if an elementary ship resists.

**Prior art (verify).** LifeWiki, "Spaceship" (period table) and "List of unsolved problems in Conway's Game of Life." Omniperiodicity (oscillators only) settled in arXiv 2312.02799 (2023); the analogous spaceship-period question remains open. Verify the exact gap period is still open.
