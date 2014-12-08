/* 1065 is to find the longest antichain, we sort it first and then pull out the chain one by one. It is easy to know that we can pick elements in each chain to get the longest antichain. The prove can be gotten through wiki Dilworth's theorem which use the inductive proof.*/

#include<iostream>
#include<cstdio>
#include<algorithm>
#include<string>
#include<queue> // for bfs
#define INF 10000000
#define MAX_N 5010
#define MAX_M 1000
using namespace std;
int n, ans, T;
struct stick{
  int len;
  int wid;
  int vis;
};
stick sticks[MAX_N];

bool cmp(stick a, stick b){
  if(a.len<b.len) return true;
  if(a.len==b.len) return a.wid<=b.wid;
  else return false;
}

void solve(){
  ans=0;
  int nowindex;
  int nextindex;
  sort(sticks, sticks+n, cmp);
  for(int i=0; i<n; i++){
    //      printf("%d %d %d\n",i,sticks[i].len, sticks[i].wid);
    if(sticks[i].vis==0){
      //      printf("%d %d %d\n",i,sticks[i].len, sticks[i].wid);
      ans++;
      nowindex=i;
      sticks[i].vis==1;
      for(nextindex=nowindex;nextindex<n; nextindex++){
	if(sticks[nextindex].wid>=sticks[nowindex].wid&&sticks[nextindex].vis==0){
	  sticks[nextindex].vis=1;
	  nowindex=nextindex;
	}
      }
    }
  }
}

int main(){
  scanf("%d", &T);
  while(T--){
  scanf("%d", &n);
  for(int i=0; i<n; i++){
    scanf("%d", &sticks[i].len);
    scanf("%d", &sticks[i].wid);
    sticks[i].vis=0;
  }
  solve();
  printf("%d\n", ans);
}
}
