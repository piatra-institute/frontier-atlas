# PROMPT FOR CERTIFIED BUSY-BEAVER FRONTIER RESULTS

## Deciding holdout machines, new BB(6) lower bounds, and small BB variants - with machine-checked proofs

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 23 of 50  
**Area:** computation models & automated reasoning  
**Modes:** `[cert]` `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The busy beaver function measures the extreme edge of what a finite program can do before halting, and it is the cleanest decidability frontier in the atlas: every claim about it is either a halting proof, a non-halting proof, or an exhaustive statement that no machine of a given size does better - each of which is machine-checkable. The value \(\mathrm{BB}(5)=47{,}176{,}870\) was **settled in July 2024** by the bbchallenge collaboration and delivered as a Coq proof (contributor mxdys, building on the deciders of more than ten collaborators); \(\mathrm{S}(2,4)=3{,}932{,}964\) was Coq-certified in August 2024. \(\mathrm{BB}(6)\) is open and astronomically large - a specific 6-state machine already forces a lower bound in the pentation range - and it is now known to be "hard" in a precise sense: certain 6-state holdouts encode Collatz-like problems (the "Antihydra"). This prompt asks for a *certified* advance: a formally verified halting or non-halting proof for a named holdout machine, a new certified \(\mathrm{BB}(6)\) lower bound, or the complete settling of a small BB variant. Heuristic simulation, an uncertified decider run, or a lower bound without a replayable witness is a partial result, never a solution. The on-machine verifier that closes the loop is a Coq/Rocq or Lean kernel checking the halting/non-halting proof, plus an independent re-run of the machine to the claimed step count.

## 1. Exact problem statement

Fix the model precisely, because BB values are convention-sensitive.

A **Turing machine** with \(m\) states and \(k\) symbols is a partial function
\[
\delta:\{1,\dots,m\}\times\{0,\dots,k-1\}\ \rightharpoonup\ \{0,\dots,k-1\}\times\{\mathrm{L},\mathrm{R}\}\times(\{1,\dots,m\}\cup\{\mathsf{H}\}),
\]
operating on a **two-way infinite tape** of cells, each holding a symbol in \(\{0,\dots,k-1\}\). The machine starts in state \(1\) on an **all-blank tape** (blank \(=0\)) with the head on a distinguished cell. At each step it reads the symbol under the head, and if \(\delta\) is defined it writes a symbol, moves L or R, and enters the next state; it **halts** when it enters \(\mathsf H\) or when \(\delta\) is undefined on the current (state, symbol) pair. This is the bbchallenge convention; state count on \(k=2\) is written \(\mathrm{BB}(m)\).

Two standard cost measures:
- the **shift function** \(\mathrm{S}(m,k)\): the maximum number of steps taken before halting, over all machines that halt on the blank tape; and
- the **ones/sigma function** \(\Sigma(m,k)\): the maximum number of non-blank symbols left on the tape at halt.

Write \(\mathrm{BB}(m)=\mathrm{S}(m,2)\) unless stated otherwise; note \(\Sigma(m)\le \mathrm{S}(m)\). Both are non-computable - they eventually dominate every total computable function:
\[
\forall\,\text{computable total } f\ \ \exists m_0\ \forall m\ge m_0:\ \mathrm{S}(m)>f(m).
\]
Yet each fixed value is a finite combinatorial fact: \(\mathrm{S}(m,k)=\max\) over halting machines of a halting time, and the certifying obstacle is a matching upper bound - a proof that **every** machine of that size either halts within the bound or never halts.

The certified upper bound ranges over a finite set. Up to the symmetries that fix blank-tape behaviour (permuting the non-start states, relabelling non-blank symbols, and reflecting tape direction on the first move), the raw count of \(m\)-state \(k\)-symbol machines is \(\bigl(2k(m+1)\bigr)^{mk}\) before isomorph reduction; the bbchallenge pipeline generates them in a **Tree Normal Form** (TNF), extending a partial machine only when a new transition is first reached and pruning branches that provably cannot be extremal. The known anchor values are
\[
\mathrm{S}(1)=1,\quad \mathrm{S}(2)=6,\quad \mathrm{S}(3)=21,\quad \mathrm{S}(4)=107,\quad \mathrm{S}(5)=47{,}176{,}870,
\]
\[
\Sigma(1)=1,\ \Sigma(2)=4,\ \Sigma(3)=6,\ \Sigma(4)=13,\ \Sigma(5)=4098,\qquad \mathrm{S}(2,4)=3{,}932{,}964 .
\]

**The questions.** (i) Determine \(\mathrm{S}(6)\) or improve its certified lower bound. (ii) Decide named individual "holdout" machines (halts / never halts) that block a size class. (iii) Settle a small variant completely: \(\mathrm{S}(3,3)\), \(\Sigma(3,3)\), or a comparable \((m,k)\) whose whole enumeration is within reach. Every answer is either an explicit witness machine (for a lower bound) or an exhaustive-plus-individual argument that closes a class (for an exact value).

**Holdouts and the hardness barrier.** A **holdout** is a single machine the automated deciders cannot classify; a size class is closed only when every holdout is resolved by hand. Some holdouts are provably hard: a "Cryptid" machine's halting is equivalent to a statement of the form "the orbit \(x_{t+1}=g(x_t)\) of a Collatz-like map \(g:\mathbb N\to\mathbb N\) ever enters a target set," which no current method decides. The Antihydra (a 6-state machine, June 2024) is the paradigm: it halts iff a specific parity-driven sequence attains a bounded imbalance, an open number-theoretic question. Thus a *complete* \(\mathrm{S}(6)\) is currently out of reach; the realistic products are certified lower bounds, certified individual verdicts, and certified reductions.

## 2. Resolution standard

A result is a **resolution** only in one of these certified forms.

- **Exact value of a variant.** For a specific \((m,k)\), a machine-checked statement \(\mathrm{S}(m,k)=N\) (resp. \(\Sigma\)): a witness machine halting in exactly \(N\) steps, **plus** a certificate that every machine in the isomorph-reduced enumeration halts by step \(N\) or provably never halts. The completeness argument must be a formally verified enumeration certificate (the bbchallenge deciders, ported to or re-checked by Coq/Rocq or Lean) - not a solver log.
- **Certified lower bound for BB(6).** An explicit 6-state machine \(M\) together with a formally verified proof that \(M\) halts on the blank tape after exactly \(T\) steps, giving \(\mathrm{S}(6)\ge T\). The proof - typically an accelerated-simulation / closed-form induction - must be checked by a Coq/Rocq or Lean kernel, and the step count independently reproduced by a direct simulator up to any tractable prefix.
- **Deciding a holdout.** For a named machine (e.g. an Antihydra-class 6-state Cryptid, the \(\mathrm{BB}(3,3)\) "Bigfoot" holdout, or a bbchallenge undecided-index machine), a formally verified **non-halting** proof (a closed-form invariant / certified translated-cycle / certified counter argument) or a formally verified **halting** proof with exact step count.

Formally, an exact-value certificate for \((m,k)\) is a machine-checked proof of the conjunction
\[
\bigl(\exists M^\star\ \text{halting in exactly } N \text{ steps}\bigr)\ \wedge\ \Bigl(\forall M\in \mathrm{TNF}(m,k):\ \mathrm{halt}(M)\le N\ \vee\ \neg\,\mathrm{halts}(M)\Bigr),
\]
where the second conjunct is discharged by the certified decider suite plus a finite list of individually certified holdouts.

**Named certified form.** The deliverable is one of: *(a)* a formally-verified halting/non-halting proof (Coq/Rocq or Lean) for a specific machine; *(b)* an exhaustive machine-enumeration certificate closing a size class, itself formally checked; or *(c)* a certified universality/hardness construction linking a holdout to a stated open problem. Each ships with the machine in canonical form, the proof script, and an independent replay.

**Not accepted as resolution.**
- A long empirical simulation with no halting/non-halting proof (a machine that "hasn't halted in \(10^{12}\) steps" is undecided, not proven non-halting).
- A lower bound stated as a number with no explicit witness machine, or with a witness whose step count is not independently reproduced.
- A decider that classifies a class but whose completeness/soundness is only argued informally or only run, not certified.
- Beating a record by adopting a different tape/halt convention without stating it; convention must match §1.
- "\(\mathrm{BB}(6)\) is uncomputable / independent of ZFC in general" hand-waving offered in place of a specific settled machine or value.
- A Collatz-like reduction presented as *deciding* a holdout; a reduction shows hardness, it does not settle behavior.
- A formal proof that "compiles" only because an extra axiom was added to the kernel context; the axiom set must be empty or fully disclosed.
- An enumeration whose isomorph-reduction (TNF) is buggy or incomplete, so the "all machines" quantifier is not actually covered.

## 3. Graded partial-result targets

**P1 - Reproduce the frontier.** Re-derive \(\mathrm{BB}(5)=47{,}176{,}870\) and \(\mathrm{S}(2,4)=3{,}932{,}964\) with an independent toolchain:
- re-run the champion machines to their exact halting times with the independent simulator;
- re-compile the published Coq/Rocq proofs and confirm a green kernel check with an empty (or fully disclosed) axiom set;
- reproduce the TNF enumeration count and record which decider family closes which sub-class.

*Certificate:* a green kernel check plus matching step counts; a written map of which deciders close which sub-classes. Validates the pipeline end to end.

**P2 - Certified lower-bound reproduction for BB(6).** Take the current \(\mathrm{S}(6)\) champion and produce an *independent* formally verified proof that it halts after exactly the claimed number of steps. *Certificate:* a Coq/Rocq or Lean proof object, checked, with the accelerated-simulation invariant stated explicitly and a direct simulator agreeing on a computable prefix.

**P3 - Decide a batch of open bbchallenge indices.** Formally close a nonempty set of currently-undecided small machines (remaining hard analogues in a variant, or specific 6-state sub-families) with certified non-halting proofs - translated cycles, closed-form counters, certified closed-position sets. Prefer machines that:
- fall to an existing decider family whose soundness is already formalized (cheapest certified wins); or
- admit a short bespoke invariant (a linear or affine counter) that can be hand-formalized.

*Certificate:* one machine-checked proof per index, with the decider's soundness lemma formalized and the axiom set disclosed.

**P4 - New certified BB(6) lower bound.** Exhibit a 6-state machine with a **larger** certified halting time than the current record, with a formally verified halting proof. Acceptable routes:
- a genuinely new machine whose accelerated-simulation invariant yields a larger hyperoperation expression;
- a certified sharpening of the current champion's step count (a tighter closed form).

*Certificate:* the machine in canonical form, the checked proof, the exact symbolic step expression, and a citation of the beaten record with source and access date. A lower bound with no independently checked halting proof does not count.

**P5 - Settle a small variant.** Completely determine \(\mathrm{S}(3,3)\) or \(\Sigma(3,3)\) (or another \((m,k)\) whose enumeration you can finish), including certified disposal of the Collatz-like holdouts blocking it. This requires:
- a certified TNF enumeration of the whole \((m,k)\) class;
- a certified verdict (halt-by-\(N\) or never-halts) for every machine via the decider suite;
- an individually certified proof for each residual holdout - and, where a holdout is Collatz-hard (the \((3,3)\) "Bigfoot"), either a breakthrough number-theoretic argument or an explicit statement that the value is conditional on / blocked by that open problem.

*Certificate:* exact value, witness machine, and a formally verified enumeration-completeness certificate; each holdout gets its own halting or non-halting proof or a documented hardness reduction.

**P6 - Certified hardness map.** For a named holdout you cannot decide, produce a *certified reduction* linking its behavior to a precisely stated open problem (a specific Collatz-like or number-theoretic conjecture), so the community can retire attempts to decide it directly. *Certificate:* a formal statement of the reduction and, where possible, a machine-checked equivalence of the two halting conditions.

## 4. Known results and prior art

**This area moved a lot recently - web-verify every figure below before a session.**

- **\(\mathrm{BB}(5)=\mathrm{S}(5)=47{,}176{,}870\), \(\Sigma(5)=4098\)** - settled July 2024 by the bbchallenge collaboration; the completeness proof was written and checked in Coq by mxdys, aggregating deciders from 10+ contributors. (verify)
- **\(\mathrm{S}(2,4)=3{,}932{,}964\)** - Coq-certified August 2024 (mxdys, bbchallenge). (verify)
- **\(\mathrm{BB}(6)\) open, pentation-scale.** With the hyperoperation notation \(a\uparrow\uparrow n\) (tetration) and \(a\uparrow\uparrow\uparrow n = a\uparrow\uparrow(a\uparrow\uparrow(\cdots))\) (pentation), the pre-2024 lower-bound record was on the order of \(10\uparrow\uparrow 15\) (Kropitz, ~2022). In 2024–2025 the certified \(\mathrm{S}(6)\) lower bound leapt well past tetration into pentation territory; the mid-2025 record (mxdys, ~June 2025) is on the order of \(2\uparrow\uparrow 2\uparrow\uparrow 2\uparrow\uparrow 9\) (equivalently a pentation-level tower) or comparable - **verify the exact current expression and holder on the bbchallenge wiki/forum.** (verify)
- **"Antihydra" (June 2024)** - a 6-state "Cryptid" holdout whose halting is equivalent to a Collatz-like statement about a specific integer sequence; deciding \(\mathrm{BB}(6)\) requires resolving such machines, which is why \(\mathrm{BB}(6)\) is regarded as "hard." (verify)
- **\(\mathrm{BB}(3,3)\)** - open; the "Bigfoot" holdout (sligocki, ~2023) is Collatz-hard, so a full \(\mathrm{S}(3,3)\) requires disposing of a Collatz-like problem. (verify)
- **Independence phenomena.** A ~7910-state (later reduced) machine whose halting is independent of ZFC (Yedidia–Aaronson, ~2016) frames the meta-hardness; earlier Σ records and the historical survey (Michel; Marxen–Buntrock) are background. (verify names/years)
- **Tooling lineage.** bbchallenge deciders: cyclers, translated cyclers, backward reasoning, "n-gram closed position set" (NGramCPS), finite automata reduction, and the Coq pipeline (Turing machine deciders, part I, 2025 arXiv). (verify)

Status as of mid-2026 - re-verify against the current literature and record trackers (the bbchallenge wiki, forum, and the undecided-machine index) before starting any session.

## 5. Attack plan

`[cert]` primary, `[search]` supporting. One workstation suffices for the certification work; the historical enumeration was distributed but its *outputs* (decider verdicts, holdout lists) are downloadable and re-checkable locally.

1. **Stand up the checker first.** Install Coq/Rocq (and/or Lean 4) and compile the published bbchallenge Coq development end to end; confirm \(\mathrm{BB}(5)\) and \(\mathrm{S}(2,4)\) check green. This is P1 and it validates everything downstream.
2. **Independent simulator.** Write a small, separate high-performance TM simulator (C++/Rust) with big-integer step counters and macro/acceleration (block simulation, "chain"/"macro" acceleration, run-length tape encoding) to reproduce champion halting times and to sanity-check any lower-bound witness on a computable prefix. Keep it independent of the proof code so a bug cannot corrupt both. Cross-check every reproduced count against the published value bit-for-bit.
3. **Certified non-halting.** Port/re-implement the decider families as *proof-producing* deciders whose soundness lemma is formalized; target the current undecided-index machines (P3). The workhorse families:
   - **Cyclers** - the configuration (state, head, finite tape window) repeats exactly; a certified visited-set replay proves the loop.
   - **Translated cyclers** - the configuration repeats up to a fixed tape shift; certify the shift-invariant.
   - **Backward reasoning** - no halting configuration has a length-\(k\) predecessor chain; a bounded search certifies unreachability of every halt transition.
   - **Closed-position sets / n-gram CPS** - a finite set of local tape patterns closed under the transition and excluding halt; certified by checking closure.
   - **Finite-automata reduction (FAR)** - a weighted/deterministic automaton over reachable tapes proves the halt state is never entered.
4. **Lower-bound engineering (P2/P4).** For a candidate 6-state halter:
   - run the block/macro simulator to detect a regular tape structure (nested repeated blocks) after macro-steps;
   - conjecture a closed-form invariant \(C(t)\) describing the tape after the \(t\)-th macro-phase and the phase-transition recurrence;
   - prove the recurrence by induction inside Coq/Rocq or Lean, so the kernel certifies the exact final step count;
   - keep pentation-scale counts as **symbolic** hyperoperation expressions (e.g. \(2\uparrow\uparrow 2\uparrow\uparrow 2\uparrow\uparrow 9\)), never evaluated numerically, using exact big-integer arithmetic only for tractable prefixes.
5. **Variant closure (P5).** For \((3,3)\), generate the isomorph-free enumeration (canonical form under state/symbol permutations), run the certified deciders, and hand-formalize each residual holdout. Expect a small number of Collatz-hard residues (P6).

**Failure modes.** (a) Simulation without proof - the dominant trap; a machine silent for \(10^{12}\) steps is undecided. (b) Convention drift - a "record" under a one-way tape or different halt rule is not comparable. (c) Uncertified decider output - a verdict is only as good as its formalized soundness. (d) Kernel-trust gaps - a proof that "compiles" against an axiom you added is not a proof; keep the axiom set empty and print it. (e) Overflow/precision - pentation-scale counts must stay symbolic. (f) Collatz walls - some holdouts are genuinely beyond current mathematics; recognize and reduce (P6) rather than burn a session simulating.

## 6. Verification and auditability requirements

1. **Exact or certified computation** for every load-bearing claim: halting/non-halting proofs checked by a Coq/Rocq or Lean kernel with an explicitly printed (ideally empty) axiom list; step counts as exact big integers or closed-form symbolic expressions; floating point never touches a bound.
2. **Independent verification:** each halting witness re-run by the separate simulator to a computable prefix; each non-halting/enumeration certificate re-checked by a small standalone replay written apart from the search code; where feasible, a second proof assistant or a second decider corroborates. Concretely:
   - a cycler/translated-cycler certificate replayed by a stand-alone visited-set checker;
   - a closed-position-set certificate re-verified by an independent closure check over the pattern set;
   - a lower-bound induction re-derived symbolically and its base cases re-simulated;
   - the TNF enumeration re-counted by an independent canonical generator.
3. **Reproducibility:** machines in canonical (isomorph-reduced) form, decider versions, proof-assistant versions, and environment recorded; a SHA-256 manifest over machines, proof scripts, and logs; every beaten record cited with source and access date so the claimed gain is unambiguous.
4. **Preservation:** simulator source, decider source, and proof scripts are part of the record; anything not preserved is stated explicitly (the sister-program lost-source lesson).
5. **Honest reporting:** state up front whether the resolution standard was met, whether a record was *strictly* improved and under which convention, and - for any undecided holdout - that it remains undecided and, if applicable, is reduced to a named open problem. A long empty simulation is never reported as a non-halting result.
