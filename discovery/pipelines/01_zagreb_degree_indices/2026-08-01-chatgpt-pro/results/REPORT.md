# Degree-index inequality sweep: exact results

Exhaustive connected-graph census: n=1..9, 273,193 graphs including K1; 273,192 nontrivial graphs.
Independent primary/secondary index agreement and five exact identities: 273,193/273,193 graphs.

## Clean connected counterexample

graph6: `P]oCGGC@?G?_@?@??_?G?@??`
n=17, m=18, degrees=[11, 4, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
M1=172, M2=182
M1/n=172/17; M2/m=91/9
M1/n - M2/m = 1/153 > 0; m*M1 - n*M2 = 2.

## Literal printed typo counterexample

graph6: `CF` (K1,3). F=30; literal RHS=24; corrected RHS=30.

## Auto-fit summary

{
  "generated": 56,
  "broken_on_n8_n9": 26,
  "survived_n8_n9": 30,
  "survived_n8_n9_but_broken_adversarial": 1,
  "hardened_survivors": 29,
  "training_graphs_n2_to_n7": 995,
  "push_graphs_n8_to_n9": 272197,
  "adversarial_parameter_instances": 8931
}
