---
id: vine-nsewwss-d10-horizontal-circuit-distance
result_class: B1
statement: >-
  For the NSEWWSS d=10 horizontal Vine-code construction in Table 2, with lattice vectors v1=[38,38], v2=[28,0], code parameters [[557,6,10]], and the supplied syndrome-extraction circuit, the circuit distance is exactly 10 (the table conjectures d_X=d_Z=d_circuit=10).
source:
  primary_locator: >-
    Georgia M. Nixon, Campbell K. McLauchlan, and Charles C. L. van Rest, “Vine Codes: Low-Overhead Quantum LDPC Codes on a Planar Square Grid,” arXiv:2606.20263v1, Table 2, https://arxiv.org/html/2606.20263v1#S3. Supplement: Zenodo record 20746752, Vine_code_files.zip, reported MD5 24bf2c5d721214eb1be7407c64f8c224, https://zenodo.org/records/20746752.
  access_date: 2026-08-02
  status_evidence: >-
    The June 2026 source explicitly marks the d=10 circuit distances as conjectural/extrapolated. Exact-title, arXiv-ID, code-family, and table-row searches on 2026-08-02 found no later certified circuit-distance result.
baseline:
  current_value_or_range: >-
    Table 2 reports routing qubits 236 -> 140 and total physical qubits 1248 for this row; smaller patches underpin the extrapolation. The Zenodo archive was identified but could not be downloaded in this environment (rate/network failure), so internal circuit filenames and exact-distance tooling are not frozen.
  replay_command: >-
    python checkers/check_vine_distance.py fixtures/vine_horizontal_preflight.json
witness:
  format: >-
    Frozen Stim circuit or detector-error-model file identified by archive path and SHA-256, plus either (a) <=9 circuit faults producing an undetected nontrivial logical observable, or (b) a proof certificate excluding all <=9 faults and a weight-10 logical fault set.
  checker_command: >-
    python checkers/check_vine_distance.py fixtures/vine_horizontal_preflight.json
  checker_hash: sha256:92aa4e912fb5dc2ad089f0beabf8f2fc39a69e4a1084be36f4b67e9a4e6210f3
  calibration_cases: >-
    dependency/artifact preflight: fixtures/vine_horizontal_preflight.json; no positive or near-miss distance instance is available without the archive; malformed: fixtures/malformed.json; frontier: this exact Table 2 row is unresolved.
search_edge: >-
  Freeze the Stim detector error model, split X/Z mechanisms, quotient detector/fault variables by lattice symmetries, and solve exact minimum logical fault weight with MILP/SAT or tensor-network dynamic programming, emitting a small fault set or proof log. This is an explicit route, but neither the archive grammar nor an end-to-end certified solver benchmark is presently available.
budget:
  model: "GPT-5.6 Pro plus Stim and exact MILP/SAT"
  wall_clock: "24 h"
  cpu_gpu: "32 CPU cores; optional GPU for tensor contraction"
  memory: "128 GB"
stop_rules: >-
  Stop immediately if the statement/status changes or the baseline cannot be replayed. Freeze on disagreement between two independent implementations. Require a method review after 20% of budget without new structural information; pause after a repeated plateau with no new representation; kill if measured growth exceeds the forecast by 4x. Do not attack until the archive file, hash, circuit-to-DEM command, one smaller known distance, and independent verifier are frozen.
publication_path: >-
  Georgia M. Nixon, Campbell K. McLauchlan, and Charles C. L. van Rest; quantum error correction / quantum LDPC code community and the Zenodo artifact maintainers.
aliases: ["vine-horizontal-d10", "nsewwss-horizontal-circuit-distance"]
---

# vine-nsewwss-d10-horizontal-circuit-distance

**Admission label:** `needs-edge`  
**Gate count:** 5/9 green  
**Scout rank:** 12 of 17 (ordinal judgment; no score total)

## Admission gates

| # | Gate | State | Evidence |
|---:|---|:---:|---|
| 1 | Statement pinned | GREEN | Exact Table 2 row and success condition d_circuit=10 pinned. |
| 2 | Primary source pinned | GREEN | arXiv table and Zenodo record/checksum pinned. |
| 3 | Open status fresh | GREEN | Fresh source and searches found no certification. |
| 4 | Artifact grammar fixed | RED | Red: archive-internal circuit filename and canonical DEM conversion are not frozen. |
| 5 | Checker exists and calibrated | RED | Red: current checker is only a preflight; no distance proof is verified. |
| 6 | Baseline reproduces | RED | Smaller-patch baseline and exact row are not replayed. |
| 7 | Search edge stated | RED | Symmetry/MILP/tensor edge is unbenchmarked and depends on missing artifact grammar. |
| 8 | Budget and stop rule fixed | GREEN | 24-hour resources and artifact-first stop rule fixed. |
| 9 | Scientific path named | GREEN | Authors and QEC validation route named. |

## Priority vector

`[5, 3, 4, 4, 5, 2, 4, 2]` in the fixed order: open-status confidence, reachability, method advantage, witness/lemma plausibility, scientific value, verification quality, competition penalty, end-to-end cost.

| Dimension | Score | Evidence |
|---|:---:|---|
| open-status confidence | 5 | Very fresh explicitly conjectural table row. |
| reachability | 3 | Distance 10 is small, but circuit fault hypergraphs may be large. |
| method advantage | 4 | Geometry symmetry and exact optimization could beat heuristic extrapolation. |
| witness/lemma plausibility | 4 | A <=9 fault witness would be compact; confirmation is harder. |
| scientific value | 5 | A corrected hardware-overhead table is publishable frontier data. |
| verification quality | 2 | Currently weak until circuit/DEM and proof verifier are frozen. |
| competition penalty | 4 | Recent niche code family, moderate QEC attention. |
| end-to-end cost | 2 | High setup/memory cost compared with graph cards. |

## Scout notes

Result class is B1 because the target is a finite table datum. A refutation is a <=9 logical fault set; confirmation requires an exact lower-bound certificate plus a weight-10 logical.

## Deep-attack admission consequence

Do not allocate deep compute. Build and benchmark the stated search edge and reproduce the source baseline; where gate 5 is red, finish the independent checker before any generation/search.
