# 29. A small Post correspondence instance with a record-long shortest solution

**Find.** A binary Post Correspondence Problem (PCP) instance with a small number of pairs (small "size", e.g. 3-5 pairs over a 2-letter alphabet) whose shortest solution is longer than the current record for that size class. The maximal shortest-solution length as a function of instance size (the PCP "hardest instances") is tracked; pushing it at a fixed size is a concrete, checkable target (verify the current record for the chosen size).

**What counts as a win.** One PCP instance (a list of pairs (u_i, v_i)) plus one explicit index sequence i_1 ... i_L such that u_{i_1}...u_{i_L} = v_{i_1}...v_{i_L}, where either (a) the instance is a fresh solvable instance whose *shortest* solution is provably longer than the record, or (b) simply a solvable instance whose exhibited solution beats the record length. One-sided: exhibiting a match certifies solvability.

**Checker (seconds).** Concatenate the top and bottom strings along the index sequence and assert equality; assert every index is in range. Milliseconds. (For a *shortest*-solution claim, additionally BFS the configuration graph up to that length to confirm minimality.)

**Search plan.** Structured/exhaustive: BFS/IDA* over PCP configurations (the "difference" string frontier) with pruning; enumerate small instances and record those whose shortest solution is long; SAT encodings bounding solution length. Zhao and Ling's search framework is the model.

**Prior art (verify).** Ling & Zhao, and the "hardest small PCP instances" tables (verify the record shortest-solution length for the target size). Post (1946); Matiyasevich-Senizergues small undecidable PCP results.
