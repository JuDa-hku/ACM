#include<iostream>
#include<cstdio>
#include<algorithm>
#define INF 10000000
#define MAX_N 1000
#define MAX_M 1000
int w[MAX_N], v[MAX_N], dp[MAX_N][MAX_N];
int N, W, res;
int times=0;
using namespace std;
int solve(int W,int num){
   if(dp[W][num]!=0){
     times++;
     return dp[W][num];
   }
  if(num>=N||W<0||w[num]>W){
    times++;
    return 0;
  }
  if(w[num]<=W){
    int with_num=solve(W-w[num], num+1)+v[num];
    int without_num=solve(W, num+1);
    dp[W][num]=max(with_num, without_num);
    times++;
    return dp[W][num];
  }
}
int main(){
  N=5;
  w[0]=2;
  v[0]=3;
  w[1]=1;
  v[1]=2;
  w[2]=3;
  v[2]=4;
  w[3]=2;
  v[3]=2;
  w[4]=3;
  v[4]=3;
  W=5;
  res=solve(W, 0);
  cout<<res<<endl;
  cout<<times<<endl;
}
