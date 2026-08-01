# Batch sweep: refute digraph and tournament invariant conjectures

**Mode:** one ChatGPT Pro session, code sandbox, batch throughput.
**Goal:** an explicit digraph/tournament violating a stated bound, or hardened survivors. Refutation is the clean win.

**Family + panel.** Digraphs and tournaments; invariants: minimum out-degree δ+, directed girth, first- and second-out-neighbourhood sizes |N+(v)|, |N++(v)|, domination number, score sequence, feedback arc set, king count, and cycle counts.

**Enumerate.** All tournaments to n=8 via exhaustive orientation + isomorph rejection (count-check A000568: 1,1,2,4,12,56,456,6880 for n=1..8) and all digraphs to n=5 (A000273: 1,3,16,218,9608 for n=1..5). Larger tournaments sampled from structured families.

**Conjecture generation.** Anchor on named open statements: Seymour's second-neighbourhood conjecture (some v has |N++(v)| ≥ |N+(v)|; proven for tournaments, open for general digraphs); the Caccetta-Haggkvist conjecture (min out-degree ≥ n/r forces a cycle of length ≤ r; open); and Woodall's / Sumner's tournament conjectures. Auto-fit score-sequence and neighbourhood bounds on small cases.

**Adversarial families.** Rotational/circulant tournaments (quadratic-residue / Paley tournaments), transitive-plus-perturbation tournaments, blow-ups of small digraphs, and sparse digraphs with prescribed out-degree targeting Caccetta-Haggkvist thresholds.

**Checker (exact).** Recompute out-neighbourhoods, girth (shortest directed cycle by BFS), and score sequences directly from the arc set; verify each claimed extremal vertex by exhaustive neighbourhood counting. Emit violators as arc lists / adjacency matrices.

**Verification discipline.** Generator is not verifier: recompute all directed invariants with a second implementation; confirm tournament property (exactly one arc per pair) and re-check isomorph rejection in a second canonicalizer. Cite each conjecture, noting where it is proven for tournaments only. Report candidates generated / broken / survived, with explicit digraph witnesses.
