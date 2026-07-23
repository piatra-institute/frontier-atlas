#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

namespace {
constexpr int N = 510;
constexpr int M = 2504;
constexpr int C = 84;

std::vector<std::pair<int,int>> load_edges(const std::string& path) {
    std::ifstream in(path);
    if (!in) throw std::runtime_error("cannot open edge file");
    std::vector<std::pair<int,int>> edges;
    std::string tag;
    int declared_n = -1, declared_m = -1;
    while (in >> tag) {
        if (tag == "p") {
            std::string kind;
            in >> kind >> declared_n >> declared_m;
            if (kind != "edge") throw std::runtime_error("bad edge header");
        } else if (tag == "e") {
            int u, v;
            in >> u >> v;
            --u; --v;
            if (u < 0 || u >= N || v < 0 || v >= N || u == v)
                throw std::runtime_error("bad edge endpoint");
            if (u > v) std::swap(u, v);
            edges.emplace_back(u, v);
        } else {
            throw std::runtime_error("unknown edge-file token");
        }
    }
    std::sort(edges.begin(), edges.end());
    if (declared_n != N || declared_m != M || static_cast<int>(edges.size()) != M)
        throw std::runtime_error("wrong edge counts");
    if (std::adjacent_find(edges.begin(), edges.end()) != edges.end())
        throw std::runtime_error("duplicate edge");
    return edges;
}

std::vector<std::array<std::uint8_t,N>> load_colorings(const std::string& path) {
    std::ifstream in(path);
    if (!in) throw std::runtime_error("cannot open coloring file");
    std::string line;
    if (!std::getline(in, line)) throw std::runtime_error("empty coloring file");
    std::vector<std::array<std::uint8_t,N>> rows;
    int expected_id = 1;
    while (std::getline(in, line)) {
        std::stringstream ss(line);
        std::string field;
        if (!std::getline(ss, field, ',')) throw std::runtime_error("missing id");
        if (std::stoi(field) != expected_id) throw std::runtime_error("bad coloring id");
        std::array<std::uint8_t,N> row{};
        for (int v = 0; v < N; ++v) {
            if (!std::getline(ss, field, ',')) throw std::runtime_error("short coloring row");
            int color = std::stoi(field);
            if (color < 0 || color > 4) throw std::runtime_error("color outside 0..4");
            row[v] = static_cast<std::uint8_t>(color);
        }
        if (std::getline(ss, field, ',')) throw std::runtime_error("long coloring row");
        rows.push_back(row);
        ++expected_id;
    }
    if (static_cast<int>(rows.size()) != C) throw std::runtime_error("wrong coloring count");
    return rows;
}
} // namespace

int main(int argc, char** argv) {
    try {
        if (argc != 3) {
            std::cerr << "usage: verify_coloring EDGE_FILE COLORINGS_CSV\n";
            return 2;
        }
        const auto edges = load_edges(argv[1]);
        const auto rows = load_colorings(argv[2]);
        std::array<std::array<bool,N>,N> adjacent{};
        for (const auto& [u,v] : edges) adjacent[u][v] = adjacent[v][u] = true;

        for (int r = 0; r < C; ++r) {
            for (const auto& [u,v] : edges) {
                if (rows[r][u] == rows[r][v])
                    throw std::runtime_error("monochromatic listed edge");
            }
        }

        int nonedges = 0;
        for (int u = 0; u < N; ++u) {
            for (int v = u + 1; v < N; ++v) {
                if (adjacent[u][v]) continue;
                ++nonedges;
                bool same = false, different = false;
                for (int r = 0; r < C; ++r) {
                    if (rows[r][u] == rows[r][v]) same = true;
                    else different = true;
                }
                if (!same || !different)
                    throw std::runtime_error("uncovered nonedge relation");
            }
        }
        if (nonedges != 127291) throw std::runtime_error("wrong nonedge count");
        std::cout << "VERIFIED C++\n"
                  << "  proper colorings: " << C << "\n"
                  << "  edges checked per coloring: " << M << "\n"
                  << "  pair-flexible nonedges: " << nonedges << "\n";
        return 0;
    } catch (const std::exception& error) {
        std::cerr << "FAILED: " << error.what() << "\n";
        return 1;
    }
}
