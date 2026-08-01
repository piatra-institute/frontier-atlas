# 01. Strictly volatile Life oscillator of an open period

**Find.** A pattern in Conway's Game of Life that is a *strictly volatile* oscillator of a period p for which no strictly volatile oscillator is currently known. A strictly volatile oscillator is one in which every live-or-dead cell inside the bounding box changes state at some point during the cycle (no cell is constant). Life is now omniperiodic (all periods have *some* oscillator, 2023), but strict volatility at small periods is still open; period 7 is a documented gap (verify).

**What counts as a win.** One explicit pattern (RLE) that (a) has minimal period exactly p and (b) is strictly volatile. One-sided: exhibiting one settles existence. A non-strict oscillator, or period != p, does not count.

**Checker (seconds).** Load the RLE into a Life engine, run 2p generations. Confirm state at t=p equals t=0, state at t=k != t=0 for 0<k<p (minimal period), and that for every cell in the bounding box there exists some t in [0,p) where it is live and some t where it is dead. Pure integer simulation.

**Search plan.** Structured/SAT: enumerate small volatile candidates with a SAT-based oscillator search (e.g. LLS / Logic Life Search encoding period-p constraints plus a per-cell "toggles" clause). Also mine Catagolue and known p-oscillator stamp collections, then perturb.

**Prior art (verify).** LifeWiki, "List of unsolved problems in Conway's Game of Life" (strictly volatile oscillators); omniperiodicity proof, arXiv 2312.02799 (2023). Exact smallest open period: verify.
