// Exact checker for the difficult 2-slice restricted tensor over F2.
//
// For slices M0,M1, tensor rank over F2 equals
//   min_Z rank(Z)+rank(M0+Z)+rank(M1+Z).
// If this sum were <=8, one of the three matrices would have rank <=2.
// We enumerate every 6x6 binary matrix of rank 0, 1, or 2 and test all
// three possible centers. For the supplied orbit-5 slices, Z=0 gives 9;
// absence of a value <=8 proves exact rank 9.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <set>
#include <string>
#include <utility>
#include <vector>

static int rank6(uint64_t matrix) {
    std::array<uint8_t, 6> rows{};
    for (int i = 0; i < 6; ++i) rows[i] = static_cast<uint8_t>((matrix >> (6 * i)) & 63ULL);
    int rank = 0;
    for (int column = 5; column >= 0; --column) {
        int pivot = -1;
        for (int row = rank; row < 6; ++row) {
            if ((rows[row] >> column) & 1U) { pivot = row; break; }
        }
        if (pivot < 0) continue;
        std::swap(rows[rank], rows[pivot]);
        for (int row = 0; row < 6; ++row) {
            if (row != rank && ((rows[row] >> column) & 1U)) rows[row] ^= rows[rank];
        }
        ++rank;
    }
    return rank;
}

static uint64_t outer6(uint8_t column, uint8_t row) {
    uint64_t matrix = 0;
    for (int i = 0; i < 6; ++i) {
        if ((column >> i) & 1U) matrix |= (uint64_t(row) << (6 * i));
    }
    return matrix;
}

static int det2(uint8_t k) {
    return (((k >> 0) & 1) & ((k >> 3) & 1)) ^ (((k >> 1) & 1) & ((k >> 2) & 1));
}

static uint64_t rank2_matrix(
    uint8_t u0, uint8_t u1, uint8_t v0, uint8_t v1, uint8_t k) {
    // Fixed bases for a 2D column space and a 2D row space; k ranges over GL(2,2).
    const int k00 = (k >> 0) & 1, k01 = (k >> 1) & 1;
    const int k10 = (k >> 2) & 1, k11 = (k >> 3) & 1;
    uint64_t matrix = 0;
    for (int i = 0; i < 6; ++i) {
        const int a = (u0 >> i) & 1, b = (u1 >> i) & 1;
        const int x = (a & k00) ^ (b & k10);
        const int y = (a & k01) ^ (b & k11);
        const uint8_t row = (x ? v0 : 0) ^ (y ? v1 : 0);
        matrix |= (uint64_t(row) << (6 * i));
    }
    return matrix;
}

struct Search {
    int minimum_tested = 100;
    uint64_t witness_z = 0;
    uint64_t rank_le_2_count = 0;
    uint64_t z_count = 0;
};

static void test_z(uint64_t z, uint64_t m0, uint64_t m1, Search& search) {
    ++search.z_count;
    const int value = rank6(z) + rank6(m0 ^ z) + rank6(m1 ^ z);
    if (value < search.minimum_tested) {
        search.minimum_tested = value;
        search.witness_z = z;
    }
}

static void test_low_rank_seed(uint64_t seed, uint64_t m0, uint64_t m1, Search& search) {
    ++search.rank_le_2_count;
    test_z(seed, m0, m1, search);
    test_z(m0 ^ seed, m0, m1, search);
    test_z(m1 ^ seed, m0, m1, search);
}

int main(int argc, char** argv) {
    if (argc != 3) {
        std::cerr << "usage: two_slice_rank9 M0_HEX M1_HEX\n";
        return 2;
    }
    const uint64_t m0 = std::stoull(argv[1], nullptr, 16);
    const uint64_t m1 = std::stoull(argv[2], nullptr, 16);
    if ((m0 >> 36) || (m1 >> 36)) {
        std::cerr << "each matrix must fit in 36 bits\n";
        return 2;
    }

    // The 651 two-dimensional subspaces of F2^6, each with a fixed basis.
    std::set<uint64_t> subspace_keys;
    for (uint8_t u = 1; u < 64; ++u) {
        for (uint8_t v = u + 1; v < 64; ++v) {
            const uint8_t w = u ^ v;
            subspace_keys.insert(1ULL | (1ULL << u) | (1ULL << v) | (1ULL << w));
        }
    }
    if (subspace_keys.size() != 651) {
        std::cerr << "2D-subspace enumeration failed\n";
        return 3;
    }
    std::vector<std::pair<uint8_t, uint8_t>> bases;
    for (uint64_t key : subspace_keys) {
        std::vector<uint8_t> nonzero;
        for (uint8_t x = 1; x < 64; ++x) if ((key >> x) & 1ULL) nonzero.push_back(x);
        if (nonzero.size() != 3 || static_cast<uint8_t>(nonzero[0] ^ nonzero[1]) != nonzero[2]) {
            std::cerr << "invalid 2D subspace\n";
            return 3;
        }
        bases.emplace_back(nonzero[0], nonzero[1]);
    }
    std::vector<uint8_t> gl2;
    for (uint8_t k = 0; k < 16; ++k) if (det2(k)) gl2.push_back(k);
    if (gl2.size() != 6) return 3;

    Search search;
    test_low_rank_seed(0, m0, m1, search); // rank 0
    for (uint8_t u = 1; u < 64; ++u) {
        for (uint8_t v = 1; v < 64; ++v) {
            test_low_rank_seed(outer6(u, v), m0, m1, search); // every rank-1 matrix
        }
    }
    uint64_t rank2_count = 0;
    for (const auto& ub : bases) {
        for (const auto& vb : bases) {
            for (uint8_t k : gl2) {
                const uint64_t matrix = rank2_matrix(ub.first, ub.second, vb.first, vb.second, k);
                if (rank6(matrix) != 2) return 3;
                test_low_rank_seed(matrix, m0, m1, search);
                ++rank2_count;
            }
        }
    }

    constexpr uint64_t expected_rank1 = 63ULL * 63ULL;
    constexpr uint64_t expected_rank2 = 651ULL * 651ULL * 6ULL;
    constexpr uint64_t expected_total = 1ULL + expected_rank1 + expected_rank2;
    if (rank2_count != expected_rank2 || search.rank_le_2_count != expected_total) return 3;

    const int upper_from_zero = rank6(m0) + rank6(m1);
    const int wr0 = rank6(search.witness_z);
    const int wr1 = rank6(m0 ^ search.witness_z);
    const int wr2 = rank6(m1 ^ search.witness_z);

    std::cout << "TWO_SLICE OK"
              << " rank0=1 rank1=" << expected_rank1
              << " rank2=" << expected_rank2
              << " tested_z=" << search.z_count
              << " minimum_tested=" << search.minimum_tested
              << " upper_from_Z0=" << upper_from_zero
              << " witness_ranks=" << wr0 << "," << wr1 << "," << wr2
              << "\n";

    // Exact-rank-9 proof conditions.
    if (upper_from_zero != 9) return 1;
    if (search.minimum_tested < 9) return 1;
    return 0;
}
