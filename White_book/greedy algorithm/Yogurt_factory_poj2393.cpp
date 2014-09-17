#include<iostream>
#include<cstdio>
#include<algorithm>
#include<string>
#include<queue> // for bfs
#define MAX_N 10020
#define INF 1000000
using namespace std;
int N, C[MAX_N], Y[MAX_N], S, tmpQ[MAX_N];
long long res=0;
int minValue;

int main(){
  cin>>N;
  cin>>S;
  minValue=INF;
  for(int i=0; i<N; i++){
    scanf("%d %d", &C[i], &Y[i]);
    if(minValue+S<C[i]) C[i]=minValue+S;
    minValue=C[i];
    res+=minValue*Y[i];
  }
  cout<<res<<endl;
  return 0;
}

/*
4 5
88 200
89 400
97 300
91 500
*/
