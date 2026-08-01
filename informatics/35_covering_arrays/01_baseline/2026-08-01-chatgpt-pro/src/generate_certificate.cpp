#include <algorithm>
#include <array>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <filesystem>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

namespace fs = std::filesystem;

static constexpr int N = 12;
static constexpr int V = 3;
static constexpr int FULL_MASK = (1 << (V * V)) - 1;

using Matrix = std::array<int, 9>;
using Column = std::array<uint8_t, N>;

static const std::vector<std::array<int, 3>> PERMS = {
    {0,1,2}, {0,2,1}, {1,0,2}, {1,2,0}, {2,0,1}, {2,1,0}
};

static std::string matrix_key(const Matrix& m) {
    std::ostringstream out;
    for (int i = 0; i < 9; ++i) {
        if (i) out << ',';
        out << m[i];
    }
    return out.str();
}

static Matrix transpose_matrix(const Matrix& m) {
    Matrix t{};
    for (int i = 0; i < 3; ++i)
        for (int j = 0; j < 3; ++j)
            t[3*i+j] = m[3*j+i];
    return t;
}

static Matrix permute_matrix(const Matrix& m,
                             const std::array<int,3>& pr,
                             const std::array<int,3>& pc) {
    Matrix out{};
    for (int i = 0; i < 3; ++i)
        for (int j = 0; j < 3; ++j)
            out[3*i+j] = m[3*pr[i] + pc[j]];
    return out;
}

static Matrix canonical_matrix(const Matrix& m) {
    bool first = true;
    Matrix best{};
    for (const auto& pr : PERMS) {
        for (const auto& pc : PERMS) {
            Matrix a = permute_matrix(m, pr, pc);
            Matrix at = transpose_matrix(a);
            if (first || a < best) { best = a; first = false; }
            if (at < best) best = at;
        }
    }
    return best;
}

static int pair_mask(const Column& a, const Column& b) {
    int mask = 0;
    for (int r = 0; r < N; ++r) {
        mask |= 1 << (3 * static_cast<int>(a[r]) + static_cast<int>(b[r]));
    }
    return mask;
}

static std::pair<Column, Column> base_columns(const Matrix& m) {
    Column c0{}, c1{};
    int r = 0;
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            for (int q = 0; q < m[3*i+j]; ++q) {
                if (r >= N) throw std::runtime_error("matrix sum exceeds 12");
                c0[r] = static_cast<uint8_t>(i);
                c1[r] = static_cast<uint8_t>(j);
                ++r;
            }
        }
    }
    if (r != N) throw std::runtime_error("matrix sum is not 12");
    return {c0, c1};
}

static std::string column_string(const Column& c) {
    std::string s;
    s.reserve(N);
    for (uint8_t x : c) s.push_back(static_cast<char>('0' + x));
    return s;
}

static void rgs_rec(int pos, int max_seen, Column& c, std::vector<Column>& out) {
    if (pos == N) {
        if (max_seen == 2) out.push_back(c);
        return;
    }
    int max_value = std::min(2, max_seen + 1);
    for (int x = 0; x <= max_value; ++x) {
        c[pos] = static_cast<uint8_t>(x);
        rgs_rec(pos + 1, std::max(max_seen, x), c, out);
    }
}

static std::vector<Column> all_rgs_columns() {
    std::vector<Column> out;
    out.reserve(90000);
    Column c{};
    c[0] = 0;
    rgs_rec(1, 0, c, out);
    return out;
}

struct Bitset {
    std::vector<uint64_t> w;
    int n = 0;

    Bitset() = default;
    explicit Bitset(int n_, bool fill=false) : w((n_+63)/64, fill ? ~uint64_t(0) : 0), n(n_) {
        if (fill && (n % 64)) w.back() &= ((uint64_t(1) << (n % 64)) - 1);
    }
    bool any() const {
        for (uint64_t x : w) if (x) return true;
        return false;
    }
    int count() const {
        int s = 0;
        for (uint64_t x : w) s += __builtin_popcountll(x);
        return s;
    }
    int first() const {
        for (size_t i = 0; i < w.size(); ++i) {
            if (w[i]) return static_cast<int>(64*i + __builtin_ctzll(w[i]));
        }
        return -1;
    }
    void reset(int i) { w[i/64] &= ~(uint64_t(1) << (i%64)); }
    void set(int i) { w[i/64] |= uint64_t(1) << (i%64); }
};

static Bitset intersect(const Bitset& a, const Bitset& b) {
    assert(a.n == b.n);
    Bitset out(a.n);
    for (size_t i = 0; i < a.w.size(); ++i) out.w[i] = a.w[i] & b.w[i];
    return out;
}

struct CliqueRun {
    int target = 0;
    uint64_t count = 0;
    std::vector<int> first_witness;
    std::vector<uint64_t> nodes_by_depth;
};

static void clique_dfs(const std::vector<Bitset>& adj,
                       Bitset candidates,
                       int depth,
                       std::vector<int>& chosen,
                       CliqueRun& run,
                       bool stop_after_first) {
    run.nodes_by_depth[depth]++;
    if (depth == run.target) {
        run.count++;
        if (run.first_witness.empty()) run.first_witness = chosen;
        return;
    }
    const int need = run.target - depth;
    if (candidates.count() < need) return;

    while (candidates.any()) {
        if (candidates.count() < need) return;
        int v = candidates.first();
        candidates.reset(v);  // children use only later vertices in this deterministic order
        chosen.push_back(v);
        Bitset next = intersect(candidates, adj[v]);
        clique_dfs(adj, std::move(next), depth + 1, chosen, run, stop_after_first);
        chosen.pop_back();
        if (stop_after_first && run.count > 0) return;
    }
}

static CliqueRun enumerate_k_cliques(const std::vector<Bitset>& adj,
                                     int target,
                                     bool stop_after_first) {
    CliqueRun run;
    run.target = target;
    run.nodes_by_depth.assign(target + 1, 0);
    Bitset all(static_cast<int>(adj.size()), true);
    std::vector<int> chosen;
    clique_dfs(adj, std::move(all), 0, chosen, run, stop_after_first);
    return run;
}

static std::string json_array_u64(const std::vector<uint64_t>& xs) {
    std::ostringstream out;
    out << '[';
    for (size_t i = 0; i < xs.size(); ++i) {
        if (i) out << ',';
        out << xs[i];
    }
    out << ']';
    return out.str();
}

static std::string json_array_int(const std::vector<int>& xs) {
    std::ostringstream out;
    out << '[';
    for (size_t i = 0; i < xs.size(); ++i) {
        if (i) out << ',';
        out << xs[i];
    }
    out << ']';
    return out.str();
}

static bool verify_upper_array(const fs::path& root, std::ostream& log) {
    const int A[13][8] = {
        {2,1,0,1,1,2,0,1},
        {0,1,2,0,0,1,0,2},
        {2,1,2,2,2,1,1,0},
        {0,2,0,0,1,1,2,0},
        {2,2,2,0,2,0,2,2},
        {0,0,1,0,2,1,1,1},
        {0,2,1,2,2,2,0,2},
        {1,2,0,1,2,1,1,2},
        {2,0,1,1,0,2,2,0},
        {1,1,1,2,1,0,2,1},
        {0,2,2,1,0,0,1,1},
        {1,0,0,2,0,0,0,0},
        {1,0,2,0,1,2,1,2}
    };
    std::ofstream out(root / "array_CA_13_2_8_3.csv");
    out << "c0,c1,c2,c3,c4,c5,c6,c7\n";
    for (int r = 0; r < 13; ++r) {
        for (int c = 0; c < 8; ++c) {
            if (c) out << ',';
            out << A[r][c];
        }
        out << '\n';
    }
    out.close();

    std::ofstream cert(root / "certificate" / "upper_coverage_counts.csv");
    cert << "column_i,column_j,count_00,count_01,count_02,count_10,count_11,count_12,count_20,count_21,count_22\n";
    bool ok = true;
    int global_min = 99, global_max = 0;
    for (int i = 0; i < 8; ++i) {
        for (int j = i + 1; j < 8; ++j) {
            int cnt[9] = {0};
            for (int r = 0; r < 13; ++r) cnt[3*A[r][i] + A[r][j]]++;
            cert << i << ',' << j;
            for (int q = 0; q < 9; ++q) {
                cert << ',' << cnt[q];
                if (cnt[q] == 0) ok = false;
                global_min = std::min(global_min, cnt[q]);
                global_max = std::max(global_max, cnt[q]);
            }
            cert << '\n';
        }
    }
    cert.close();
    log << "upper_array_coverage=" << (ok ? "PASS" : "FAIL")
        << " min_multiplicity=" << global_min
        << " max_multiplicity=" << global_max << "\n";
    return ok;
}

int main(int argc, char** argv) {
    if (argc != 2) {
        std::cerr << "usage: generate_certificate <project-root>\n";
        return 2;
    }
    fs::path root = fs::absolute(argv[1]);
    fs::create_directories(root / "certificate");
    fs::create_directories(root / "logs");
    std::ofstream log(root / "logs" / "generator.log");
    if (!log) throw std::runtime_error("cannot open generator.log");

    auto start = std::chrono::steady_clock::now();
    log << "generator=generate_certificate.cpp\n";
    log << "model=CA(N=12;t=2,k=8,v=3) lower bound and CA(13;2,8,3) upper witness\n";

    if (!verify_upper_array(root, log)) {
        std::cerr << "upper array failed coverage\n";
        return 1;
    }

    // All positive 3x3 matrices summing to 12 are J + three distributed units.
    std::map<Matrix, int> orbit_sizes;
    int labelled_matrix_count = 0;
    for (int a = 0; a < 9; ++a) {
        for (int b = a; b < 9; ++b) {
            for (int c = b; c < 9; ++c) {
                Matrix m{};
                m.fill(1);
                m[a]++; m[b]++; m[c]++;
                Matrix canon = canonical_matrix(m);
                orbit_sizes[canon]++;
                labelled_matrix_count++;
            }
        }
    }
    if (labelled_matrix_count != 165 || orbit_sizes.size() != 7) {
        throw std::runtime_error("unexpected multiplicity-matrix orbit count");
    }

    std::vector<Column> rgs = all_rgs_columns();
    if (rgs.size() != 86526) throw std::runtime_error("unexpected RGS count");
    log << "positive_matrices_sum12=" << labelled_matrix_count << "\n";
    log << "matrix_orbits=" << orbit_sizes.size() << "\n";
    log << "restricted_growth_columns_length12_using_3_symbols=" << rgs.size() << "\n";

    std::ofstream patterns_file(root / "certificate" / "multiplicity_patterns.csv");
    patterns_file << "pattern_id,m00,m01,m02,m10,m11,m12,m20,m21,m22,orbit_size\n";

    std::ofstream summary(root / "certificate" / "lower_bound_summary.json");
    summary << "{\n";
    summary << "  \"claim\": \"no CA(12;2,8,3) exists\",\n";
    summary << "  \"labelled_positive_3x3_matrices_sum_12\": 165,\n";
    summary << "  \"matrix_orbits_under_S3xS3_and_transpose\": 7,\n";
    summary << "  \"restricted_growth_columns\": 86526,\n";
    summary << "  \"patterns\": [\n";

    int pattern_id = 0;
    for (auto it = orbit_sizes.begin(); it != orbit_sizes.end(); ++it, ++pattern_id) {
        const Matrix& m = it->first;
        const int orbit_size = it->second;
        patterns_file << pattern_id;
        for (int x : m) patterns_file << ',' << x;
        patterns_file << ',' << orbit_size << '\n';

        auto [c0, c1] = base_columns(m);
        std::vector<Column> candidates;
        candidates.reserve(1500);
        for (const auto& x : rgs) {
            if (pair_mask(c0, x) == FULL_MASK && pair_mask(c1, x) == FULL_MASK)
                candidates.push_back(x);
        }

        const int n = static_cast<int>(candidates.size());
        std::vector<Bitset> adj;
        adj.reserve(n);
        for (int i = 0; i < n; ++i) adj.emplace_back(n, false);
        uint64_t edge_count = 0;

        std::ostringstream pfx;
        pfx << "pattern_" << pattern_id;
        std::ofstream cfile(root / "certificate" / (pfx.str() + "_candidates.txt"));
        cfile << "# index canonical_column\n";
        for (int i = 0; i < n; ++i) cfile << i << ' ' << column_string(candidates[i]) << '\n';
        cfile.close();

        std::ofstream efile(root / "certificate" / (pfx.str() + "_edges.txt"));
        efile << "# u v (compatibility means all 9 ordered pairs occur)\n";
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (pair_mask(candidates[i], candidates[j]) == FULL_MASK) {
                    adj[i].set(j);
                    adj[j].set(i);
                    efile << i << ' ' << j << '\n';
                    edge_count++;
                }
            }
        }
        efile.close();

        CliqueRun k6 = enumerate_k_cliques(adj, 6, false);
        if (k6.count != 0) throw std::runtime_error("unexpected K6; lower bound false");

        int max_clique = 0;
        std::vector<int> max_witness;
        for (int k = 5; k >= 1; --k) {
            CliqueRun hit = enumerate_k_cliques(adj, k, true);
            if (hit.count > 0) {
                max_clique = k;
                max_witness = hit.first_witness;
                break;
            }
        }
        CliqueRun max_all = enumerate_k_cliques(adj, max_clique, false);

        std::ofstream plog(root / "logs" / (pfx.str() + "_enumeration.log"));
        plog << "pattern_id=" << pattern_id << '\n';
        plog << "matrix=" << matrix_key(m) << '\n';
        plog << "matrix_orbit_size=" << orbit_size << '\n';
        plog << "base_c0=" << column_string(c0) << '\n';
        plog << "base_c1=" << column_string(c1) << '\n';
        plog << "candidate_count=" << n << '\n';
        plog << "edge_count=" << edge_count << '\n';
        plog << "k6_count=" << k6.count << '\n';
        plog << "k6_nodes_by_depth=" << json_array_u64(k6.nodes_by_depth) << '\n';
        plog << "max_clique_size=" << max_clique << '\n';
        plog << "max_clique_count=" << max_all.count << '\n';
        plog << "max_clique_witness=" << json_array_int(max_witness) << '\n';
        plog.close();

        log << "pattern=" << pattern_id
            << " matrix=" << matrix_key(m)
            << " orbit_size=" << orbit_size
            << " candidates=" << n
            << " edges=" << edge_count
            << " K6=0"
            << " omega=" << max_clique
            << " max_cliques=" << max_all.count
            << "\n";

        summary << "    {\n";
        summary << "      \"id\": " << pattern_id << ",\n";
        summary << "      \"matrix\": [";
        for (int i = 0; i < 9; ++i) { if (i) summary << ','; summary << m[i]; }
        summary << "],\n";
        summary << "      \"matrix_orbit_size\": " << orbit_size << ",\n";
        summary << "      \"base_c0\": \"" << column_string(c0) << "\",\n";
        summary << "      \"base_c1\": \"" << column_string(c1) << "\",\n";
        summary << "      \"candidate_count\": " << n << ",\n";
        summary << "      \"edge_count\": " << edge_count << ",\n";
        summary << "      \"k6_count\": 0,\n";
        summary << "      \"k6_nodes_by_depth\": " << json_array_u64(k6.nodes_by_depth) << ",\n";
        summary << "      \"maximum_clique_size\": " << max_clique << ",\n";
        summary << "      \"maximum_clique_count\": " << max_all.count << ",\n";
        summary << "      \"maximum_clique_witness\": " << json_array_int(max_witness) << "\n";
        summary << "    }" << (std::next(it) == orbit_sizes.end() ? "\n" : ",\n");
    }
    summary << "  ],\n";
    summary << "  \"conclusion\": \"Every hypothetical CA(12;2,8,3) normalizes to one of the seven patterns and would induce a K6 in its compatibility graph; all seven graphs are K6-free.\"\n";
    summary << "}\n";
    summary.close();
    patterns_file.close();

    auto end = std::chrono::steady_clock::now();
    double seconds = std::chrono::duration<double>(end - start).count();
    log << std::fixed << std::setprecision(6) << "elapsed_seconds=" << seconds << '\n';
    log << "result=PASS\n";
    log.close();

    std::cout << "certificate generated in " << seconds << " s\n";
    return 0;
}
