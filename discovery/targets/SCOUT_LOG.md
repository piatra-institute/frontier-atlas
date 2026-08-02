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

## Scout runs

### 2026-08-02 - ChatGPT Pro (GPT-5.6 Pro), bundle `scout_targets_2026-08-02/`
- Screened 43 claim-level candidates from 13 source families; rejected 26 (8 already
  resolved/refuted, 7 famous/watched/hardened, 5 no finite cheap witness, 3 unpinnable
  status, 3 no credible edge). Produced 17 target cards: **1 `ready`**, 3 `needs-status`,
  13 `needs-edge`. Self-validated bundle (schema + 9 gates + score vectors + checker hashes;
  114-entry SHA-256 manifest).
- Citation integrity (Claude Code spot-check, 3/3 real and faithful): arXiv:2607.18334
  (signed circulants, Suvagiya), 2607.20137 (triangle-free zero-forcing, Annor-Howerton),
  2510.01086 (inverse KL matroids, Braden-Ferroni-Matherne-Nepal). No fabricated IDs in the
  sample; the scout also correctly kept only the *surviving* open piece of 2510.01086 (whose
  main conjecture is already refuted by a rank-19 matroid in the same paper).
- Provenance note: ChatGPT's sandbox could not read our `TARGET_CARD_TEMPLATE.md` or
  `BREAKTHROUGH_STRATEGY.md`, so the copies inside the bundle are reconstructions. Do NOT
  overwrite the repo originals with them.
- Sole `ready` card: `signed-circulant-c2-global-spectral-minimum` (refute or extend
  Conjecture 3 of arXiv:2607.18334). Attacked same day, see
  `../attacks/signed_circulant_c2_spectral_min/2026-08-02-claude-code/`: independently
  re-derived the source's `n<=18` verification and extended the exhaustive check to n=24.
  Conjecture HOLDS at every order, no counterexample, still open. Result: B1 verification +
  finite-range extension, not a resolution. Honest caveat: gate 7 (search edge) was optimistic
  - the real method (a bandwidth-2 transfer recurrence) is not built; only a 34x symmetry
  constant was demonstrated, so brute force caps near n=26-28.
- Lesson: the scout succeeded (first well-formed, real, fresh target the project has
  produced), but "all gates green" is not "high counterexample odds." The signed-circulant
  passed the gates because its checker/baseline were trivial to stand up, not because the
  conjecture is likely false. Highest-EV targets for an actual refutation are the human
  extremal `needs-edge` cards (augmented-Sombor Turan, total 2-coalition degree bound), where
  a wrong extremal guess is a finite counterexample - those need a checker built before attack.
