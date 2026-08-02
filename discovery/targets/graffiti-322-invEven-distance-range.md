# Target card: Graffiti 322 (triangle-free InvEven vs distance-eigenvalue range)

**Status: needs-status + needs-edge. NOT ready for deep compute.** Captured as a real
lead from a genuine scout; the gate assessment below is honest.

```yaml
id: graffiti-322-invEven-le-distance-range
result_class: B2                      # refute a currently-open Graffiti conjecture
statement: >-
  If G is triangle-free then InvEven(G) <= range of the eigenvalues of the distance
  matrix D(G). InvEven(G) = sum_v 1/Ev(v), where Ev(v) = number of vertices at even
  distance from v. "range" here is the Aouchiche-Hansen definition (number of DISTINCT
  eigenvalues of D(G)). NOTE: under the ordinary range (max - min eigenvalue) the
  conjecture is already refuted by C_4 (InvEven(C_4)=4 > range approx 1.70); the AH
  distinct-values version is the one reported as still open.
source:
  primary_locator: >-
    Roucairol & Cazenave, "Refutation of Spectral Graph Theory Conjectures with Search
    Algorithms", arXiv:2409.18626, Sep 2024, Section 5.2. Original conjecture 322 in
    Fajtlowicz "Written on the Wall" (Graffiti); a copy is on the authors' repo
    github.com/RoucairolMilo/refutationExperimentalMathematics.
  access_date: 2026-08-02
  status_evidence: >-
    Paper states 322 is open under the AH range definition and their search battery could
    not refute it. NOT independently confirmed against a live tracker; the "range" and
    "InvEven" definitions differ across sources and MUST be pinned from Written on the Wall.
baseline:
  current_value_or_range: no known counterexample under the AH-range definition
  replay_command: enumerate triangle-free graphs to n<=10, compute InvEven and distinct
    distance eigenvalues, confirm the inequality holds (calibrate the checker)
witness:
  format: a triangle-free graph on n vertices (graph6) with InvEven(G) > range_AH(D(G))
  checker_command: build D(G); high-precision eigenvalues; count distinct (AH range) with
    a clustering tolerance stated explicitly; compute InvEven; check violation
  calibration_cases: C_4 (refutes the ordinary-range version); small triangle-free graphs
    as negatives; a graph with many-distinct distance eigenvalues
search_edge: >-
  WEAK. Roucairol-Cazenave's MCTS/GBFS/NRPA battery (15-min budgets) could not refute it
  under AH-range. A real edge would be EXHAUSTIVE enumeration of triangle-free graphs to
  larger n (they searched, not enumerated) plus targeted structured families (long cycles,
  bipartite incidence graphs, triangle-free-process outputs) chosen to maximize distinct
  distance eigenvalues while keeping InvEven high. Until one of these is shown to beat their
  search on calibration, this gate is RED.
budget: preflight enumeration to n<=11 (workstation), then a fixed structured-family sweep
stop_rules: if exhaustive n<=11 and the structured families all satisfy it, mark low-
  reachability and stop; if the AH-range definition turns out to make it trivially true or
  already-refuted, close as definition artifact
publication_path: Roucairol & Cazenave (authors); the Graffiti/Written-on-the-Wall maintainers
aliases: []
```

## Gate assessment (honest)

1. statement pinned - PARTIAL (exact InvEven/range definitions must come from Written on the Wall).
2. source pinned - YES.
3. open status fresh - PARTIAL (paper says open under AH-range; not tracker-confirmed).
4. artifact grammar - YES (triangle-free graph, graph6).
5. checker first - buildable (distance matrix eigenvalues + InvEven), but the "distinct
   eigenvalues" count needs a stated numerical tolerance.
6. baseline reproduces - trivially (no counterexample known).
7. **search edge - RED.** Their search already tried; no stated edge yet.
8. budget/stop - drafted.
9. publication path - YES.

**Verdict: not ready.** Two obligations before deep compute: (a) fetch Written on the Wall
from the authors' repo and pin the EXACT statement + range/InvEven definitions; (b) state a
concrete method edge over their search (exhaustive enumeration to larger n, or a structured
family argument) and show it beats their result on calibration.

## Scout note

This is the honest yield of one real scout pass over a refutation paper: its clean small-
witness refutations are already taken (197 refuted; the previously-refuted 12 reproduced),
and the survivors need a genuinely different method than the authors' search. The durable
lead is the survivor list in Written on the Wall (~1000 Graffiti conjectures, many with
open/ambiguous status) - a scout should fetch it and pin the still-open, definition-clean
ones, not re-run the search the authors already ran.
