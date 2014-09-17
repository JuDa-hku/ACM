#include<iostream>
#include<cstdio>
#include<algorithm>
#include<string>
#include<queue> // for bfs
#include<set>
#define INF 10000000
#define MAX_N 1000
#define MAX_M 1000
using namespace std;
set<string> res;
char map[5][5];
int dx[]={0,0,-1,1};
int dy[]={-1,1,0,0};
void dfs(int x, int y, int d, string s){
  int nx, ny;
  s+=map[x][y];
  if(d==5) {res.insert(s); return;}
  for(int i=0; i<4; i++){
    nx=x+dx[i]; ny=y+dy[i];
    if((nx>4||nx<0||ny>4||ny<0))
      continue;
    else{
      dfs(nx, ny, d+1, s);
    }
  }
}

int main(){
  for(int i=0; i<5; i++)
    for(int j=0; j<5; j++)
      cin>>map[i][j];
  for(int i=0; i<5; i++)
    for(int j=0; j<5; j++)
      dfs(i, j, 0, "");
  cout<<res.size()<<endl;
  set<string>::iterator iter;
  for(iter=res.begin();iter!=res.end();iter++)
    cout<<*iter<<endl;
}
