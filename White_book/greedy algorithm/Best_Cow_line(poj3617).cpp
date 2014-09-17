#include<iostream>
#include<cstdio>
#include<algorithm>
#include<string>
#define INF 10000000
#define MAX_N 1000
using namespace std;
string S;
string T;
void solve(){
  while(S.size()!=0)
    if(S[0]>=S[S.size()-1]){
      T=T+S[S.size()-1];
      S=S.substr(0, S.size()-1);
    }
    else{
      T=T+S[0];
      S=S.substr(1);
    }
  cout<<T<<endl;
}
int main(){
  cin>>S;
  T=' ';
  solve();
}
