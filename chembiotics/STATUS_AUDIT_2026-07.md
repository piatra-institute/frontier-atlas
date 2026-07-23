# Chembio status audit - July 2026

**Why this file exists.** The eight chembiotics prompt-writing agents each finished writing their prompts but were killed by a session limit *before* returning their end-of-run "which of these may already be solved" summaries - the same audit the physics batch delivered. This file reconstructs that audit directly: a main-loop pass plus targeted web searches (July 2026) on the problems where a 2024–2025 result could plausibly have moved the target.

**Headline.** None of the 50 problems is resolved. But this is the field the `STRATEGY.md` warned about: most Pack B entries (and several Pack A) are *accuracy-ceiling* problems where "solved" is a moving benchmark, not a QED. On several, the **SOTA baseline moved decisively in 2025** - a session must re-baseline against the results below before claiming any contribution, or it will "beat" a baseline that is already two generations stale. Re-baseline ≠ resolved.

## WATCH - verified 2025 movement, re-baseline before the session

| # | Problem | What moved (2025) | Still open? |
|---|---------|-------------------|-------------|
| B01 / B04 | Non-coding variant effect / regulatory genome | **AlphaGenome** (DeepMind, 2025): unified 1-Mb DNA→function model, SOTA on **25/26 variant-effect** and **22/24 genome-track** tasks. It is now *the* baseline to beat; the old Enformer/Borzoi framing in the prompts is stale. | Yes - causal effect is still wet-gated (MPRA/reporter), accuracy on unseen enhancers unsolved. Problem open; **baseline changed**. |
| A21 | 2D Hubbard ground state | Two 2025 NQS results - Pfaffian-based hidden-fermion states (arXiv 2511.07566) and transformer NQS (arXiv 2507.02644, Nat. Commun. 2026) - resolved much of the metallic/stripe/superconducting **energetics**; SC found to coexist with partially-filled stripes for next-neighbor hopping t′ < −0.1; half-filled stripe in the ground state at the studied coupling. | Yes - "does the ground state superconduct" is still called a major open question. **Graded targets must re-baseline against these energies.** |
| B20 | De novo enzymes at natural k_cat/K_M | **RFdiffusion2** zinc metallohydrolases (Nature 2025) to k_cat/K_M ≈ 5.3×10⁴; de novo **serine hydrolases** to ≈ 2.2×10⁵ M⁻¹s⁻¹, approaching natural (~10⁵). | Yes - and the prompt's framing is *confirmed*: most gain is from binding (lower K_M); **k_cat still 1–3 orders below natural**. The open gap is now specifically the catalytic-*rate* gap. Update the prompt's target numbers. |
| A12 / A13 | Boltzmann-weighted sampling / conformational ensembles | **Transferable Boltzmann Generators** (2025) now generalize beyond their training set with reweighting; a wave of AF2-based generative ensemble models (flow/diffusion). | Yes - general Boltzmann-correct ensembles for arbitrary systems unsolved; fast-moving, **re-baseline the generator SOTA**. |
| A05 | Universal ML force field at CCSD(T) | Foundation MLIPs (MACE-lineage) + transfer-learning/fine-tuning now reach CCSD(T) accuracy on **specific domains** routinely (2025). | Yes - *universal, transferable across all chemical space* is still open. P3 (domain fine-tune to CCSD(T)) is now near-standard practice; raise the bar. |
| A15 | Absolute binding free energy < 1 kcal/mol | 2025 protocols (OneOPES ~1 kcal/mol MUE; QM/MM ~0.60 kcal/mol MAE on some sets; Felis/ByteFF toolkits). | Yes - and this **confirms the prompt's benchmark-integrity clause**: experimental reproducibility RMSE is ≈ 0.95–1.34 kcal/mol, so "sub-kcal/mol vs experiment" is at the *experimental noise floor*. The honest target is a converged, cycle-closed method, not chasing sub-noise agreement. |

## VERIFIED STILL OPEN - checked, no concern

- **B05 (RNA 3D structure).** CASP16 (2025) assessment: RNA prediction remains poor - **no unseen natural RNA above TM-score 0.8**, AlphaFold3 included; success only where experimental templates exist; top groups were human experts. The prompt's "clearest next AlphaFold, data-limited" framing is accurate. No change.

## Not individually re-checked this pass - standard per-prompt re-verify applies

The remaining 42 problems (A01–A04, A06–A11, A14, A16–A20; B02–B03, B06–B19, B21–B29) showed no known resolution as of this audit and were not individually web-searched. Every one carries the mandatory "Status as of mid-2026 - re-verify against current literature before starting any session" line; that check is not optional, especially for the accuracy-ceiling Pack B entries where a new model can reset the baseline between now and a session. Two standing cautions:

- **Accuracy-ceiling problems** (most of Pack B, plus A02 retrosynthesis, A17 MSM automation): treat "SOTA has moved" as the default expectation, not a surprise. The audit target is always "beat the *current* baseline on a leakage-safe split," and the current baseline drifts monthly.
- **Design problems** (B20–B25): 2025 raised in-silico success rates but the wet-lab-gate is unchanged - an improved filter is still a hypothesis until an assay closes it.

## What this audit did not do

This is a main-loop reconstruction with ~7 targeted searches, not the per-problem sweep the eight agents would have produced. The six WATCH rows are grounded in the searches above; the 42 unchecked problems rest on my knowledge plus the built-in re-verify rule. A fuller web-backed sweep over all 50 is worth running once agent capacity resets (limit reset 11:30 Europe/Bucharest) - but no prompt is wrong or unusable in the meantime; the WATCH items need *re-baselining*, not rewriting.

**Sources for the WATCH findings:**
- AlphaGenome - [Nature 2025](https://www.nature.com/articles/s41586-025-10014-0), [bioRxiv 2025.06.25.661532](https://www.biorxiv.org/content/10.1101/2025.06.25.661532v1.full)
- Hubbard NQS - [arXiv 2511.07566](https://arxiv.org/abs/2511.07566), [arXiv 2507.02644](https://arxiv.org/abs/2507.02644)
- De novo enzymes - [Baker Lab serine hydrolases, Science 2025](https://www.bakerlab.org/wp-content/uploads/2025/02/science.adu2454.pdf), [metallohydrolases, Nature 2025](https://www.nature.com/articles/s41586-025-09746-w)
- RNA / CASP16 - [Assessment of nucleic acid structure prediction in CASP16, bioRxiv 2025](https://www.biorxiv.org/content/10.1101/2025.05.06.652459v2.full), [AlphaFold3 at CASP16](https://onlinelibrary.wiley.com/doi/10.1002/prot.70044)
- Boltzmann generators - [Transferable Boltzmann Generators, OpenReview 2025](https://openreview.net/forum?id=AYq6GxxrrY)
- Foundation MLIP - [Fine-tuning unifies foundation MLIPs at ab initio accuracy, arXiv 2511.05337](https://arxiv.org/pdf/2511.05337)
- Absolute binding FE - [Optimizing ABFE for production, ChemRxiv 2025](https://chemrxiv.org/doi/full/10.26434/chemrxiv-2025-q08ld-v2), [maximal accuracy of rigorous BFE, Commun. Chem. 2023](https://www.nature.com/articles/s42004-023-01019-9)
