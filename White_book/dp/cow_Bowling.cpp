#include<iostream>
#include<cstdio>
#include<algorithm>
#include<string>
#include<queue> // for bfs
#define INF 10000000
#define MAX_N 400
#define MAX_M 1000
using namespace std;
int data[MAX_N][MAX_N];
int res[MAX_N][MAX_N];
int N;
int ans=0;

void solve(){
  res[1][1]=data[1][1];
  for(int i=2; i<=N; i++)
    for(int j=1; j<=i; j++){
      int tmp=0, tmp1=0;
      if(j-1>0&&i-1>0)
	tmp=data[i][j]+res[i-1][j-1];
      if(i-1>0)
	tmp1=data[i][j]+res[i-1][j];
      res[i][j]=max(tmp, tmp1);
      ans=max(ans, res[i][j]);
    }
}
int main(){
  cin>>N;
  for(int i=1; i<=N; i++)
    for(int j=1; j<=i; j++)
      cin>>data[i][j];
  solve();
  cout<<ans<<endl;
}



/*
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
*/
