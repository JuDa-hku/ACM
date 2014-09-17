#include<iostream>
#include<cstdio>
#include<algorithm>
#define INF 10000000
#define MAX_N 1000
#define MAX_M 1000
using namespace std;
int w, h;
int gra[MAX_N][MAX_N];
int best ;
int dx[4]={1,-1,0,0};
int dy[4]={0,0,1,-1};
void dfs(int posx, int posy, int step){
  int nposx, nposy;
   if(step>best) 
      return;
  for(int i=0; i<4; i++){
    nposx=posx+dx[i];
    nposy=posy+dy[i];
    if(nposx>=h||nposx<0||nposy>=w||nposy<0||gra[nposx][nposy]==1)
      continue;
    while(nposx<h&&nposx>=0&&nposy<w&&nposy>=0&&gra[nposx][nposy]!=1){
      if(gra[nposx][nposy]==3){
	if (step+1<best)
	      best=step+1;
	break;
      }
      nposx=nposx+dx[i];
      nposy=nposy+dy[i];
    }
    if(gra[nposx][nposy]==3)
      continue;
    if(nposx<h&&nposx>=0&&nposy<w&&nposy>=0){
      gra[nposx][nposy]=0;
      dfs(nposx-dx[i], nposy-dy[i], step+1);
      gra[nposx][nposy]=1;
    }
  }
}


void solve(){
}
int main(){
  while(true){
    best=12;
    cin>>w;
    cin>>h;
    if(w==0&&h==0)
      break;
    for (int i = 0; i < h; i++)
      for(int j=0; j<w; j++)
	cin>>gra[i][j];
// find start position
    int posX, posY;
    for(int i=0; i<h; i++)
      for(int j=0; j<w; j++)
	if(gra[i][j]==2){
	  posX=i;
	  posY=j;
	}
    dfs(posX, posY, 0);
    if(best>10) cout<<-1<<endl;
    else    cout<<best<<endl;
  }
}
