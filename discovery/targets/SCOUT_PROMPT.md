# Scout session: produce pinned target cards (do NOT attack)

**Mode:** one ChatGPT Pro session, web search heavy. This is Stage 0 (scout), separate
from any deep attack. You will NOT search for witnesses. You will find, pin, and
status-check candidate open problems and write target cards.

Read `../../TARGET_CARD_TEMPLATE.md` first: the card schema, the 9 admission gates, the
priority scorecard, and result classes B0-B4. Every card you write must follow it.

## What to find

Currently-open claims settled by a **small explicit object**. Two lanes, both wanted; label
every card with its lane.

- **Lane A (toolchain).** The object's certificate is a seconds-long machine check: a
  counterexample, an existence witness, a beaten loose record. Our SAT/CP-SAT/enumeration
  stack attacks these directly.
- **Lane B (composition).** The object is small but its certificate is a proof: "here is the
  group/algebra/construction, and here is why it has the property." Attacked by literature
  composition and formalization, not by search.

A cheap checker is a **lane label, not a value filter**. It says which of our methods applies;
it says nothing about whether the problem is reachable or worth doing. Evidence: the
2026-08-02 scout screened 43 candidates and admitted 1 on cheap-checkability, and that one
(signed circulants) simply proved true through n=24. Meanwhile the strongest AI math result of
2026-08 (non-sofic groups) is Lane B and would have failed admission gate 5 outright. Do not
discard a target because its certificate is a proof; label it Lane B and pin it anyway.

**Lane B is the higher-yield lane. Weight the shortlist toward it.** Both AI-assisted advances
recorded in `../../FRONTIER_LOG.md` for late 2026-07 and early 2026-08 are Lane B. Lin-Li
(arXiv:2607.27199, sumset/difference-set exponent) is the sharper case: eight published agent
systems, AlphaEvolve included, ground out values of 1.079-1.145 by enumerating explicit integer
sets in Python, and the true answer was 2, realized by sets of size about `10^143`. Enumeration
could not have reached it at any budget. The theorem came from relaxing the enumerable-witness
evaluator and letting the agent propose constructions and arguments in natural language.

**Ask the size question before admitting a Lane A card.** State on the card what size the
extremal or witnessing object plausibly has, and why. If the honest answer is "unbounded" or
"far beyond enumeration", the target is Lane B or not a target; do not admit it as Lane A because
the checker is easy to write. A cheap checker on a search space that cannot contain the answer
produces a plateau, not a result.

**Pin the incumbent record yourself.** AlphaEvolve reported 1.1219 against a 1973 baseline of
1.0598 while a 2013 human construction (Penman-Wells) stood at 1.1259 under the same
normalization. Never take a baseline from the paper or system that is claiming to beat it: find
the current best independently, and if you cannot, mark the card `needs-status`.

Prefer sources **recent (roughly 6-24 months) with little follow-up**, mature enough to have a
precise statement and an author who cares, but not ground down by years of negative search.

Sources to mine (cite exactly; no fabricated arXiv IDs/DOIs):
- **freshly published technical criteria, applied to object classes their authors did not
  test** (the fast-follower lane, highest priority). A criterion published in the last ~6
  months whose stated applications are few is an opening: enumerate object classes, ideally
  from a DIFFERENT field, that plausibly satisfy it. Worked example: Fournier-Facio
  (arXiv:2608.02025, 2026-08-03) took the two-day-old non-soficity criterion from OpenAI's
  Leavitt-algebra construction and produced torsion-free non-sofic groups. This is
  reachable at small budget because the hard machinery is already public;
- specific **extremal / index-conjecture papers** that state "we conjecture the extremal
  graph/object is X" - obscure, small-witness, and a wrong extremal guess is a finite
  counterexample;
- **surviving conjectures inside recent computational-refutation papers** - a conjecture
  the authors STATED but their search did NOT break is a search-edge opening if you bring
  a different representation or method;
- maintained registries with EXPLICIT unresolved finite cells (TPDB nontermination,
  specific automata/state-complexity cells, difference-set / covering-design tables) -
  fetch the exact open cell and its current status;
- recent arXiv (math.CO, math.MG, cs.DM, math.NT, math.GR, quant-ph) papers that state
  "we conjecture", "we ask whether", where a counterexample is a finite object;
- recent real-rootedness / log-concavity conjectures on specific polynomial families;
- a recent preprint stuck on a small finite lemma (for the proof-obligation lane).

Explicitly avoid: **machine-generated conjecture outputs** (TxGraffiti/Graffiti/AutoGraphiX)
- they are fitted on a database of small graphs, so by construction they hold there and any
counterexample must be large, which is incumbent search territory; settled classical
inequalities; hardened numeric records; and **curated research-workshop problem lists**
(e.g. Barbados) - a scout pass found these dominated by asymptotic/structural conjectures
that need proofs, not small witnesses.

**Do NOT blanket-avoid famous problems.** Evidence (2026-08-01/03, non-sofic groups): a
roughly 25-year Gromov-Weiss problem, heavily watched, fell anyway. It fell because the
community's candidate objects (Higman's group, non-residually-finite central extensions of
higher-rank lattices, HNN extensions) were the wrong region, and the answer came from unit
groups of Leavitt algebras. Fame is not the disqualifier; a narrow, well-swept construction
space is. Reject a famous problem only when you can say what the candidate-object space is
and why it is exhausted. Where a famous problem has a wide construction space and the
community's search has concentrated on a few families, say so on the card: that concentration
is the search edge.

## For each candidate, write a target card

`<canonical-id>.md` in this directory, filled per the template. Run the 9 admission
gates and mark each green/red with evidence. Critically:
- **Statement pinned** - exact quantifiers, domain, success condition, quoted from source.
- **Source pinned** - paper/table locator + theorem/row + access date.
- **Open status fresh** - search for follow-up resolutions; if you cannot confirm it is
  still open, mark the card `needs-status`, not `ready`.
- **Lane** - `lane-A` (machine-checkable certificate) or `lane-B` (proof-shaped certificate).
- **Checker specified** - Lane A: the exact seconds-long check, plus one positive and one
  near-miss negative calibration case. Lane B: state instead what a correct proof would have
  to establish, what is already public that it could compose, and how the claim would be
  checked (formalization target, or the specialist who could referee it). Gate 5 is satisfied
  for Lane B by a stated verification route, not by a script.
- **Baseline** - the current best/known range and how to replay it cheaply.
- **Search edge** - state what representation, symmetry, tool, data, or model capability
  would beat prior attempts. If you cannot state one, the card is `needs-edge`, not ready.
- **Publication path** - the author, maintainer, or venue that would absorb a result.

## Output

- 10-20 target cards.
- A ranked shortlist (`SHORTLIST.md`) scoring each on the 8 scorecard dimensions (0-5,
  keep the vector, no single total), with a one-line reachability and search-edge note.
- Honest labels: the lane (`lane-A`/`lane-B`), and which cards pass ALL gates (`ready`) versus
  `needs-status` or `needs-edge`. Report how many candidates you screened and rejected, and why.
  Do not let Lane A dominate the shortlist merely because its cards are easier to make green.

## Discipline

No fabricated citations. Do not claim openness you did not check. Do not attack the
targets - scouting only. A card that cannot state its search edge is not a research
target yet; say so.
