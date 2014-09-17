#include<iostream>
#include<cstdio>
#include<algorithm>
#include<string>
#include<cmath>
#include<queue> // for bfs
#define INF 10000000
#define MAX_N 1000
#define MAX_M 1000
#define eps 0.00001
using namespace std;
int n, d;
pair<float, float> interv[MAX_N];

int solve(){
  int ans=1;
  float thisleft=interv[0].first;
  float thisright=interv[0].second;
  for(int i=0; i<n; i++){
    float nextright=interv[i].second;
    float nextleft=interv[i].first;
    if(nextleft-thisright>eps){
      ans++;
      thisright=nextright;
      thisleft=nextleft;
      continue;
    }
    if(thisright-nextleft>eps&&thisright-nextright>eps){
      thisleft=nextleft;
      thisright=nextright;
      continue;
    }
    if(thisright-nextleft>eps&&nextright-thisright>eps){
      thisleft=nextleft;
      continue;
    }
  }
  return ans;
}
int main(){
  int flag=1;
  bool tag;
  while(true){
    cin>>n;
    cin>>d;
    if(n==0&&d==0) break;
    int x,y;
    for(int i=0; i<n; i++){
      cin>>x;
      cin>>y;
      if(d<y)  tag=true;
      else{
      interv[i].first=x-sqrt(float(d*d-y*y));
      interv[i].second=x+sqrt(float(d*d-y*y));
      }
    }
    if(tag){
      cout<<"Case "<<flag<<": "<<-1<<endl;
      tag=false;
      flag++;}
    else{
      sort(interv, interv+n);
      cout<<"Case "<<flag<<": "<<solve()<<endl;
      flag++;
  }
}
}


/*
3 2
1 2
-3 1
2 1

1 2
0 2

2 2
0 4
1 1

2 2
0 2
0 1

0 0
*/
