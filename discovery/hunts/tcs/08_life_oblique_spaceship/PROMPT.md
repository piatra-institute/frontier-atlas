# 08. An elementary oblique Life spaceship of a new slope

**Find.** An *elementary* (single-object, not engineered from many parts) oblique spaceship in Conway's Life travelling at a slope (dx:dy with dx != dy, both nonzero) for which no elementary ship is known. Oblique motion is rare in Life: Sir Robin (the (2,1)c/6 knightship, 2018) was the first elementary non-orthogonal, non-diagonal ship. Other slopes remain open (verify current knightship/oblique tables).

**What counts as a win.** One RLE of a self-contained spaceship translating by (dx, dy) with dx != dy every p generations. One-sided: existence only. Large engineered "macro" obliques (e.g. Gemini-style constructions) do not count as *elementary*.

**Checker (seconds).** Simulate p generations; assert the full live-cell set reappears shifted by exactly (dx, dy) and by no smaller shift at any earlier phase (true period p). Confirm connectivity/support is a single small object, not a distributed construction. Integer-exact.

**Search plan.** Structured de-novo: ikpx2 (iterative partial extension) is the tool that found Sir Robin; run it targeting new slopes with small period. SAT (LLS) for small boxes. Seed from oblique near-misses in ConwayLife search threads.

**Prior art (verify).** LifeWiki, "Oblique spaceship," "Knightship," "Sir Robin" (2018); ikpx2 by Adam P. Goucher. Verify which slopes remain without an elementary example.
