"""RESOLVE stage — two parallel objects: pure residual kept, tempered generator derived."""

from __future__ import annotations

import math
from dataclasses import dataclass

from represent import LOG2, Residual, measure_pythagorean_comma


@dataclass(frozen=True)
class TemperedFifth:
    log: float
    ratio: float

    @classmethod
    def equal_tempered(cls) -> "TemperedFifth":
        log = (7.0 / 12.0) * LOG2
        return cls(log=log, ratio=math.exp(log))


def residual_after_tempering() -> Residual:
    """By construction this must be numerically zero (within float noise)."""
    tf = TemperedFifth.equal_tempered()
    # 12 * tempered - 7 * octave
    log_val = 12.0 * tf.log - 7.0 * LOG2
    return Residual.from_log(log_val)


def pure_vs_tempered_cents() -> dict:
    pure = measure_pythagorean_comma()
    temp = residual_after_tempering()
    return {
        "pure_comma_cents": pure.cents,
        "tempered_closing_residual_cents": temp.cents,
        "tempered_fifth_ratio": TemperedFifth.equal_tempered().ratio,
        "tempered_fifth_cents_from_pure": 1200.0 * (TemperedFifth.equal_tempered().log - math.log(1.5)) / LOG2,
    }
