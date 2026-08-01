# Discovery: the winnable atlas

191 tasks selected on the solvability signature (small explicit witness, cheap exact
checker, under-tested, plausibly open or false, one-sided). This is the rebuilt
center of the atlas: where a win is actually reachable at session scale, unlike the
legacy record/proof/reality-gated bank. Every task was generated with grounded
citations (named tables and databases, no fabricated arXiv IDs) and honest
`(verify)` flags where openness needs a live re-check.

## Composition

| set | count | shape | index |
|---|---:|---|---|
| `pipelines/` | 30 (+1 seed) | batch refutation over a class; one session tests hundreds of claims | [INDEX](pipelines/INDEX.md) |
| `graph_conjectures/` | 1 | the seed pipeline (generic graph-invariant inequalities) | - |
| `hunts/combinatorics/` | 45 | find an object / refute a claim: SRGs, designs, cages, coverings, snakes | [INDEX](hunts/combinatorics/INDEX.md) |
| `hunts/tcs/` | 45 | Life objects, cellular automata, octal games, Boolean functions, automata | [INDEX](hunts/tcs/INDEX.md) |
| `hunts/numbergeom/` | 45 | Sidon/Costas/difference sets, Casas-Alvero-style refutations, polytope counterexamples | [INDEX](hunts/numbergeom/INDEX.md) |
| `hunts/quantum/` | 25 | MUB/AME/SIC existence, QECC cells, Bell/KS witnesses (exact linear algebra) | [INDEX](hunts/quantum/INDEX.md) |

## Two ways to work

- **Pipeline (throughput).** Paste one `pipelines/NN/PROMPT.md` into a ChatGPT Pro
  session; it generates many candidate claims, adversarially breaks them in its
  sandbox, and returns refutations plus survivors. One session = hundreds of shots.
- **Hunt (single witness).** Attack one `hunts/.../NN/PROMPT.md`: search for the one
  object that settles it. A hit is checkable here in seconds.

Both run under `../SOLVER.md`: the searcher (ChatGPT Pro) proposes, a second system
(Claude Code) re-derives every claim, and every result ships a `CLAIM.md`, an
independent checker, a manifest, and the honest denominator.

## Honest tiering (read the per-category INDEX flags)

- **Primary (best odds):** the pipelines, especially chemical/topological-index and
  OEIS/degree-domination sweeps (hundreds of published bounds, many false, sub-10-vertex
  witnesses); and the under-tested hunts (open SRG parameter rows, coverings/packings,
  cages, snakes/coils).
- **Verify first:** many hunts carry `(verify)` because the exact open cell drifts
  (Brouwer/La Jolla/LifeWiki/Catagolue/codetables update). Re-confirm the target is
  still open before spending compute, per `../SOLVER.md`.
- **Long shots (lower odds, kept honestly):** record-beats that are strict one-sided
  improvements of a hardened best-known (e.g. superperm n=7, sorting n=13, MOLS-10,
  circulant Hadamard, sphere-packing dims). These are the old record trap; treat as
  low-probability upside, not expected wins. Each category INDEX flags them.

## Starting point

The single highest-yield first run is a pipeline: `pipelines/01_zagreb_degree_indices`
or the seed `graph_conjectures`. Enumerate small graphs, generate index inequalities,
break them against extremal families. If nothing false surfaces, the survivors are
candidate conjectures; if one breaks, that is a clean refutation, verified here.
