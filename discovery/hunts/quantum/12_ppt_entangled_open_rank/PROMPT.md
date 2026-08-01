# A PPT entangled state at an open rank cell

**Find:** a PPT entangled (bound entangled) state on C^m tensor C^n with rank pair (rank rho, rank rho^{Gamma}) = (r,s) at an (m,n,r,s) cell left undetermined in the low-rank PPT classification.

## What counts as a win
An explicit density matrix rho that is PPT and entangled with the target ranks. One-sided: it realises the open cell.

## Checker
Two exact steps. (1) PPT: verify rho >= 0 and its partial transpose rho^{Gamma} >= 0 by exact eigenvalues (rational or algebraic entries). (2) Entanglement by the range criterion: certify that no product vector |a>|b> lies in range(rho) with |a>|b*> in range(rho^{Gamma}). For low rank this is a small polynomial system; prove it has no solution by resultants / Groebner basis over the exact field. Runtime: seconds.

## Search plan
Build candidates from unextendible product bases and from edge states supported on chosen ranges; parametrise a PPT face and push toward the boundary numerically, then rationalise. Verify emptiness of the product-vector variety symbolically.

## Prior art (verify)
Chen and Djokovic classified low-rank PPT entangled states in 2x4, 3x3, 3x4 and mapped many rank cells, leaving some undetermined. Confirm the chosen (m,n,r,s) is still open in that series.
