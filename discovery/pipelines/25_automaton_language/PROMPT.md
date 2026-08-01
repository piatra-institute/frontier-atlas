# Batch sweep: refute automaton and formal-language conjectures

**Mode:** one ChatGPT Pro session, code sandbox, batch throughput.
**Goal:** an explicit automaton beating a claimed synchronizing/state-complexity bound, or hardened survivors. A bound-beating automaton is a small, exactly-checkable witness.

**Family + panel.** Deterministic finite automata (DFAs); quantities: shortest reset (synchronizing) word length, whether an automaton is synchronizing, and the state complexity of language operations (union, intersection, star, reversal, concatenation) — the number of states of the minimal DFA of the result. Anchor: the Cerny conjecture (a synchronizing n-state DFA has a reset word of length ≤ (n−1)^2; open, tight only for the Cerny series).

**Enumerate.** Exhaustive small DFAs: all synchronizing DFAs on n≤6 states over a 2-letter alphabet up to isomorphism (the Kisielewicz-Szykula-Wroblewski catalogue gives the extremal reset lengths per n — cross-check against it), plus larger structured automata. For state complexity, enumerate small minimal DFAs and combine.

**Conjecture generation.** Test the (n−1)^2 bound and, more productively, the finer conjecture that only the Cerny automata attain it — search for any automaton within the top reset-length band. Test published state-complexity bounds for operations by trying to exceed the claimed worst case. Auto-generate automata by local edits of near-extremal ones.

**Adversarial families.** The Cerny series C_n and its known relatives, slowly-synchronizing families (Ananichev-Volkov-Gusev), Eulerian automata, and random DFAs conditioned to be synchronizing.

**Checker (exact).** Compute the shortest reset word exactly by BFS over the subset automaton (power-set), never by heuristic; compute state complexity by minimizing the product/subset DFA (Hopcroft/Moore) exactly. Emit the automaton (transition table) and the certified reset word.

**Verification discipline.** Generator is not verifier: recompute reset length with a second exact subset-BFS and re-minimize with a second algorithm; verify the reported word actually synchronizes. Cite Cerny and the extremal catalogue, or mark "could not verify." Report candidates generated / broken / survived, with transition tables.
