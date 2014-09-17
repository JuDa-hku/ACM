#include<iostream>
#include<cstdio>
#include<algorithm>
#include<string>
#include<queue> // for bfs
#define INF 10000000
#define MAX_N 50001
#define MAX_M 1000
using namespace std;
int N, S;
struct Stall{
  int begin;
  int end;
  int id;
  int stIndex;
  bool operator< (const Stall &a)const{
    return a.end<end;
  }
} cow[MAX_N];
priority_queue<Stall> pq;
int bar[MAX_N];


int solve(){
  Stall stall1;
  stall1.begin=stall1.end=0;
  stall1.stIndex=1;
  S=1;
  pq.push(stall1);
    for(int i=1; i<=N; i++){
      Stall s=pq.top();
      if(s.end<cow[i].begin){
	pq.pop();
	s.end=cow[i].end;
	pq.push(s);
	bar[cow[i].id]=s.stIndex;
      }
      else{
	Stall newstall;
	S++;
	newstall.begin=cow[i].begin;
	newstall.end=cow[i].end;
	newstall.stIndex=S;
	pq.push(newstall);
	bar[cow[i].id]=S;
      }
    }
  return S;
}

bool cmp(const Stall &a,const Stall &b){
  return a.begin<b.begin;
}


int main(){
  cin>>N;
  for(int i=1; i<=N; i++){
    cin>>cow[i].begin;
    cin>>cow[i].end;
    cow[i].id=i;
  }
  sort(cow+1, cow+N+1, cmp);
  cout<<solve()<<endl;
  for(int i=1; i<=N; i++)
    cout<<bar[i]<<endl;
}
