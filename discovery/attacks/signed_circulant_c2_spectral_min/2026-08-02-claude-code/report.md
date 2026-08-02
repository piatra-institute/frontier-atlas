# Signed circulant C_n(1,2): independent verification and extension of Conjecture 3

**Target.** `discovery/targets/signed-circulant-c2-global-spectral-minimum` (scout card).
**Source.** Suvagiya, "Signed circulants at the Ramanujan bound," arXiv:2607.18334v1,
2026-07-19, Conjecture 3.

## The conjecture

`C_n(1,2)` is the 4-regular circulant on `Z/nZ` with edges of steps 1 and 2. For an edge
signing, `A_sigma` is the signed adjacency matrix and `rho(A_sigma)` its spectral radius.
Conjecture 3: for every even `n >= 8`,

    min_sigma rho(A_sigma) = rho_-(n) = 2*sqrt(cos(pi/n)^2 + cos(2*pi/n)^2),

achieved by the alpha = -1 twisted switching class. The source verifies this exhaustively
through `n = 18`.

## What this run did

Independent re-implementation (`verify_extend.py`), not importing the scout checker:
spanning-tree gauge, batched `eigvalsh`, own bit indexing. For each order it enumerates all
`2^(n+1)` switching classes, takes the minimum spectral radius, and compares to `rho_-(n)`;
any class below `rho_-(n) - 1e-9` would be reported as a counterexample.

## Results

| n | switching classes | min spectral radius | rho_-(n) | abs err | verdict | time |
|---:|---:|---|---|---:|---|---:|
| 8  | 512         | 2.326846269604655 | 2.326846269604654 | 8.9e-16 | holds | 0.0s |
| 10 | 2,048       | 2.497212040956834 | 2.497212040956833 | 8.9e-16 | holds | 0.0s |
| 12 | 8,192       | 2.594619588218836 | 2.594619588218835 | 8.9e-16 | holds | 0.0s |
| 14 | 32,768      | 2.654979724879704 | 2.654979724879703 | 8.9e-16 | holds | 0.2s |
| 16 | 131,072     | 2.694804747545854 | 2.694804747545853 | 8.9e-16 | holds | 0.8s |
| 18 | 524,288     | 2.722402271489240 | 2.722402271489240 | 4.4e-16 | holds | 3.7s |
| 20 | 2,097,152   | 2.742288646612572 | 2.742288646612570 | 1.8e-15 | holds | 18.8s |
| 22 | 8,388,608   | 2.757080523468867 | 2.757080523468866 | 4.4e-16 | holds | 87.1s |
| 24 | 33,554,432  | 2.768375418932017 | 2.768375418932016 | 1.3e-15 | holds | 416.5s |

- `n = 8..18`: agrees with the source and with the scout checker to machine precision (the
  two independent implementations match on the full overlap). This is the cross-check.
- `n = 20, 22, 24`: new orders the source did not publish. The conjecture holds at each; the
  minimizer is the alpha = -1 twist in every case; no counterexample.

## Honest status

This is **not** a resolution. It extends the exhaustive finite verification from `n = 18` to
`n = 24` and independently confirms the source's own range. The conjecture is a statement about
all even `n`; enumeration cannot close it. Value: an author-absorbable confirmation note, and
each held order lowers the prior on a counterexample at a reachable size (i.e., the "find a
counterexample" outcome looks less likely, as expected for a clean closed-form conjecture with
a stated extremal mechanism).

The realistic brute-force ceiling on this host is about `n = 26-28` (2^27 to 2^29 classes). A
genuine step would be either (a) an exact bandwidth-2 transfer-matrix / threshold recurrence
that decides the minimum in time polynomial in `n` (which could yield an all-`n` proof), or
(b) targeted large-`n` structured families where a counterexample, if any, would live. Neither
is done here.

## Replay

    python3 verify_extend.py 8 10 12 14 16 18 20 22 24
