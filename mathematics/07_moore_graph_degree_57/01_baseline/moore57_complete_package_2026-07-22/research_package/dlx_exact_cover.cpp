#include <algorithm>
#include <fstream>
#include <iostream>
#include <limits>
#include <string>
#include <vector>

class DLX {
public:
    DLX(int columns, int rows, long long nonzeros)
        : ncol(columns), nrow(rows),
          left(columns + 1 + nonzeros + 5), right(left.size()),
          up(left.size()), down(left.size()), column(left.size()),
          size(columns + 1, 0), row_id(left.size()) {
        for (int i = 0; i <= ncol; ++i) {
            left[i] = i - 1;
            right[i] = i + 1;
            up[i] = down[i] = i;
            column[i] = i;
        }
        left[0] = ncol;
        right[ncol] = 0;
        next_node = ncol + 1;
    }

    void add_row(int id, const std::vector<int>& columns) {
        int first = -1;
        int previous = -1;
        for (int zero_based : columns) {
            int c = zero_based + 1;
            int x = next_node++;
            column[x] = c;
            row_id[x] = id;
            ++size[c];
            up[x] = up[c];
            down[x] = c;
            down[up[c]] = x;
            up[c] = x;
            if (first < 0) {
                first = previous = x;
                left[x] = right[x] = x;
            } else {
                right[previous] = x;
                left[x] = previous;
                right[x] = first;
                left[first] = x;
                previous = x;
            }
        }
    }

    bool solve() { return search(0); }
    long long visited_nodes() const { return nodes; }
    int maximum_depth() const { return max_depth; }

private:
    int ncol;
    int nrow;
    int next_node;
    std::vector<int> left, right, up, down, column, size, row_id;
    long long nodes = 0;
    int max_depth = 0;

    void cover(int c) {
        left[right[c]] = left[c];
        right[left[c]] = right[c];
        for (int i = down[c]; i != c; i = down[i]) {
            for (int j = right[i]; j != i; j = right[j]) {
                up[down[j]] = up[j];
                down[up[j]] = down[j];
                --size[column[j]];
            }
        }
    }

    void uncover(int c) {
        for (int i = up[c]; i != c; i = up[i]) {
            for (int j = left[i]; j != i; j = left[j]) {
                ++size[column[j]];
                up[down[j]] = j;
                down[up[j]] = j;
            }
        }
        left[right[c]] = c;
        right[left[c]] = c;
    }

    bool search(int depth) {
        ++nodes;
        max_depth = std::max(max_depth, depth);
        if (right[0] == 0) return depth == 54;
        if (depth >= 54) return false;

        int chosen = -1;
        int smallest = std::numeric_limits<int>::max();
        for (int c = right[0]; c != 0; c = right[c]) {
            if (size[c] < smallest) {
                smallest = size[c];
                chosen = c;
                if (smallest <= 1) break;
            }
        }
        if (chosen < 0 || smallest == 0) return false;

        cover(chosen);
        for (int r = down[chosen]; r != chosen; r = down[r]) {
            for (int j = right[r]; j != r; j = right[j]) cover(column[j]);
            if (search(depth + 1)) return true;
            for (int j = left[r]; j != r; j = left[j]) uncover(column[j]);
        }
        uncover(chosen);
        return false;
    }
};

int main(int argc, char** argv) {
    if (argc != 2) {
        std::cerr << "usage: dlx_exact_cover INSTANCE.txt\n";
        return 2;
    }
    std::ifstream input(argv[1]);
    int ncol = 0, nrow = 0;
    input >> ncol >> nrow;
    if (!input || ncol != 3024) {
        std::cerr << "invalid header\n";
        return 2;
    }
    for (int i = 0, value = 0; i < 56; ++i) input >> value; // fixed permutation, audit metadata

    std::vector<int> row_type(nrow);
    std::vector<std::vector<int>> rows(nrow, std::vector<int>(56));
    for (int r = 0; r < nrow; ++r) {
        input >> row_type[r];
        for (int& c : rows[r]) input >> c;
        if (!input) {
            std::cerr << "truncated row " << r << "\n";
            return 2;
        }
    }

    DLX solver(ncol, nrow, static_cast<long long>(nrow) * 56);
    for (int r = 0; r < nrow; ++r) solver.add_row(r, rows[r]);
    bool satisfiable = solver.solve();
    std::cout << "satisfiable=" << (satisfiable ? "true" : "false")
              << " nodes=" << solver.visited_nodes()
              << " max_depth=" << solver.maximum_depth() << "\n";
    return 0;
}
