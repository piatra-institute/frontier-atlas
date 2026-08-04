# Frontier log

Living record of external results that resolve, advance, or sit adjacent to atlas problems, plus internal rescopes. The atlas targets open problems, and this class turns over fast (three AI-assisted events in the two weeks below, several adjacent to the atlas). `SOLVER.md` requires re-verifying a problem's status before investing; this log is where that drift is tracked. Re-verify against primary sources before acting on any entry: statuses here are dated and decay.

## Status legend

- `claimed` - announced, not yet examined here.
- `read-abstract` - abstract or summary read here (possibly via a summarizing tool), not full text.
- `read-full` - full argument read here, not independently re-derived.
- `checked` - re-derived or re-ran a verifier here.
- `community-confirmed` - independently refereed or accepted by the field.

A Lean certificate proves a formal statement has a machine-checked proof. It does not prove the formal statement matches the informal claim, nor that the target was open. Those checks stay human: statement-match, was-it-open, refereeing.

## External results (post-build)

### 2026-08-03 - Fournier-Facio, "A torsion-free non-sofic group" (corroborates OpenAI result #3)

- Source: arXiv:2608.02025, Francesco Fournier-Facio, posted 2026-08-03 (paper header renders 2026-08-04).
- Abstract, verified here 2026-08-04: OpenAI announced a non-sofic group, the unit group of the
  binary Leavitt algebra; this paper exhibits a different source of examples "relying on the same
  technical criterion", including torsion-free groups.
- Why it matters: an independent specialist reused the criterion within about two days and got a
  strictly stronger object (torsion-free). Short of refereeing, this is the strongest available
  evidence that OpenAI result #3 is real, and it is evidence of the criterion's reusability rather
  than of the specific group. Upgrades #3 to community-engaged; still not refereed.
- Not verified here: that the proof builds on Kun and Kun-Thom (search summary only, not checked
  against the PDF); the MathOverflow explanation by Andreas Thom (q. 513866, mathoverflow.net is
  not fetchable from this environment); the "page 78" locator. All second-hand via an r/math thread.
- Atlas impact: none closed. The impact is methodological, see below.
- Status: `read-abstract`.

#### Method lessons (internal rescope, applied to `discovery/targets/SCOUT_PROMPT.md`)

1. **A cheap checker is a lane label, not a value filter.** This witness is one line (a Leavitt
   algebra over F_2, take its unit group) and its certificate is a long proof, so admission gate 5
   as written would have rejected the problem. Cheap-checkability selects for what a machine can
   verify, not for what a machine can discover. Corroborated internally: the 2026-08-02 scout
   screened 43 candidates, admitted 1, and that one (signed circulants) proved true through n=24.
2. **Do not blanket-avoid famous problems.** Non-soficity is a roughly 25-year Gromov-Weiss
   problem and heavily watched. It fell because the community's candidate objects (Higman's group,
   non-residually-finite central extensions of higher-rank lattices, HNN extensions) were the wrong
   region, not because nobody looked. Fame is not the disqualifier; an exhausted construction space is.
3. **The mechanism is cross-domain transfer.** Leavitt algebras and Thompson's group V (ring theory,
   operator algebras) imported into geometric group theory. Field-siloed problem lists hide these.
4. **Target what unlocks a list.** Non-soficity existence reopens Gottschalk surjunctivity,
   Kervaire-Laudenbach, the determinant conjecture, and L^2-Betti approximation, all previously known
   only for sofic groups. Score downstream unlock, not just isolated value.
5. **It composed existing human machinery**, it did not invent from nothing. The fast-follower lane
   (apply a fresh public criterion to object classes its authors did not test) is the part of this
   pattern reachable at our budget; Fournier-Facio executed exactly that in about two days.
- Adjacent and still open: a non-hyperlinear group (would give an explicit group-based counterexample
  to Connes embedding; if finitely presented, consequences in quantum information).

### 2026-08-01 - OpenAI, "Ten Advances in Mathematics and Theoretical Computer Science"

- Source: openai.com/index/ten-advances-in-mathematics + paper cdn.openai.com/pdf/ten-proofs-oai.pdf.
- Method: internal model ("Astra"); ~$2000 of tokens at Sol API rates; human-prepared manuscripts; each argument formalized in a Lean certificate.
- Results (asymptotic bounds, disproofs, constructions):
  1. Sphere packing: Cohn-Elkies LP exponent pinned, `limsup Δ_d^{1/d} ≤ √(e/2π)` (α*=0.6044, first improvement since 1978).
  2. Binary/spherical codes: exponential-factor upper-bound improvement, all parameters.
  3. Non-sofic groups: explicit construction (existence), the unit group of the binary Leavitt
     algebra. Corroborated 2026-08-03 by an independent specialist reusing the criterion, see the
     entry above; this is the only one of the ten with outside engagement recorded here.
  4. Connes rigidity: disproof.
  5. Permanent: `Ω(n²loglog n)` division-free circuits, `Ω(n⁴/log n)` arithmetic formulas.
  6. Quantum parallel repetition: exponential repetition for finite two-player entangled games.
  7. Closest vector problem: `n^{1/400}` hardness via 3SAT.
  8. Ehrhart volume: sharp `(n+1)^n/n!` in every dimension (full resolution).
  9. Multicolor Ramsey: `R_k(3) = k^{Θ(k)}` (Erdős 183).
  10. Compactness and degeneracy: disproofs (Erdős 146, 180).
- Atlas impact: none closed. Checked the four closest problems:
  - `mathematics/15_ramsey_multicolor_3333` - result #9 is asymptotic in k; the specific R(3,3,3,3) value (bracket 51..62) is untouched. Survives.
  - `mathematics/35_optimal_binary_codes` - result #2 is asymptotic; a specific open Brouwer-table cell is not settled. Survives.
  - `mathematics/06_kissing_number_11` - result #1 is a high-dim LP exponent; a finite kissing value is untouched. Survives.
  - `informatics/47_arithmetic_circuits`, `informatics/20_formula_lower_bounds` - result #5 is asymptotic + algebraic (and Boolean-formula-free); both prompts are exact-finite (and /20 is Boolean De Morgan). Different models. Survive.
  - Pattern: OpenAI's ten are all asymptotic; the atlas is exact-finite with on-machine certificates. The regimes are near-disjoint.
- Status: `read-full` for front matter + ten-item abstract + Chapter 1; `read-abstract` for chapters 2-10. Lean certificates claimed, not independently checked here. Statement-match, was-it-open, and refereeing pending.
- Flag: OpenAI's Oct-2025 "GPT-5 solved 10 Erdős problems" claim was retracted ("open" meant one curator did not personally know the solution; known work reproduced). This paper is better hedged and Chapter 1 reads as rigorous, but the retraction is why the human checks above are not optional.

### 2026-07 - Maxwell conjecture disproved

- Claim: Gabrielov-Novikov-Shapiro form (≤ `(n-1)²` non-degenerate equilibria for n point charges) is false.
- Source: arXiv:2607.27197v1, Arathoon, Ball, Kvalheim, "The Maxwell Conjecture is False" (dated 29 Jul 2026).
- Result: five charges (unit triangle plus two tuned axial charges, `q_ε = (3/4)ε³ − (5/32)ε⁵`) give at least 24 non-degenerate critical points; `(5-1)²=16`. The central equilibrium bifurcates into 21; three edge equilibria persist.
- Method: construction suggested by an LLM (OpenAI GPT-5.6 Sol); details verified by the authors and by Mathematica/Maple.
- Atlas impact: not in the atlas (grepped physics + mathematics). Now settled, so it cannot enter as an open problem.
- Still open: the `n=3` case (is 4 the max?), and the sharp bound as a function of n. A re-scoped "certify max equilibria for n=3, or improve the general bound" prompt would fit.
- Status: `read-full` (6-page paper), not independently re-derived.

### 2026-mid - Ziegler cross-polytope conjecture disproved

- Claim: for simplicial 0/1-polytopes, `2d` vertices in dimension d does not force central symmetry.
- Source: arXiv:2606.31640, Kaibel, Pokutta, "A Counterexample to Ziegler's Cross-Polytope Conjecture for Simplicial 0/1-Polytopes."
- Result: explicit 14 vertices in `{0,1}^7`, convex hull a simplicial 7-polytope, not centrally symmetric; exactly five such polytopes in dimension 7.
- Method: agentic framework, arXiv:2603.15914 (Zimmer, Pelleriti, Roux, Pokutta, "The Agentic Researcher"). Per the authors' post, a stalled Lean formalization localized the counterexample; this mechanism is a narrative account, not stated in the abstract read here.
- Atlas impact: not in the atlas (grepped). Now settled.
- Status: `read-abstract` (WebFetch summary of both abstracts, small-model), not full-text. The post's "local open-weight models (DeepSeek V4 flash + GLM 5.2)" claim is uncorroborated by the framework abstract, which describes any frontier LLM via CLI agents.

## Build-time rescopes

Several problems were rescoped at build time because they had already been resolved, rather than removed: busy beaver BB(5), Wang tiles / Jeandel-Rao, Life omniperiodicity, the sensitivity conjecture (Huang), Dejean, Hall-Paige, PCP with 5 provers. See each program's `STRATEGY.md` and `chembiotics/STATUS_AUDIT_2026-07.md`. Re-verify before use.
