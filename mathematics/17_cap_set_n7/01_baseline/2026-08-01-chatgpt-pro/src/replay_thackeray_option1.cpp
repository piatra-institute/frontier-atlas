#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <tuple>
#include <vector>
using P=std::array<int,6>;
static int enc(const P&p){int z=0,m=1;for(int i=0;i<6;++i){z+=p[i]*m;m*=3;}return z;}
static P dec(int z){P p{};for(int i=0;i<6;++i){p[i]=z%3;z/=3;}return p;}
static int dot(const P&a,const P&b){int s=0;for(int i=0;i<6;++i)s+=a[i]*b[i];return s%3;}
static int negsum(int x,int y){auto a=dec(x),b=dec(y);P c{};for(int i=0;i<6;++i)c[i]=(6-a[i]-b[i])%3;return enc(c);}
static std::vector<int> cap112(){
 const std::set<std::array<int,3>> D{{0,1,2},{1,2,5},{0,1,3},{1,3,4},{0,2,4},{1,4,5},{0,3,5},{2,3,4},{0,4,5},{2,3,5}};
 std::vector<int>A;
 for(int z=0;z<729;++z){auto p=dec(z);std::vector<int>s;int twos=0;bool full=true;for(int i=0;i<6;++i){if(p[i])s.push_back(i);else full=false;if(p[i]==2)++twos;}bool inR=full&&twos%2==0,inD=false;if(s.size()==3)inD=D.count({s[0],s[1],s[2]});if(inD||inR)A.push_back(z);}assert(A.size()==112);return A;
}
int main(){
 auto A=cap112(); const P ell{0,0,1,1,0,1};
 std::array<int,3> slices{};for(int x:A)++slices[dot(ell,dec(x))];assert((slices==std::array<int,3>{22,45,45}));
 std::vector<P>K;for(int z=0;z<729;++z){auto v=dec(z);if(dot(ell,v)==0)K.push_back(v);}assert(K.size()==243);
 std::map<std::tuple<int,int,int,int,int>,int> cases;
 int total=0, fully_blocked=0;
 for(int sign:{1,2})for(const auto&v:K){
   std::vector<int>B;B.reserve(112);
   for(int x:A){auto p=dec(x);int layer=dot(ell,p);P q{};for(int i=0;i<6;++i)q[i]=(sign*p[i]+layer*v[i])%3;B.push_back(enc(q));}
   assert(std::set<int>(B.begin(),B.end()).size()==112);
   std::array<int,729>n{};for(int x:A)for(int y:B)++n[negsum(x,y)];
   int zeros=0,ones=0,twos=0,low=0,mn=999,mx=0;
   for(int z=0;z<729;++z){zeros+=n[z]==0;ones+=n[z]==1;twos+=n[z]==2;low+=n[z]<=2;mn=std::min(mn,n[z]);mx=std::max(mx,n[z]);}
   if(zeros==0)++fully_blocked;
   ++cases[{low,ones,twos,mn,mx}];++total;
 }
 assert(total==486 && fully_blocked==486);
 const std::map<std::tuple<int,int,int,int,int>,int> expected{
   {{112,112,0,1,112},2},
   {{2,0,2,2,56},440},
   {{0,0,0,11,46},44}
 };
 assert(cases==expected);
 std::cout<<"PASS: Thackeray Proposition 4.1 Option-1 finite subsearch replay\n";
 std::cout<<"normalized transformations checked 486 (=2*3^5)\n";
 std::cout<<"all 729 middle-layer points are cross-blocked in every transformation\n";
 std::cout<<"case histogram: (low<=2, n=1, n=2, min, max) -> transformations\n";
 for(auto const&[k,v]:cases){auto [low,one,two,mn,mx]=k;std::cout<<low<<' '<<one<<' '<<two<<' '<<mn<<' '<<mx<<" -> "<<v<<'\n';}
 std::cout<<"Scope: this replays the 486-option search after the paper's structural normalization; it does not certify that normalization.\n";
}
