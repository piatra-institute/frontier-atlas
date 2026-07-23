import unittest

import numpy as np

from conway99.model import build_model
from conway99.projector import (
    BASELINE_VALUES,
    B_to_G,
    G_to_B,
    baseline_G,
    baseline_G_from_line_graph_polynomial,
    relation_type,
)


class ProjectorTests(unittest.TestCase):
    def test_two_independent_baseline_constructions_agree(self):
        self.assertTrue(
            np.array_equal(baseline_G(), baseline_G_from_line_graph_polynomial())
        )

    def test_baseline_diagonal_and_relation_values(self):
        model = build_model(7)
        G0 = baseline_G()
        self.assertTrue(np.all(np.diag(G0) == 50))
        seen = set()
        for i, e in enumerate(model.base_edges):
            for j in range(i + 1, len(model.base_edges)):
                relation = relation_type(e, model.base_edges[j])
                seen.add(relation)
                self.assertEqual(G0[i, j], BASELINE_VALUES[relation])
        self.assertEqual(seen, set(BASELINE_VALUES))

    def test_binary_lift_round_trip(self):
        rng = np.random.default_rng(99)
        upper = rng.integers(0, 2, size=(84, 84), dtype=np.int64)
        B = np.triu(upper, 1)
        B = B + B.T
        G = B_to_G(B)
        recovered = G_to_B(G)
        self.assertTrue(np.array_equal(B, recovered))
        self.assertTrue(np.array_equal(G % 15, baseline_G() % 15))


if __name__ == "__main__":
    unittest.main()
