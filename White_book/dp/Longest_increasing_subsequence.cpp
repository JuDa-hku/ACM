/* find the longest increasing subsequence, for example {1, 5, 2, 3, 4, 7, 0}, the longest increasing subsequence is 1,2,3,4,7.*/

#include<iostream>
#include<cstdio>
#include<algorithm>
#define INF 10000000
#define MAX_N 1000
#define MAX_M 1000
using namespace std;
int a[6]={1,5,2,3,4,1}, n=6;
int dp[MAX_N];
int result=1;
void solve(){
  for(int i=0; i<n; i++){
    dp[i]=1;
    int res=1;
    for(int j=i-1; j>=0; j--){
      if(a[j]<a[i]){
	res=max(dp[j]+1, res);
      }
    }
    dp[i]=res;
    result=max(res, result);
  }
  cout<<result<<endl;
  int tmp=INF;
  for(int i=n-1; i>=0; i--){
    if(dp[i]==result&&dp[i]<=tmp){
      cout<<a[i];
      tmp=a[i];
      result--;
    }
  }
}
int main(){
  solve();
}
