#include <algorithm>
#include <bit>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <functional>
#include <iostream>
#include <limits>
#include <numeric>
#include <sstream>
#include <string>
#include <vector>

using u64 = std::uint64_t;

struct Graph {
    int n{};
    std::vector<u64> adj;
    int m{};
};

static Graph parse_graph6(const std::string& line) {
    std::string s = line;
    while (!s.empty() && (s.back() == '\r' || s.back() == '\n')) s.pop_back();
    if (s.empty()) throw std::runtime_error("empty graph6 line");
    std::size_t pos = 0;
    int n = 0;
    unsigned char c0 = static_cast<unsigned char>(s[pos++]);
    if (c0 != '~') {
        n = static_cast<int>(c0) - 63;
    } else {
        if (pos >= s.size()) throw std::runtime_error("bad graph6 header");
        if (static_cast<unsigned char>(s[pos]) != '~') {
            if (pos + 3 > s.size()) throw std::runtime_error("short graph6 medium header");
            n = ((static_cast<unsigned char>(s[pos]) - 63) << 12)
              | ((static_cast<unsigned char>(s[pos+1]) - 63) << 6)
              |  (static_cast<unsigned char>(s[pos+2]) - 63);
            pos += 3;
        } else {
            throw std::runtime_error("n > 258047 is unsupported here");
        }
    }
    if (n < 0 || n > 63) throw std::runtime_error("unsupported graph order");
    Graph g{n, std::vector<u64>(n, 0), 0};
    int bitpos = 5;
    int value = 0;
    auto next_bit = [&]() -> int {
        if (bitpos == 5) {
            if (pos >= s.size()) throw std::runtime_error("short graph6 payload");
            value = static_cast<unsigned char>(s[pos++]) - 63;
        }
        int b = (value >> bitpos) & 1;
        if (bitpos == 0) bitpos = 5; else --bitpos;
        return b;
    };
    for (int j = 1; j < n; ++j) {
        for (int i = 0; i < j; ++i) {
            if (next_bit()) {
                g.adj[i] |= (u64{1} << j);
                g.adj[j] |= (u64{1} << i);
                ++g.m;
            }
        }
    }
    return g;
}

static bool is_connected_graph(const Graph& g) {
    if (g.n == 0) return false;
    u64 all = (g.n == 64 ? ~u64{0} : ((u64{1} << g.n) - 1));
    u64 seen = 1, frontier = 1;
    while (frontier) {
        u64 nxt = 0;
        u64 f = frontier;
        while (f) {
            int v = std::countr_zero(f);
            f &= f - 1;
            nxt |= g.adj[v];
        }
        nxt &= all & ~seen;
        seen |= nxt;
        frontier = nxt;
    }
    return seen == all;
}

struct Metrics {
    int n{}, m{}, Delta{}, delta{};
    bool tree{}, regular{};
    int gamma{}, gamma_t{}, indep_dom{}, gamma_c{}, gamma_R{}, gamma_pr{};
    int alpha{}, tau{}, mu_star{};
    u64 gamma_set{}, gamma_t_set{}, indep_dom_set{}, gamma_c_set{}, gamma_R_twos{}, gamma_R_ones{}, gamma_pr_set{};
    u64 alpha_set{}, mu_unmatched{};
    std::vector<std::pair<int,int>> gamma_pr_matching;
    std::vector<std::pair<int,int>> mu_matching;
};

static std::vector<std::pair<int,int>> reconstruct_perfect_matching(
    u64 mask, const std::vector<int8_t>& pm_choice) {
    std::vector<std::pair<int,int>> out;
    while (mask) {
        int v = std::countr_zero(mask);
        int u = pm_choice[mask];
        if (u < 0) throw std::runtime_error("perfect-matching reconstruction failed");
        out.emplace_back(v, u);
        mask &= ~(u64{1} << v);
        mask &= ~(u64{1} << u);
    }
    return out;
}

static Metrics compute_metrics(const Graph& g) {
    if (g.n > 24) throw std::runtime_error("bitmask panel solver intended for n <= 24");
    const int n = g.n;
    const u64 all = (u64{1} << n) - 1;
    const std::size_t N = std::size_t{1} << n;
    Metrics r;
    r.n = n; r.m = g.m;
    r.Delta = 0; r.delta = n ? n : 0;
    for (int v = 0; v < n; ++v) {
        int d = std::popcount(g.adj[v]);
        r.Delta = std::max(r.Delta, d);
        r.delta = std::min(r.delta, d);
    }
    r.tree = (n >= 1 && g.m == n - 1);
    r.regular = (r.Delta == r.delta);

    std::vector<unsigned char> pc(N, 0), independent(N, 0), connected(N, 0);
    std::vector<u64> closed_union(N, 0), open_union(N, 0);
    independent[0] = 1;
    connected[0] = 0;
    for (std::size_t mask = 1; mask < N; ++mask) {
        u64 m = static_cast<u64>(mask);
        int v = std::countr_zero(m);
        u64 rest = m & (m - 1);
        pc[mask] = static_cast<unsigned char>(pc[rest] + 1);
        independent[mask] = static_cast<unsigned char>(independent[rest] && ((g.adj[v] & rest) == 0));
        closed_union[mask] = closed_union[rest] | g.adj[v] | (u64{1} << v);
        open_union[mask] = open_union[rest] | g.adj[v];
    }

    // Connectivity of every nonempty induced vertex set, independently of domination.
    for (std::size_t mask = 1; mask < N; ++mask) {
        u64 S = static_cast<u64>(mask);
        u64 seen = S & -S;
        u64 frontier = seen;
        while (frontier) {
            u64 nxt = 0;
            u64 f = frontier;
            while (f) {
                int v = std::countr_zero(f);
                f &= f - 1;
                nxt |= g.adj[v];
            }
            nxt &= S & ~seen;
            seen |= nxt;
            frontier = nxt;
        }
        connected[mask] = static_cast<unsigned char>(seen == S);
    }

    // Perfect matching DP on induced subgraphs. choice[mask] stores the mate of the least vertex.
    std::vector<int8_t> pm_state(N, -1), pm_choice(N, -1);
    pm_state[0] = 1;
    std::function<bool(u64)> has_pm = [&](u64 mask) -> bool {
        int8_t& state = pm_state[mask];
        if (state != -1) return state == 1;
        if (std::popcount(mask) & 1) { state = 0; return false; }
        int v = std::countr_zero(mask);
        u64 rest = mask & ~(u64{1} << v);
        u64 candidates = g.adj[v] & rest;
        while (candidates) {
            int u = std::countr_zero(candidates);
            candidates &= candidates - 1;
            if (has_pm(rest & ~(u64{1} << u))) {
                state = 1; pm_choice[mask] = static_cast<int8_t>(u); return true;
            }
        }
        state = 0; return false;
    };
    for (u64 mask = 0; mask <= all; ++mask) {
        if ((std::popcount(mask) & 1) == 0) (void)has_pm(mask);
    }

    const int INF = 1000000;
    r.gamma = r.indep_dom = r.gamma_c = r.gamma_R = r.alpha = INF;
    r.gamma_t = r.gamma_pr = INF;
    r.mu_star = INF;
    r.alpha = 0;

    for (u64 mask = 0; mask <= all; ++mask) {
        int k = pc[mask];
        if (independent[mask] && k > r.alpha) { r.alpha = k; r.alpha_set = mask; }

        if (closed_union[mask] == all) {
            if (k < r.gamma) { r.gamma = k; r.gamma_set = mask; }
            if (independent[mask] && k < r.indep_dom) { r.indep_dom = k; r.indep_dom_set = mask; }
            if (mask != 0 && connected[mask] && k < r.gamma_c) { r.gamma_c = k; r.gamma_c_set = mask; }
            if ((k % 2 == 0) && has_pm(mask) && k < r.gamma_pr) {
                r.gamma_pr = k; r.gamma_pr_set = mask;
            }
        }
        if (n >= 2 && open_union[mask] == all && k < r.gamma_t) {
            r.gamma_t = k; r.gamma_t_set = mask;
        }

        int roman = 2 * k + n - pc[closed_union[mask]];
        if (roman < r.gamma_R) {
            r.gamma_R = roman;
            r.gamma_R_twos = mask;
            r.gamma_R_ones = all & ~closed_union[mask];
        }

        // A matching is maximal iff its unmatched vertices form an independent set.
        // For unmatched set U, G[V\U] must have a perfect matching.
        if (independent[mask]) {
            u64 matched = all & ~mask;
            if (has_pm(matched)) {
                int val = (n - k) / 2;
                if (val < r.mu_star) {
                    r.mu_star = val;
                    r.mu_unmatched = mask;
                }
            }
        }
    }
    r.tau = n - r.alpha;
    if (r.gamma_t == INF) r.gamma_t = -1;
    if (r.gamma_pr == INF) r.gamma_pr = -1;
    if (r.mu_star == INF) r.mu_star = -1;
    if (r.gamma_pr >= 0) r.gamma_pr_matching = reconstruct_perfect_matching(r.gamma_pr_set, pm_choice);
    if (r.mu_star >= 0) r.mu_matching = reconstruct_perfect_matching(all & ~r.mu_unmatched, pm_choice);
    return r;
}

static std::string edge_list_string(const std::vector<std::pair<int,int>>& E) {
    std::ostringstream os;
    for (std::size_t i = 0; i < E.size(); ++i) {
        if (i) os << ';';
        os << E[i].first << '-' << E[i].second;
    }
    return os.str();
}

int main(int argc, char** argv) {
    if (argc < 3) {
        std::cerr << "usage: sweep OUT.csv graph1.g6 [graph2.g6 ...]\n";
        return 2;
    }
    std::ofstream out(argv[1]);
    if (!out) { std::cerr << "cannot open output\n"; return 2; }
    out << "graph6,n,m,Delta,delta,tree,regular,gamma,gamma_set,gamma_t,gamma_t_set,independent_domination,independent_domination_set,connected_domination,connected_domination_set,roman_domination,roman_twos,roman_ones,paired_domination,paired_domination_set,paired_matching,alpha,alpha_set,tau,min_maximal_matching,mu_unmatched,mu_matching,ore_slack,tx_i_mu_slack\n";
    std::uint64_t total = 0;
    auto t0 = std::chrono::steady_clock::now();
    for (int a = 2; a < argc; ++a) {
        std::ifstream in(argv[a]);
        if (!in) { std::cerr << "cannot open " << argv[a] << "\n"; return 2; }
        std::string line;
        std::uint64_t count = 0;
        while (std::getline(in, line)) {
            if (line.empty() || line.rfind(">>graph6<<", 0) == 0) continue;
            Graph g = parse_graph6(line);
            if (!is_connected_graph(g)) {
                std::cerr << "input contains disconnected graph: " << line << "\n";
                return 3;
            }
            Metrics r = compute_metrics(g);
            int ore_slack = (r.n >= 2 ? r.n - 2 * r.gamma : -999);
            int tx_slack = r.mu_star - r.indep_dom;
            out << line << ',' << r.n << ',' << r.m << ',' << r.Delta << ',' << r.delta << ','
                << (r.tree?1:0) << ',' << (r.regular?1:0) << ','
                << r.gamma << ',' << r.gamma_set << ','
                << r.gamma_t << ',' << r.gamma_t_set << ','
                << r.indep_dom << ',' << r.indep_dom_set << ','
                << r.gamma_c << ',' << r.gamma_c_set << ','
                << r.gamma_R << ',' << r.gamma_R_twos << ',' << r.gamma_R_ones << ','
                << r.gamma_pr << ',' << r.gamma_pr_set << ',' << edge_list_string(r.gamma_pr_matching) << ','
                << r.alpha << ',' << r.alpha_set << ',' << r.tau << ','
                << r.mu_star << ',' << r.mu_unmatched << ',' << edge_list_string(r.mu_matching) << ','
                << ore_slack << ',' << tx_slack << '\n';
            ++count; ++total;
        }
        std::cerr << argv[a] << ": " << count << " graphs\n";
    }
    auto t1 = std::chrono::steady_clock::now();
    std::cerr << "total " << total << " graphs in "
              << std::chrono::duration<double>(t1-t0).count() << " s\n";
    return 0;
}
