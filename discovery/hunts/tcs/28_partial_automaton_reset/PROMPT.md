# 28. A carefully-synchronizing partial automaton with long reset word

**Find.** A partial deterministic finite automaton (PFA) on n states over a small alphabet that is carefully synchronizing and whose shortest carefully-synchronizing word is longer than the best known for that (n, k). For PFAs the reset threshold can grow far faster than for complete DFAs (superpolynomially in some models); the exact extremal lengths at small n over a binary/ternary alphabet are open and actively pushed (verify the record).

**What counts as a win.** One explicit PFA (partial transition tables) whose shortest careful reset word (a word defined on all used states that maps the whole state set to one state, never leaving the domain) is longer than the tabulated best for its (n, k). One-sided: a longer example advances the frontier.

**Checker (seconds).** BFS over subsets of states under partial transitions, tracking only subsets on which the word so far is defined; report the shortest word bringing the full set to a singleton. Assert its length exceeds the recorded best. For n <= 20 the bitset subset search is fast; partiality only prunes transitions.

**Search plan.** Structured: extend Martyugin's and Gonze-Jungers-style constructions of slowly carefully-synchronizing PFAs; SAT/ILP encoding "no careful reset word shorter than L" to certify a long shortest word for a fixed candidate; local search perturbing near-extremal PFAs.

**Prior art (verify).** Martyugin, "Careful synchronization of partial automata" and reset-threshold bounds; Gonze, Jungers on synchronization of PFAs; the reset-threshold results list (arXiv 2508.15655, 2025). Verify best-known careful reset length at the target (n, k).
