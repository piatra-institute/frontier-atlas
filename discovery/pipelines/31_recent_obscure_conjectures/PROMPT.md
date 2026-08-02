# Batch sweep: refute recent, obscure, unwatched conjectures

**Mode:** one ChatGPT Pro session, web search + code sandbox, batch throughput.
**Goal:** an explicit small witness refuting a stated conjecture from a recent,
low-traffic paper - a real open-problem result. Or a list of tested conjectures that
survived.

**Why this target.** Two prior runs taught the lesson: settled classes (classical
Zagreb) only reproduce, and popular conjecture systems (TxGraffiti) are actively
refuted by a watching community within months. The winnable claims are **open AND
unwatched**: conjectures stated in individual recent papers that nobody has followed
up on, in low-traffic corners.

## Sourcing (the hard, high-value part)

Search arXiv (math.CO, math.MG, cs.DM, math.NT, math.GR, quant-ph) and journals for
papers from the **last ~18 months** that STATE a conjecture, "we ask whether", "it
would be interesting to determine if", or "we conjecture that", where the potential
counterexample is a **small finite object** (a graph, matrix, set, polytope,
sequence, code, configuration). Prefer papers with **few citations and no visible
follow-up** - obscure is the point. Explicitly avoid: famous named conjectures,
TxGraffiti / Graffiti / AutoGraphiX outputs (watched), and settled classical
inequalities. Harvest 20-60 such conjectures with exact statements.

For each, record: exact statement, author + paper (name it; no fabricated IDs), the
witness type, and a cheap exact checker. Confirm no follow-up already resolved it
(search); if you cannot confirm openness, mark "(verify)".

## Attack

For each conjecture build the checker and search for a counterexample: exhaustive
small-case enumeration (nauty, exhaustive), SAT/ILP, structured/extremal families,
or evolutionary construction. A single witness that the checker validates refutes it.

## What counts

- **Refutation:** an explicit small object, re-verified by an independently written
  checker, violating a conjecture confirmed to be currently open. This is a result.
- **Survivor:** the conjecture held over the search; report the range covered.
- NOT a result: refuting your own fitted guess, refuting an already-resolved
  conjecture, or a witness that isn't cheaply checkable.

## Discipline

Generator is not verifier: recompute any witness's violation with a second,
independent implementation. No fabricated citations - name the paper and quote the
exact conjecture. Confirm openness before claiming a refutation is new. Report the
denominator: conjectures harvested / confirmed-open / tested / refuted / survived,
with witnesses in a canonical encoding.

## Honest framing

Most conjectures are true, so expect mostly survivors and the occasional dud. But an
obscure recent conjecture is the one place a small witness can still be found before
anyone else looks - a refutation here is a genuine, citable open-problem result.
