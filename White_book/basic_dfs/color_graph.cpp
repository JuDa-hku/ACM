#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#define INF 10000000
#define MAX_N 1000
#define MAX_M 1000
using namespace std;
vector<int> G[MAX_N];
int V=3;
int color[MAX_N];
bool visit[MAX_N];




bool dfs(int v, int c){
  color[v]=c;
  for(int i=0; i<G[v].size(); i++){
    if(color[G[v][i]]==c) return false;
    if(color[G[v][i]]==0&&!dfs(G[v][i], -c)) return false;
  }
  return true;
}

void solve(){
  for(int i=0; i<V; i++){
    if(color[i]==0){
      if(!dfs(i,1)){
	  cout<<"NO"<<endl;
	  return;
	}
	}
}
  cout<<"Yes"<<endl;
}
int main(){
  G[0].push_back(1);
  G[0].push_back(2);
  G[1].push_back(0);
  G[1].push_back(2);
  G[2].push_back(0);
  G[2].push_back(1);
  // G[3].push_back(0);
  // G[3].push_back(2);
  solve();
}
