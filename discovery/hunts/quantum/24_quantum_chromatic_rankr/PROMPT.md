# A smaller graph separating rank-r quantum chromatic numbers

**Find:** a graph on fewer than 21 vertices that separates a rank-r quantum chromatic number from the classical chromatic number (equivalently, a small graph carrying a rank-r quantum coloring but no classical coloring with the same number of colors), in the regime where the minimal such graph is not established.

## What counts as a win
A graph G plus an explicit rank-r projective coloring with c colors, where the classical chromatic number of G exceeds c, on fewer vertices than the smallest known example. One-sided: a smaller separating graph.

## Checker
A rank-r c-coloring assigns to each vertex v projectors {P_{v,1},...,P_{v,c}} on C^{rc}, each of rank r, summing to I, and requires P_{u,a} P_{v,a} = 0 for every edge uv and color a. Verify these identities exactly (algebraic entries). Compute the classical chromatic number of G exactly (finite backtracking) and confirm it exceeds c. Runtime: seconds.

## Search plan
Start from Kochen-Specker / orthogonality-graph gadgets and the known 21-vertex example; contract and prune vertices while re-solving the projector constraints (an SDP feasibility, then exact rationalisation). Verify the classical chromatic gap exactly.

## Prior art (verify)
The minimal graph separating the standard quantum and classical chromatic numbers is the 14-vertex Mancinska-Roberson graph (proven minimal). For rank-r variants, the smallest known separating graph has 21 vertices ("On the Quantum Chromatic Numbers of Small Graphs"); its minimality is not established. Confirm the rank-r cell is still open.
