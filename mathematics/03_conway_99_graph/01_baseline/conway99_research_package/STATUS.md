# Research status

## Resolution state

**UNRESOLVED as of package reconstruction on 21 July 2026.**

No graph certificate and no complete nonexistence certificate are included.

## Rigorously retained results

1. The fixed-vertex reduction to an `84 x 84` matrix `B` is exact.
2. The equations
   \[
   BM=MT,
   \qquad
   B^2=12I-B-MM^T+2J
   \]
   are equivalent to the full strongly regular graph equation after reconstructing `A`.
3. A point-star induces a perfect matching on 12 vertices.
4. Its orbits under `C2 wr S6` are exactly classified by the 11 partitions of 6.
5. The package independently enumerates all 10,395 labeled perfect matchings and checks the 11 orbit sizes.
6. The exact OPB generator implements the incidence and common-neighbor equations.
7. The generalized `m=2` instance is solved completely and validates the reduction, reconstruction, verifier, and OPB semantics.
8. The integral matrix formulation
   \[
   G^2=105G,\quad G\mathbf 1=0,\quad G_{ii}=50
   \]
   is derived and implemented, with the residue class of `G mod 15` fixed in advance.

## Results that are not claimed

- No claim that the integral-projector viewpoint is absent from all prior literature.
- No claim that any of the 11 Conway cases is satisfiable or unsatisfiable.
- No claim that a direct OPB run will finish in practical time.
- No claim that necessary spectral or modular conditions settle existence.

## Exact remaining gap

Determine whether at least one of the 11 normalized cases admits a binary symmetric zero-diagonal matrix `B` satisfying both reduced equations. A negative result must close all 11 cases with independently checkable completeness and proof certificates.
