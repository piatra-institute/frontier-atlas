# 06. A smaller Garden-of-Eden orphan in Life

**Find.** A Life configuration with no predecessor (an "orphan," i.e. the finite core of a Garden of Eden) whose bounding box / live-cell count is smaller than the current record. The smallest known orphans have been shrunk repeatedly by SAT search; a strictly smaller one is a clean improvement (verify the current record before starting).

**What counts as a win.** One pattern P (the constrained cells) such that no assignment of the surrounding cells yields a predecessor mapping onto P under the Life rule, with size strictly below the record. One-sided: the pattern plus an UNSAT certificate settles it.

**Checker (seconds).** Encode "does there exist a previous generation whose image contains P" as SAT over the bounded predecessor grid (Life transition clauses per cell). Feed to a DRAT-producing solver; a checked UNSAT proof certifies P is an orphan. Re-verify with an independent SAT encoding and DRAT-trim.

**Search plan.** SAT: minimize orphan size by binary-searching the bounding box and pushing cells to "don't care," reusing the Hartman/Heule/others orphan-search encodings; symmetry-break the grid; use incremental solving. Evolutionary shrinking of a known orphan by relaxing cells and re-testing UNSAT.

**Prior art (verify).** LifeWiki, "Garden of Eden"; the smallest-orphan record traces to SAT searches by Hartman, Heule, and collaborators (record size and date: verify). No-predecessor existence is the Moore-Myhill Garden-of-Eden theorem context.
