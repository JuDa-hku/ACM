/* the lcs problem is a classic problem, for example the lcs of abcd and becd is bcd. We need to find the longest equal subsequences of the given sequences.*/
#include<iostream>
#include<cstdio>
#include<algorithm>
#define INF 10000000
#define MAX_N 1000
#define MAX_M 1000
char S[MAX_N], T[MAX_N];
int dp[MAX_N][MAX_N], n, m;
using namespace std;
void solve(){
  for(int i=0; i<n; i++)
    for(int j=0; j<m; j++){
      if(S[i]==T[j]){
	dp[i+1][j+1]=dp[i][j]+1;
      }
      else{
	dp[i+1][j+1]=max(dp[i][j+1], dp[i+1][j]);
      }
    }
  cout<<dp[n][m]<<endl;
  int index=dp[n][m];
  char lcs[index+1];
  lcs[index]='\0';
  int i=n, j=m;
  while(i>0&&j>0){
    if(S[i-1]==T[j-1]){
      index--;
      lcs[index]=S[i-1];
      cout<<S[i-1]<<endl;
      i--;
      j--;
    }
    else{
      if(dp[i][j]==dp[i][j-1]){
	j--;
      }
      if(dp[i][j]==dp[i-1][j]){
	i--;
      }
    }
}
  cout<<lcs<<endl;
}


int main(){
  cin>>m>>n;
  for(int i=0; i<n; i++)
    cin>>S[i];
  for(int i=0; i<m; i++)
    cin>>T[i];
  solve();
}
