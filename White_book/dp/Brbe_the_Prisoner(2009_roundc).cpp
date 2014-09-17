#include<iostream>
#include<cstdio>
#include<algorithm>
#define INF 10000000
#define MAX_Q 1000
#define MAX_M 1000
using namespace std;
int P,Q, A[MAX_Q+2];
int dp[MAX_Q+1][MAX_Q+2];

void solve(){
  A[0]=0;
  A[Q+1]=P+1;
  for (int i = 0; i <=Q ; ++i)
      dp[i][i+1]=0;
  for(int w=2; w<=Q+1; w++){
    for(int i=0; i+w<=Q+1; i++){
      int j=i+w, t=INF;
      for(int k=i+1; k<j; k++)
	t=min(t, dp[i][k]+dp[k][j]);
      dp[i][j]=t+A[j]-A[i]-2;
    }
}
  cout<<dp[0][Q+1]<<endl;
}

int main(){
}
