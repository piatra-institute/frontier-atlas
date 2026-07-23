#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;

struct Clause { vector<int> lits; int w1=0,w2=0; };

struct RupChecker {
  int nvars;
  vector<Clause> clauses;
  vector<vector<int>> watches;
  vector<int8_t> val;
  vector<int> trail, units;
  size_t qhead=0;
  bool has_empty=false;
  explicit RupChecker(int nv):nvars(nv),watches(2*nv+2),val(nv+1,0){}
  int wi(int lit) const { int v=abs(lit); return 2*(v-1)+(lit<0); }
  bool lit_true(int lit) const { int8_t x=val[abs(lit)]; return x && ((x>0)==(lit>0)); }
  bool lit_false(int lit) const { int8_t x=val[abs(lit)]; return x && ((x>0)!=(lit>0)); }
  bool enqueue(int lit){ int v=abs(lit); int8_t want=lit>0?1:-1; if(val[v]) return val[v]==want; val[v]=want; trail.push_back(lit); return true; }
  void add_clause(vector<int> c){
    sort(c.begin(),c.end(),[](int a,int b){return abs(a)==abs(b)?a<b:abs(a)<abs(b);});
    c.erase(unique(c.begin(),c.end()),c.end());
    for(size_t i=1;i<c.size();++i) if(c[i]==-c[i-1]) return; // tautology, harmless
    int id=(int)clauses.size(); clauses.push_back({move(c),0,0}); auto &cl=clauses.back();
    if(cl.lits.empty()){has_empty=true;return;}
    if(cl.lits.size()==1){units.push_back(cl.lits[0]);return;}
    cl.w1=0;cl.w2=1;watches[wi(cl.lits[0])].push_back(id);watches[wi(cl.lits[1])].push_back(id);
  }
  bool propagate(){
    while(qhead<trail.size()){
      int false_lit=-trail[qhead++]; auto &ws=watches[wi(false_lit)]; size_t p=0;
      while(p<ws.size()){
        int cid=ws[p]; Clause &c=clauses[cid];
        int fw = (c.lits[c.w1]==false_lit)?c.w1:c.w2;
        int ow = (fw==c.w1)?c.w2:c.w1; int other=c.lits[ow];
        if(lit_true(other)){++p;continue;}
        int replacement=-1;
        for(int j=0;j<(int)c.lits.size();++j){ if(j==ow||j==fw) continue; if(!lit_false(c.lits[j])){replacement=j;break;} }
        if(replacement>=0){
          if(fw==c.w1)c.w1=replacement;else c.w2=replacement;
          int moved=c.lits[replacement]; ws[p]=ws.back();ws.pop_back();watches[wi(moved)].push_back(cid);continue;
        }
        if(lit_false(other)) return false;
        if(!enqueue(other)) return false;
        ++p;
      }
    }
    return true;
  }
  void reset(){ for(int lit:trail)val[abs(lit)]=0;trail.clear();qhead=0; }
  bool rup(const vector<int>& cand){
    if(has_empty)return true;
    reset();
    for(int u:units) if(!enqueue(u)){reset();return true;}
    for(int lit:cand) if(!enqueue(-lit)){reset();return true;}
    bool ok=!propagate(); reset(); return ok;
  }
};


vector<vector<int>> radius_formula(const vector<string>& rows,int r,int &nvars){
  const int n=43, npairs=903; vector<vector<int>> f;
  auto pid=[&](int a,int b){ return 1 + a*(2*n-a-1)/2 + (b-a-1); };
  for(int a=0;a<n-4;++a)for(int b=a+1;b<n-3;++b)for(int c=b+1;c<n-2;++c)for(int d=c+1;d<n-1;++d)for(int e=d+1;e<n;++e){
    int v[5]={a,b,c,d,e}; int ids[10],bits[10],q=0,ones=0;
    for(int i=0;i<5;++i)for(int j=i+1;j<5;++j){ids[q]=pid(v[i],v[j]);bits[q]=rows[v[i]][v[j]]=='1';ones+=bits[q];++q;}
    if(ones<=r){ vector<int> cl;cl.reserve(10);for(int t=0;t<10;++t)cl.push_back(bits[t]?-ids[t]:ids[t]);f.push_back(move(cl)); }
    if(10-ones<=r){ vector<int> cl;cl.reserve(10);for(int t=0;t<10;++t)cl.push_back(bits[t]?ids[t]:-ids[t]);f.push_back(move(cl)); }
  }
  if(r==0){for(int x=1;x<=npairs;++x)f.push_back({-x});nvars=npairs;return f;}
  auto S=[&](int i,int j){return npairs+(i-1)*r+j;}; // 1<=i<=902, 1<=j<=r
  for(int i=1;i<npairs;++i)f.push_back({-i,S(i,1)});
  for(int i=2;i<npairs;++i){
    f.push_back({-S(i-1,1),S(i,1)});
    for(int j=2;j<=r;++j){f.push_back({-i,-S(i-1,j-1),S(i,j)});f.push_back({-S(i-1,j),S(i,j)});}
  }
  for(int i=2;i<=npairs;++i)f.push_back({-i,-S(i-1,r)});
  nvars=S(npairs-1,r);return f;
}

vector<vector<int>> read_proof(const string& path){
  ifstream in(path);if(!in)throw runtime_error("cannot open proof "+path);vector<vector<int>> out;string line;
  while(getline(in,line)){if(line.empty())continue;istringstream ss(line);string first;ss>>first;if(!ss)continue;if(first=="d")continue;vector<int> c;int x=stoi(first);if(x)c.push_back(x);while(x&&ss>>x)if(x)c.push_back(x);out.push_back(move(c));}
  return out;
}
int main(int argc,char**argv){
 if(argc<4){cerr<<"usage: checker matrix proofdir max_radius [start_radius] [proof_start] [proof_end]\n";return 2;}
 ifstream in(argv[1]);vector<string> rows;string line;while(getline(in,line))if(!line.empty())rows.push_back(line);if(rows.size()!=43)throw runtime_error("matrix size");
 string dir=argv[2];int maxr=stoi(argv[3]);int startr=(argc>=5?stoi(argv[4]):1);
 size_t check_start=(argc>=6?stoull(argv[5]):0);size_t check_end=(argc>=7?stoull(argv[6]):SIZE_MAX);long long total=0;
 for(int r=startr;r<=maxr;++r){
   int nv;auto f=radius_formula(rows,r,nv);cerr<<"r="<<r<<" clauses="<<f.size()<<" vars="<<nv<<"\n";RupChecker ck(nv);for(auto &c:f)ck.add_clause(c);
   string p=dir+"/radius_"+to_string(r)+".drup";auto proof=read_proof(p);size_t stop=min(check_end,proof.size());
   for(size_t i=0;i<stop;++i){
     if(i>=check_start && !ck.rup(proof[i])){cerr<<"FAIL radius "<<r<<" step "<<i+1<<"\n";return 1;}
     ck.add_clause(proof[i]);
   }
   if(stop==proof.size() && !proof.empty() && !proof.back().empty()){cerr<<"FAIL radius "<<r<<" final clause not empty\n";return 1;}
   size_t checked=stop>check_start?stop-check_start:0;
   cout<<"VERIFIED radius="<<r<<" checked_steps="<<checked<<" range=["<<check_start<<","<<stop<<") total_additions="<<proof.size()<<"\n";total+=checked;
 }
 cout<<"VERIFIED_ALL checked_steps="<<total<<"\n";
}
