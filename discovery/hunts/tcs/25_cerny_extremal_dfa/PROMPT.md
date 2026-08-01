# 25. A new extremal synchronizing automaton meeting (n-1)^2

**Find.** A synchronizing deterministic finite automaton on n states (small n, e.g. 8 <= n <= 16) whose shortest reset word has length exactly (n-1)^2 and which is *not* isomorphic to Cerny's automaton or the other few known extremal families. The Cerny conjecture (reset threshold <= (n-1)^2) is open; extremal automata attaining the bound are extremely rare, and finding new ones for specific n is a documented, actively-searched question.

**What counts as a win.** One explicit DFA (n states, small alphabet) with shortest reset word length exactly (n-1)^2, shown non-isomorphic to the known extremal list. One-sided: a new extremal automaton is a result (and a counterexample above (n-1)^2, if it ever appeared, would refute the conjecture outright).

**Checker (seconds).** Compute the shortest reset word by BFS over the power-set of states under the transition monoid, from the full set toward singletons (bijective back-search): the level at which a singleton is first reached is the reset threshold. For n <= 20 the 2^n subset space is tractable in seconds with bitset states. Assert it equals (n-1)^2.

**Search plan.** Structured/exhaustive: orderly generation of small binary-alphabet automata with isomorph rejection, filtered to synchronizing, then reset-length computed; target the tight cells. Local search perturbing near-extremal automata. Compare hits against the tabulated extremal list.

**Prior art (verify).** Cerny (1964); Volkov survey "Synchronizing automata and the Cerny conjecture" (2008); "List of Results on the Cerny Conjecture and Reset Thresholds" (arXiv 2508.15655, 2025); Ananichev-Gusev-Volkov on slowly synchronizing series. Open.
