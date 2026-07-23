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

vector<vector<int>> base_extension_clauses(const string& line){
  vector<int> vals;for(unsigned char ch:line)if(ch!='\r'&&ch!='\n')vals.push_back((int)ch-63);
  if(vals.empty()||vals[0]!=42)throw runtime_error("expected graph6 order 42");
  bool a[42][42]{};int bitpos=0;
  for(int j=1;j<42;++j)for(int i=0;i<j;++i){int v=vals[1+bitpos/6];int bit=(v>>(5-bitpos%6))&1;bitpos++;a[i][j]=a[j][i]=bit;}
  vector<vector<int>> ind,cli;
  for(int i=0;i<39;++i)for(int j=i+1;j<40;++j)for(int k=j+1;k<41;++k)for(int l=k+1;l<42;++l){
    int e=a[i][j]+a[i][k]+a[i][l]+a[j][k]+a[j][l]+a[k][l];
    if(e==0)ind.push_back({i+1,j+1,k+1,l+1});
    else if(e==6)cli.push_back({-(i+1),-(j+1),-(k+1),-(l+1)});
  }
  ind.insert(ind.end(),cli.begin(),cli.end());return ind;
}

vector<vector<int>> twobad_formula(const string& g6,int &nvars){
  auto base=base_extension_clauses(g6);int m=base.size();vector<vector<int>> f;f.reserve(6*m);
  for(int i=0;i<m;++i){auto c=base[i];c.push_back(43+i);f.push_back(move(c));}
  const int k=2, top=42+m;auto S=[&](int i,int j){return top+(i-1)*k+j;};
  for(int i=1;i<m;++i)f.push_back({-(42+i),S(i,1)});
  for(int i=2;i<m;++i){
    f.push_back({-S(i-1,1),S(i,1)});
    f.push_back({-(42+i),-S(i-1,1),S(i,2)});
    f.push_back({-S(i-1,2),S(i,2)});
  }
  for(int i=2;i<=m;++i)f.push_back({-(42+i),-S(i-1,2)});
  nvars=S(m-1,2);return f;
}

vector<vector<int>> read_proof(const string& path){
  ifstream in(path);if(!in)throw runtime_error("cannot open proof "+path);vector<vector<int>> out;string line;
  while(getline(in,line)){if(line.empty())continue;istringstream ss(line);string first;ss>>first;if(!ss)continue;if(first=="d")continue;vector<int> c;int x=stoi(first);if(x)c.push_back(x);while(x&&ss>>x)if(x)c.push_back(x);out.push_back(move(c));}
  return out;
}

int main(int argc,char**argv){
  if(argc<5){cerr<<"usage: checker graph6 proofdir start end\n";return 2;}
  string gpath=argv[1],pdir=argv[2];int start=stoi(argv[3]),end=stoi(argv[4]);
  ifstream gin(gpath);vector<string> lines;string line;while(getline(gin,line))if(!line.empty())lines.push_back(line);
  long long steps=0;int checked=0;
  for(int idx=start;idx<end;++idx){
    if(idx==41||idx==255)continue;
    int nv;auto f=twobad_formula(lines.at(idx),nv);RupChecker ck(nv);for(auto &c:f)ck.add_clause(c);
    char name[128];snprintf(name,sizeof(name),"%s/twobad_%03d.drup",pdir.c_str(),idx);auto proof=read_proof(name);bool empty=false;
    for(size_t s=0;s<proof.size();++s){if(!ck.rup(proof[s])){cerr<<"FAIL graph "<<idx<<" proof step "<<s+1<<"\n";return 1;}if(proof[s].empty())empty=true;ck.add_clause(proof[s]);}
    if(!empty){cerr<<"FAIL graph "<<idx<<" no empty clause\n";return 1;}steps+=proof.size();checked++;if(idx%25==0)cerr<<idx<<" ok\n";
  }
  cout<<"VERIFIED graphs="<<checked<<" proof_steps="<<steps<<"\n";return 0;
}
