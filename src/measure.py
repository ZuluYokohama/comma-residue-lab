"""MEASURE stage — pure evaluation of the restricted residual."""

from __future__ import annotations

import json
from pathlib import Path

from represent import measure_pythagorean_comma, Residual

EPSILON_LOG = 1e-15


def run_measure() -> Residual:
    r = measure_pythagorean_comma()
    out = {
        "log_value": r.log_value,
        "cents": r.cents,
        "abs_log": abs(r.log_value),
        "H0_threshold": EPSILON_LOG,
        "H0_rejected": abs(r.log_value) > EPSILON_LOG,
    }
    Path("measurements").mkdir(exist_ok=True)
    Path("residue").mkdir(exist_ok=True)
    with open("measurements/H0_result.json", "w") as f:
        json.dump(out, f, indent=2)
    with open("residue/pythagorean_comma.json", "w") as f:
        json.dump({"log_value": r.log_value, "cents": r.cents}, f, indent=2)
    return r


if __name__ == "__main__":
    r = run_measure()
    print(f"log residual = {r.log_value}")
    print(f"cents        = {r.cents}")
    print(f"H0 rejected  = {abs(r.log_value) > EPSILON_LOG}")
