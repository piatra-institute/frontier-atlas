#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <tuple>
#include <vector>

static int64_t C2(int64_t x) { return x * (x - 1) / 2; }
static int64_t C3(int64_t x) { return x * (x - 1) * (x - 2) / 6; }

struct Type {
    int a, b, c;
    int64_t P, Q, dP, slack;
};

int main() {
    constexpr int n = 7;
    constexpr int m = 292;
    constexpr int hmax = 112;
    constexpr int64_t directions = (2187 - 1) / 2;  // 1093
    constexpr int64_t pair_mult = (729 - 1) / 2;    // 364
    constexpr int64_t triple_mult = (243 - 1) / 2; // 121

    const std::array<int,3> base{98,97,97};
    const std::array<int,3> edge{112,112,68};
    const int64_t P0 = C2(98) + C2(97) + C2(97);
    const int64_t Q0 = C3(98) + C3(97) + C3(97);
    const int64_t P1 = C2(112) + C2(112) + C2(68);
    const int64_t Q1 = C3(112) + C3(112) + C3(68);
    assert(P0 == 14065 && Q0 == 446976);
    assert(P1 - P0 == 645 && Q1 - Q0 == 58980);
    assert(3932 * (P1 - P0) == 43 * (Q1 - Q0));

    std::vector<Type> types;
    for (int a=0; a<=hmax; ++a) {
        for (int b=0; b<=a; ++b) {
            int c = m-a-b;
            if (0 <= c && c <= b) {
                int64_t P = C2(a)+C2(b)+C2(c);
                int64_t Q = C3(a)+C3(b)+C3(c);
                int64_t dP = P-P0;
                int64_t s = 43*(Q-Q0)-3932*dP;
                types.push_back({a,b,c,P,Q,dP,s});
            }
        }
    }
    assert(types.size() == 184);
    for (const auto &t: types) assert(t.slack >= 0);

    const int64_t totalP = pair_mult*C2(m);
    const int64_t totalQ = triple_mult*C3(m);
    const int64_t totalSlack = 43*(totalQ-directions*Q0)
                              -3932*(totalP-directions*P0);
    assert(totalP == 15464904);
    assert(totalQ == 496944580);
    assert(totalSlack == 2328);

    std::vector<Type> zero, low;
    for (const auto &t: types) {
        if (t.slack == 0) zero.push_back(t);
        if (0 < t.slack && t.slack <= totalSlack) low.push_back(t);
    }
    assert(zero.size() == 2);
    assert(std::tie(zero[0].a,zero[0].b,zero[0].c) == std::tie(base[0],base[1],base[2]));
    assert(std::tie(zero[1].a,zero[1].b,zero[1].c) == std::tie(edge[0],edge[1],edge[2]));

    std::sort(low.begin(), low.end(), [](const Type& x, const Type& y){ return x.slack < y.slack; });

    const std::vector<std::tuple<int,int,int,int64_t,int64_t>> expected{
        {98,98,96,1,196}, {99,97,96,2,435}, {99,98,95,4,784},
        {100,96,96,5,1152}, {100,97,95,6,1305},
        {99,99,94,8,1482}, {100,98,94,9,1764}
    };
    assert(low.size() == expected.size());
    for (size_t i=0; i<low.size(); ++i) {
        auto got = std::make_tuple(low[i].a,low[i].b,low[i].c,low[i].dP,low[i].slack);
        assert(got == expected[i]);
    }

    std::vector<std::array<int,7>> solutions;
    std::array<int,7> counts{};
    std::function<void(int,int64_t)> rec = [&](int i, int64_t rem) {
        if (i == 7) {
            if (rem == 0) solutions.push_back(counts);
            return;
        }
        for (int k=0; k*low[i].slack<=rem; ++k) {
            counts[i]=k;
            rec(i+1, rem-k*low[i].slack);
        }
        counts[i]=0;
    };
    rec(0,totalSlack);
    assert(solutions.size() == 4);

    const std::set<std::array<int,7>> expected_solutions{
        {2,0,1,1,0,0,0}, {3,1,0,0,1,0,0},
        {3,4,0,0,0,0,0}, {6,0,0,1,0,0,0}
    };
    assert((std::set<std::array<int,7>>(solutions.begin(),solutions.end()) == expected_solutions));

    const int64_t targetDP = totalP-directions*P0;
    assert(targetDP == 91859);
    for (const auto &sol: solutions) {
        int64_t positiveDP=0;
        for (int i=0;i<7;++i) positiveDP += sol[i]*low[i].dP;
        assert(positiveDP == 11);
        const int64_t residual = targetDP-positiveDP;
        assert(residual == 91848);
        assert(residual % (P1-P0) == 258);
    }

    std::cout << "PASS: independent C++ exact checker\n";
    std::cout << "184 types; total slack 2328; 4 partitions; all fail mod 645.\n";
    std::cout << "Assuming a(6)<=112, no 292-cap exists, so a(7)<=291.\n";
    return 0;
}
