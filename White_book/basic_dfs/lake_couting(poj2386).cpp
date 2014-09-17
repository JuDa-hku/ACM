//N*M yard, connected lakes are regarded as one lake, count the total number of lakes in the yard.
#include<iostream>
#define MAX_N 100
#define MAX_M 100
using namespace std;
int N, M;
char field[MAX_N][MAX_M+1];
void dfs(int x, int y){
  //replace the given place as .
  field[x][y]='.';
  for(int dx=-1; dx<=1; dx++)
    for(int dy=-1; dy<=1; dy++){
      int nx=dx+x;
      int ny=dy+y;
      if(nx<N&&ny<M&&nx>=0&&ny>=0&&field[nx][ny]=='W')
	dfs(nx, ny);
    }
}

void solve(){
  int res=0;
  for(int i=0; i<N; i++)
    for(int j=0; j<M; j++){
      if(field[i][j]=='W'){
	dfs(i, j);
	res++;
      }
    }
  cout<<"the result is "<<res<<endl;
}
int main(){
  cout<<"input N and M:";
  cin>>M>>N;
  cout<<"Input the yard with W and .:";
    for(int i=0; i<N; i++)
      for(int j=0; j<M; j++){
	cin>>field[i][j];
      }
    solve();
}
