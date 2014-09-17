#include<iostream>
#include<cstdio>
#include<algorithm>
#include<string>
#include<cstring>
#include<queue> // for bfs
#define MAX_N 100
#define MAX_M 100020
using namespace std;
int A[MAX_N], C[MAX_N],dp[MAX_M], n, m;

void solve(){
  memset(dp, -1, sizeof(dp));
  dp[0]=0;
  for(int i=0; i<n; i++)
    for(int j=0; j<=m; j++){
      if(dp[j]>=0)
	dp[j]=C[i];
      else if(j<A[i]||dp[j-A[i]]<=0)
	dp[j]=-1;
      else
	dp[j]=dp[j-A[i]]-1;
    }
}

int main(){
  while(true){
  cin>>n;
  cin>>m;
  if(n==0&&m==0)
    break;
  for(int i=0; i<n; i++)
    scanf("%d", &A[i]);
  for(int i=0; i<n; i++)
    scanf("%d", &C[i]);
  solve();
  int res=0;
  for(int j=1; j<=m; j++)
    if(dp[j]>=0)
      res++;
  cout<<res<<endl;
  }
}

/*
3 10
1 2 4 2 1 1
2 5
1 4 2 1
0 0
*/
