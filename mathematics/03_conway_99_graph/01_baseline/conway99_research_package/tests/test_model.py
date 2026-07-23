import unittest

import numpy as np

from conway99.model import build_model, validate_model_identities
from conway99.small_instances import m2_unique_solution
from conway99.verify import reconstruct_A, verify_A, verify_B


class ModelTests(unittest.TestCase):
    def test_conway_dimensions_and_identities(self):
        model = build_model(7)
        self.assertEqual(model.base_vertex_count, 14)
        self.assertEqual(model.second_layer_count, 84)
        self.assertEqual(model.full_vertex_count, 99)
        self.assertEqual(model.degree, 14)
        self.assertEqual(model.b_degree, 12)
        self.assertTrue(all(validate_model_identities(model).values()))

    def test_m2_block_reconstruction(self):
        B = m2_unique_solution()
        reduced = verify_B(B, m=2, verify_full=True)
        self.assertTrue(reduced.valid, reduced.to_dict())
        A = reconstruct_A(B, m=2)
        full = verify_A(A, m=2)
        self.assertTrue(full.valid, full.to_dict())
        self.assertEqual(A.shape, (9, 9))
        self.assertTrue(np.all(A.sum(axis=1) == 4))


if __name__ == "__main__":
    unittest.main()
