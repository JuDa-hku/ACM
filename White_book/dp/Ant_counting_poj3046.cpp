#include<iostream>
#include<cstdio>
#include<algorithm>
#include<string>
#include<queue> // for bfs
#define INF 10000000
#define MAX_N 1001
#define MAX_M 100001
#define M 1000000

using namespace std;
int N[MAX_N], T, A, S, B, dp[MAX_N][MAX_M], ans;
void solve(){
for(int i=0; i<=T; i++)
  dp[i][0]=1;
for(int i=0; i<T; i++)
  for(int j=1; j<=B; j++){
if(j-1-N[i]>=0){
dp[i+1][j]=(dp[i+1][j-1]+dp[i][j]-dp[i][j-1-N[i]]+M)%M;
}
 else{
dp[i+1][j]=(dp[i+1][j-1]+dp[i][j])%M;
}
}
for(int i=S; i<=B; i++)
  ans+=dp[T][i];
cout<<ans%M<<endl;
}


int main(){
cin>>T>>A>>S>>B;
for(int i=0; i<A; i++){
int tmp;
scanf("%d", &tmp);
N[tmp-1]++;
}
solve();
}

/*
7 63 2 48
1 1 1 1 1 1 1 1 1 
2 2 2 2 2 2 2 2 2
3 3 3 3 3 3 3 3 3
4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5
6 6 6 6 6 6 6 6 6
7 7 7 7 7 7 7 7 7
*/
