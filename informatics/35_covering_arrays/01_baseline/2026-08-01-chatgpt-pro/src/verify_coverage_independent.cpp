#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

static std::vector<int> parse_csv_row(const std::string& line) {
    std::vector<int> row;
    std::stringstream ss(line);
    std::string field;
    while (std::getline(ss, field, ',')) row.push_back(std::stoi(field));
    return row;
}

int main(int argc, char** argv) {
    if (argc != 2) {
        std::cerr << "usage: verify_coverage_independent <array.csv>\n";
        return 2;
    }
    std::ifstream in(argv[1]);
    if (!in) throw std::runtime_error("cannot open array");
    std::string line;
    std::getline(in, line); // header
    std::vector<std::vector<int>> a;
    while (std::getline(in, line)) {
        if (!line.empty()) a.push_back(parse_csv_row(line));
    }
    if (a.size() != 13) throw std::runtime_error("expected 13 rows");
    for (const auto& row : a) {
        if (row.size() != 8) throw std::runtime_error("expected 8 columns");
        for (int x : row) if (x < 0 || x >= 3) throw std::runtime_error("symbol outside 0..2");
    }
    int checked = 0;
    for (int i = 0; i < 8; ++i) {
        for (int j = i + 1; j < 8; ++j) {
            uint16_t mask = 0;
            for (const auto& row : a) mask |= uint16_t(1u << (3 * row[i] + row[j]));
            if (mask != 0x1FFu) {
                std::cerr << "FAIL pair=" << i << ',' << j << " mask=" << mask << '\n';
                return 1;
            }
            ++checked;
        }
    }
    std::cout << "coverage_checker=bitmask-cpp\n";
    std::cout << "array=CA(13;2,8,3)\n";
    std::cout << "column_pairs_checked=" << checked << "\n";
    std::cout << "result=PASS\n";
    return 0;
}
