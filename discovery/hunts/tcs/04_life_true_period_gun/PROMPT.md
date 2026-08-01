# 04. Life true-period glider gun of an open period

**Find.** A true-period glider gun in Conway's Life for a period p that currently has no known true-period gun. A gun of period p emits a glider (or ship) every p generations and returns to its start after p; "true-period" forbids simply merging several higher-frequency guns or using a period-multiplying backend. Several small p have no known true-period gun (pull the current open-period list from LifeWiki; verify).

**What counts as a win.** One RLE of a stable gun whose emission period and internal period are both exactly p. One-sided: existence only. A pseudo-period or composite gun does not count.

**Checker (seconds).** Run the pattern for several p generations. Verify the mechanism (bounding box interior) returns to its initial state every p steps, and that exactly one glider is released per p-cycle crossing a fixed downstream line. Integer-exact; confirm minimality of p by checking no divisor of p is also a full period.

**Search plan.** Structured engineering: combine a period-p oscillator/reaction with a glider-producing edge; search Catagolue and the ConwayLife gun collections for near-misses; use glider-injection and reflector toolkits (Snark, syringes) to stabilize. SAT (LLS) for compact cores.

**Prior art (verify).** LifeWiki, "Gun" (true-period gun table) and "List of unsolved problems in Conway's Game of Life." Confirm the target period p still lacks a true-period gun before starting.
