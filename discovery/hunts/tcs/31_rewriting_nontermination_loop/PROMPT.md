# 31. A non-termination loop for an open term/string rewriting system

**Find.** For a specified string or term rewriting system whose termination is listed OPEN in the Termination Problem Data Base (TPDB) / Termination Competition, an explicit witness of non-termination: a "loop" (a term t rewriting in >= 1 steps to a context/substitution instance of itself, C[t sigma]) or an infinite derivation with a periodic structure. Many small TPDB entries resist both termination provers and non-termination provers (verify the chosen instance is still open).

**What counts as a win.** One term t and one finite rewrite sequence t ->+ C[t sigma] exhibiting a loop (which entails an infinite derivation). One-sided: a loop certificate refutes termination outright. (Terminating systems cannot be settled this way; the win is the non-termination direction.)

**Checker (seconds).** Replay the given rewrite sequence: at each step verify the applied rule matches (find the redex, apply the substitution) and that the final term equals C[t sigma] for the stated context C and substitution sigma. Then the loop lemma gives non-termination. Purely syntactic matching; milliseconds.

**Search plan.** Structured: bounded forward rewriting / narrowing search for self-embedding terms; unfold-and-match heuristics (as in AProVE / TTT2 non-termination modules) to spot loops; SAT/SMT search for a substitution closing a candidate cycle.

**Prior art (verify).** Termination Competition and the TPDB (open/unknown-status entries); AProVE (Giesl et al.) and TTT2 (Korp, Sternagel, Zankl, Middeldorp) non-termination techniques; the "loop" criterion (Zantema). Verify the instance is currently unsolved.
