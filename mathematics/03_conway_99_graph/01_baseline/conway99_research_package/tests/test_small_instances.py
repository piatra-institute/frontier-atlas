import unittest

import numpy as np

from conway99.small_instances import (
    brute_force_reduced_solutions,
    m2_unique_solution,
    spectral_feasibility,
)


class SmallInstanceTests(unittest.TestCase):
    def test_m2_has_one_labeled_reduced_solution(self):
        solutions = list(brute_force_reduced_solutions(2))
        self.assertEqual(len(solutions), 1)
        expected = np.array(
            [
                [0, 1, 1, 0],
                [1, 0, 0, 1],
                [1, 0, 0, 1],
                [0, 1, 1, 0],
            ],
            dtype=np.int64,
        )
        self.assertTrue(np.array_equal(solutions[0], expected))
        self.assertTrue(np.array_equal(m2_unique_solution(), expected))

    def test_m3_fails_elementary_spectral_feasibility(self):
        report = spectral_feasibility(3)
        self.assertFalse(report["feasible"])
        self.assertEqual(report["discriminant"], 17)
        self.assertEqual(report["trace_if_equal"], -3)

    def test_m7_passes_elementary_spectral_feasibility(self):
        report = spectral_feasibility(7)
        self.assertTrue(report["feasible"])
        self.assertEqual(report["eigenvalues"], ["3", "-4"])
        self.assertEqual(report["multiplicities"], ["54", "44"])


if __name__ == "__main__":
    unittest.main()
