#include<iostream>
#include<cstdio>
#include<algorithm>
#include<string>
#include<queue> // for bfs
#define INF 10000000
#define MAX_N 25002
#define MAX_M 1000
using namespace std;
int N, T;
pair<int, int> itv[MAX_N];
int solve(){
  int nend, ans=0, end;
  if(itv[0].first!=1) return -1;
  nend=0;end=0;
  for(int i=0; i<N; i++){
    // judge the connection
    if(itv[i].first>end+1)
      return -1;
    // for the coming cow
    for(int j=i; j<N; j++){
      if(j==N-1&&end==T)
	return ans+1;
      if(itv[j].first<=end+1&&itv[j].second>nend){
	nend=itv[j].second;
	i=j;
      }
    }
    end=nend;
    //    cout<<nend<<endl;
    ans++;
    if(end==T) return ans;
  }
  return -1;
}

int main(){
  cin>>N;
  cin>>T;
  for (int i = 0; i < N; ++i)
    {
      scanf("%d %d", &itv[i].first, &itv[i].second);
    }
  sort(itv, itv+N);
  cout<<solve()<<endl;
}

/*
  4 10
  1 3
  2 5
  3 7
  4 10
*/

/*
  5 20
  1 3
  2 7
  4 5
  3 8
  7 20
*/
/*
4 10
1 4
6 8
8 9
9 10
*/
/*
6 10
1 6 
1 5
2 7
3 8
4 9
8 10
*/

// at first I use
// if(itv[N-1].second!=T) return -1 
// this spend me a lot of time to debug
