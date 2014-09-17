//we have n work to do. Work i start at s_i and end at t_i. For each work, you can choose to take it or not take it. How can you choose to maximaze the number of work you take.
#include<iostream>
#include<cstdio>
#include<algorithm>
#define INF 10000000
#define MAX_N 1000
using namespace std;
int N;
int S[MAX_N];
int T[MAX_N];
pair<int, int> itv[MAX_N];
// sort the pair according to the first int and then second int
void solve(){
  for(int i=0; i<N; i++){
    itv[i].first=T[i];
    itv[i].second=S[i];
}
  sort(itv, itv+N);
  int ans=0, t=0;
  for(int i=0; i<N; i++){
    if(t<=itv[i].second) {
      ans++;
      t=itv[i].first;
      cout<<itv[i].first<<endl;
    }
  }
  printf("%d\n", ans);
}
int main(){
  cin>>N;
  for(int i=0; i<N; i++)
    cin>>S[i]>>T[i];
  solve();
}
