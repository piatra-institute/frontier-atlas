#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <utility>
#include <vector>
using P=std::array<int,7>;
static int enc(const P&p){int z=0,m=1;for(int i=0;i<7;++i){z+=p[i]*m;m*=3;}return z;}
static P dec(int z){P p{};for(int i=0;i<7;++i){p[i]=z%3;z/=3;}return p;}
static int negsum(int x,int y){P a=dec(x),b=dec(y),c{};for(int i=0;i<7;++i)c[i]=(6-a[i]-b[i])%3;return enc(c);}

static int min_cover_union(const std::vector<std::pair<int,int>>&A,const std::vector<std::pair<int,int>>&B){
    std::array<std::vector<int>,236> adj;
    std::set<std::pair<int,int>> edges;
    for(auto e:A){if(e.first>e.second)std::swap(e.first,e.second);edges.insert(e);}
    for(auto e:B){if(e.first>e.second)std::swap(e.first,e.second);edges.insert(e);}
    for(auto [u,v]:edges){adj[u].push_back(v);adj[v].push_back(u);}
    for(auto &v:adj)assert(v.size()<=2);
    std::array<uint8_t,236>seen{};int answer=0;
    for(int s=0;s<236;++s)if(!seen[s]&&!adj[s].empty()){
        int verts=0,deg_sum=0;std::vector<int>stack{s};seen[s]=1;
        while(!stack.empty()){int u=stack.back();stack.pop_back();++verts;deg_sum+=adj[u].size();for(int v:adj[u])if(!seen[v]){seen[v]=1;stack.push_back(v);}}
        int e=deg_sum/2;
        bool cycle=(e==verts);
        if(cycle){assert(e%2==0);answer+=e/2;}
        else {assert(e==verts-1);answer+=(e+1)/2;}
    }
    return answer;
}
int main(int argc,char**argv){
    std::string path=argc>1?argv[1]:"cf236.txt";std::ifstream f(path);if(!f)return 2;
    std::vector<int>C;std::string s;while(f>>s){P p{};for(int i=0;i<7;++i)p[i]=s[i]-'0';C.push_back(enc(p));}assert(C.size()==236);
    std::array<int,2187>idx;idx.fill(-1);for(int i=0;i<236;++i)idx[C[i]]=i;
    std::vector<std::vector<std::pair<int,int>>> blockers(2187);
    for(int i=0;i<236;++i)for(int j=i+1;j<236;++j){int q=negsum(C[i],C[j]);if(idx[q]<0)blockers[q].push_back({i,j});}
    std::vector<int>O;for(int q=0;q<2187;++q)if(idx[q]<0)O.push_back(q);assert(O.size()==1951);
    int best=999;std::pair<int,int>bestpq{};std::map<int,uint64_t>hist;std::map<std::pair<int,int>,int>best_by_counts;
    uint64_t tested=0;
    for(size_t i=0;i<O.size();++i)for(size_t j=i+1;j<O.size();++j){
        int p=O[i],q=O[j];int v=min_cover_union(blockers[p],blockers[q]);++hist[v];++tested;
        int kp=(int)blockers[p].size(), kq=(int)blockers[q].size();
        auto key=std::make_pair(std::min(kp,kq),std::max(kp,kq));
        auto it=best_by_counts.find(key);if(it==best_by_counts.end()||v<it->second)best_by_counts[key]=v;
        if(v<best){best=v;bestpq={p,q};}
    }
    std::cout<<"outside pairs tested "<<tested<<"\nminimum removals to unlock two outside points "<<best<<"\n";
    std::cout<<"witness blocker counts "<<blockers[bestpq.first].size()<<' '<<blockers[bestpq.second].size()<<"\n";
    for(int q:{bestpq.first,bestpq.second}){auto p=dec(q);for(int x:p)std::cout<<x;std::cout<<"\n";}
    std::cout<<"cover-size histogram\n";for(auto [k,v]:hist)std::cout<<k<<' '<<v<<"\n";
    std::cout<<"minimum by blocker-count pair (only entries <=20 cover shown)\n";
    for(auto [k,v]:best_by_counts)if(v<=20)std::cout<<k.first<<' '<<k.second<<' '<<v<<"\n";
}
