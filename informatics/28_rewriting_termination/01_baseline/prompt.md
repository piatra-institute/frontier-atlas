# PROMPT FOR A CERTIFIED TERMINATION VERDICT ON AN OPEN TERM-REWRITING SYSTEM

## Settling a TPDB problem no tool has decided - with a CeTA-checked CPF certificate

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 28 of 50  
**Area:** computation models & automated reasoning  
**Modes:** `[cert]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

A term-rewriting system (TRS) terminates if it admits no infinite rewrite sequence. Termination is undecidable in general, yet a large industry of automated provers - driven by the annual **Termination Competition** over the **Termination Problems Data Base (TPDB)** - decides thousands of systems, and, crucially, emits **machine-checkable certificates** in the **CPF** (Certification Problem Format) that the formally-verified checker **CeTA** (extracted from the Isabelle/HOL library **IsaFoR**) independently validates. A residue of TPDB problems remains **open**: no competing tool proves termination or non-termination. This prompt targets one such open TRS (or a specific open derivational-complexity question) and asks for a **certified verdict**: a termination or non-termination proof rendered as a CPF certificate that CeTA accepts. That closes the loop with a formally-verified checker - the strongest ground truth in the atlas. Anything short - an uncertified prover "YES/NO", a proof CeTA rejects, or a hand argument without a CPF rendering - is a partial result. The problem is a decidability frontier: some open TPDB systems are genuinely hard (their termination encodes deep combinatorics), so honest calibration is required.

## 1. Exact problem statement

Fix the model precisely; TPDB spans several rewriting formats.

A **first-order term-rewriting system** over a signature \(\mathcal F\) (function symbols with arities) and variables \(\mathcal V\) is a finite set \(R\) of rules \(\ell\to r\) with \(\ell,r\in \mathrm{Term}(\mathcal F,\mathcal V)\), \(\ell\notin\mathcal V\), and \(\mathrm{Var}(r)\subseteq\mathrm{Var}(\ell)\). The **rewrite relation** \(\to_R\) is the closure of \(R\) under substitution and context: \(s\to_R t\) iff \(s=C[\ell\sigma]\), \(t=C[r\sigma]\) for some context \(C\), substitution \(\sigma\), rule \(\ell\to r\). \(R\) is **terminating** (strongly normalizing, SN) iff there is no infinite chain \(t_0\to_R t_1\to_R\cdots\).

Equivalently, \(R\) is terminating iff \(\to_R\) is a **well-founded** relation:
\[
\mathrm{SN}(R)\ \Longleftrightarrow\ \neg\,\exists\,(t_i)_{i\in\mathbb N}\ \forall i:\ t_i\to_R t_{i+1}.
\]
The standard route to a *proof* is a reduction order \(\succ\) (a well-founded, stable, monotone strict order) with \(\ell\succ r\) for every rule; the dependency-pair framework refines this into a modular chain of processors.

**Variants in TPDB (state which one).** plain TRS; **relative** termination \(R/S\) (no infinite \(\to_R\)-step-containing chain modulo \(S\)); **string rewriting** (SRS, unary signature); **innermost** termination; **context-sensitive**; **higher-order**; **conditional**; and **complexity** categories (derivational or runtime complexity bounds). The **derivational complexity** of a terminating \(R\) is \(\mathrm{dc}_R(n)=\max\{\,k : t_0\to_R^{k} t_k,\ |t_0|\le n\,\}\); questions ask the exact asymptotic class (linear/polynomial/exponential) for a specific system.

**The open target.** An **open TPDB problem** is a benchmark for which, at the latest Termination Competition, no participating tool produced an accepted (certified or even uncertified, per category) YES (terminating) or NO (non-terminating) verdict - it remains "open"/"maybe". Fix one such problem \(P\) (a specific `.trs`/`.srs`/`.xml` benchmark with a stable TPDB identifier) or a specific open derivational-complexity question. **The task:** produce a certified verdict for \(P\).

## 2. Resolution standard

A result resolves \(P\) only as a **certified verdict**.

- **Certified termination.** A termination proof of \(P\) expressed as a **CPF certificate** - built from methods in CeTA's supported repertoire (reduction pairs / interpretations: polynomial, matrix, arctic; dependency-pair framework with processors: dependency graph, reduction-pair, usable rules, subterm criterion; root-labeling, semantic labeling, RFC match-bounds; rule removal) - that **CeTA accepts** (returns CERTIFIED). Certificate: the CPF file + CeTA's acceptance + CeTA/IsaFoR version.
- **Certified non-termination.** A non-termination proof as a CPF certificate - a **loop** (a rewrite sequence \(t\to^+ C[t\sigma]\)) or a certified **non-looping** non-termination witness (via the supported strategies/derivation constructions) - that CeTA accepts.
- **Certified complexity bound.** For a derivational/runtime-complexity target, a CPF complexity certificate (a proved upper bound with a matching family for the lower bound) that CeTA accepts, pinning the exact complexity class.
The trust chain is explicit: a prover emits a CPF proof \(\pi\); CeTA (a Haskell program extracted from the Isabelle/HOL library IsaFoR, whose soundness theorems are machine-checked) decides
\[
\textsf{CeTA}(R,\pi)\in\{\textsf{CERTIFIED},\ \textsf{REJECTED}\},
\]
and \(\textsf{CERTIFIED}\) entails the stated termination/non-termination/complexity property by an Isabelle-proved soundness theorem. The deliverable is a \(\pi\) with \(\textsf{CeTA}(R,\pi)=\textsf{CERTIFIED}\).

- **Named certified form.** A **CeTA-accepted CPF certificate** (a formally-verified termination / non-termination / complexity proof). The verdict is only as strong as CeTA's acceptance; an uncertified prover claim is never the deliverable.

**Not accepted as resolution.**
- A prover (AProVE/TTT2/matchbox/NaTT/…) printing YES/NO with **no** CPF certificate, or with a CPF certificate CeTA **rejects**.
- A verdict backed only by a resource-limited run ("no infinite reduction found in \(N\) steps") rather than a proof.
- A hand proof not rendered into a CeTA-checkable certificate (unless it is itself formalized in Isabelle/IsaFoR and merged, which is an acceptable alternative certified form - state it).
- Solving a *modified* system (different strategy, added/removed rule, wrong format) and claiming the original benchmark.
- A complexity **upper** bound with no matching lower-bound family (or vice versa) presented as the exact class.
- An unreplayable tool run (missing versions, seeds, resource limits) - the certificate must replay to CERTIFIED on a clean machine.
- Confusing category: an *innermost*-termination certificate does not settle *full* termination, etc.
- A certificate that certifies only under a private, modified CeTA build whose extra soundness lemmas are not themselves machine-checked.
- A "termination" claim for a benchmark whose TPDB identifier or format was silently altered.

## 3. Graded partial-result targets

**P1 - Reproduce the certified pipeline.** Take several *already-solved, already-certified* TPDB benchmarks:
- re-run a prover (AProVE/TTT2/matchbox) to emit CPF and confirm CeTA returns CERTIFIED;
- deliberately corrupt a certificate (flip an interpretation coefficient) and confirm CeTA REJECTS;
- record the exact CeTA/IsaFoR and prover versions.

*Certificate:* a log of CeTA verdicts with versions. Validates the toolchain and the trust base.

**P2 - Certify an uncertified-but-decided benchmark.** Find a benchmark that some tool decides but only *without* a certificate (a known YES/NO lacking a CeTA-accepted proof):
- reproduce the tool's verdict and extract the underlying argument;
- re-express it using CeTA-supported methods and emit CPF;
- confirm CeTA CERTIFIED.

*Certificate:* the CPF file + CeTA CERTIFIED. Real progress: converts folklore into certified fact.

**P3 - New certified termination of an open TRS.** For a chosen open TPDB termination problem, engineer a proof from CeTA-supported methods and get CeTA to accept it:
- try a well-chosen matrix/arctic interpretation (raise the dimension until the constraints are satisfiable);
- or a DP-framework decomposition with usable rules and a bespoke ordering on the residual dependency pairs;
- document the method chain and confirm CeTA CERTIFIED.

*Certificate:* CPF + CeTA CERTIFIED + the method chain documented.

**P4 - New certified non-termination of an open TRS.** For a chosen open problem believed non-terminating:
- search for a **loop** \(t\to^+ C[t\sigma]\) by bounded unfolding / narrowing (AProVE, NTI);
- if no loop exists, search for a certified **non-looping** non-termination witness via the supported strategy/derivation constructions;
- render the witness as CPF and confirm CeTA acceptance.

*Certificate:* CPF + CeTA CERTIFIED + the explicit looping context/substitution (or the non-looping derivation).

**P5 - Certified derivational-complexity class.** For a specific open complexity question, pin the exact class:
- an interpretation-based CPF **upper**-bound certificate (e.g. a matrix interpretation giving a polynomial bound), CeTA-accepted;
- a hand-built **lower**-bound witness family \((t_n)\) with \(|t_n|=O(n)\) and \(\mathrm{dc}_R(n)\) matching the upper class;
- confirm the two meet.

*Certificate:* both CPF certificates (where CeTA supports the complexity category) + the witness family.

**P6 - Formalized bespoke method (windfall).** If an open problem needs a technique outside CeTA's repertoire:
- formalize the method and its soundness theorem in IsaFoR (Isabelle/HOL);
- extend CeTA's certificate grammar and checker to the new method;
- certify the verdict with the extended, re-verified CeTA.

*Certificate:* the Isabelle development (soundness proved) + the new certificate accepted by the extended CeTA; upstreaming to IsaFoR is the gold standard.

## 4. Known results and prior art

**This area moved a lot recently - web-verify tool versions, the open-problem list, and CeTA's supported methods before a session.**

- **Termination Competition (annual; termCOMP)** - decides TPDB benchmarks across TRS-standard, relative, SRS, innermost, complexity, and certified tracks; the **certified** categories require CeTA-accepted CPF. Re-check the most recent edition's results and its list of unsolved/open benchmarks. (verify latest year and open list)
- **AProVE** (RWTH Aachen; Giesl et al.) - the leading termination/complexity prover; DP framework, many processors; emits CPF. (verify)
- **TTT2** (Tyrolean Termination Tool 2; Innsbruck) - termination prover with CPF output. (verify)
- **matchbox** (Waldmann) - specializes in string rewriting and matrix/automata methods (match-bounds, weighted automata); strong on hard SRS. (verify)
- **NaTT, MU-TERM, NTI, MnM, AutoNon** - further competition tools (runtime complexity, non-termination, context-sensitive). (verify)
- **CeTA / IsaFoR** (Innsbruck; Thiemann, Sternagel, et al.) - the formally-verified certifier, extracted from the Isabelle/HOL library IsaFoR; **CPF** is its input format (arXiv 1410.8220 for the format). Its supported-method set grows over time - verify what it currently certifies (interpretations, DP processors, semantic/root labeling, match-bounds, loops, non-looping non-termination, complexity). (verify)
- **Recent work** - non-termination certification via strategies and non-looping derivations (CeTA experiments page); ongoing Agda-based "Cetera" certified-termination efforts (Hofbauer–Waldmann, ~2025). (verify)
- **Certified categories** - termCOMP runs dedicated *certified* tracks (certified TRS termination, certified complexity) where only CeTA-accepted CPF counts; the residue of benchmarks unsolved *even without* certification is the hardest open set. (verify)
- **Undecidability backdrop** - termination is \(\Pi^0_2\)-complete in general, so no tool can be complete; the open benchmarks persist because they need a method outside the current automated portfolio. (verify)

Status as of mid-2026 - re-verify against the current literature and record trackers (termCOMP results, the TPDB repository, the CeTA/IsaFoR changelog) before starting any session. The set of "open" benchmarks and CeTA's method coverage both drift year to year.

## 5. Attack plan

`[cert]`. One workstation suffices; the provers and CeTA all run locally.

1. **Stand up the trust base (P1).** Install CeTA (or build from IsaFoR), AProVE, TTT2, and matchbox; pull the current TPDB; confirm the certified pipeline on solved benchmarks and confirm CeTA rejects corrupted CPF.
2. **Pick an open target.** From the latest termCOMP unsolved list, choose a benchmark in a category CeTA certifies:
   - start with SRS or plain TRS, where matchbox/AProVE + CeTA are strongest;
   - read the rules and run small-scale rewriting to guess a likely verdict (terminating vs non-terminating);
   - prefer benchmarks whose likely proof method CeTA already supports.
3. **Termination search (P3).** Drive AProVE/TTT2/matchbox with method portfolios aimed at *certifiable* proofs:
   - matrix and arctic interpretations of increasing dimension (SAT/SMT-backed coefficient search with proof output);
   - the dependency-pair framework with usable rules, dependency graph, and the subterm criterion;
   - match-bounds and weighted-automata methods (matchbox) for SRS;
   - force CPF output and feed every candidate to CeTA, iterating until CERTIFIED;
   - where automation stalls, hand-craft an interpretation/ordering and encode it as CPF directly.
4. **Non-termination search (P4).** Search for loops (bounded unfolding / narrowing; AProVE and NTI's loop detection) and render the loop as CPF; for suspected non-looping non-termination, use the supported strategy-based constructions.
5. **Complexity (P5) and formalization (P6).** For complexity targets:
   - combine an interpretation-based upper-bound certificate with a hand-built lower-bound family;
   - if a needed method is uncertified, extend IsaFoR/CeTA (Isabelle/HOL) - a larger but decisive effort;
   - keep every extension's soundness theorem machine-checked so the trust base is not weakened.

**Failure modes.** (a) YES/NO without a certificate - the dominant trap; an uncertified prover verdict is not the deliverable. (b) CeTA rejection - the prover's proof uses a method or detail CeTA does not accept; either change methods or extend CeTA. (c) Undecidability wall - some open benchmarks are open because they are genuinely hard; recognize when to switch targets rather than burn a session. (d) Format/strategy drift - solving the wrong variant (innermost vs full, relative vs plain). (e) Interpretation blow-up - high-dimension matrix searches explode; bound dimensions and use SAT/SMT-backed interpretation search with proof output. (f) Version skew - a certificate that certifies under one CeTA build must be reported with that exact version.

## 6. Verification and auditability requirements

1. **Exact or certified computation:** the load-bearing artifact is a **CeTA-accepted CPF certificate** (or a merged IsaFoR formalization); a prover's YES/NO is exploration only until CeTA certifies it; complexity claims require both bound directions.
2. **Independent verification:** CeTA *is* the independent checker, and additionally:
   - re-run the certificate on a clean machine with a pinned CeTA build;
   - confirm CeTA rejects a deliberately corrupted variant of the certificate;
   - where feasible obtain a second tool's independently-certified proof of the same benchmark;
   - for non-termination, re-execute the loop witness directly in a standalone rewriter.
3. **Reproducibility:** the exact TPDB benchmark identifier, prover versions and invocation, resource limits, CPF file, and CeTA/IsaFoR version recorded; SHA-256 manifest over benchmark, certificate, and logs; the benchmark's prior "open" status cited with the termCOMP edition and access date.
4. **Preservation:** the CPF certificate, prover configuration/source where available, any bespoke interpretation or IsaFoR extension, and the CeTA verdict logs are part of the record; anything not preserved is stated explicitly.
5. **Honest reporting:** state up front whether CeTA returned CERTIFIED, in which category and under which versions, and whether the benchmark was previously open (with the termCOMP citation). An uncertified verdict, or one CeTA rejects, is never reported as settling the problem; a wrong-variant result is flagged as such.
