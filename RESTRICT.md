# RESTRICT

## Admitted objects

- Base frequency: fixed positive real (conventionally 1.0 for pure ratio work; 440.0 Hz for auditory mapping is optional and post-hoc).
- Generators: strictly the two ratios 2/1 (octave) and 3/2 (perfect fifth). No other primes admitted in the free generators at this stage.
- Finite pitch-class cardinality: exactly 12. (The classical circle-of-fifths identification target.)
- Representation of pitch: log-frequency (natural log of the ratio to base). Additive group isomorphic to the multiplicative group of positive ratios.

## Explicit refusals

- No admission of the pure major third (5/4) as a free generator in the first construction. That would change the free group and is a different problem.
- No continuous tempering parameters until the MEASURE stage has produced a concrete residual number.
- No claim of exact closure under the free group action on a finite set; the obstruction is expected and must be measured, not assumed zero.
- No floating-point equality tests without an explicit epsilon declared in MEASURE.
- No deletion of intermediate numerical residuals.

## Invariants that later stages may not weaken

1. All constructed pitches must be positive reals.
2. The map from abstract generators to concrete ratios is a group homomorphism from the free abelian group Z² into (R>0, ×).
3. Any statement "the system is closed" must be accompanied by a measured residual whose absolute value is reported; residual = 0 is only allowed if the numerical test passes under the declared epsilon.
4. Failed candidate constructions remain in the tree under `residue/` or `failed/`.

These restrictions are the only starting point for REPRESENT.
