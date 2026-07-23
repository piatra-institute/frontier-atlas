import re
import tempfile
import unittest
from pathlib import Path

from conway99.opb import encoding_counts, write_opb, x_var, y_var
from conway99.small_instances import m2_unique_solution


TERM_RE = re.compile(r"([+-]\d+)\s+([A-Za-z_][A-Za-z0-9_]*)")


def evaluate_constraint(line, assignment):
    # Split at the comparison operator.
    match = re.search(r"\s(=|>=|<=)\s(-?\d+)\s*;", line)
    if match is None:
        raise AssertionError(f"cannot parse: {line}")
    operator = match.group(1)
    rhs = int(match.group(2))
    lhs_text = line[: match.start()]
    lhs = sum(int(coef) * assignment.get(var, 0) for coef, var in TERM_RE.findall(lhs_text))
    return {"=": lhs == rhs, ">=": lhs >= rhs, "<=": lhs <= rhs}[operator]


class OpbTests(unittest.TestCase):
    def test_counts_for_conway_case(self):
        counts = encoding_counts(7, with_case=True)
        self.assertEqual(counts.x_variables, 3486)
        self.assertEqual(counts.y_variables, 285852)
        self.assertEqual(counts.total_variables, 289338)
        self.assertEqual(counts.incidence_equalities, 1176)
        self.assertEqual(counts.case_fix_constraints, 66)
        self.assertEqual(counts.total_constraints, 862284)

    def test_m2_generated_model_is_satisfied_by_exact_solution(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "m2.opb"
            counts = write_opb(path, m=2, partition=(1,))
            lines = path.read_text(encoding="ascii").splitlines()
            constraints = [line for line in lines if line and not line.startswith("*")]
            self.assertEqual(len(constraints), counts.total_constraints)
            self.assertEqual(counts.total_constraints, 59)

            B = m2_unique_solution()
            assignment = {}
            for i in range(4):
                for j in range(i + 1, 4):
                    assignment[x_var(i, j)] = int(B[i, j])
            for i in range(4):
                for j in range(i + 1, 4):
                    for k in range(4):
                        if k in {i, j}:
                            continue
                        assignment[y_var(i, j, k)] = int(B[i, k] and B[j, k])

            failures = [line for line in constraints if not evaluate_constraint(line, assignment)]
            self.assertEqual(failures, [])


if __name__ == "__main__":
    unittest.main()
