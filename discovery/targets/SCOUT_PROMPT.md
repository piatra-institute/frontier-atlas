# Scout session: produce pinned target cards (do NOT attack)

**Mode:** one ChatGPT Pro session, web search heavy. This is Stage 0 (scout), separate
from any deep attack. You will NOT search for witnesses. You will find, pin, and
status-check candidate open problems and write target cards.

Read `../../TARGET_CARD_TEMPLATE.md` first: the card schema, the 9 admission gates, the
priority scorecard, and result classes B0-B4. Every card you write must follow it.

## What to find

Explicit, finite, currently-open claims with a small cheap-to-check witness or lemma,
from **recent (roughly 6-24 months), low-traffic sources with little follow-up**. The
ideal target is mature enough to have a precise statement and an author who cares, but
not yet ground down by years of negative search.

Sources to mine (cite exactly; no fabricated arXiv IDs/DOIs):
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

Explicitly avoid: famous named conjectures; TxGraffiti/Graffiti/AutoGraphiX outputs
(watched, refuted fast); settled classical inequalities; hardened records; and **curated
research-workshop problem lists** (e.g. Barbados) - a scout pass found these are dominated
by asymptotic/structural conjectures that need proofs, not small witnesses.

## For each candidate, write a target card

`<canonical-id>.md` in this directory, filled per the template. Run the 9 admission
gates and mark each green/red with evidence. Critically:
- **Statement pinned** - exact quantifiers, domain, success condition, quoted from source.
- **Source pinned** - paper/table locator + theorem/row + access date.
- **Open status fresh** - search for follow-up resolutions; if you cannot confirm it is
  still open, mark the card `needs-status`, not `ready`.
- **Checker specified** - the exact seconds-long check, and one positive + one near-miss
  negative calibration case.
- **Baseline** - the current best/known range and how to replay it cheaply.
- **Search edge** - state what representation, symmetry, tool, data, or model capability
  would beat prior attempts. If you cannot state one, the card is `needs-edge`, not ready.
- **Publication path** - the author, maintainer, or venue that would absorb a result.

## Output

- 10-20 target cards.
- A ranked shortlist (`SHORTLIST.md`) scoring each on the 8 scorecard dimensions (0-5,
  keep the vector, no single total), with a one-line reachability and search-edge note.
- Honest labels: which cards pass ALL gates (`ready`), which are `needs-status` or
  `needs-edge`. Report how many candidates you screened and rejected, and why.

## Discipline

No fabricated citations. Do not claim openness you did not check. Do not attack the
targets - scouting only. A card that cannot state its search edge is not a research
target yet; say so.
