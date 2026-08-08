"""Single entry point that replays MEASURE → RESOLVE → V&V."""

from measure import run_measure
from resolve import pure_vs_tempered_cents
from vv import run_vv

if __name__ == "__main__":
    print("=== MEASURE ===")
    r = run_measure()
    print(r)
    print("\n=== RESOLVE (pure vs tempered) ===")
    print(pure_vs_tempered_cents())
    print("\n=== V&V ===")
    print(run_vv())
