#include<iostream>
#include<algorithm>
#include<cstdio>
#define MAX_N 100
using namespace std;
int N, R;
int X[MAX_N];
void solve(){
  sort(X, X+N);

  int i = 0, ans = 0;
  while(i < N){
    int s = X[i++];
    while(i<N && X[i]<=s+R) i++;
    int p = X[i-1];
    while(i<N&&X[i]<=p+R) i++;
    ans++;
      }
  printf("%d\n", ans);
}
int main(){
  printf("input N: ");
  cin>>N;
  printf("input R: ");
  cin>>R;
  for(int i=0; i<N; i++)
    cin>>X[i];
  solve();
    }
      
  
