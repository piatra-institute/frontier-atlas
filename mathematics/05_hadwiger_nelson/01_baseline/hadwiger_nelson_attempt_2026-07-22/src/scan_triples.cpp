#include <bits/stdc++.h>
using namespace std;

int main(int argc, char** argv) {
    if (argc != 3) {
        cerr << "usage: scan_triples KEMPE_SAMPLES_U8 EDGE_FILE\n";
        return 2;
    }
    const int N = 510, R = 3001, W = (R + 63) / 64;
    vector<unsigned char> C((size_t)N * R);
    ifstream f(argv[1], ios::binary);
    f.read((char*)C.data(), C.size());
    if ((size_t)f.gcount() != C.size()) { cerr << "bad input\n"; return 1; }
    vector<unsigned char> edge((size_t)N * N, 0);
    ifstream e(argv[2]);
    string s; int n, m;
    while (e >> s) {
        if (s == "p") { string edgeword; e >> edgeword >> n >> m; }
        else if (s == "e") { int u, v; e >> u >> v; --u; --v; edge[u*N+v] = edge[v*N+u] = 1; }
        else { getline(e, s); }
    }
    size_t P = (size_t)N * (N - 1) / 2;
    vector<uint64_t> B(P * W, 0);
    auto pid = [&](int a, int b)->size_t {
        if (a > b) swap(a, b);
        return (size_t)a * (2LL*N - a - 1) / 2 + (b - a - 1);
    };
    for (int a=0; a<N; ++a) for (int b=a+1; b<N; ++b) {
        uint64_t* q = &B[pid(a,b)*W];
        for (int r=0; r<R; ++r)
            if (C[(size_t)r*N+a] == C[(size_t)r*N+b]) q[r>>6] |= 1ULL << (r&63);
    }
    uint64_t lastmask = (R%64) ? ((1ULL<<(R%64))-1) : ~0ULL;
    long long triples=0, missing=0; array<long long,5> misscnt{};
    vector<array<int,4>> examples;
    for (int u=0; u<N; ++u) for (int v=u+1; v<N; ++v) {
        if (edge[u*N+v]) continue;
        const uint64_t* A = &B[pid(u,v)*W];
        for (int w=v+1; w<N; ++w) {
            if (edge[u*N+w] || edge[v*N+w]) continue;
            ++triples;
            const uint64_t* D = &B[pid(u,w)*W];
            const uint64_t* E = &B[pid(v,w)*W];
            bool seen[5] = {false,false,false,false,false};
            for (int j=0; j<W; ++j) {
                uint64_t mask=(j==W-1?lastmask:~0ULL), a=A[j], d=D[j], ee=E[j];
                seen[0] |= (a & d) != 0;
                seen[1] |= (a & (~d) & mask) != 0;
                seen[2] |= (d & (~a) & mask) != 0;
                seen[3] |= (ee & (~a) & mask) != 0;
                seen[4] |= ((~a) & (~d) & (~ee) & mask) != 0;
                if (seen[0]&&seen[1]&&seen[2]&&seen[3]&&seen[4]) break;
            }
            int mm=0;
            for (int k=0; k<5; ++k) if (!seen[k]) { mm |= 1<<k; ++misscnt[k]; }
            if (mm) { ++missing; if (examples.size()<1000) examples.push_back({u+1,v+1,w+1,mm}); }
        }
    }
    cout << "independent triples " << triples << " with missing sampled pattern " << missing << "\n";
    const char* names[] = {"AAA","AAB","ABA","ABB","ABC"};
    for (int k=0; k<5; ++k) cout << names[k] << " missing " << misscnt[k] << "\n";
    for (auto x : examples) {
        cout << x[0] << " " << x[1] << " " << x[2] << " mask=" << x[3] << " patterns=";
        for (int k=0; k<5; ++k) if (x[3]>>k&1) cout << names[k] << ",";
        cout << "\n";
    }
    return 0;
}
