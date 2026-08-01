#include <algorithm>
#include <array>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <limits>
#include <random>
#include <tuple>
#include <vector>

struct Solver {
 static constexpr int K=7,T=3,V=3,Q=27,NT=35;
 int N;
 std::vector<std::array<int,K>> a;
 std::array<std::array<int,3>,NT> triples{};
 std::array<std::array<int,Q>,NT> cnt{};
 std::vector<std::pair<int,int>> missing; // rebuilt
 int miss=0;
 std::mt19937_64 rng;
 Solver(int n,uint64_t seed):N(n),a(n),rng(seed){int z=0;for(int i=0;i<K;i++)for(int j=i+1;j<K;j++)for(int k=j+1;k<K;k++)triples[z++]={i,j,k};}
 int idx(const std::array<int,K>&r,const std::array<int,3>&c)const{return 9*r[c[0]]+3*r[c[1]]+r[c[2]];}
 int weight(int c)const{if(c==0)return 10000;if(c==1)return 20;if(c==2)return 2;return 0;}
 void init(){for(auto&x:cnt)x.fill(0);for(int r=0;r<N;r++)for(int c=0;c<K;c++)a[r][c]=std::uniform_int_distribution<int>(0,2)(rng);for(auto&r:a)for(int q=0;q<NT;q++)cnt[q][idx(r,triples[q])]++;rebuild();}
 void rebuild(){missing.clear();for(int q=0;q<NT;q++)for(int x=0;x<Q;x++)if(cnt[q][x]==0)missing.push_back({q,x});miss=missing.size();}
 struct Eval{int row;int dmiss;int denergy;};
 Eval eval_row(int r,int target_t,int target_x){
   auto nr=a[r];auto C=triples[target_t];nr[C[0]]=target_x/9;nr[C[1]]=(target_x/3)%3;nr[C[2]]=target_x%3;
   int dm=0,de=0;
   for(int q=0;q<NT;q++){
     int oi=idx(a[r],triples[q]),ni=idx(nr,triples[q]);if(oi==ni)continue;
     int co=cnt[q][oi],cn=cnt[q][ni];
     dm += ((co-1)==0)-(co==0); // old tuple decrement
     dm += ((cn+1)==0)-(cn==0); // new tuple increment (first term always false)
     de += weight(co-1)-weight(co)+weight(cn+1)-weight(cn);
   }
   return {r,dm,de};
 }
 void apply(int r,int target_t,int target_x){
   auto nr=a[r];auto C=triples[target_t];nr[C[0]]=target_x/9;nr[C[1]]=(target_x/3)%3;nr[C[2]]=target_x%3;
   for(int q=0;q<NT;q++){int oi=idx(a[r],triples[q]),ni=idx(nr,triples[q]);if(oi!=ni){cnt[q][oi]--;cnt[q][ni]++;}}
   a[r]=nr;rebuild();
 }
 bool run(double seconds){
   auto start=std::chrono::steady_clock::now();int restart=0,best=999;std::vector<std::array<int,K>> besta;
   uint64_t iter=0;
   while(std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<seconds){
     init();restart++;
     for(int local=0;local<2000000;local++,iter++){
       if(miss==0){std::cerr<<"FOUND N="<<N<<" restart="<<restart<<" iter="<<iter<<" elapsed="<<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<"\n";for(auto&r:a){for(int c=0;c<K;c++){if(c)std::cout<<',';std::cout<<r[c];}std::cout<<'\n';}return true;}
       if(miss<best){best=miss;besta=a;std::cerr<<"best N="<<N<<" miss="<<best<<" restart="<<restart<<" local="<<local<<"\n";}
       auto target=missing[std::uniform_int_distribution<int>(0,(int)missing.size()-1)(rng)];
       std::vector<Eval> ev;ev.reserve(N);
       int bestdm=999,bestde=999;
       for(int r=0;r<N;r++){auto e=eval_row(r,target.first,target.second);if(e.dmiss<bestdm||(e.dmiss==bestdm&&e.denergy<bestde)){bestdm=e.dmiss;bestde=e.denergy;ev.clear();ev.push_back(e);}else if(e.dmiss==bestdm&&e.denergy==bestde)ev.push_back(e);}
       int r;
       if(std::uniform_real_distribution<double>(0,1)(rng)<0.03)r=std::uniform_int_distribution<int>(0,N-1)(rng);else r=ev[std::uniform_int_distribution<int>(0,(int)ev.size()-1)(rng)].row;
       apply(r,target.first,target.second);
       // occasional random perturbation
       if(local>0 && local%200000==0){for(int z=0;z<20;z++){int rr=std::uniform_int_distribution<int>(0,N-1)(rng),c=std::uniform_int_distribution<int>(0,K-1)(rng);a[rr][c]=std::uniform_int_distribution<int>(0,2)(rng);}for(auto&x:cnt)x.fill(0);for(auto&r0:a)for(int q=0;q<NT;q++)cnt[q][idx(r0,triples[q])]++;rebuild();}
       if(std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()>=seconds)break;
     }
   }
   std::cerr<<"NOT_FOUND N="<<N<<" best="<<best<<" restarts="<<restart<<" iterations="<<iter<<"\n";return false;
 }
};
int main(int argc,char**argv){int N=argc>1?std::stoi(argv[1]):39;double sec=argc>2?std::stod(argv[2]):30;uint64_t seed=argc>3?std::stoull(argv[3]):1;Solver s(N,seed);return s.run(sec)?0:1;}
