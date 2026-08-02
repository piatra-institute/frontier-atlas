# From Frontier Atlas to a Breakthrough Engine

**Deep critique and operating plan, based on the repository as of 2026-08-02**

## Executive judgment

Frontier Atlas is already a credible **verification workbench**. It is not yet a
credible **breakthrough-production system**.

Its strongest ideas are correct and unusually well enforced: generators must not
verify themselves, claims should be small, encodings must be auditable, exact
artifacts beat persuasive prose, failed searches must not be dressed as proofs, and
the denominator matters. The recent attempt packages show that this discipline can
catch overclaims and produce trustworthy reproductions.

The central weakness is one layer earlier. The atlas is much more rigorous about
checking an answer than about deciding **which question to spend a session on, why
the search should reach its answer, and what evidence should cause the portfolio to
continue, pivot, or stop**. A cheap checker makes a result easy to validate; it does
not make the result easy to find. That distinction is the main unresolved problem in
the repository.

The atlas should therefore stop growing as a catalog of prompts and become a
measured research funnel:

```text
live primary-source scouting
    -> pinned open statement
    -> executable target card and prewritten checker
    -> cheap calibrated probe
    -> measured search response
    -> selective deep attack
    -> blind independent verification
    -> novelty/statement-match review
    -> expert contact and publication
```

The breakthrough thesis should be:

> Find neglected claims for which this team has a specific search advantage, not
> merely claims for which a hypothetical answer would be easy to check.

That change preserves the best parts of [SOLVER.md](SOLVER.md) while correcting the
selection and execution failures visible in the runs so far.

## Scope and evidence

This is a repository audit, not an independent literature-status audit. It draws on
the local task descriptions, run artifacts, manifests, claims, strategy files, and
frontier log. Any recommendation to attack a scientific claim still requires the
live primary-source check mandated by `SOLVER.md`.

The local evidence is already strong enough to support a strategic change:

| Observation | Repository evidence | Implication |
|---|---|---|
| The legacy bank contains 200 tasks, but only 38 are tagged witness-shaped | [TRIAGE.md](TRIAGE.md) | The project has correctly rejected indiscriminate attacks on famous problems. |
| The discovery tree actually contains 192 prompts: 31 numbered pipelines, one seed, and 160 hunts | local file audit; the READMEs still say 191 | Inventory is growing faster than its control plane. |
| Only two discovery pipelines have recorded runs | Zagreb and domination attempt folders | “Throughput” is still an aspiration, not a measured capability. |
| Both discovery runs produced zero new open-problem results | the Zagreb reproduction and the domination `CLAIM.md` | Cheap exhaustive testing alone has not supplied target quality. |
| Five recent T2 targets produced reproductions and zero new records | [README.md](README.md) and their `CLAIM.md` files | Hardened records are correctly being demoted. |
| Nine original mathematics targets were worked; all are listed as partial | [mathematics/README.md](mathematics/README.md) | “Certified partial result per session” is achievable, but is not evidence of breakthrough probability. |
| Only eight `CLAIM.md` files and one `NEXT_STEPS.md` exist in the whole tree | local file audit | The attempt lifecycle is not uniformly represented or resumable. |
| Of 192 discovery prompts, 188 mention verification, but only 10 contain an executable-looking command and only 7 contain a URL or explicit arXiv identifier | conservative static audit | The prompts describe research areas more often than executable, source-pinned experiments. |
| The repository has no root-level CI or audit workflow | local file audit | The verification doctrine is manual and can silently decay. |

At least sixteen attacked targets are visible in the repository when the nine
original worked mathematics targets, five recent T2 targets, and two discovery runs
are counted. None claims a frontier breakthrough. That is not a condemnation: the
sample is small, the reporting is honest, and many useful technical artifacts were
created. But it is enough to reject the implicit model that more task prompts plus
more model sessions will mechanically produce a major discovery.

## What is genuinely strong

The critique should not erase the project's real assets.

### 1. The epistemic standards are unusually good

[CLAIM_TEMPLATE.md](CLAIM_TEMPLATE.md) asks for the exact proposition, checker,
trust base, encoding fidelity, review level, provenance, and full cost denominator.
This is the right audit surface. The best packages, especially the cap-set,
bilinear-rank, and covering-array work, separate heuristic discovery from exact
verification and clearly label known reproductions.

### 2. Failures are reported as failures

The domination run states “No new result,” the superpermutation package says that
873 does not reach the known 872 construction, and the covering-array search records
a five-interaction plateau without turning it into a nonexistence claim. This is a
major advantage over research workflows that optimize for an attractive narrative.

### 3. Encoding fidelity is recognized as the fragile layer

The repository understands that a perfect SAT proof can certify the wrong model.
That insight in `SOLVER.md` and `CLAIM_TEMPLATE.md` is more important than adding a
third solver. It should be made operational, not weakened.

### 4. The project can build exact computational machinery quickly

The attempts produced exact graph enumeration, finite-field tensor checks,
DRAT-checked calibration, independent covering-array reductions, exhaustive
small-instance tests, and SHA-256 manifests. The technical execution capacity is
real. The strategic goal is to point it at targets where that capacity is scarce.

### 5. The repository learns, but informally

The first discovery run established that sweeping settled graph-index inequalities
can only reproduce. The second established that a “live” machine-generated list may
already be mostly resolved by the time a session begins. Pipeline 31, recent obscure
conjectures, is an intelligent response. The problem is that these lessons live in
prose and have not yet changed the portfolio machinery.

## The central category error: verification cost is not discovery distance

The current T1/T2/T3 classification is useful but too coarse. It treats witness
shape as a proxy for tractability:

- a witness exists;
- the witness is finite;
- the checker runs in seconds;
- therefore a model-plus-workstation attack is “winnable.”

Only the third conclusion follows. A 69-vertex strongly regular graph, a fourth MUB
in dimension 6, an APN permutation in dimension 8, a Moore graph of degree 57, and a
small Life object can all be checked cheaply once found. Their search spaces,
community hardening, and structural obstructions are radically different.

The atlas needs at least four separate notions:

1. **Certificate complexity:** how hard is it to check a candidate?
2. **Search entropy:** how much effective space remains after known structure and
   symmetry reduction?
3. **Claim survival:** how likely is the target both open and false/constructible?
4. **Method advantage:** why should this workflow beat prior searches on this target?

The existing `W` tag measures mostly the first. Major discovery depends primarily
on the other three.

This explains the observed results. Covering arrays, superpermutations, cap sets,
and bilinear rank all have excellent checkers. They still did not move because
specialist communities have already pushed the accessible search frontier. The
same danger applies to several T1 entries. “One witness settles it” and “a witness
is reachable in this budget” are not synonyms.

## Deep critique of the current system

### 1. The triage is a hand-coded taxonomy, not a calibrated prediction

[tools/triage.py](tools/triage.py) is transparent, which is good, but every tag is a
static manual assignment. It has no fields for status date, known search scale,
previous compute, falsehood prior, competing teams, solver advantage, estimated
branching factor, or evidence from atlas attempts.

It also contains questionable semantic assignments. “Existence” in many-body
localization, self-correcting memory, or a continuum physics conjecture is not
necessarily certified by one small finite object. Conversely, a proof-shaped task
may contain a narrow finite lemma that is ideal for an AI/formalization attack.

The classification should remain as a description of answer shape, but it should no
longer determine priority by itself.

### 2. Most discovery tasks are topics, not pinned experiments

Many hunt prompts say “choose an open cell,” “pick a currently open family,” or
“verify the target.” That is appropriate in an ideation document but not in the unit
handed to an expensive research session. The model must first do target discovery,
literature review, status verification, encoding design, tool installation, baseline
reproduction, and only then begin research. A 90-minute session can be consumed
before the scientific search starts.

The domination run demonstrates this failure exactly. It spent valuable effort
learning that most advertised TxGraffiti targets had already moved, that another
had a public but inaccessible counterexample claim, and that only a small remainder
was apparently open. That status audit was useful, but it should have been a cheap
preflight completed before a deep run.

Every expensive attempt should begin with one exact statement and one exact target
instance. “Find which problem is still open” must be a different pipeline.

### 3. Prompt count creates a false sense of throughput

The discovery README advertises a volume strategy, but 192 prompts are not 192
searchable targets. They include overlaps such as Costas order 32 in three
categories, perfect one-factorization in two, MOLS-10 in multiple locations, sparse
rulers in two, and related snake/coil tasks in several. Overlap can be useful when
methods differ, but there is no canonical target ID connecting the aliases, shared
status, attempts, or total cost.

The documentation already drifts: the tree has pipeline 31, while the root and
discovery READMEs count only 30 numbered pipelines and 191 total tasks. This is
minor editorially but important diagnostically. The project lacks a generated
inventory and a single source of truth.

### 4. “Open” and “unwatched” are treated as annotations instead of resources

Novelty is a load-bearing part of a breakthrough. Yet the repository stores mostly
named sources and `(verify)` prose, not a dated evidence bundle:

- the exact theorem or conjecture text;
- a primary-source locator and page/theorem number;
- the latest known status and access date;
- searches for follow-up papers;
- the best known construction or verified range;
- ideally, confirmation from the author or relevant maintainer for ambiguous cases.

The first two discovery runs show that openness has a shorter half-life than the
prompts. It should be represented as expiring data. A target whose status evidence
is older than a set window should automatically become ineligible for a deep run.

### 5. The portfolio has no expected-value model

The pipeline index uses qualitative “high/med/low richness,” but these values are not
updated from observed conversion. Pipeline 09 remains recommended as a starting
point even after its run found no open refutation and exposed severe target drift.
Freshness, obscurity, witness size, and publication value are discussed, but they
are not combined into a decision rule.

A useful priority estimate is not “importance” and not “checkability.” It is:

```text
expected value per unit cost
  ~= P(still open)
     x P(reachable witness or lemma | open, method, budget)
     x scientific value if successful
     x P(statement match and external acceptance)
     / end-to-end cost
```

The numbers can be coarse ordinal estimates. The discipline of decomposing the
probability is more important than false numerical precision.

### 6. Reproduction is too often the session, rather than the admission test

Reproducing the baseline is necessary. It validates definitions, code, and toolchain.
But it should usually be time-boxed preflight work performed by a reusable harness.
The recent attempts often devoted most of a session to rediscovering a known value,
then had only a weak generic heuristic left for the live frontier.

A target should not enter a deep queue until its baseline replays cheaply. If
baseline reproduction itself is difficult, that is an infrastructure task with its
own deliverable, not yet a breakthrough attempt.

### 7. Search repetitions are not a research program without a mechanism

The covering-array result is especially informative: two searches reach the same
five-uncovered-interaction floor. The next useful move is not “more restarts.” It is
to explain that plateau:

- Which interactions remain together?
- Are they invariant under a symmetry or local move?
- Does an LP dual, unsat core, or hitting-set structure expose an obstruction?
- Can the move set be expanded specifically to cross it?
- Does a smaller calibrated instance exhibit the same trap?

Major breakthroughs usually come from a new representation, reduction, symmetry,
lemma, or move operator. Compute should reveal the obstruction and then change the
method. It should not merely scale a search whose response curve is flat.

### 8. The exclusion of analytic work is an overcorrection

Five failed T2 record attempts support demoting hardened records. They do not show
that all proof-shaped work is out of scope. In fact, [FRONTIER_LOG.md](FRONTIER_LOG.md)
records recent AI-assisted asymptotic and proof advances, and describes proof-failure
localization as part of the Ziegler counterexample story.

The right alternative is not to attack grand T3 statements head-on. It is to create
a second lane for **small, formalizable, load-bearing lemmas**:

- a proof obligation on which a recent preprint is stuck;
- a finite reduction that removes a major case;
- a symbolic identity that collapses a parameter family;
- an unsat core that suggests the missing structural lemma;
- a Lean formalization failure that localizes an incorrect assumption;
- a theorem strengthening suggested by exhaustive data and short enough for expert
  review.

Witness search and lemma search should reinforce one another. A failed proof can
generate a counterexample search; a failed witness search can generate a structural
lemma.

### 9. The verifier is independent more often in principle than in packaging

The manifests checked during this audit are internally consistent. That is good.
The repository-wide packaging contract is nevertheless uneven:

- only eight claim files exist;
- three omit an explicit encoding-fidelity section;
- the Zagreb discovery run has no run-level `CLAIM.md`;
- several run folders omit the exact prompt copy;
- the domination run preserves second-method result tables but not the independent
  implementation that produced them;
- only one paused line has a `NEXT_STEPS.md`;
- no root workflow reruns manifests and fast checkers.

There is also a weaker form of “independence” when a second model sees the first
model's package and simply replays its route. The strongest verification protocol is
blind and asymmetric:

1. freeze the statement and candidate;
2. give the verifier the statement and artifact, not the generator's derivation;
3. require a separately authored parser/encoding;
4. compare exact outputs;
5. only then reveal and reconcile the methods.

### 10. Artifact policy and actual storage diverge

[ARTIFACTS.md](ARTIFACTS.md) says bulky derived output should live under a
regenerate-only directory. The tracked tree nevertheless includes a 24.2 MB
domination panel and a 10.6 MB cap-search result, among other large generated files.
The repository is already about 55.9 MB of tracked content.

This will become a serious constraint if throughput succeeds. The manifest system
works; use it as intended. Track small load-bearing certificates and source. Move
large reproducible panels to `generated/` or durable external storage with hashes.

### 11. The chembiotics strategy is internally inconsistent

The root triage marks all 50 chembiotics tasks reality-gated, while the chembiotics
README and strategy call 21 of them closed-loop because a simulation or synthetic
benchmark can act as verifier. The root's skepticism is closer to the scientific
risk: a force field, docking score, or GCMC simulation may exactly verify performance
under a model without verifying reality.

This program needs three labels, not two:

1. **formal closed-loop:** proof, exact identity, or fully specified synthetic truth;
2. **model closed-loop:** exact relative to a simulator, with external-validity risk;
3. **reality-gated:** held-out experimental data or a new wet-lab result required.

Only the first belongs under the same “resolution” semantics as a finite
combinatorial certificate. The second can yield a methods paper, but not a claim that
the physical problem is solved. The third requires a partner and prospective study
design before model work begins.

### 12. “Major breakthrough” has no explicit acceptance criterion

The repository distinguishes new results from reproductions, but it does not define
major. A tiny refutation of a low-value autogenerated claim, a new Life spaceship, a
one-row covering improvement, and a theorem eliminating a field-wide obstruction
are all “wins” of very different scientific weight.

Without an explicit value threshold, the portfolio will optimize for easily counted
witnesses rather than consequential knowledge.

## Define the outcome before optimizing for it

The atlas should use the following result classes.

### B0: calibration

A known result is reproduced with an independent checker. This validates a harness.
It is not a research contribution by itself.

### B1: frontier datum

A live table entry, record, finite case, or verified range is improved. The novelty
and baseline are independently confirmed. This is a real contribution, though its
importance varies.

### B2: open-claim resolution

A currently open claim is proved or refuted, with statement match, exact evidence,
and independent expert review. This is the default breakthrough target.

### B3: method breakthrough

A new search, reduction, or proof method produces material gains across multiple
independent targets or unlocks a previously inaccessible scale. A new optimizer is
not a breakthrough because it wins one cherry-picked benchmark; transfer is part of
the claim.

### B4: major scientific breakthrough

A B2 or B3 result changes the frontier of a significant area, removes an important
obstruction, or creates substantial downstream capability. This requires domain
experts and publication-level validation. The atlas can generate and verify the
core result, but cannot award this label to itself.

Heuristic nulls, model-generated conjectures, status audits, and reproductions may be
valuable inputs. They should never be counted as B1-B4 unless they meet the stated
criteria.

## Replace static tiering with gates and a scorecard

### Non-negotiable admission gates

A target may receive deep compute only when all of these are true:

1. **Statement pinned:** exact quantifiers, domain, conventions, and success
   condition are written down.
2. **Primary source pinned:** theorem/conjecture number or database cell, exact
   locator, and access date are stored.
3. **Open status fresh:** checked against follow-ups and authoritative trackers
   within the last 30 days; shorter for fast-moving records.
4. **Artifact grammar fixed:** the candidate's canonical format is specified.
5. **Checker exists first:** a small independent checker passes positive and
   adversarial negative calibration cases before search.
6. **Baseline reproduced:** the current best or last known range replays within a
   fixed preflight budget.
7. **Search edge stated:** the target card explains what representation, data,
   symmetry, model capability, or algorithm is new relative to known attempts.
8. **Budget and stop rule fixed:** wall time, CPU/GPU hours, model budget, and the
   evidence required for continuation are committed in advance.
9. **Scientific path named:** the likely expert, community, venue, or table maintainer
   who can validate and absorb a result is known.

If any gate fails, the task is not “low priority”; it is not ready.

### Priority score after admission

Score each dimension from 0 to 5, with written evidence:

| Dimension | High score means |
|---|---|
| Open-status confidence | primary sources, recent search, authoritative maintainer, no competing resolution |
| Reachability | small residual search space, weak prior search, useful relaxations, observable progress |
| Method advantage | a concrete representation/tool edge that prior work did not use |
| Witness/lemma plausibility | structural or empirical reason the claim may fail or the object may exist |
| Scientific value | a real open claim, consequential bound, or transferable method |
| Verification quality | exact, cheap, encoding-faithful, independently implementable |
| Competition penalty | low attention, slow-moving frontier, no heavily optimized incumbent team |
| End-to-end cost | cheap sourcing, search, verification, and external review |

Do not collapse this into an unexplained total. Preserve the vector so a cheap but
low-value target is visibly different from a high-value long shot.

## Make the target card the atomic unit

The current atomic unit is mostly a `PROMPT.md`. Replace it with a versioned target
card from which prompts are generated. Each card should include:

```yaml
id: canonical-target-id
result_class: B1 | B2 | B3
statement: exact statement
source:
  primary_locator: paper/table URL plus theorem or row
  access_date: YYYY-MM-DD
  status_evidence: follow-up searches and maintainer/author note
baseline:
  current_value_or_range: ...
  replay_command: ...
witness:
  format: ...
  checker_command: ...
  checker_hash: ...
search_edge: why this attack differs from prior work
calibration_cases: positive, negative, and known frontier cases
budget: model, wall-clock, CPU/GPU, memory
stop_rules: explicit continuation and kill criteria
publication_path: expert, community, tracker, or venue
aliases: other atlas folders referring to the same target
```

Prompts then become disposable views of durable target intelligence. One status
update fixes every alias.

## A portfolio designed for breakthroughs

For a small compute team, no more than ten targets should be active at once. A useful
allocation is:

### 60%: recent, neglected, finite claims

This is the strongest version of
`discovery/pipelines/31_recent_obscure_conjectures`. Search papers from roughly the
last 6-24 months for explicit finite conjectures, questions, or lemmas with cheap
checkers and little follow-up. Curate the claims first; do not ask the same model
session to find, validate, encode, and attack them.

The value is not merely obscurity. The ideal target has not yet accumulated years of
negative search, but is mature enough to have a precise statement and an author who
cares about the answer.

### 25%: proof-obligation and obstruction mining

Take a narrow lemma or failed formal proof from an active line. Use symbolic
computation, finite model finding, SAT, counterexample generation, and formalization
to decide the obligation. This is where model reasoning can contribute more than
generic stochastic search.

The output must still be small and checkable: a countermodel, a formal lemma, an
exact reduction, or an unsat certificate. This lane recovers the strongest parts of
proof-shaped work without returning to frontal attacks on famous conjectures.

### 15%: reusable method and harness development

Invest only in infrastructure that lowers cost across several admitted targets:

- canonical graph generation plus a library of exact invariants;
- polynomial-family enumeration plus exact Sturm verification;
- a SAT/DRAT finite-design skeleton with symmetry-breaking audits;
- search telemetry, response-curve tracking, and checkpointing;
- automatic target-card, manifest, and claim validation.

Infrastructure is successful when it changes the conversion funnel, not when it
merely adds code.

Hardened record hunts should consume no standing allocation. They can enter as an
exception only when a new method has already shown an advantage on calibrated
instances.

## What to do with the existing atlas

### Promote after operationalization

1. **Recent obscure conjectures (pipeline 31).** This is the best strategic direction
   in the current tree. Its next artifact should be a curated, dated set of 10-20
   exact target cards, not another general prompt.
2. **Exact real-rootedness/log-concavity counterexample mining.** These have excellent
   certificates, but only after one specific still-open polynomial family and input
   grammar are pinned.
3. **Machine registries with explicit unresolved instances.** TPDB nontermination,
   selected automata/state-complexity cells, and similarly maintained finite
   registries can work if the exact instance and current status are fetched before
   the search session.
4. **Fresh finite claims that expose a proof/search loop.** Prefer targets where a
   failed formal proof can guide counterexample construction or an exhaustive census
   can suggest a short structural lemma.

### Keep conditional

- Open SRG, design, code, AME, ETF, and related existence cells have perfect witness
  checkers but may have enormous search entropy. Admit them only with a new symmetry,
  algebraic construction, decomposition, or learned proposal distribution that beats
  known calibration cases.
- Life and cellular-automaton objects may be highly discoverable and valuable to
  their communities. Decide explicitly whether that community impact satisfies the
  project's definition of a major result.
- OEIS mining can yield valid counterexamples, but many entries have ambiguous
  status or modest scientific importance. Restrict it to published, attributable
  conjectures with a clear external audience.

### Demote or close

- Zagreb and the other settled inequality families should be retained only as
  regression benchmarks.
- Domination pipeline 09 should not be run again generically. Reopen it only for a
  newly pinned claim, the inaccessible order-60 witness, or a genuinely new
  construction family.
- “Fresh index family” is not itself evidence of an open valuable claim. Sombor and
  similar pipelines need exact live targets before priority.
- Famous T1 objects such as MUB(6), APN dimension 8, MOLS-10, Moore-57, or circulant
  Hadamard should be treated as hardened long shots despite their cheap checkers.
- All simulation- or wet-lab-gated chembiotics work should be managed in a separate
  empirical portfolio with partner, dataset, leakage, and prospective-validation
  requirements.

## The execution loop

### Stage 0: scout separately from attack

A scout session reads primary sources, verifies status, extracts exact statements,
and creates target cards. It does not search for witnesses. A second review rejects
cards with unclear novelty, semantics, or value.

### Stage 1: write the checker before the generator

Implement the smallest possible checker and canonical parser. Test it against:

- at least one known positive;
- at least one nearly valid negative;
- malformed inputs;
- a second implementation on small cases;
- transformations that should preserve validity.

This prevents the search code from silently defining its own easier problem.

### Stage 2: reproduce only enough frontier to calibrate

Set a strict preflight budget, for example two hours or 5% of the intended deep
budget. If the known result cannot be reproduced, record an infrastructure blocker.
Do not spend the research allocation rediscovering it from scratch unless the
reproduction itself is a publishable audit.

### Stage 3: run cheap probes and measure gradients

Before deep compute, test several genuinely different methods or representations.
Record more than the best score:

- distribution over runs;
- improvement versus time;
- residual constraint structure;
- diversity of near-misses;
- sensitivity to seeds and symmetry choices;
- performance against known smaller instances;
- memory and proof-size scaling.

Promote a target only if there is either a positive response curve or a specific
structural hypothesis explaining why the deep method should cross the observed
barrier.

### Stage 4: deep attack with checkpoints and kill rules

Examples of useful kill rules:

- status or statement ambiguity discovered: stop immediately;
- baseline not reproduced in preflight: move to infrastructure, not research;
- repeated plateaus with no new representation or lemma: pause;
- projected proof/search growth exceeds budget by more than a fixed factor: stop;
- second implementation disagrees: freeze the claim and debug before any new search;
- no new structural information after 20% of budget: require a method review.

“Persist” should mean persistent hypothesis revision, not persistent consumption of
the same search distribution.

### Stage 5: blind verification and novelty review

Verification should be performed from the frozen statement, canonical artifact, and
checker contract. The verifier should not inherit the generator's explanation until
after its independent result is recorded.

Then conduct three human checks:

1. Does the formal claim match the informal target?
2. Was the target genuinely open at the timestamp?
3. Would a domain expert consider the result new and meaningful?

These are different from checking the certificate.

### Stage 6: expert contact is part of completion

For a prospective B2-B4 result, contact the conjecture's author, database maintainer,
or a relevant expert with the exact artifact and checker. A major result is not done
when the local verifier prints `PASS`; it is done when statement match, novelty, and
scientific framing survive informed external scrutiny.

## Turn every attempt into portfolio information

Create a machine-readable attempt ledger. One row or JSON object per attempt should
record:

- target ID and immutable statement version;
- status-check timestamp;
- method and representation;
- seed count and compute/model cost;
- baseline and best score;
- search-coverage description;
- response-curve summary;
- outcome class B0-B4 or null;
- artifacts and verifier status;
- updated reachability assessment;
- exact next obligation;
- continue, pause, kill, or publish decision.

The portfolio dashboard should show a conversion funnel:

```text
ideas scouted
  -> statements pinned
  -> still-open targets confirmed
  -> checkers ready
  -> baselines reproduced
  -> probes with useful signal
  -> deep attempts
  -> valid candidates
  -> independently verified novel results
  -> externally reviewed results
```

The key metric is not prompt count. It is conversion and cost between stages. After
20-30 attempts, the atlas should be able to say which target features and methods
actually predict progress.

## A concrete 30-day reset

### Days 1-3: freeze growth and repair the control plane

- Add no new task prompts.
- Generate the inventory from the filesystem and reconcile 191 versus 192.
- Give overlapping tasks canonical IDs and aliases.
- Mark every target `idea`, `needs-status`, `ready`, `active`, `paused`, `closed`, or
  `benchmark`.
- Demote all unpinned `(verify)` prompts to `needs-status`.
- Update the pipeline index with the domination outcome and pipeline 31.

### Days 4-7: curate twenty candidates, admit at most ten

- Scout recent finite conjectures and exact maintained-table gaps.
- Store primary-source evidence and exact statements.
- Score each target across openness, reachability, method advantage, value,
  competition, and cost.
- Reject any target without a plausible search edge.
- Ask a domain expert to review the top five statements before compute.

### Week 2: build three reusable harnesses

Recommended starting set:

1. graphs: canonical generation, exact invariant plugins, structured-family builders,
   graph6 certificates;
2. combinatorial polynomials: exact enumeration, coefficient audit, Sturm/root
   certificates;
3. finite SAT structures: declarative constraints, audited symmetry breaking,
   CaDiCaL plus DRAT/LRAT verification.

Calibrate every harness on a known counterexample and a known true boundary. The
Zagreb and settled small-cap artifacts are useful regression tests here.

### Week 3: broad cheap probes

- Run multiple short, method-diverse probes on the admitted targets.
- Record complete denominators and response curves.
- Promote at most two targets to deep attacks.
- For flat searches, extract residual structure or unsat cores before spending more.

### Week 4: two deep attacks and blind review

- Give each promoted target a fixed budget and checkpoint schedule.
- Run independent verification blind to the generator's derivation.
- If there is a candidate, begin expert novelty review immediately.
- If there is no candidate, publish the portfolio update internally: what changed in
  the reachability estimate, which obstruction was learned, and why the target is
  paused or killed.

At the end of the month, judge the reset by operational metrics: ten pinned targets,
all with prewritten checkers; three reusable calibrated harnesses; complete attempt
costs; two evidence-based deep promotions; and zero sessions wasted on discovering
that their target was already closed.

## Repository changes required to support the strategy

The following are higher leverage than adding another 100 prompts:

1. **A generated target registry.** One `targets.yaml`/CSV or per-target card schema,
   with canonical IDs, aliases, status timestamps, and stage.
2. **An attempt ledger.** Append-only JSONL/CSV with cost, method, result, posterior
   update, and decision.
3. **A repository auditor.** Check counts, required run files, stale status dates,
   manifest coverage, claim-template fields, duplicate IDs, and forbidden large
   derived artifacts.
4. **Root verification commands and CI.** A fast tier for manifests and small
   checkers; opt-in slow tiers for certificates and exhaustive regeneration.
5. **A uniform attempt skeleton.** Frozen prompt, `CLAIM.md`, source, independent
   verifier, `REPRODUCE.md`, manifest, telemetry, and `NEXT_STEPS.md` or terminal
   decision.
6. **Artifact-policy enforcement.** Track load-bearing certificates; move bulky
   regenerable panels to the prescribed directories or external archival storage.
7. **A novelty evidence bundle.** Primary source snapshot/locator, access date,
   follow-up search, and expert/maintainer correspondence when available.
8. **Blind verification metadata.** Record exactly what context the verifier saw and
   whether its implementation and encoding were independently authored.

## Final doctrine

The atlas should keep these principles:

- exact beats plausible;
- a small auditable claim beats a grand narrative;
- generator is not verifier;
- a heuristic null is not a theorem;
- costs and failed attempts belong in the result;
- encoding fidelity is part of the proof.

It should add these principles:

- **Open, reachable, and valuable are three separate tests.**
- **A cheap checker is an admission condition, not a tractability forecast.**
- **No deep run begins with target selection still unresolved.**
- **Every attack must name its edge over prior work.**
- **Compute continues only when the response curve or a structural hypothesis earns
  it.**
- **A failed run must update a machine-readable belief, not only produce a report.**
- **Witness search and proof-obligation mining are complementary.**
- **External novelty and statement-match review are part of verification.**
- **The portfolio optimizes for consequential verified novelty, not prompt count.**

The project does not need a larger atlas. It needs a narrower, live, instrumented
frontier and a ruthless feedback loop. If that is built, the existing verification
discipline becomes a genuine competitive advantage: the team can move quickly on
neglected claims while producing artifacts that experts can trust. Without it, the
likely outcome is an expanding library of excellent reproductions and honest
near-misses. With it, a major breakthrough becomes unlikely in the honest sense—but
no longer accidental.
