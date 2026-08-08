"""CONSTRUCT stage — candidate scale from free generators."""

from __future__ import annotations

from typing import List

from represent import Pitch


def stack_of_fifths(n: int = 12) -> List[Pitch]:
    """Naive orbit under repeated addition of the fifth generator."""
    return [Pitch(a=0, b=k).reduce_octave() for k in range(n)]


def ordered_by_log(pitches: List[Pitch]) -> List[Pitch]:
    return sorted(pitches, key=lambda p: p.log_freq)
