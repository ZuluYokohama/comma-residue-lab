"""REPRESENT stage — pure data structures.

No numerical search, no tempering, no claims of closure.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import math
from typing import Tuple


LOG2 = math.log(2.0)
LOG3_2 = math.log(1.5)


@dataclass(frozen=True)
class Generator:
    name: str
    ratio: Fraction
    log: float

    @staticmethod
    def octave() -> "Generator":
        return Generator("octave", Fraction(2, 1), LOG2)

    @staticmethod
    def fifth() -> "Generator":
        return Generator("fifth", Fraction(3, 2), LOG3_2)


@dataclass(frozen=True)
class Pitch:
    """Integer coefficients in the free group, plus log-frequency."""
    a: int  # octave exponent
    b: int  # fifth exponent

    @property
    def log_freq(self) -> float:
        return self.a * LOG2 + self.b * LOG3_2

    @property
    def ratio(self) -> float:
        return math.exp(self.log_freq)

    def reduce_octave(self) -> "Pitch":
        """Fold into [0, log2) by subtracting integer octaves."""
        # keep b fixed; adjust a so that 0 <= log_freq < LOG2
        lf = self.log_freq
        k = math.floor(lf / LOG2)
        return Pitch(self.a - k, self.b)


@dataclass
class Residual:
    """Measured obstruction to the classical closing relation."""
    log_value: float
    cents: float

    @classmethod
    def from_log(cls, log_value: float) -> "Residual":
        # 1 octave = 1200 cents; cents = 1200 * log2(ratio) = 1200 * log_value / LOG2
        cents = 1200.0 * log_value / LOG2
        return cls(log_value=log_value, cents=cents)


def classical_closing_element() -> Pitch:
    """12 fifths minus 7 octaves — the element whose image under λ is the comma."""
    return Pitch(a=-7, b=12)


def measure_pythagorean_comma() -> Residual:
    """Direct evaluation of the restricted residual. No free parameters."""
    p = classical_closing_element()
    return Residual.from_log(p.log_freq)
