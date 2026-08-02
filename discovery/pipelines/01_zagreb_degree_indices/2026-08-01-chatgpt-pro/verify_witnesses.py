#!/usr/bin/env python3
from fractions import Fraction
from sweep import verified_indices

HV17 = "P]oCGGC@?G?_@?@??_?G?@??"
TYPO = "CF"


def main() -> None:
    hv = verified_indices(HV17)
    hv_gap = Fraction(hv["M1"], hv["n"]) - Fraction(hv["M2"], hv["m"])
    assert hv["n"] == 17 and hv["m"] == 18
    assert hv["M1"] == 172 and hv["M2"] == 182
    assert hv_gap == Fraction(1, 153)
    assert hv["m"] * hv["M1"] - hv["n"] * hv["M2"] == 2

    typo = verified_indices(TYPO)
    literal_rhs = 2 * typo["M2"] + typo["m"] * (typo["n"] - 2)
    corrected_rhs = 2 * typo["M2"] + typo["m"] * (typo["n"] - 2) ** 2
    assert typo["F"] == 30
    assert literal_rhs == 24 and typo["F"] > literal_rhs
    assert corrected_rhs == 30 and typo["F"] == corrected_rhs

    print("HV witness verified")
    print(f"  graph6 = {HV17}")
    print(f"  M1/n - M2/m = {hv_gap}")
    print("Literal Furtula-Gutman typo witness verified")
    print(f"  graph6 = {TYPO}")
    print(f"  F = {typo['F']}, literal RHS = {literal_rhs}, corrected RHS = {corrected_rhs}")


if __name__ == "__main__":
    main()
