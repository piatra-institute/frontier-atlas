# 02. Life spaceship of an unrealized velocity

**Find.** A Conway's Life spaceship whose velocity (p, dx, dy) is not on the list of realized spaceship velocities. The spaceship-velocity problem (which of the theoretically possible rational velocities are realizable) is the largest open problem remaining after omniperiodicity. Many slow orthogonal/diagonal/oblique speeds have no known example; pick a target speed from LifeWiki's realized-velocity table that is currently absent (verify the specific gap before starting).

**What counts as a win.** One RLE that translates by (dx, dy) every p generations for a velocity not previously realized. One-sided: existence only. Reproducing a known velocity does not count.

**Checker (seconds).** Simulate p generations; assert the live-cell set at t=p equals the t=0 set shifted by (dx, dy), and that no smaller period achieves a translation (true period). Confirm the velocity is |dx|,|dy| <= p (sub-light) and matches the claimed unrealized (p, dx, dy). Integer-exact.

**Search plan.** Structured de-novo search: gfind / zfind (Eppstein) and the newer ikpx2 partial-extension search for orthogonal and oblique ships; SAT encodings (LLS) for very slow speeds. Seed from near-misses in the ConwayLife "unfinished ships" threads.

**Prior art (verify).** LifeWiki, "Spaceship" and its velocity table; "List of unsolved problems in Conway's Game of Life" (spaceship velocities). Eppstein, "Searching for spaceships," arXiv cs/0004003. Confirm the chosen (p, dx, dy) is still unrealized.
