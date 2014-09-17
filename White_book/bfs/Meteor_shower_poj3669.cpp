#include<iostream>
#include<cstdio>
#include<queue>
#include<algorithm>
#include<cstring>
#define INF 10000000
#define MAX_N 350
#define MAX_M 350
#define bug puts("here")
using namespace std;
int dx[]={0,0,0,-1,1};
int dy[]={0,1,-1,0,0};
int desTime[MAX_N][MAX_N];
int M;
struct metor{
  int x,y,t;
};
queue<metor> que;
int bfs(){
  int k;
  metor tmp, now, nx;
  if(desTime[0][0]==0) return -1;
  else if(desTime[0][0]==-1) { return 0;}
  tmp.x=tmp.y=tmp.t=0;
  que.push(tmp);
  while(!que.empty()){
    now=que.front();
    que.pop();
    for(k=1;k<5;k++){
      nx.x=now.x+dx[k];
      nx.y=now.y+dy[k];
      nx.t=now.t+1;
      if(nx.x<0||nx.y<0) continue;
      if(desTime[nx.x][nx.y]==-1){return nx.t;}
      if(nx.t>=desTime[nx.x][nx.y]) continue;
      desTime[nx.x][nx.y]=0; // when the point will be destoried in the near future, to gurantee that people do not stay there for a long time, the point can be regared as being destoried at time 0.
      que.push(nx);
    }
  }
  return -1;
}




int main(){
  int x,y,t, xx,yy;
  cin>>M;
  memset(desTime,-1,sizeof(desTime)); 
  for (int i = 0; i < M; ++i)
    {
      cin>>x;
      cin>>y;
      cin>>t;
      for(int k=0; k<5; k++){
	xx=x+dx[k];
	yy=y+dy[k];
	if(xx<0||yy<0) continue;
	if(desTime[xx][yy]==-1){
	  desTime[xx][yy]=t;
	}
	else{
	  desTime[xx][yy]=min(desTime[xx][yy], t);
	}
      }
    }
  int ans=bfs();
  cout<<ans<<endl;
}
