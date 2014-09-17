#include<iostream>
#include<cstdio>
#include<queue>
#define MAX_N 100
#define MAX_M 100
using namespace std;
const int INF = 1000000;
typedef pair<int, int> P;

//input
char maze[MAX_N][MAX_M+1];
int N, M;
int sx, sy; //start point
int gx, gy; //end point
int d[MAX_N][MAX_M+1];
int dx[4]={1, 0 , -1, 0};
int dy[4]={0, 1 , 0, -1};

int bfs(){
  queue<P> que;
  for(int i=0; i<N; i++)
    for(int j=0; j<M; j++) d[i][j]=INF;
  que.push(P(sx, sy));
  d[sx][sy]=0;
  while(que.size()){
    P p=que.front(); que.pop();
    if(p.first==gx && p.second==gy) break;
    for(int i=0; i<4; i++){
      int nx=p.first+dx[i], ny=p.second+dy[i];
      if(0<=nx&&nx<N&&0<=ny&&ny<M&&maze[nx][ny]!='#'&&d[nx][ny]==INF){
	que.push(P(nx, ny));
	d[nx][ny]=d[p.first][p.second]+1;
      }
    }
  }
  return d[gx][gy];
}

void solve(){
  int res=bfs();
  printf("%d\n", res);
}

int main(){
  cout<<"N and M"<<endl;
  cin>>N;
  cin>>M;
  cout<<"The maze"<<endl;
  for (int i = 0; i < N; ++i)
    for(int j = 0; j<M; ++j)
      cin>>maze[i][j];
  cout<<"start point"<<endl;
  cin>>sy>>sx;
  cout<<"end point"<<endl;
  cin>>gy>>gx;
  for (int i = 0; i < N; ++i){
    for(int j = 0; j<M; ++j){
      cout<<maze[i][j];
    }
  cout<<endl;
  }
  cout<<sy<<sx<<endl;
  cout<<gy<<gx<<endl;
  solve();
}
