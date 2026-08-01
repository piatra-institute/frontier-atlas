#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <set>
#include <string>
#include <vector>
static int ipow3(int n){int r=1;while(n--)r*=3;return r;}
static int encode(const std::vector<int>&p){int e=0,w=1;for(int x:p){e+=x*w;w*=3;}return e;}
static std::vector<int> decode(int e,int n){std::vector<int>p(n);for(int i=0;i<n;i++){p[i]=e%3;e/=3;}return p;}
int main(int argc,char**argv){
 if(argc<2||argc>3){std::cerr<<"usage: verify_lines points.txt [expected_size]\n";return 2;}
 std::ifstream in(argv[1]);if(!in){std::cerr<<"cannot open input\n";return 2;}
 std::string s;int n=-1;std::set<int>seen;
 while(std::getline(in,s)){if(s.empty())continue;if(n<0)n=(int)s.size();if((int)s.size()!=n){std::cerr<<"inconsistent dimension\n";return 1;}
  std::vector<int>p(n);for(int i=0;i<n;i++){if(s[i]<'0'||s[i]>'2'){std::cerr<<"bad coordinate\n";return 1;}p[i]=s[i]-'0';}
  if(!seen.insert(encode(p)).second){std::cerr<<"duplicate\n";return 1;}}
 if(n<=0){std::cerr<<"empty\n";return 1;}if(argc==3&&seen.size()!=(size_t)std::stoul(argv[2])){std::cerr<<"wrong size\n";return 1;}
 int N=ipow3(n);std::vector<unsigned char>member(N,0);for(int x:seen)member[x]=1;
 std::set<std::vector<int>>lines;
 for(int a=0;a<N;a++){auto pa=decode(a,n);for(int d=1;d<N;d++){auto pd=decode(d,n);std::vector<int>p1(n),p2(n);for(int j=0;j<n;j++){p1[j]=(pa[j]+pd[j])%3;p2[j]=(pa[j]+2*pd[j])%3;}
  std::vector<int>L{a,encode(p1),encode(p2)};std::sort(L.begin(),L.end());lines.insert(L);}}
 std::uint64_t expected=(std::uint64_t)N*(N-1)/6;if(lines.size()!=expected){std::cerr<<"wrong line count "<<lines.size()<<" expected "<<expected<<"\n";return 1;}
 for(auto&L:lines)if(member[L[0]]+member[L[1]]+member[L[2]]>2){std::cerr<<"FAIL full line "<<L[0]<<" "<<L[1]<<" "<<L[2]<<"\n";return 1;}
 std::cout<<"PASS line-enumeration: n="<<n<<" size="<<seen.size()<<" lines="<<lines.size()<<"\n";
}
