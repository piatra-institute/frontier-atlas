# Batch sweep: generate and adversarially refute graph-invariant conjectures

**Mode:** one ChatGPT Pro session, code sandbox, batch throughput (not one problem).
**Goal:** produce EITHER a refutation of a stated invariant inequality (an explicit
counterexample graph) OR a small set of novel, computationally-supported, unproven
inequalities among graph invariants that survive exhaustive small-graph testing and
adversarial families. Both are real outputs; the refutation is the cleaner win.

This is the TxGraffiti / Graffiti / Conjecturing paradigm run inside one sandbox.
Most guessed inequalities are true or trivial; the value is in volume plus cheap
failure. Test hundreds, keep the few that matter.

## Method

1. **Enumerate.** Generate all connected graphs up to n = 9 vertices (n = 10 if time
   allows) with nauty `geng` (install it, or use an equivalent non-isomorphic
   generator; `networkx` graph atlas covers n <= 7). Sanity-check the counts against
   the known number of connected graphs A001349: n=1..10 = 1, 1, 2, 6, 21, 112, 853,
   11117, 261080, 11716571. If your counts differ, your enumeration is wrong; stop
   and fix it.

2. **Compute an invariant panel** for every graph. At least: order n, size m, min and
   max degree, independence number alpha, clique number omega, chromatic number chi,
   domination number gamma, total domination, matching number, vertex and edge
   connectivity, diameter, radius, girth, number of triangles, spectral radius
   lambda1, algebraic connectivity, graph energy, Randic index, first and second
   Zagreb indices. Use exact integer/rational or high-precision values; note where a
   value is only numerical (spectral).

3. **Generate candidate inequalities** on a SMALL sample (n <= 7): for pairs and small
   triples of invariants, fit the tightest linear or simple ratio bound that holds on
   the whole sample (upper and lower). This is the conjecture step; you will produce
   many candidates, most over-fit.

4. **Adversarially refute** each candidate on a LARGER test set: all connected graphs
   up to n = 9 or 10, PLUS structured families that break naive bounds: complete
   graphs, complete bipartite and Turan graphs, cycles, paths, trees, hypercubes,
   Kneser and Johnson graphs, cocktail-party graphs, random regular graphs, line
   graphs, and Cartesian/tensor products of small graphs (push these to hundreds of
   vertices, since invariants are cheap). Any graph violating a candidate is a
   counterexample; record it in graph6 and discard the candidate.

5. **Filter survivors for novelty and non-triviality.** Discard bounds that are
   immediate (e.g. alpha <= n), that follow from one textbook inequality, or that you
   can identify in the literature. Do NOT claim novelty you cannot support; when
   unsure, label a survivor "novel-looking, not verified against literature." Flag any
   survivor that is tight (has equality cases) and relates invariants not usually
   bounded against each other.

6. **Attempt to prove** the single strongest survivor, or to break it harder with a
   targeted construction. A proved survivor is a theorem; a broken one is discarded.

## What counts / does not count

- A **refutation**: an explicit graph (graph6) violating a clearly stated inequality,
  re-verified by recomputing the invariants independently. This is a result.
- A **survivor**: a stated inequality, its equality cases, support statistics (how many
  graphs tested, over what n and families), and an honest novelty assessment. Valuable
  only if non-trivial and not already known.
- NOT a result: a bound that is trivial, already published, or holds only on the small
  sample you fit it on.

## Verification discipline (required)

- Generator is not verifier: any reported counterexample or survivor must have its
  invariants recomputed by a SECOND, independently written function (ideally a second
  library or a from-scratch implementation), and the two must agree.
- Enumeration counts must match A001349 (above).
- No fabricated citations. If you assert a bound is known, name the source; if you
  cannot, say "could not verify against literature."
- Report the denominator: how many candidate inequalities were generated, how many
  broken, how many survived, and total sandbox time.

## Deliverables (zip)

- `CLAIM.md`: the exact statement(s) claimed - each refutation (inequality + graph6
  witness) and each survivor (inequality + support + novelty status), with the trust
  base and the denominator.
- `invariants.py` (+ the independent recompute) and the enumeration/generation code.
- `candidates.csv` (all generated bounds), `refuted.csv` (broken + witness graph6),
  `survivors.md` (kept bounds with support and equality cases).
- `verify.py`: re-checks every reported refutation and survivor from graph6 inputs.
- `MANIFEST.sha256` and a `REPRODUCE.md` with the toolchain.

## Honest framing

Expect most sessions to yield only survivors (candidate conjectures), not a headline
refutation, because most stated bounds are true. That is fine: a strong, novel,
computationally-hardened conjecture is a genuine contribution, and a clean refutation
of any stated bound is a clean win. Report exactly what happened, including "nothing
non-trivial survived" if that is the truth.
