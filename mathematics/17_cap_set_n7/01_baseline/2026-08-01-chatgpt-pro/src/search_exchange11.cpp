#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_set>
#include <vector>

struct Mask {
    std::array<uint64_t,4> w{};
    void set(int i){w[i>>6]|=uint64_t(1)<<(i&63);}
    bool test(int i)const{return (w[i>>6]>>(i&63))&1;}
    bool operator==(const Mask&o)const{return w==o.w;}
    bool operator<(const Mask&o)const{return w<o.w;}
};
struct Record {
    Mask m; uint16_t q;
    bool operator<(const Record&o)const { return m<o.m || (!(o.m<m) && q<o.q); }
    bool operator==(const Record&o)const { return m==o.m && q==o.q; }
};
using P=std::array<int,7>;
static int enc(const P&p){int z=0,m=1;for(int i=0;i<7;++i){z+=p[i]*m;m*=3;}return z;}
static P dec(int z){P p{};for(int i=0;i<7;++i){p[i]=z%3;z/=3;}return p;}
static int negsum(int x,int y){P a=dec(x),b=dec(y),c{};for(int i=0;i<7;++i)c[i]=(6-a[i]-b[i])%3;return enc(c);}

int main(int argc,char**argv){
    std::string path=argc>1?argv[1]:"cf236.txt";
    std::ifstream f(path);if(!f){std::cerr<<"cannot open "<<path<<"\n";return 2;}
    std::vector<int>C;std::string s;
    while(f>>s){assert(s.size()==7);P p{};for(int i=0;i<7;++i)p[i]=s[i]-'0';C.push_back(enc(p));}
    assert(C.size()==236);
    std::array<int,2187>idx;idx.fill(-1);for(int i=0;i<236;++i)idx[C[i]]=i;
    std::vector<std::vector<std::pair<int,int>>> blockers(2187);
    for(int i=0;i<236;++i)for(int j=i+1;j<236;++j){int q=negsum(C[i],C[j]);if(idx[q]<0)blockers[q].push_back({i,j});}
    std::vector<int> low10,low11;
    for(int q=0;q<2187;++q)if(idx[q]<0){if(blockers[q].size()==10)low10.push_back(q);if(blockers[q].size()==11)low11.push_back(q);}
    assert(low10.size()==24&&low11.size()==416);
    const size_t expected=low11.size()*(1u<<11)+low10.size()*(1u<<10)*(236-10);
    std::vector<Record> records;records.reserve(expected);
    auto enumerate_min=[&](int q,auto emit){
        const auto&e=blockers[q];size_t lim=size_t(1)<<e.size();
        for(size_t bits=0;bits<lim;++bits){Mask m;for(size_t k=0;k<e.size();++k)m.set(((bits>>k)&1)?e[k].second:e[k].first);emit(m);}
    };
    for(int q:low11)enumerate_min(q,[&](const Mask&m){records.push_back({m,(uint16_t)q});});
    for(int q:low10)enumerate_min(q,[&](const Mask&m10){for(int i=0;i<236;++i)if(!m10.test(i)){Mask m=m10;m.set(i);records.push_back({m,(uint16_t)q});}});
    assert(records.size()==expected);
    std::cout<<"generated size-11 cover records "<<records.size()<<"\n";
    std::sort(records.begin(),records.end());
    records.erase(std::unique(records.begin(),records.end()),records.end());
    std::cout<<"unique (removal set, unlocked point) records "<<records.size()<<"\n";
    size_t best=0,unique=0;Mask bestMask{};
    for(size_t i=0;i<records.size();){size_t j=i+1;while(j<records.size()&&records[j].m==records[i].m)++j;++unique;if(j-i>best){best=j-i;bestMask=records[i].m;}i=j;}
    std::cout<<"unique size-11 removal sets "<<unique<<"\n";
    std::cout<<"maximum individually unlocked outside points "<<best<<"\n";
    std::cout<<"best removed indices";for(int i=0;i<236;++i)if(bestMask.test(i))std::cout<<' '<<i;std::cout<<"\n";
    std::vector<int> unlocked;
    for(int q=0;q<2187;++q)if(idx[q]<0&&blockers[q].size()<=11){bool ok=true;for(auto [i,j]:blockers[q])if(!bestMask.test(i)&&!bestMask.test(j)){ok=false;break;}if(ok)unlocked.push_back(q);}
    assert(unlocked.size()==best);
    std::cout<<"best unlocked points\n";for(int q:unlocked){auto p=dec(q);for(int x:p)std::cout<<x;std::cout<<"\n";}
    if(best<=11)std::cout<<"CERTIFIED LOCAL OBSTRUCTION: no exchange removing <=11 cap points can add more points than it removes.\n";
    else std::cout<<"candidate requires compatibility checking\n";
}
