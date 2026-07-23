#include <array>
#include <cctype>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

constexpr int N = 167;
constexpr int R = 4;
using State = std::array<std::array<int, N>, R>;

State read_csv(const std::string& path) {
    std::ifstream in(path);
    if (!in) throw std::runtime_error("cannot open input");
    State x{};
    std::string line, token;
    for (int r = 0; r < R; ++r) {
        if (!std::getline(in, line)) throw std::runtime_error("too few rows");
        std::stringstream ss(line);
        int i = 0;
        while (std::getline(ss, token, ',')) {
            if (i >= N) throw std::runtime_error("too many columns");
            std::size_t p = 0;
            int v = std::stoi(token, &p);
            while (p < token.size() && std::isspace(static_cast<unsigned char>(token[p]))) ++p;
            if (p != token.size() || (v != -1 && v != 1)) throw std::runtime_error("invalid entry");
            x[r][i++] = v;
        }
        if (i != N) throw std::runtime_error("wrong column count");
    }
    if (std::getline(in, line)) throw std::runtime_error("too many rows");
    return x;
}

int main(int argc, char** argv) {
    if (argc != 2) {
        std::cerr << "usage: verify_sequences candidate.csv\n";
        return 2;
    }
    try {
        State x = read_csv(argv[1]);
        std::array<int, N - 1> c{};
        std::array<int, R> sums{};
        for (int r = 0; r < R; ++r) {
            for (int i = 0; i < N; ++i) sums[r] += x[r][i];
            for (int t = 1; t < N; ++t) {
                int s = 0;
                for (int i = 0; i < N; ++i) s += x[r][i] * x[r][(i + t) % N];
                c[t - 1] += s;
            }
        }
        std::int64_t full = 0;
        int max_abs = 0, nonzero_unique = 0;
        for (int t = 0; t < N - 1; ++t) {
            full += std::int64_t(c[t]) * c[t];
            int a = c[t] < 0 ? -c[t] : c[t];
            if (a > max_abs) max_abs = a;
            if (t < 83 && c[t] != 0) ++nonzero_unique;
        }
        std::cout << "shape=4x167\nrow_sums=[" << sums[0] << ',' << sums[1] << ',' << sums[2] << ',' << sums[3] << "]\n";
        std::cout << "full_score=" << full << "\nmax_abs_paf=" << max_abs
                  << "\nnonzero_unique=" << nonzero_unique
                  << "\nexact_complementary_quad=" << (full == 0 ? "true" : "false") << "\n";
        return 0;
    } catch (const std::exception& e) {
        std::cerr << "verification error: " << e.what() << '\n';
        return 2;
    }
}
