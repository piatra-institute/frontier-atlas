# Claim

One worked attempt's exact result, kept small and separate from the bulky proof or search output. Copy to `<domain>/<task>/<NN_attempt>/CLAIM.md` and fill in. This file is the audit surface: an auditor should learn exactly what is claimed, and how to check it, without reading the heavy artifacts.

**Claim.** The exact proposition proven or computed, stated precisely: a bound, an exact value, an obstruction, a construction, a nonexistence. No hedging words; if partial or restricted, say so here.

**Checker.** The command that binds this claim to the artifact, e.g. `verify.py cert.lrat` or `lean4checker`. Names the artifact and its hash. Pin checker/solver/toolchain versions so the check replays.

**Trust base.** What the claim rests on: axioms or oracles, exact vs floating-point, any unverified lemma or solver assumption. An auditor reads this to see the whole trust surface at a glance.

**Encoding fidelity.** Why the encoding or definition faithfully captures the stated problem (the fidelity risk lives here, not in the proof trace). Name the small auditable encoding artifact.

**Review level.** self | agent | human | community (see FRONTIER_LOG.md). Never label a result more reviewed than it is.

**Provenance.** Model and tools used; what the model produced vs what the checker confirmed.

**Cost and attempts.** Total model spend including failed runs and abandoned lines, the number of attempts behind this result, and any harness or compute beyond a single workstation. Report the denominator, not just the winning run.
