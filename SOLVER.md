# Solver protocol

Run every attempt under this. The prompt gives the problem; this gives the method.

**Stance.** This is an unsolved problem. A correct, verifiable new result - even a partial one (a new record, an exact value, an obstruction, a certified bound) - is a real contribution. Be ambitious; do not stop at the obvious. Persist, and pivot when a line stalls rather than grinding it.

**Method** (you already reason - do not narrate performative "step by step"; reason at the depth the problem needs):

1. Orient. Survey the landscape, state the prior art you rely on, pick an angle, name your plan.
2. Compute, do not just argue. Run the tools this prompt names (SAT/CAS/code); test every conjecture numerically first; let tool output correct you.
3. Adversarially self-verify. After any claim, try hard to break it: counterexamples, edge cases, independent re-derivation, run the verifier. Treat it as wrong until it survives. Formalize to attack, not only to confirm: a stalled Lean/Coq proof is a signal, and the obligation it cannot discharge can localize a counterexample. Mine failed proofs; do not just discard them.
4. Report honestly. State exactly what is and is not established. A certified partial result beats an unverified claim of the full one. Never dress a partial, restricted, or numerical result as the full resolution. No fabricated citations; flag every uncertainty.
5. Preserve the record. Keep source, seeds, and a SHA-256 manifest so the result replays (see ARTIFACTS.md).

**Re-verify first.** Prior art in the prompt is "as of mid-2026" and may be stale; confirm the problem is still open before investing.

**Reality-gated problems (chembiotics Pack B).** The verifier is empirical, so "verify" means a leakage-safe held-out evaluation plus calibrated, falsifiable predictions - never a proof, and never an in-silico metric presented as a real-world result.
