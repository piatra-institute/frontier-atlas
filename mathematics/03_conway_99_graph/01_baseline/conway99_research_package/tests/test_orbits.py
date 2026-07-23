import math
import unittest

from conway99.orbits import (
    alternating_signature,
    build_case_records,
    fixed_q_matching,
    integer_partitions,
    matching_representative,
    orbit_of_representative,
    signature_counts,
)


EXPECTED_COUNTS = {
    (6,): 3840,
    (5, 1): 2304,
    (4, 2): 1440,
    (4, 1, 1): 720,
    (3, 3): 640,
    (3, 2, 1): 960,
    (3, 1, 1, 1): 160,
    (2, 2, 2): 120,
    (2, 2, 1, 1): 180,
    (2, 1, 1, 1, 1): 30,
    (1, 1, 1, 1, 1, 1): 1,
}


class OrbitTests(unittest.TestCase):
    def test_exactly_eleven_signatures_cover_all_matchings(self):
        counts = signature_counts(7)
        self.assertEqual(dict(counts), EXPECTED_COUNTS)
        self.assertEqual(sum(counts.values()), math.prod(range(1, 12, 2)))
        self.assertEqual(set(counts), set(integer_partitions(6)))

    def test_representatives_have_declared_signatures(self):
        q = fixed_q_matching(7)
        for partition in integer_partitions(6):
            representative = matching_representative(partition, 7)
            self.assertEqual(alternating_signature(representative, q), partition)

    def test_group_orbits_match_signature_classes(self):
        for partition, expected_size in EXPECTED_COUNTS.items():
            representative = matching_representative(partition, 7)
            orbit = orbit_of_representative(representative, 7)
            self.assertEqual(len(orbit), expected_size, partition)

    def test_manifest_is_deterministic(self):
        records = build_case_records(7)
        self.assertEqual(len(records), 11)
        self.assertEqual(records[0]["partition"], [6])
        self.assertEqual(records[-1]["partition"], [1, 1, 1, 1, 1, 1])


if __name__ == "__main__":
    unittest.main()
