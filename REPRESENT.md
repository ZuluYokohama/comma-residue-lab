# REPRESENT

## Abstract group

Free abelian group G = Z · e_oct + Z · e_fifth.

Homomorphism φ: G → (R>0, ×) defined by

    φ(a·e_oct + b·e_fifth) = 2^a * (3/2)^b

## Log-frequency coordinates

Work exclusively in additive coordinates:

    λ = log ∘ φ : G → R

    λ(a,b) = a·log(2) + b·log(3/2)

This turns multiplicative consistency into additive vector arithmetic.

## Finite pitch-class set

Target identification: the 12-element quotient that forces

    12 · e_fifth  ≡  7 · e_oct   (mod the relation that closes the circle)

I.e., after twelve fifths one should have climbed exactly seven octaves.

The obstruction to this relation is the object to be measured.

## Computational objects (Python)

- `Generator` : named ratio with exact Fraction or float log.
- `Pitch` : (a, b) integer coefficients + cached log-frequency.
- `Scale` : ordered list of 12 Pitches after reduction modulo the intended relation.
- `Residual` : numeric value of λ(12·e_fifth - 7·e_oct) together with its cents conversion.

No optimization or tempering parameters are present yet.
