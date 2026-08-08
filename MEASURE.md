# MEASURE

## Procedure

1. Evaluate λ of the classical closing element Pitch(a=-7, b=12).
2. Convert the log residual to cents (1200 * log2(ratio)).
3. Compare absolute residual against the H0 threshold 1e-15.

## Declared epsilon

EPSILON_LOG = 1e-15

Any residual whose absolute value exceeds EPSILON_LOG is reported as non-zero obstruction.

## Result

See `measurements/H0_result.json` and `residue/pythagorean_comma.json`.

H0 is rejected. The measured residual is retained as first-class data.
