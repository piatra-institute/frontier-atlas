# PROMPT TEMPLATE - Piatra Institute informatics program

Each attempt subfolder (`NN_slug/`, inside a task) contains one `prompt.md` following this structure. Theoretical-CS problems are closed-loop (a proof, an exact/SAT-certified search, an exhaustive enumeration, or a machine-checked construction settles a claim), so every prompt carries a genuine *resolution* standard. Sections may grow, none may be dropped.

---

# PROMPT FOR <TARGET THEOREM, VALUE, OR OPTIMAL OBJECT>

## <One-line subtitle naming the problem>

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** NN of 50
**Area:** <algorithms & bilinear complexity · Boolean & cryptographic functions · complexity & communication · computation models & automated reasoning · discrete dynamics & pattern search · quantum computation & codes · search, sequences & games>
**Modes:** `[search]` `[cert]` `[enum]` `[sym]` `[opt]` `[proof]` *(keep only the applicable tags)*

### Abstract

One paragraph: the problem, why it matters (foundational or adjacent utility: algorithms, cryptography, verification, quantum hardware), and why it is matched to current AI methods (certified/SAT search, exhaustive enumeration, symbolic/algebraic computation, computer-assisted proof, bound optimization). Name the on-machine verifier that closes the loop. State that anything short of the section-2 standard is a partial result, never a solution.

## 1. Exact problem statement

Full definitions and the precise statement of the open question. Fix the model of computation, the cost measure (comparators, gates, multiplications, states, T-count, distance…), the size regime, and any normalization. If several inequivalent formulations circulate, state the one adopted here and why. No informal target is accepted.

## 2. Resolution standard

The exact object(s) or theorem to produce and the certified form of proof (a DRAT/LRAT-checked UNSAT proof for an optimality lower bound; an explicit construction with an independently-checked cost; an exhaustive isomorph-free enumeration; a formal Lean/Coq proof; an exact rational LP/SDP certificate). Then a list titled **Not accepted as resolution**: the weakened, heuristic, numerical-only, or single-instance claims that must not be represented as solving the problem (e.g. a good construction with no matching lower bound; an unreplayable solver run; asymptotic hand-waving where an exact value is asked).

## 3. Graded partial-result targets

Ordered milestones P1, P2, … from "reproduce the known frontier with our own verified toolchain" up to "strongest result short of full resolution". Each carries its own certificate standard (what artifact proves it, how it is independently checked). These are the realistic product of a session.

## 4. Known results and prior art

Best current values, bounds, records, and methods, with named references (authors and approximate year where confident; never fabricated arXiv IDs, DOIs, or page numbers; mark uncertain items "(verify)"). CS records move fast: busy beaver, sorting networks, matrix-multiplication decompositions, and Life constructions have all shifted in 2023-2025. **Status as of mid-2026 - re-verify against the current literature (and record trackers) before starting any session.**

## 5. Attack plan

Concrete first computations per mode tag, naming real tools: SAT/SMT/MaxSAT with proof logging (CaDiCaL, kissat, CryptoMiniSat → DRAT/LRAT); exhaustive/canonical search (nauty/Traces, bliss, orderly generation); CAS and algebra (SageMath, GAP, Magma-if-available, Macaulay2/Singular, flip-graph search for tensor rank); interval/exact arithmetic (Arb/FLINT); ILP/LP with exact certificates (SCIP, QSopt_ex/SoPlex); quantum tooling (Qiskit, Stim, PyZX, gridsynth/feynman for T-count); model-of-computation harnesses (busy-beaver deciders / bbchallenge tooling, Golly/lifelib for cellular automata, AProVE/TTT2 for rewriting termination, automata libraries); and Lean 4 / Coq for formalization. State what fits on one workstation and the expected failure modes (search blow-up, unverified solver output, canonicity bugs).

## 6. Verification and auditability requirements

1. **Exact or certified computation** for any load-bearing claim (SAT proof traces, exact/interval arithmetic, isomorph-free completeness, formally checked proofs); floating point is for exploration only.
2. **Independent verification:** for each certificate a small standalone checker written separately from the search code (a DRAT/LRAT checker, an enumeration replay, a cost re-evaluator, a second solver); dual implementations where warranted.
3. **Reproducibility:** all encodings, seeds, solver versions, and environment recorded; SHA-256 manifest over every artifact; the baseline record being improved is cited with source and access date so the claimed gain is unambiguous.
4. **Preservation:** search and construction source code is part of the record. Anything not preserved is stated explicitly (the Hadamard-668 lost-source lesson).
5. **Honest reporting:** the report states up front whether the resolution standard was met, whether a record was strictly improved, and in which model; a heuristic optimum or an unreplayable search is never represented as a certified result.
