# Claim

**Claim.** A valid superpermutation on 6 symbols of length **873** was constructed (max-overlap greedy) and verified (all 720 permutations occur as length-6 substrings). This does **not** beat, or even match, the known record: 867 <= s(6) <= 872 (upper bound Houston). The greedy is optimal for n <= 5 (it reproduces 1, 3, 9, 33, 153 exactly) but gives 873 = sum_{k<=6} k! for n=6, one above the record. No new result on s(6).

**Checker.** `python3 src/superperm.py 6` rebuilds and verifies; `verify(s,6)` scans every length-6 window and confirms all 720 permutations are present. The string is `superperm_n6.txt`. Re-run 2026-08-01: valid=True, 0 missing, length 873.

**Trust base.** Exact substring scan over an explicit string; no solver, no floating point. A superpermutation witness is self-certifying (anyone can re-scan it).

**Encoding fidelity.** Superpermutation = a string over {1..n} containing every one of the n! permutations as a contiguous length-n substring; s(n) is the minimal length. The verifier checks exactly this.

**Review level.** self. Not human-refereed.

**Provenance.** Claude Code (Opus), 2026-08-01. Greedy construction + exact verifier written and run here.

**Cost and attempts.** Local, seconds. One max-overlap greedy construction; no ATSP / Chaffin-method search was run. Matching 872 (let alone beating it toward 867) needs a dedicated search, not plain greedy. Denominator: a single construction, no search sweep.
