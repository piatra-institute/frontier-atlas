# 13. A turmite whose long-term behaviour is open

**Find.** For a specified 2-state, 2-colour turmite (a generalized Langton's ant on a square grid with a small transition table) whose asymptotic behaviour is *unclassified*, a witness settling it: either an eventual "highway" (a periodic drifting structure that repeats forever) or an eventual bounded cycle. Many of the 2x2 turmite table entries in Pegg's/Wikipedia's enumeration are marked with unknown long-term behaviour (verify the specific table entry).

**What counts as a win.** For a highway: a step count t0 and period P, dx, dy such that the whole configuration at step t0 + P equals the configuration at t0 translated by (dx, dy) and the ant's internal state/heading matches. For a bounded cycle: an exact configuration+state recurrence. One-sided: exhibiting either finite certificate settles that turmite.

**Checker (seconds).** Simulate the turmite deterministically to t0 + P; verify the claimed translational or exact recurrence of (grid patch, ant position mod translation, heading, internal state). Because the dynamics are deterministic, one matched recurrence proves eventual periodicity forever. Integer-exact.

**Search plan.** Structured: run each unclassified table far (10^8-10^9 steps is cheap), hash the local window + ant state to auto-detect recurrence, and report the first repeat. Highways usually declare themselves within millions of steps if they exist.

**Prior art (verify).** Wikipedia, "Turmite" (transition-table enumeration with unknown entries); Gajardo/Goles and Propp on generalized ants; Langton's ant highway result (Bunimovich-Troubetzkoy). Verify the entry is still open.
