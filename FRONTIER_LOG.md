# Frontier log

Living record of external results that resolve, advance, or sit adjacent to atlas problems, plus internal rescopes. The atlas targets open problems, and this class turns over fast (four AI-assisted events in the two weeks below, several adjacent to the atlas). `SOLVER.md` requires re-verifying a problem's status before investing; this log is where that drift is tracked. Re-verify against primary sources before acting on any entry: statuses here are dated and decay.

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

### 2026-07-29 - Lin-Li, "Settling the Optimal Exponent Relating Sumsets and Difference Sets"

- Source: arXiv:2607.27199v1, Haowei Lin (Tencent Hunyuan), Shanda Li (Carnegie Mellon), 29 Jul 2026,
  8 pages. Adjacent arXiv ID to the Maxwell disproof below, same day.
- Claim: for finite nonempty `A` in an abelian group, `sigma(A) = |A+A|/|A|` and
  `delta(A) = |A-A|/|A|` satisfy the classical `sigma^(1/2) <= delta <= sigma^2`. The exponent 2 was
  known optimal; whether the exponent 1/2 could be improved was open. Writing
  `C(A) = log sigma(A) / log delta(A)`, so that `C(A) <= 2` always, they construct an explicit
  `A_K` in Z for every positive even K with `C(A_K) > 2K/(K+3)`. Hence `sup C(A) = 2` and the
  exponent 1/2 is optimal too. Corollary 2.1: the supremum is approached but never attained, by
  Staps' characterization of the equality cases.
- Construction: a base-12 digit gadget `W = {0,1,2,4,5,9}`, a three-state carry automaton, a
  symmetric additive basis `I = H union V` in `Z/QZ` with `s = 2^K + 1` and `Q = s^2`, glued by the
  Chinese remainder theorem with `d = 22(K+2)`, `n = 12^d`, `q = Qn`.
- Method: Hyra (Tencent Hunyuan research agent, Hy3 model) run about 24 hours under the SimpleTES
  framework, with GPT-5.6 Sol as an exploration judge that the authors state was "used only to guide
  exploration, not to certify mathematical correctness". The authors then independently checked the
  construction, corrected the exposition, and prepared the argument manually. GPT-5.6 Sol was used
  separately to convert the natural-language proof to Lean 4, at
  github.com/linhaowei1/sum-diff-proof (repo exists, language Lean, pushed 2026-07-30).
- Checked here 2026-08-06, independent Python re-derivation, all pass: `(W+W) mod 12 = Z/12Z` and
  `(W-W) mod 12 = Z/12Z minus {6}`; the integer difference set `W-W` exactly as printed; `t_j` by
  brute-force enumeration of `Y_j` giving 1, 11, 127, 1475, 17143, matching both the recurrence
  `t_{j+2} = 13 t_{j+1} - 16 t_j` and closed form (5) to machine precision; the carry automaton
  reproduced exactly as `M = [[5,3,3],[4,5,3],[4,4,4]]` with no unlisted nonempty images, and
  `(M^2 - 13M + 16I)1 = 0`; Lemma 2.4 for K = 2, 4, 6, 8; and Lemmas 2.5, 2.6, 2.7 together with the
  size formula (14) exactly, on five scaled-down `(K,d)` instances. Not checked here: the Lean
  development, and the Penman-Wells normalization claim below (only that Lin-Li assert it).
- Extraction caveat: `pdftotext` drops superscripts and renders `s = 2^K + 1` as `2K+1`, which
  contradicts the paper's own `2^K = 1 (mod 3)` and `alpha = 2^(K+1-d)` steps. Confirmed against
  arxiv.org/html/2607.27199v1. Read the HTML for this paper, not extracted PDF text.
- Atlas impact: nothing closed. Nearest relative is
  `discovery/pipelines/21_additive_small_sets/PROMPT.md`, which sweeps the same quantities (`|A+A|`,
  `|A-A|`, sum-vs-difference balance, doubling constant) by exhaustive enumeration of
  `A` in `{0..24}`. For the sigma/delta exponent question specifically that window is provably empty:
  see the scale note below. The pipeline's other targets (minimal MSTD sets, Sidon, Davenport) are
  genuinely small-set questions and survive.
- Status: `checked` for sections 2.1-2.5 and the size formula; `read-full` for the rest.

#### Method lessons (the most directly useful external result the atlas has logged)

Table 1 of the paper is a complete public ledger of AI agents attacking exactly the kind of target
this atlas hunts: maximize a scalar over finite integer sets, cheap exact checker, clean baseline.

| date | method | value |
|---|---|---|
| 1969 | Marica (human) | 1.0290 |
| 1973 | Freiman-Pigarev (human) | 1.0598 |
| 2013 | Penman-Wells (human) | 1.1259 |
| 2025-11 | AlphaEvolve, Gemini 2.0 Pro + Flash | 1.1219 |
| 2025-12 | LoongFlow, DeepSeek-R1-250528 | 1.1035 |
| 2026-04 | SimpleTES, gpt-oss-120b (with post-training) | 1.1449 |
| 2026-07 | OpenHands / OpenClaw / Codex / EvoMaster, GPT-5.4 | 1.0786 - 1.1207 |
| 2026-07 | Claude Fable 5 (manuscript-internal) | 1.1133 |
| 2026-07 | Codex GPT-5.5 with human guidance (manuscript-internal) | 1.2851 |
| 2026-07 | explicit family `A_K`, Hyra with Hy3 (this paper) | `sup C(A) = 2` |

1. **A published AI-math headline sat below a 2013 human construction.** AlphaEvolve
   (Georgiev, Gomez-Serrano, Tao, Wagner) baselined on Freiman-Pigarev 1.0598 and reported 1.1219;
   Lin-Li state that Penman-Wells had 1.1259 under the same normalization. This is exactly the
   wrong-baseline failure the atlas's verification discipline exists to catch, now recorded in the
   highest-profile AI-mathematics program there is. Asserted by Lin-Li, not independently confirmed
   here. Practical rule: pin the incumbent record from the literature before scoring any agent run
   against it, and treat a baseline supplied by the generator as unverified.
2. **The search region was provably wrong, not merely under-explored.** SimpleTES scores `C(A)`
   from an explicitly enumerated Python list, so memory caps the set size. The smallest even K whose
   bound beats every prior record is K=4, giving `2K/(K+3) = 1.1429` with `d = 132` and
   `|A_K|` about `10^143`. No enumeration reaches that, ever. Eight agent systems ground out
   1.079 to 1.145 inside a window that could not contain the answer. Before running a search, ask
   what size the extremal object plausibly has; if the answer is "unbounded", enumeration is not an
   approach, it is a way to produce a plateau.
3. **What broke it was dropping the enumerable-witness evaluator.** The authors explicitly relaxed
   SimpleTES to let agents "propose constructions and supporting arguments in natural language",
   and that is the run that produced the theorem. Lane A cheap-checkability was the binding
   constraint, not the enabler.
4. **Generator is not verifier, stated by the authors themselves.** An LLM judge guided exploration;
   correctness came from human checking plus Lean. Their section 3 is a usable template for
   reporting AI involvement honestly, and worth copying.
5. **Second Lane B breakthrough in one week.** With Fournier-Facio (2026-08-03) above, both genuine
   AI-assisted advances logged here came from proof-shaped certificates and would have failed
   admission gate 5 as originally written. The 2026-08-04 rescope of `SCOUT_PROMPT.md` was directed
   at the right thing; this entry says the correction was not strong enough. The lever is not volume
   of cheap Lane A triage. It is working in natural-language construction space against a proof
   obligation, and spending computation on verification rather than on search.

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
