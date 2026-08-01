# Counterexample to an open log-concavity or unimodality claim

**Refute.** A specific open conjecture that a combinatorially defined integer sequence is log-concave or unimodal: exhibit an instance whose sequence has an internal dip (a_k^2 < a_{k-1} a_{k+1} for log-concavity, or a strict interior valley for unimodality).

**What counts as a win (one-sided).** One explicit sequence (from the combinatorial data) violating the claimed inequality at a specific index. A single violation refutes the conjecture; failure proves nothing.

**Checker (seconds).** Compute the sequence exactly for the flagged instance and test the log-concavity inequalities a_k^2 >= a_{k-1} a_{k+1} (or unimodality) at every interior index; report the first failing k. Exact big-integer arithmetic; constant work per index.

**Search plan.** Enumerate the defining objects (partitions, posets, polytope f-/h-vectors, lattice-path families) and compute the sequences for many instances; screen for the first violated inequality; batch over parameter ranges. Evolutionary search over the objects scored by the most negative log-concavity gap.

**Prior art (verify).** Numerous log-concavity and unimodality conjectures remain open (and some were refuted by small counterexamples). See Richard Stanley, "Log-concave and unimodal sequences in algebra, combinatorics, and geometry" (ca. 1989), and Braenden's survey (ca. 2015) for open cases. Select a currently open sequence family and confirm its status (verify).
