# PROMPT FOR A CERTIFIED UNIVERSALITY RESULT ON A SMALL CELLULAR AUTOMATON

## The smallest universal CA - and settling the (non)universality of specific tiny rules

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 30 of 50  
**Area:** computation models & automated reasoning  
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

A cellular automaton (CA) updates an infinite lattice of cells in parallel by a fixed local rule; a handful of them can simulate arbitrary computation. The landmark is **Rule 110** - a 1D, 2-state, 3-neighbor elementary CA proved (weakly) **computationally universal** by Matthew Cook, via simulation of cyclic tag systems through colliding gliders. The open territory is the **smallest universal CA** under each precise notion, and the **(non)universality classification of specific small rules**. Two universality notions must be kept apart: **computational** universality (the CA can *simulate* a universal machine, typically weakly - on a periodic background with an engineered encoding) and **intrinsic** universality (the CA can simulate *every* CA of its class, via a rescaling/bulking simulation) - a strictly stronger, more robust property with its own minimal-size questions. This prompt asks for a certified advance on a *specific* small CA: a machine-checkable universality proof (a certified simulation of a fixed universal system, with the background/encoding made explicit), a certified **non-universality**/decidability result for a specific small rule (placing it below the frontier), or a smaller universal construction under a stated notion. The verifier is a certified simulation certificate or a proved decision procedure. Universality proofs are subtle - an engineered encoding can smuggle in the computation - so the notion and the encoding's simplicity must be certified. A rule "believed universal" from glider zoology is a partial result.

## 1. Exact problem statement

A **cellular automaton** is \((d,S,N,f)\): dimension \(d\), finite state set \(S\), neighborhood \(N\subseteq\mathbb Z^d\) (\(|N|=\nu\)), and local rule \(f:S^\nu\to S\); the global map \(F:S^{\mathbb Z^d}\to S^{\mathbb Z^d}\) applies \(f\) uniformly. Size is measured by \((|S|,\nu)\) (and \(d\)); for 1D radius-\(r\) CAs \(\nu=2r+1\). **Elementary CAs** are \(d=1,|S|=2,r=1\) (256 rules, Wolfram numbering).

**Universality notions (state the one you use).**
- **Computational (weak) universality.** There is a computable encoding of instances of a fixed universal problem into configurations of \(F\) - typically a **spatially periodic background** with a finite engineered perturbation - such that the orbit of \(F\) simulates the computation and a decodable halting/output condition holds. The encoding must be simple (not itself performing the computation).
- **Computational (standard) universality.** As above but from a finite/quiescent-background configuration, no engineered infinite background.
- **Intrinsic universality.** \(F\) simulates every CA (of a stated class) under a space-time rescaling ("bulking"): with block size \(m\), packing time \(T\), and offset, there is an encoding \(\beta:S'\to S^{m}\) such that for every CA \(G\) in the class,
\[
\beta\circ G\ =\ F^{T}\circ\beta \quad\text{(on the block-coded configurations)},
\]
so every \(G\)'s orbit appears verbatim inside \(F\)'s orbit. Strictly stronger than computational universality and the right notion for a robust "smallest universal CA."

**The open questions.**
1. **Smallest universal CA per notion.** The minimal \((|S|,\nu,d)\) admitting a universal CA - for computational universality (Rule 110 is 1D/2-state/3-neighbor, weak), for intrinsic universality (known small intrinsically-universal CAs exist but minimality is open), and for standard-background universality.
2. **(Non)universality of specific small rules.** For a named small rule (an elementary rule, a small 2-state radius-1 2D rule, a specific totalistic rule), decide whether it is universal (in a stated notion) or **non-universal** because its dynamics are decidable/simple (nilpotent, eventually periodic, bounded-communication, or with a decidable prediction problem).

**Deliverables in scope.**
1. A certified universality proof for a specific small CA under a named notion.
2. A certified **non-universality** / decidability result for a specific small rule, extending the proven-simple region.
3. A smaller universal construction (fewer states/neighbors, or a stronger notion at the same size) with a certified simulation.

## 2. Resolution standard

A result resolves a case only in certified form.

- **Certified universality.** For a specific CA \(F\) and a named notion, a **certified simulation proof**: a machine-checkable argument (Coq/Rocq, Lean, or a checked structured proof) that \(F\) simulates a fixed universal system - a specific universal machine, a cyclic/2-tag system, Rule 110, or (for intrinsic universality) a universal CA family - with the encoding, the (periodic) background, and the space-time rescaling fully specified and the simulation step-faithful, including the halting/output correspondence. The encoding's **simplicity** is itself a certified lemma.
- **Certified non-universality / decidability.** For a specific small rule, a proved decision procedure for its prediction/reachability problem, or a proved structural property (nilpotency, eventual periodicity, finite communication complexity, a subshift-of-finite-type invariant) that **precludes** universality - a total algorithm or theorem with a correctness proof, formalized where feasible.
Formally, a computational-universality certificate is a machine-checked simulation
\[
\forall x:\quad \mathcal S(x)\!\downarrow\ \Longleftrightarrow\ \exists t\ \bigl(F^{t}(\mathrm{enc}(x))\ \text{satisfies the halt predicate}\bigr),
\]
with \(\mathrm{enc}\) certified simple and the background \(b\) an explicit hypothesis; an intrinsic-universality certificate proves the bulking identity above for a universal class.

- **Named certified form.** A **certified universality construction** (checked simulation of a fixed universal system, notion and background explicit) or a **formally verified decision procedure / structural non-universality proof** for a specific rule.

**Not accepted as resolution.**
- A rule "believed universal" from glider/collision catalogues, with no simulation proof.
- A construction that quietly relies on an infinite engineered background while claiming **standard** universality - the weak-vs-standard trap (as with small UTMs).
- An encoding that performs part of the computation (the "cheating encoding" objection); simplicity must be certified.
- Conflating **computational** with **intrinsic** universality - a Rule-110-style simulation does not establish intrinsic universality.
- A non-universality claim from simulation ("rule looks simple") rather than a proved decision procedure or structural theorem.
- Silent neighborhood/state-set convention changes to shrink \((|S|,\nu)\).
- A non-universality claim that only rules out *one* notion (e.g. "not intrinsically universal") while implying the rule is simple in every sense.
- A bulking simulation with an unstated or unbounded packing time \(T\), or a block encoding that is not itself simple.

## 3. Graded partial-result targets

**P1 - Reproduce Rule 110's universality with a checked simulation.** Formalize (or write a replayable structural checker for) Cook's simulation of cyclic tag systems by Rule 110:
- reproduce the glider collisions and the periodic "ether" background in the simulator;
- state the periodic background and glider encoding as explicit hypotheses, labeled **weak**;
- check the step-faithful correspondence between glider events and cyclic-tag steps.

*Certificate:* a machine-checked (or replayably-checked) simulation of a cyclic tag system, with the background as an explicit hypothesis. Validates the pipeline and the notion discipline.

**P2 - Certify a known small intrinsically-universal CA.** Take a known small intrinsically-universal CA (1D, small radius):
- specify the block encoding \(\beta\), block size \(m\), and packing time \(T\);
- prove the bulking identity \(\beta\circ G=F^{T}\circ\beta\) for the universal target class;
- confirm on sampled member CAs in the simulator.

*Certificate:* a checked simulation of a universal CA family under an explicit rescaling.

**P3 - Certified non-universality of a specific small rule.** For a named elementary rule (or small 2D rule) whose dynamics are simple:
- prove a decision procedure for its prediction problem, or
- prove a structural theorem (nilpotency, eventual periodicity, finite communication complexity) that precludes universality;
- confirm the rule genuinely sits below the frontier under the stated notion.

*Certificate:* a proved-total decision procedure or a machine-checked structural theorem, with an enumeration confirming class coverage where applicable.

**P4 - Certify a candidate small rule as universal.** For a specific small rule conjectured universal (a totalistic rule, a small radius-1 2D rule):
- catalogue its gliders/backgrounds and design an encoding of a fixed universal system;
- prove the step-faithful simulation and the halting correspondence;
- prove the encoding-simplicity lemma and name the notion (weak / standard / intrinsic).

*Certificate:* checked simulation + certified encoding-simplicity lemma.

**P5 - A smaller / stronger universal construction.** Exhibit a universal CA at an \((|S|,\nu,d)\) improving on the current frontier for a stated notion. Candidate wins:
- a smaller **intrinsically**-universal CA (fewer states or smaller neighborhood);
- an intrinsically-universal CA matching a size where only **computational** universality was known;
- a standard-background universal CA where only weak universality was known.

*Certificate:* the rule, the simulation certificate, the notion and overhead \((m,T)\), and a citation of the frontier improved with source and access date.

**P6 - Frontier / classification artifact.** A certified table over a small rule family (e.g. all elementary rules, or all 2-state radius-1 2D outer-totalistic rules):
- tag each rule as proved universal (notion + simulated system), proved non-universal (decision procedure / structural theorem), or open;
- index per-rule proof objects so an auditor can replay any cell;
- state the size measure so cells are comparable.

*Certificate:* per-rule proof objects indexed and replayable, with the notion fixed per column.

## 4. Known results and prior art

**This area moved a lot recently - web-verify every attribution below before a session.**

- **Rule 110 universal** - conjectured by Wolfram (~1985), proved (weakly) computationally universal by **Matthew Cook** (announced ~1998–2002; full proof "Universality in Elementary Cellular Automata", Complex Systems ~2004) via simulation of **cyclic tag systems** through glider collisions on a periodic background. (verify)
- **Intrinsic universality** - Ollinger, Richard, Boyer, Delorme, Theyssier and others constructed small intrinsically-universal 1D CAs and studied the notion via bulking/simulation preorders; the *minimal* size for intrinsic universality (states × neighborhood) is not settled. (verify names/results)
- **Non-universality / decidability** - nilpotency of CAs is undecidable in general (Kari), but *specific* small rules have decidable prediction problems; Wolfram-class-1/2 rules (eventually periodic / simple) are non-universal, and many elementary rules are provably simple. Communication-complexity and de Bruijn-graph methods classify small rules. (verify)
- **Game of Life** - 2D, outer-totalistic; computationally universal (glider-gun / logic-gate constructions) and known intrinsically universal; a reference point for 2D minimality. (verify)
- **Surveys** - Ollinger's "Universalities in cellular automata" survey; the small-UTM survey (Woods–Neary) for the parallel weak-vs-standard discussion. (verify)
- **Weak-vs-intrinsic caution** - the same encoding-simplicity and background subtleties that dog small UTMs apply here; a weak computational-universality result is not intrinsic universality and not standard-background universality. (verify)
- **Wolfram classes** - the informal class 1/2/3/4 taxonomy is a heuristic, not a proof of (non)universality; class-4 "complex" rules are candidates, class-1/2 rules are non-universal targets, but each needs a certificate. (verify)
- **Higher-radius / multi-state small CAs** - beyond elementary, the frontier includes small \((|S|,\nu)\) 1D rules and small 2D outer-totalistic rules; the minimal intrinsically-universal size across these families is the live open quantity. (verify)

Status as of mid-2026 - re-verify against the current literature and record trackers before starting any session. Intrinsic-universality minimality and small-rule classifications are the entries most likely to have advanced.

## 5. Attack plan

`[search]`, but the deliverable is a proof; one workstation suffices.

1. **Simulation harness.** Use **Golly / lifelib** (and a custom 1D radius-\(r\) simulator) to run candidate rules, catalogue gliders/backgrounds, and prototype encodings; represent periodic backgrounds symbolically. Reproduce Rule 110 glider collisions to validate the pipeline (P1).
2. **Fix the simulated system.** For computational universality, target cyclic tag systems or a specific tiny UTM (a clean, formalization-friendly source). For intrinsic universality, fix a universal CA family and design the block/rescaling encoding.
3. **Certified simulation.** In Coq/Rocq or Lean:
   - define \(F\), the encoding, the background, and the invariant relating orbits to the simulated system;
   - prove step-faithfulness and the halting/output correspondence;
   - prove encoding-simplicity as a lemma to defeat the cheating-encoding objection;
   - print the axiom set and confirm it is empty.
4. **Non-universality direction (P3).** For a target small rule, search for a decidability/structural certificate:
   - a de Bruijn-graph / subshift-of-finite-type invariant on the space-time diagram;
   - bounded communication complexity of the prediction problem;
   - a nilpotency or eventual-periodicity proof;
   - a finite reachability closure of the reachable local patterns;
   then prove totality/correctness and enumerate the rule class (canonical forms under state/reflection symmetry) to confirm coverage.
5. **Frontier push (P5).** Attempt a smaller or stronger construction; measure size by \((|S|,\nu,d)\) under one fixed notion and compare against the cited frontier.

**Failure modes.** (a) Notion drift - conflating weak/standard/intrinsic universality; every claim must name the notion. (b) Cheating encodings - an encoding doing the computation makes universality vacuous; certify simplicity. (c) Zoology-not-proof - a glider catalogue is evidence, not a simulation proof. (d) Background smuggling - an infinite engineered background presented as standard universality. (e) Non-universality mirage - "the rule looks simple" is not a decision procedure. (f) Kernel-trust - print the axiom set of any formal proof.

## 6. Verification and auditability requirements

1. **Exact or certified computation:** universality via a machine-checked simulation proof (notion, background, encoding, rescaling explicit; encoding-simplicity a lemma; axiom set printed), non-universality via a proved-total decision procedure or a checked structural theorem; simulator output is exploration only.
2. **Independent verification:** every artifact re-checked apart from the search:
   - each certified simulation re-run by an independent simulator (Golly/lifelib and a custom engine) on sampled inputs;
   - the decoded outputs confirmed against the simulated system's own reference implementation;
   - each decision procedure cross-checked by a separate enumeration/replay;
   - a second proof assistant used where the construction warrants it.
3. **Reproducibility:** rule (state set, neighborhood, local table), notion, background, encoding, simulated system, simulator and proof-assistant versions recorded; SHA-256 manifest over rules, proofs, and logs; any improved frontier cited with source and access date.
4. **Preservation:** simulator/encoding source, proof scripts, and the classification index are part of the record; anything not preserved is stated explicitly.
5. **Honest reporting:** state up front the universality notion, the simulated system, the background, and whether the result is a new frontier point, a certified reproduction, or a non-universality theorem; a weak computational-universality result is never reported as intrinsic or standard-background universality, and a glider catalogue is never reported as a universality proof.
