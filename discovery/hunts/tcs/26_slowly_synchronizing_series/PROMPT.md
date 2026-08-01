# 26. A slowly-synchronizing automaton beating the known series for its size

**Find.** A synchronizing DFA on n states over a small alphabet whose shortest reset word is longer than any produced by the known slowly-synchronizing series at that (n, alphabet size), without reaching the Cerny value (n-1)^2. Known ternary series reach n^2 - 3n + 2; whether specific n admit strictly longer reset thresholds below (n-1)^2 (filling the gap between known series and the conjectured maximum) is open (verify the record for the chosen n).

**What counts as a win.** One explicit DFA whose computed reset threshold strictly exceeds the best tabulated value for its (n, k) among non-Cerny automata. One-sided: a longer-resetting automaton for that cell is an advance.

**Checker (seconds).** Same power-set back-BFS as task 25: from the full state set, expand preimages under all letters until a singleton is reached; the distance is the reset threshold. Bitset subsets keep n <= 20 in seconds. Assert the value exceeds the recorded best for that cell.

**Search plan.** Structured: parametrized constructions extending the Ananichev-Volkov-Gusev / Dzyga-Ferens-Gusev-Szykula ternary and binary series; targeted local search that lengthens reset words (grow the "hard" preimage chain); ILP/SAT to force a long shortest-reset lower bound while keeping n fixed.

**Prior art (verify).** Ananichev, Gusev, Volkov, "Slowly synchronizing automata and digraphs" (2010); Gusev-Szykula and later works on binary/ternary slow series; the reset-threshold results list (arXiv 2508.15655, 2025). Verify best-known reset length at the target (n, k).
