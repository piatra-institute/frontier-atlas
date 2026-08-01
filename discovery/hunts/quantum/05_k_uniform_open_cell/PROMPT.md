# A k-uniform state at an open cell

**Find:** a k-uniform pure state of n qudits of local dimension d, for a triple (n,d,k) with k < floor(n/2) whose existence is undetermined.

## What counts as a win
An explicit |psi> in (C^d)^{tensor n} whose every k-party reduced density matrix is maximally mixed. One-sided: existence closes the cell. (k-uniform generalises AME, which is the k = floor(n/2) case.)

## Checker
For every subset S of k parties, compute rho_S and verify rho_S = I / d^k exactly. Amplitudes in a small number field make this exact rational/algebraic linear algebra; the number of k-subsets is polynomial. Runtime: seconds.

## Search plan
Construct from classical codes: a k-uniform state follows from an orthogonal array OA of strength k, or from an [[n,0,k+1]] additive/stabilizer structure over the relevant alphabet. For cells with no classical construction, optimise a graph/hypergraph-state or tensor-network ansatz numerically for the uniformity defect, then reconstruct exact amplitudes. Stabilizer search over GF(d) for prime-power d.

## Prior art (verify)
Existence tables for k-uniform states have open cells, especially where classical orthogonal arrays do not exist (Scott 2004; Goyeneche-Zyczkowski; and later k-uniform tables, e.g. Huber-Wyderka). Confirm the chosen (n,d,k) is still open.
