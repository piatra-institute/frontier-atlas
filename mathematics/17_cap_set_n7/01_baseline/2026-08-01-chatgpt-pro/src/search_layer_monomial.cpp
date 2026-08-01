#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <set>
#include <string>
#include <vector>

using P = std::array<int,6>;

static int enc(const P& p) {
    int n=0,m=1;
    for(int i=0;i<6;++i){ n += p[i]*m; m*=3; }
    return n;
}
static P dec(int n) {
    P p{};
    for(int i=0;i<6;++i){p[i]=n%3;n/=3;}
    return p;
}
static int add_code(int x,int y) {
    P a=dec(x),b=dec(y),c{};
    for(int i=0;i<6;++i)c[i]=(a[i]+b[i])%3;
    return enc(c);
}
static int negsum_code(int x,int y) {
    P a=dec(x),b=dec(y),c{};
    for(int i=0;i<6;++i)c[i]=(6-a[i]-b[i])%3;
    return enc(c);
}

static bool is_cap(const std::vector<int>& s) {
    std::array<bool,729> in{};
    for(int x:s)in[x]=true;
    for(size_t i=0;i<s.size();++i)for(size_t j=i+1;j<s.size();++j){
        int z=negsum_code(s[i],s[j]);
        if(in[z]) return false;
    }
    return true;
}

int main(){
    // 2-(6,3,2) design from the Calderbank-Fishburn/Edel-Bierbrauer construction.
    const std::set<std::array<int,3>> Dblocks{
        {0,1,2},{1,2,5},{0,1,3},{1,3,4},{0,2,4},
        {1,4,5},{0,3,5},{2,3,4},{0,4,5},{2,3,5}
    };
    std::vector<int>A,B;
    for(int code=0;code<729;++code){
        P p=dec(code);
        std::vector<int> supp;
        int twos=0; bool full=true;
        for(int i=0;i<6;++i){if(p[i])supp.push_back(i);else full=false;if(p[i]==2)++twos;}
        bool inR=full && (twos%2==0);
        bool inD=false,inDb=false;
        if(supp.size()==3){
            std::array<int,3> bl{supp[0],supp[1],supp[2]};
            inD=Dblocks.count(bl);
            inDb=!inD;
        }
        if(inD||inR)A.push_back(code);
        if(inDb||inR)B.push_back(code);
    }
    assert(A.size()==112 && B.size()==112 && is_cap(A) && is_cap(B));

    static uint16_t sumtab[729][729];
    for(int x=0;x<729;++x)for(int y=0;y<729;++y)sumtab[x][y]=add_code(x,y);

    std::array<int,6> perm{0,1,2,3,4,5};
    int64_t transforms=0;
    int best=-1,best_cap=-1;
    std::array<int,6> bestperm{}, bestsign{};
    std::vector<int> bestallowed;
    std::vector<int64_t> histogram(730,0);

    do {
        for(int mask=0;mask<64;++mask){
            std::array<int,6> sign{};
            for(int i=0;i<6;++i)sign[i]=((mask>>i)&1)?2:1;
            std::vector<int> TB;TB.reserve(B.size());
            for(int code:B){
                P p=dec(code),q{};
                // q_i = sign_i * p_{perm_i}
                for(int i=0;i<6;++i)q[i]=(sign[i]*p[perm[i]])%3;
                TB.push_back(enc(q));
            }
            std::array<bool,729> forbidden{};
            int nforb=0;
            for(int x:A){
                for(int y:TB){
                    int z=sumtab[x][y];
                    if(!forbidden[z]){forbidden[z]=true;++nforb;}
                }
                if(nforb==729)break;
            }
            int allowed=729-nforb;
            ++histogram[allowed];
            std::vector<int>S;
            if(allowed>=best_cap || allowed>best){
                for(int z=0;z<729;++z)if(!forbidden[z])S.push_back(z);
            }
            int capsize=-1;
            if(allowed<=40 && !S.empty() && is_cap(S)) capsize=allowed;
            if(allowed>best || (allowed==best && capsize>best_cap)){
                best=allowed;best_cap=capsize;bestperm=perm;bestsign=sign;bestallowed=S;
                std::cout<<"new best allowed="<<best<<" whole_allowed_is_cap="<<(capsize==allowed)
                         <<" transform="<<transforms<<"\n";
            }
            ++transforms;
        }
    } while(std::next_permutation(perm.begin(),perm.end()));

    std::cout<<"transforms "<<transforms<<"\n";
    std::cout<<"best allowed cardinality "<<best<<"\n";
    std::cout<<"best entire allowed cap size marker "<<best_cap<<"\n";
    std::cout<<"best permutation";for(int x:bestperm)std::cout<<' '<<x;std::cout<<"\n";
    std::cout<<"best signs";for(int x:bestsign)std::cout<<' '<<x;std::cout<<"\n";
    std::cout<<"nonzero histogram\n";
    for(int i=0;i<=729;++i)if(histogram[i])std::cout<<i<<' '<<histogram[i]<<"\n";
    std::cout<<"best allowed points\n";
    for(int z:bestallowed){P p=dec(z);for(int x:p)std::cout<<x;std::cout<<"\n";}
}
