# Certificate schema

Each file in `certificates/` stores one chamber identity.

- `bits`: signs of `z0,z1,z2,u0.z,u1.z,u2.z`.
- `degree`: maximum product degree, 3 or 4.
- `generator_names`: ordered names of the 67 affine generators.
- `selected_orbits`: explicit lists of products; each product is a sorted list of generator indices.
- `coefficients`: exact `a+b*sqrt(2)` multipliers, with `a` and `b` stored as rational numerator/denominator pairs.

The verifier does not trust a floating residual or an orbit label. It explicitly reconstructs every affine generator, expands every listed product, multiplies by the exact coefficient, sums in `Q(sqrt(2))`, and compares the result to

`3 - x0^2 - ... - x10^2`.

It separately checks that each multiplier is strictly positive under the positive real embedding of `sqrt(2)`.
