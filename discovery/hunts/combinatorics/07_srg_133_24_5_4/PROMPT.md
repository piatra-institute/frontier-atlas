# 07. Strongly regular graph srg(133,24,5,4) / generalized quadrangle GQ(6,3)

**Target.** Construct a strongly regular graph with parameters (133, 24, 5, 4), or prove none exists. These are exactly the point-graph parameters of a generalized quadrangle GQ(6,3): v = (s+1)(st+1) = 7*19, k = s(t+1) = 24, lambda = s-1 = 5, mu = t+1 = 4 with s=6, t=3. Existence of GQ(6,3) (equivalently GQ(3,6)) is open.

**What counts as a win.** A single 133-vertex SRG with these parameters proves existence (one-sided); if it also carries a GQ line structure it settles GQ(6,3). Feasible eigenvalues 5 and -4.

**Checker (seconds).** Read the 133x133 symmetric 0/1 A. Verify diag = 0, row sums = 24, and A*A = 24*I + 5*A + 4*(J - I - A). Milliseconds. For a claimed GQ, also verify the line spread gives lambda = 0 collinearity graph consistency.

**Search plan.** Prescribe an automorphism (Z_133 = Z_7 x Z_19, or a group acting on points/lines) and solve the incidence system via SAT/ILP; algebraic GQ constructions and their known nonexistence obstructions (Higman-type inequalities are satisfied here); Cayley / coset-geometry search.

**Prior art (verify).** Row marked "?" in A.E. Brouwer's SRG table (aeb.win.tue.nl/graphs/srg/); GQ(6,3) existence is a well-known open case in finite geometry (Payne-Thas, "Finite Generalized Quadrangles"). Re-verify current status.

**Openness:** documented-open. **Win-type:** existence.
