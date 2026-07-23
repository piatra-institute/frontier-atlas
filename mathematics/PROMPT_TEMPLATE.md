# PROMPT TEMPLATE - Piatra Institute mathematics program

Each attempt subfolder (`NN_slug/`) contains one `prompt.md` following this structure (tasks 12-50 were seeded from it). The existing #01-#11 predate the template and keep their original prompt documents. Sections may grow, none may be dropped.

Maths problems are closed-loop (a proof, an exact certificate, or an exhaustive search settles a claim), so every prompt carries a genuine *resolution* standard.

---

# PROMPT FOR <TARGET THEOREM, VALUE, OR DETERMINATION>

## <One-line subtitle naming the problem>

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** NN of 50
**Area:** <Ramsey/extremal · additive · discrete geometry · graph theory · designs & codes · number theory & algebra · order & extremal set systems>
**Modes:** `[search]` `[cert]` `[enum]` `[sym]` `[opt]` `[proof]` *(keep only the applicable tags)*

### Abstract

One paragraph: the problem, why it matters (foundational or adjacent utility), and why it is matched to current AI methods (certified/SAT search, exact enumeration, symbolic mining, computer-assisted proof, bound optimization). State that the resolution standard in section 2 is the target, and anything less is reported as a partial result, never as a solution.

## 1. Exact problem statement

Full definitions and the precise statement of the open question. Fix notation, ground field/ring, indexing, and normalizations. If several inequivalent formulations circulate, state the one adopted here and why. No informal phrasing is an acceptable target.

## 2. Resolution standard

What counts as a complete resolution: the exact object(s) or theorem to produce, the proof required, and in what certified form (DRAT/LRAT for SAT, Gröbner/Positivstellensatz for algebraic non-realizability, interval arithmetic for geometric optima, a formal Lean proof, or an exhaustive isomorph-free enumeration). Then a list titled **Not accepted as resolution**: the weakened, numerical-only, single-case, or heuristic claims that must not be represented as solving the problem.

## 3. Graded partial-result targets

Ordered milestones P1, P2, … from "reproduce the known frontier with our own verified toolchain" up to "strongest result short of full resolution". Each carries its own certificate standard (what artifact proves it, and how it is independently checked). These are the realistic product of a session.

## 4. Known results and prior art

Best current theorems, bounds, exact data, and methods, with named references (authors and approximate year where confident; never fabricated arXiv IDs, DOIs, or page numbers; mark uncertain items "(verify)"). **Status as of mid-2026 - re-verify against the current literature before starting any session** (bounds and records drift; several nearby problems fell in 2019-2024).

## 5. Attack plan

Concrete first computations per mode tag: SAT/SMT encodings (CaDiCaL, kissat, CryptoMiniSat with DRAT proofs), exact enumeration and isomorph rejection (nauty/Traces, orderly generation), CAS pipelines (SageMath, Pari/GP, Macaulay2/Singular, SymPy, Gröbner/resultants), interval arithmetic (Arb/FLINT), integer-relation search (PSLQ/LLL with honest multiple-testing discipline), and Lean 4 + mathlib formalization targets. State what runs on a single workstation and the expected failure modes.

## 6. Verification and auditability requirements

1. **Exact or certified computation** for any claim that depends on it (SAT proof traces, exact rational/algebraic arithmetic, interval enclosures with directed rounding, isomorph-free completeness arguments); floating point is for exploration only, never certification.
2. **Independent verification:** for each certificate, a small standalone checker written independently of the search code (a DRAT checker, an enumeration replay, a second CAS); dual implementations where warranted.
3. **Reproducibility:** all inputs, encodings, seeds, and environment recorded; SHA-256 manifest over every artifact.
4. **Preservation:** search and construction source code is part of the record. Anything not preserved is stated explicitly (the Hadamard-668 lost-source lesson).
5. **Honest reporting:** the report states up front whether the resolution standard was met, and never represents a partial, restricted, or numerical result as the full resolution.
