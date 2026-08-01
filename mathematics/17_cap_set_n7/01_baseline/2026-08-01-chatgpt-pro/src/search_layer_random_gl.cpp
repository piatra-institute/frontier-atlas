#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <random>
#include <set>
#include <vector>

using P=std::array<uint8_t,6>;
using M=std::array<std::array<uint8_t,6>,6>;
static int enc(const P&p){int z=0,m=1;for(int i=0;i<6;++i){z+=p[i]*m;m*=3;}return z;}
static P dec(int z){P p{};for(int i=0;i<6;++i){p[i]=z%3;z/=3;}return p;}
static int addcode(int x,int y){P a=dec(x),b=dec(y),c{};for(int i=0;i<6;++i)c[i]=(a[i]+b[i])%3;return enc(c);}
static P mat_apply(const M&A,const P&p){P q{};for(int i=0;i<6;++i){int s=0;for(int j=0;j<6;++j)s+=A[i][j]*p[j];q[i]=s%3;}return q;}
static M ident(){M A{};for(int i=0;i<6;++i)A[i][i]=1;return A;}

int main(int argc,char**argv){
    int trials=500000;if(argc>1)trials=std::stoi(argv[1]);
    uint64_t seed=0xA7C236291ULL;if(argc>2)seed=std::stoull(argv[2]);
    std::mt19937_64 rng(seed);
    const std::set<std::array<int,3>> Dblocks{{0,1,2},{1,2,5},{0,1,3},{1,3,4},{0,2,4},{1,4,5},{0,3,5},{2,3,4},{0,4,5},{2,3,5}};
    std::vector<int>A,B;
    for(int z=0;z<729;++z){P p=dec(z);std::vector<int>supp;int twos=0;bool full=true;for(int i=0;i<6;++i){if(p[i])supp.push_back(i);else full=false;if(p[i]==2)++twos;}bool R=full&&twos%2==0,D=false,Db=false;if(supp.size()==3){std::array<int,3>b{supp[0],supp[1],supp[2]};D=Dblocks.count(b);Db=!D;}if(D||R)A.push_back(z);if(Db||R)B.push_back(z);}
    assert(A.size()==112&&B.size()==112);
    static uint16_t sumtab[729][729];for(int x=0;x<729;++x)for(int y=0;y<729;++y)sumtab[x][y]=addcode(x,y);
    std::array<uint64_t,730>hist{};int best=-1;M bestM{};std::vector<int>bestS;
    for(int trial=0;trial<trials;++trial){
        M T=ident();
        // Deterministic mixture of near and moderately far elementary-row-operation words.
        int length=2+(trial%25);
        for(int step=0;step<length;++step){
            int op=rng()%3;
            if(op==0){int i=rng()%6,j=rng()%6;while(j==i)j=rng()%6;std::swap(T[i],T[j]);}
            else if(op==1){int i=rng()%6;for(int j=0;j<6;++j)T[i][j]=(2*T[i][j])%3;}
            else {int i=rng()%6,j=rng()%6;while(j==i)j=rng()%6;int c=1+(rng()%2);for(int k=0;k<6;++k)T[i][k]=(T[i][k]+c*T[j][k])%3;}
        }
        std::vector<int>TB;TB.reserve(112);for(int z:B)TB.push_back(enc(mat_apply(T,dec(z))));
        std::array<uint8_t,729>forb{};int nf=0;
        for(int x:A){for(int y:TB){int z=sumtab[x][y];if(!forb[z]){forb[z]=1;++nf;}}if(nf==729)break;}
        int allowed=729-nf;++hist[allowed];
        if(allowed>best){best=allowed;bestM=T;bestS.clear();for(int z=0;z<729;++z)if(!forb[z])bestS.push_back(z);std::cout<<"new best "<<best<<" trial "<<trial<<" length "<<length<<"\n";}
    }
    std::cout<<"trials "<<trials<<" seed "<<seed<<" best "<<best<<"\n";
    std::cout<<"histogram\n";for(int i=0;i<=729;++i)if(hist[i])std::cout<<i<<' '<<hist[i]<<"\n";
    std::cout<<"best matrix rows\n";for(auto&r:bestM){for(int x:r)std::cout<<x;std::cout<<"\n";}
    std::cout<<"best allowed points\n";for(int z:bestS){auto p=dec(z);for(int x:p)std::cout<<x;std::cout<<"\n";}
}
