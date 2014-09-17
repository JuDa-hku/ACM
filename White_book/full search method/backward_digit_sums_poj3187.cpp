#include<iostream>
#include<cstdio>
#include<algorithm>
#include<string>
#include<queue> // for bfs
#define INF 10000000
#define MAX_N 1000
#define MAX_M 1000
using namespace std;
int result[MAX_N], C[MAX_N];
int final[MAX_N];
bool used[MAX_N];
int N, sum;
bool tag;
bool check(int* res, int n, int sum);
void solve(int n){
  if(tag)
    return;
  if(n==N){
    //check the permutation
    if(check(result, N, sum)){
      for(int i=0; i<N; i++)
	cout<<result[i]<<' ';
      cout<<endl;
      tag=true;
     }
     return;
  }
  for(int i=1; i<=N; i++){
    if(!used[i]){
      result[n]=i;
      used[i]=true;
      solve(n+1);
      used[i]=false;
    }
  }
}

int index(int i, int n){
  int a=1, ans=1;
  while(a<=i){
    ans=ans*n/a;
    a++; n--;
  }
  return ans;
}

bool check(int* res, int n, int sum){
  int summation=0;
  for(int i=0; i<n; i++)
    summation+=res[i]*C[i];
  return (summation==sum);
}

int main(){
  cin>>N;
  cin>>sum;
  for(int i=0; i<N; i++)
    C[i]=index(i, N-1);
  solve(0);
}
