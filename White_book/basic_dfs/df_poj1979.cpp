/*There is a rectangular room, covered with square tiles. Each tile is colored either red or black. A man is standing on a black tile. From a tile, he can move to one of four adjacent tiles. But he can't move on red tiles, he can move only on black tiles.

Write a program to count the number of black tiles which he can reach by repeating the moves described above. 
*/
#include<iostream>
#include<cstdio>
#include<algorithm>
#define INF 10000000
#define MAX_N 1000
#define MAX_M 1000
using namespace std;
int W,H;
int res;
char gra[MAX_N][MAX_M];
bool vis[MAX_N][MAX_M];
void dfs(int posx, int posy){
  int x[4]={0,0,1,-1};
  int  y[4]={1,-1,0,0};
  for(int i=0; i<4; i++){
      int ni=posx+x[i];
      int nj=posy+y[i];
      if(ni>=0&&ni<H&&nj>=0&&nj<W&&vis[ni][nj]==false&&gra[ni][nj]=='.'){
    vis[ni][nj]=true;
    res++;
    dfs(ni, nj);
      }
    }
}




void solve(){
  //find the man
  int man_x, man_y;
  for(int i=0; i<H; i++)
    for(int j=0; j<W; j++)
      if(gra[i][j]=='@'){
	man_x=i;
	man_y=j;
      }
  dfs(man_x ,man_y);
}
int main(){
  while(true){
  cin>>W;
  cin>>H;
  if(W==0&&H==0) break;
  res=1;
  for(int i=0; i<H; i++)
    for(int j=0; j<W; j++){
      cin>>gra[i][j];
      vis[i][j]=false;
    }
  solve();
  cout<<res<<endl;
  }
}
