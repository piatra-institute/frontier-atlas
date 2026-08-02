# Scout log

Dated findings on where small-witness targets do and do not live. Record dead-end
genres here so they are not re-scouted. `targets/` holds only genuine candidate cards
(ideally `ready`); analysis and dead ends live here.

## Deprioritized genres (do not re-mine)

### Curated research-workshop problem lists - SKIP
- Checked: Open Problems for the 2025 Barbados Graph Theory Workshop (16 problems),
  2026-08-02.
- Finding: dominated by asymptotic / structural conjectures (tree-treewidth bounds,
  grid-minor polynomial dependence, chi-boundedness, clustered colouring, Hadwiger for
  graph classes, asymptotic dimension). These need proofs, not small witnesses. The one
  small-witness item (Seymour, weightable digraph forced planar) is actively watched by
  his group - no search edge.
- Lesson: workshop lists collect what working theorists care about, which is asymptotic.
  Wrong source for this method.

### Machine-generated / machine-fitted conjectures (Graffiti, TxGraffiti) - SKIP
- Checked: Roucairol & Cazenave, "Refutation of Spectral Graph Theory Conjectures with
  Search Algorithms", arXiv:2409.18626, Sep 2024 (Graffiti spectral conjectures); and the
  domination pipeline run (TxGraffiti conjectures), 2026-08-02.
- Finding: these conjectures are fitted on a database of small graphs, so BY CONSTRUCTION
  they hold on all small graphs. Therefore exhaustive small-enumeration (our natural edge)
  finds nothing, and any counterexample must be LARGE - which is exactly where the
  incumbents already search (MCTS/RL/GBFS). Roucairol-Cazenave ran a full search battery
  and cracked only one previously-open conjecture (Graffiti 197). TxGraffiti conjectures
  are additionally refuted fast by a watching community.
- The Graffiti 322 lead (triangle-free InvEven <= distance-eigenvalue range, open under the
  Aouchiche-Hansen range definition) lives here: not ready, no search edge, definition-
  tangled. Deprioritized.
- Lesson: doubly hard - small-enumeration can't help, large-search is incumbent territory.

## The one surviving genre to pursue

Obscure recent **human** extremal conjectures: "we conjecture the extremal graph/object is
X, proved for small cases, conjectured in general." The guess rests on intuition or a
partial proof, NOT a small-graph fit, so a medium-size counterexample is plausible and our
exact enumeration or a structured construction is a genuine edge. Scout these; pin the exact
statement, confirm open status, and state the concrete enumeration/construction edge before
any deep run.
