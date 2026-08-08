# CONSTRUCT

## Candidate 0 — pure stack of fifths

Generate the orbit

    p_k = Pitch(0, k)   for k = 0 … 11

then reduce each into a single octave. This produces a 12-tone set ordered by fifths.

No tempering. No adjustment of the generators.

## Hypothesis H0 (to be tested in MEASURE)

Under IEEE-754 double, the residual of classical_closing_element() is numerically indistinguishable from zero.

This hypothesis is expected to be false; the purpose of recording it is to keep the negative result visible.
