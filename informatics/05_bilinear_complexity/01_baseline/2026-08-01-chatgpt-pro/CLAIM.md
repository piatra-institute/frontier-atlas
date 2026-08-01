# Claim

**Claim.** Over \(\mathbb F_2\), the ordinary tensor rank of the matrix-multiplication tensor

\[
\langle2,2,3\rangle\in
\mathbb F_2^{2\times2}\otimes
\mathbb F_2^{2\times3}\otimes
\mathbb F_2^{3\times2}
\]

is exactly

\[
R_{\mathbb F_2}(\langle2,2,3\rangle)=11.
\]

This is a certified reproduction of a known value, not a new result. No claim is made over \(\mathbb Q\), \(\mathbb R\), or for border rank.

**Checker.** From the artifact directory, run:

```bash
./verify_all.sh
```

The script first checks `MANIFEST.sha256`, then verifies the upper and lower bounds. Principal bound artifacts:

- `decomposition.json`  
  SHA-256 `c92c56d638a303dc15365c7b3bf42cc55f14236a2936e6075d321e164b795279`
- `certificates/backtracking_full.json`  
  SHA-256 `b9f1970a4b475d00f0bd44726397256138cc46e4fcab05264c2669c84153a241`
- `certificates/backtracking_orbit7.json`  
  SHA-256 `3ed0d02185d24522975d1c4e2968c3856fb681e81dc99aebacb2acc8d331ed60`
- `orbits.json`  
  SHA-256 `b19dffbf6fb0aadbf32b63a3f58c0f0a549b2773fec77c85f50dccd0d00781b6`

Pinned tested toolchain: Python 3.13.5, G++ 14.2.0, C++17, GNU coreutils 9.7.

**Trust base.** Exact bit arithmetic over \(\mathbb F_2\); finite Gaussian elimination; flattening rank lower bounds; the elementary two-slice matrix-rank identity; exhaustive enumeration of every \(6\times6\) binary matrix of rank at most 2 around three centers; the substitution inequality; and a finite prefix-complete decision-tree replay. No floating point and no external solver oracle are used.

**Encoding fidelity.** `decomposition.json` fixes all coordinate orders and the 144 target coefficients. `orbits.json` fixes the four-bit restriction encoding. `verify_upper.py` reconstructs the target tensor directly from matrix multiplication. `verify_lower.py` independently reconstructs all 67 restriction subspaces, their 11 \(\mathrm{GL}_2(\mathbb F_2)^2\) orbits, each restricted tensor, and every tree closure. These are the small human-auditable encoding artifacts.

**Review level.** agent.

**Provenance.** GPT-5.6 Pro selected the target field after prior-art checking, proposed the explicit decomposition, reconstructed the finite restriction proof, and authored the generator and checkers. Independent exact Python and C++ executions confirmed the tensor identity, all finite-field inputs, orbit census, restricted bounds, rank-metric enumeration, and both substitution trees. The retrieved upstream certificate is preserved only as a provenance cross-check and is not in the verifier's trust path.

**Cost and attempts.** One field pivot; two subspace encodings, of which the first was rejected; one upper construction; two two-slice analyses, including one rejected overclaim; two generated substitution trees; one independent replay. Recorded certificate generation and the three checker runs totaled 9.46 seconds wall time, excluding compilation, with approximately 112 MB peak resident memory and no external paid compute. Model-token and currency spend are not exposed by the runtime.
