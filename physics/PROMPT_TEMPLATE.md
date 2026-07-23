# PROMPT TEMPLATE - Piatra Institute physics program

Each attempt subfolder (`NN_slug/`, inside a task) contains one `prompt.md` following this structure exactly. Sections may grow, none may be dropped.

---

# PROMPT FOR <TARGET THEOREM OR DETERMINATION>

## <One-line subtitle naming the problem area>

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** NN of 50 (Tier T)
**Source:** top-50 list #K, category <A-H, name>
**Modes:** `[search]` `[cert]` `[sym]` `[bound]` `[proof]` *(keep only the applicable tags)*

### Abstract

One paragraph: the problem, why it matters (utility or adjacent utility), and why it is matched to current AI methods. State that the complete resolution defined in section 2 is the target, and anything less is reported as a partial result, never as a solution.

## 1. Exact problem statement

Full mathematical definitions and the precise statement of the open question. Fix notation, spaces, and normalizations. If several inequivalent formulations circulate, state the one adopted here and why. No informal phrasing is an acceptable target.

## 2. Complete-resolution standard

What counts as a complete resolution: the exact object(s) to produce, the proofs required, and in what form. Then a list titled **Not accepted as resolution**: the weakened, restricted, numerical-only, or heuristic claims that must not be represented as solving the problem.

## 3. Graded partial-result targets

An ordered list P1, P2, … of independently valuable, certifiable milestones, from most accessible to strongest-short-of-resolution. Each carries its own certificate standard (what artifact proves it, and how it is independently checked). These are the realistic product of a session.

## 4. Known results and prior art

Best current theorems, bounds, exact data, and methods, with named references (authors and approximate year where confident; never fabricated identifiers). **Status as of mid-2026 - re-verify against the current literature before starting any session.**

## 5. Attack plan

Concrete first computations per mode tag: encodings (SAT/SMT/MILP), CAS pipelines (Gröbner bases, resultants, series analysis), interval arithmetic, symbolic mining of exact data, formalization targets. State what runs on a single workstation, and the expected failure modes.

## 6. Verification and auditability requirements

Every claimed result must satisfy:

1. **Exact arithmetic** (rational, algebraic, or interval with directed rounding) wherever a claim depends on it; floating point is for exploration only, never certification.
2. **Independent verification:** for each certificate, a small standalone checker written independently of the search code; dual implementations (Python and C++) where warranted.
3. **Reproducibility:** all inputs, seeds, parameters, and environment recorded; SHA-256 manifest over every artifact.
4. **Preservation:** search and construction source code is part of the record. Anything not preserved is stated explicitly.
5. **Honest reporting:** the report states up front whether the complete-resolution standard was met, and never represents a partial, restricted, or numerical result as the full resolution.
