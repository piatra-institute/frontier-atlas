#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <set>
#include <tuple>
#include <vector>
using T=std::array<int,3>;
static long long C2(long long x){return x*(x-1)/2;}
static long long C3(long long x){return x*(x-1)*(x-2)/6;}
static long long P(const T&t){return C2(t[0])+C2(t[1])+C2(t[2]);}
static long long Q(const T&t){return C3(t[0])+C3(t[1])+C3(t[2]);}
static std::vector<T> types(int M){
 std::vector<T> v; for(int a=0;a<=112;a++)for(int b=0;b<=a;b++){int c=M-a-b;if(0<=c&&c<=b)v.push_back({a,b,c});}return v;
}
int main(){
 const long long D=1093, PM=364, TM=121;
 // M=289 standard diagram.
 {
  auto ts=types(289); assert(ts.size()==208);
  std::set<T> expected{{112,112,65},{112,111,66},{112,110,67},{111,111,67}},neg,zero;
  for(auto t:ts){long long s=86*Q(t)-7793*P(t)+70101168LL;if(s<0)neg.insert(t);if(s==0)zero.insert(t);}
  assert(neg==expected); assert((zero==std::set<T>{{97,96,96},{111,110,68}}));
  long long TP=PM*C2(289),TQ=TM*C3(289),S=86*TQ-7793*TP+D*70101168LL;
  assert(TP==15148224&&TQ==481732944&&S==-499824);
  std::cout<<"PASS M=289: 208 types; exactly four negative profiles; total slack -499824.\n";
 }
 // M=291 standard diagram: every putative cap has >=7 (112,112,67) directions.
 {
  auto ts=types(291); assert(ts.size()==192);
  T bad{112,112,67}; std::set<T> neg,zero;
  long long P0=P({97,97,97}),Q0=Q({97,97,97});
  auto slack=[&](T t){return 631*(Q(t)-Q0)-57531*(P(t)-P0);};
  for(auto t:ts){long long s=slack(t);if(s<0)neg.insert(t);if(s==0)zero.insert(t);}
  assert((neg==std::set<T>{bad})); assert((zero==std::set<T>{{97,97,97},{112,111,68}}));
  assert(slack(bad)==-74250);
  long long TP=PM*C2(291),TQ=TM*C3(291);
  long long S=631*(TQ-D*Q0)-57531*(TP-D*P0);
  assert(TP==15358980&&TQ==491838985&&S==-505661);
  // With all other slacks nonnegative, n_bad * 74250 >= 505661.
  assert((505661+74250-1)/74250==7);
  std::cout<<"PASS M=291: 192 types; only (112,112,67) is negative; at least 7 such directions.\n";
 }
}
