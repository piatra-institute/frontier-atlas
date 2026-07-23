# PROMPT FOR A NEW POINT ON THE SMALLEST-UNIVERSAL-TURING-MACHINE FRONTIER

## The (states, symbols) boundary between universal and decidable tiny machines

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 24 of 50  
**Area:** computation models & automated reasoning  
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

How small can a Turing machine be and still compute anything a computer can? The question is a grid: each cell \((m,k)\) asks whether an \(m\)-state, \(k\)-symbol machine can be universal. Above a frontier curve the answer is yes (explicit universal constructions exist); below it the answer is no (the machines are too small - their halting/behavior problems are decidable). The frontier is only partly mapped, and - this is the crux - it depends sharply on **what "universal" means**: standard universality on a blank or finite tape, versus *weak* universality that permits an infinite, ultimately-periodic initial background. The famous \((2,3)\) case (Wolfram's machine, Smith's 2007 prize proof) is *weakly* universal with a non-blank periodic initial condition; whether it is universal in the standard sense is disputed. This prompt asks for a genuine new point on the frontier: a smaller universal machine (with a *certified* simulation/universality proof), or a *decidability* result placing a specific tiny machine below the frontier. The verifier that closes the loop is a machine-checked simulation certificate (a proof that machine \(M\) simulates a known-universal system with a stated overhead) or a formally verified decision procedure for a tiny machine's behavior. Any construction must state its universality notion explicitly; a weak-universality result must never be presented as a standard-universality result.

## 1. Exact problem statement

A **Turing machine** is \((Q,\Sigma,\delta)\) with \(|Q|=m\) states, \(|\Sigma|=k\) tape symbols, and \(\delta:Q\times\Sigma\rightharpoonup\Sigma\times\{\mathrm L,\mathrm R\}\times(Q\cup\{\mathsf H\})\), on a two-way infinite tape. We measure size by the pair \((m,k)\) (and sometimes the state–symbol product \(mk\) or the transition count).

**Universality notions (state the one you use).**
- **Standard universality.** There is a computable encoding \(w\mapsto \langle w\rangle\) of instances of a known-universal problem such that \(M\), started with \(\langle w\rangle\) written on an otherwise **blank** (or finite) tape, halts iff the simulated computation halts, and the output is decodable. Encoding and decoding must be simple (e.g. computable in low complexity, and in particular not themselves performing the computation).
- **Weak universality.** As above, but \(M\) starts on an infinite tape that is **blank except for a finite region and an ultimately periodic background** on one or both sides. The periodic background may not encode the input's computation.
- **Semi-weak universality.** One side blank, the other side periodic.
- **Intrinsic / efficiency refinements.** Whether the simulation is polynomial-time (Neary–Woods direction) matters for the "smallest efficient UTM" question - an exponential-overhead machine and a polynomial-overhead machine at the same \((m,k)\) are different records.

**Simulation, made precise.** \(M\) **simulates** a system \(\mathcal S\) if there are computable maps \(\mathrm{enc}\) (instances of \(\mathcal S\) to tape contents) and \(\mathrm{dec}\) (halting tapes of \(M\) to outputs of \(\mathcal S\)) and a monotone time bound \(\tau\) such that, for every instance \(x\),
\[
\mathcal S(x)\!\downarrow\ \Longleftrightarrow\ M\ \text{on}\ \mathrm{enc}(x)\ \text{halts},\qquad
\mathrm{dec}\bigl(M(\mathrm{enc}(x))\bigr)=\mathcal S(x),
\]
with \(M\) reaching the answer within \(\tau(\text{time}_{\mathcal S}(x))\) steps. **Efficiency** (Neary–Woods) asks \(\tau\) polynomial; classical small UTMs had exponential or worse \(\tau\). The encoding must be **simple** - formally, computable in low complexity (e.g. \(\mathrm{AC}^0\)/linear-time) so it cannot itself perform \(\mathcal S\)'s computation.

**The frontier.** For each notion, \(\mathcal U=\{(m,k): \exists\ \text{universal } M\}\) is upward closed in a rough sense; its lower boundary is the object of study. Below the boundary lie \((m,k)\) for which **every** machine is non-universal because its behavior is decidable (e.g. small classes reducible to decidable word problems). The **open question**: pin new boundary cells - either a new small universal construction (moving the "yes" region down) or a decidability theorem for a specific tiny class (extending the proven "no" region up).

**Deliverables in scope.**
1. A universal machine at a new small \((m,k)\) under a clearly stated notion, with a certified simulation.
2. A certified universality proof (machine-checked) for an existing candidate whose proof is only informal.
3. A decidability result for a specific tiny machine or a whole small \((m,k)\) class, extending the proven non-universal region.
4. A rigorous resolution of the standard-vs-weak status of a named borderline machine (notably \((2,3)\)).

## 2. Resolution standard

A result resolves a frontier cell only in a certified form.

- **New universal construction.** An explicit \(M\) at \((m,k)\), a fully specified encoding/decoding, and a **certified simulation proof**: a machine-checkable argument (Coq/Rocq, Lean, or a checked structured proof) that \(M\) simulates a fixed known-universal system (a specific small UTM, a tag/cyclic-tag system, Rule 110, or a 2-counter/2-tag machine) step-faithfully with a stated overhead, including the halting correspondence. The universality notion is named in the theorem.
- **Certified universality of a candidate.** For an existing informally-argued machine, a machine-checked simulation certificate meeting the above bar, upgrading "believed universal" to "proved universal (in notion X)."
- **Decidability result.** For a specific tiny machine or a whole \((m,k)\) class, a proved decision procedure for its blank-tape halting (or reachability/behavior) problem - a total algorithm with a correctness proof, ideally formalized - establishing non-universality by placing the class below the frontier.
A decidability certificate, dually, is a machine-checked proof of totality and correctness of an algorithm \(D\) with
\[
\forall M\in\text{class},\ x:\quad D(M,x)=\texttt{halts}\ \Longleftrightarrow\ M\ \text{on}\ x\ \text{halts},
\]
which - by non-universality of the class - places \((m,k)\) below the frontier.

- **Named certified form.** One of: a **certified universality construction** (checked simulation of a known-universal system), or a **formally verified decision procedure** for a tiny machine/class. The theorem statement fixes the universality notion, the simulated system, and the overhead \(\tau\).

**Not accepted as resolution.**
- A machine "believed universal" from suggestive traces, with no simulation proof.
- A construction that quietly uses a periodic/infinite initial condition while claiming *standard* universality - the \((2,3)\) trap. Weak/semi-weak results are valuable but must be labeled.
- An encoding that performs part of the computation itself (the "cheating encoding" objection to weak-universality claims); the encoding must be certified simple.
- A decidability claim that is only an empirical observation ("all small instances halt") rather than a proved total decision procedure.
- Reducing \(mk\) by a convention change (extra halt state accounting, blank-symbol reuse, one-way vs two-way tape) without stating the convention.
- An efficiency claim (polynomial \(\tau\)) with no proved time bound, or a simulation whose overhead is unbounded.
- A decidability "result" that is really an empirical halting census over finitely many inputs.
- A "smaller" machine obtained by folding the halt state into a state count under one convention while the compared record uses another.

## 3. Graded partial-result targets

**P1 - Reproduce a known small UTM with a checked simulation.** Take one of the smallest known standard-universal machines (Rogozhin's \((4,6),(5,5),(6,4),(7,4)\) family, or a Neary–Woods polynomial-time machine) and produce an independent, machine-checked certificate that it simulates its target system. Steps:
- transcribe the transition table into the simulator and reproduce published sample runs bit-for-bit;
- fix the simulated system and formalize the simulation invariant;
- obtain a green kernel check with a disclosed axiom set.

*Certificate:* a checked simulation proof plus a tested simulator reproducing sample runs.

**P2 - Certify a weak/semi-weak candidate, correctly labeled.** Formalize the simulation for one of the small weakly-universal Rule-110 machines \((7,2),(4,3),(3,4),(2,5)\) or a semi-weak Neary–Woods machine, with the periodic-background assumption made explicit in the theorem hypotheses. *Certificate:* a machine-checked proof whose hypotheses name the initial-condition class (weak / semi-weak), plus a simulator reproduction of a Rule-110 run on the encoded background.

**P3 - Resolve the (2,3) status question.** Give a rigorous account of whether Wolfram's \((2,3)\) machine is universal in the *standard* sense:
- a certified standard-universality construction with a **provably simple** encoding (settling it positively); or
- an argument that no simple blank/finite-tape encoding suffices - a partial decidability or lower-bound result on \((2,3)\) behaviour under standard initial conditions; and
- in all cases, a formal separation of the weak (Smith) result from the standard question, with the periodic-background hypothesis stated explicitly.

*Certificate:* a formal statement separating the notions and a checked proof of whichever direction is established.

**P4 - Extend the proven decidable region.** Prove that a specific tiny class - a whole \((2,k)\) or \((m,2)\) family below current constructions, or a named borderline machine - has a decidable blank-tape halting problem, hence is non-universal. Routes:
- reduce blank-tape behaviour to a decidable word problem (e.g. a one-rule or length-preserving semi-Thue system);
- exhibit a finite reachability closure (the set of reachable configurations is effectively finite or eventually periodic);
- give a Presburger- or automaton-definable invariant separating halting from non-halting configurations.

*Certificate:* a total decision procedure with a correctness proof (formalized where feasible), and an enumeration confirming coverage of the class up to isomorphism.

**P5 - A new small universal construction.** Exhibit a universal machine at an \((m,k)\) not previously known universal in your stated notion, with a certified simulation. Candidate wins:
- a smaller **efficient** (polynomial-time) UTM than the Neary–Woods family;
- a smaller **standard**-universal machine than the Rogozhin family;
- a machine matching a known size but with a strictly simpler certified encoding.

*Certificate:* the machine, encoding/decoding, checked simulation proof, overhead bound \(\tau\), and citation of the record being improved with source and access date.

**P6 - Frontier map artifact.** Assemble a certified table of the current \((m,k)\) grid - for each notion, which cells are proved universal (with which simulated system), which are proved decidable, and which are open - with a machine-readable index of the certificates. *Certificate:* the table plus links from each cell to its proof object, and a stated size measure (\(mk\) vs \(\max(m,k)\) vs transition count) so cells are comparable.

## 4. Known results and prior art

**This area moved a lot recently - web-verify every attribution below before a session.**

- **Rogozhin (~1996)** - small standard-universal machines at \((4,6),(5,5),(6,4),(7,4),(8,3),(9,3),(10,2)\) and larger-symbol variants; long the reference frontier for standard universality. (verify exact list)
- **Neary–Woods (~2007–2009)** - polynomial-time universal machines at \((3,11),(5,7),(6,6),(7,5),(8,4)\) (the smallest known *efficient* UTMs), and small **weakly** universal machines simulating Rule 110 at \((7,2),(4,3),(3,4),(2,5)\); also small **semi-weak** machines improving Watanabe. (verify pairs)
- **Cook / Wolfram** - Rule 110 universality underpins the weak small machines; the \((2,5),(3,4),\dots\) weak family simulates Rule 110. (verify)
- **Smith (2007), Wolfram \((2,3)\) prize** - proof that Wolfram's 2-state 3-symbol machine is universal, but via a **non-blank, ultimately periodic initial condition**; the standard-vs-weak status is disputed, and the "is the encoding cheating?" objection is central. (verify)
- **Survey.** Woods–Neary, "The complexity of small universal Turing machines: a survey" (arXiv 1110.2230, ~2011) is the canonical map and lists the decidability results bounding the "no" region (e.g. decidability of \((2,2)\), certain \((1,k)\)/\((m,1)\) trivialities, and small \(2\)-symbol/\(2\)-state classes). (verify)
- **Watanabe** - early semi-weak universal machines that Neary–Woods later improved; useful for the semi-weak lineage. (verify)
- **Decidable-region results** - Pavlotskaya, Kudlek, Margenstern and others proved decidability for various tiny classes (e.g. \((3,2)\), \((2,3)\) under standard conditions is a boundary case). (verify names)
- **State–symbol product** - the informal "smallest" is often read off the product \(mk\): Rogozhin's \((5,5)\) has \(mk=25\), \((4,6)\) has \(24\), \((6,4)\) has \(24\); Neary–Woods' \((6,6)=36\) buys **polynomial** time. Whether one minimizes \(mk\), \(\max(m,k)\), or the transition count changes the "record", so the measure must be fixed. (verify)
- **Lower frontier of "no"** - trivially, \((1,k)\) and \((m,1)\) machines are non-universal (their halting is decidable), and \((2,2)\) is decidable; the interesting decidable-region growth is at \((2,3),(3,2),(2,4),\dots\). (verify)

Status as of mid-2026 - re-verify against the current literature and record trackers before starting any session.

## 5. Attack plan

`[search]`, but the real work is proof engineering; one workstation suffices.

1. **Simulator harness.** Build a faithful multi-symbol TM simulator (Rust/C++) that:
   - runs candidate machines on encoded inputs and on ultimately-periodic backgrounds (represented symbolically as (finite core, left period, right period));
   - reproduces known constructions (P1) step-for-step against published traces;
   - stress-tests any new candidate on a battery of simulated-system instances before a proof is attempted.
2. **Fix the simulated system.** Choose a clean known-universal target with a formalization-friendly structure - cyclic tag systems, 2-tag systems, Rule 110, or a specific tiny UTM - so certified universality of \(M\) reduces to a checked simulation of that one system. Prefer a target that:
   - has an existing machine-checked universality proof (so the chain of trust is short); and
   - admits a low-complexity encoding into \(M\)'s tape alphabet.
3. **Certified simulation.** In Coq/Rocq or Lean:
   - define \(M\)'s transition table, the encoding \(\mathrm{enc}\), and the decoding \(\mathrm{dec}\) as functions;
   - state the invariant relating \(M\)'s configuration after a macro-block to the simulated system's configuration;
   - prove step-faithfulness (each macro-block advances \(\mathcal S\) by one step) and the halting correspondence;
   - prove the encoding-simplicity lemma (bounded complexity of \(\mathrm{enc}\)) to defeat the "cheating encoding" objection;
   - print the axiom set and confirm it is empty.
4. **Decidability direction (P4).** For a small class, search for a decision procedure:
   - reduce blank-tape behaviour to a decidable word problem, a finite reachability closure, or a Presburger/automata-definable invariant;
   - prove totality and correctness (formalize where feasible);
   - enumerate the class in canonical form under state/symbol symmetry to confirm coverage;
   - flag any machine that resists both a universality construction and a decidability proof as an open boundary cell.
5. **(2,3) resolution (P3).** Separate notions formally; attempt either a provably-simple standard encoding or a decidability/lower-bound argument on the standard-condition behaviour; keep the periodic-background hypothesis explicit throughout. Re-examine Smith's construction line by line to isolate exactly where the periodic background enters, and quantify how much computation the encoding performs.

**Failure modes.** (a) Notion drift - the single biggest error; every claim must name standard/weak/semi-weak/intrinsic. (b) Cheating encodings - an encoding that does the work makes "universality" vacuous; certify simplicity. (c) Simulation-not-proof - a candidate that "looks universal" over sample inputs is not proved universal. (d) Overhead gaps - a simulation with unbounded or unproven overhead is not a valid efficient-UTM claim. (e) Decidability mirages - "all tested inputs halt" is not a decision procedure. (f) Kernel-trust - print the axiom set of any formal proof, and reject proofs that lean on an added axiom.

## 6. Verification and auditability requirements

1. **Exact or certified computation:** universality via a machine-checked simulation proof (Coq/Rocq or Lean, axiom set printed) or a proved-total decision procedure; simulator outputs are exploration only until a proof exists.
2. **Independent verification:** every checked simulation re-validated by an independent simulator on sampled inputs; every decision procedure cross-checked by a separate enumeration/replay; a second proof assistant where warranted. In particular:
   - the encoding/decoding are re-implemented independently and agree on a battery of instances;
   - the simulated system's own reference implementation confirms the decoded outputs;
   - the axiom set of every formal proof is printed and inspected.
3. **Reproducibility:** machines in canonical form, encodings/decodings fully specified, the simulated system pinned, proof-assistant and simulator versions recorded; SHA-256 manifest over machines, proofs, and logs; any improved record cited with source and access date.
4. **Preservation:** simulator source, proof scripts, and the frontier-table index are part of the record; anything not preserved is stated explicitly.
5. **Honest reporting:** state up front the universality notion, the simulated system, the overhead, and whether the result is a new frontier point or a reproduction; a weak/semi-weak result is never reported as standard universality, and an empirical halting observation is never reported as decidability.
