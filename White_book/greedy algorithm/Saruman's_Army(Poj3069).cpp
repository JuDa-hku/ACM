#include<iostream>
#include<cstdio>
#include<algorithm>
#define INF 10000000
#define MAX_N 1000
int N;
int R;
int X[MAX_N];
using namespace std;
void solve(){
  sort(X, X+N);
  int i=0, ans=0;
  while(i<N){
    int s=X[i++];
    while(i<N&&X[i]<=s+R)
      i++;
    int p=X[i-1];
    while(i<N&&X[i]<=p+R)
      i++;
    ans++;
}
  cout<<ans<<endl;
}
int main(){
  cin>>N;
  cin>>R;
for (int i = 0; i < N; ++i)
  {
    cin>>X[i];
  }
 solve();
}
