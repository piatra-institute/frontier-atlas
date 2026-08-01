# A Butson Hadamard matrix at an open cell

**Find:** a Butson-type complex Hadamard matrix BH(n,q) (all entries qth roots of unity, H H* = n I) for a pair (n,q) whose existence is undetermined in the small-parameter tables.

## What counts as a win
An explicit n x n matrix with entries in the qth roots of unity satisfying H H* = n I. One-sided: existence closes the cell.

## Checker
Represent entries as exponents in Z_q. Verify H H* = n I by exact arithmetic over the cyclotomic integers Z[zeta_q]: every off-diagonal inner product of rows is a vanishing sum of qth roots of unity, checkable exactly, and every diagonal equals n. Runtime: milliseconds to seconds.

## Search plan
Encode the row-orthogonality (vanishing sums of roots of unity) as constraints over Z_q and solve by SAT/CP or orderly generation with isomorph rejection (monomial equivalence). Use difference-matrix and generalised-Hadamard constructions over abelian groups as seeds. Vanishing-sum classification (Lam-Leung) prunes impossible row overlaps.

## Prior art (verify)
Lampio, Ostergard, Szollosi, "Orderly generation of Butson Hadamard matrices," classify BH(n,q) for n <= 21, q <= 17 and leave cells open; later work adds constructions and nonexistence criteria. Confirm the target (n,q) is still undetermined.
