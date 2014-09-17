#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<string>
#include<queue> // for bfs
#define INF 100000
#define MAX_N 10001
#define MAX_M 1000
using namespace std;
int N,K;
double L[MAX_N];
bool C(double x){
  int sum=0;
  for(int i=0; i<N; i++)
    sum+=(int)(L[i]/x);
  return sum>=K;
}

double solve(){
  double l=0.0, r=INF;
  for(int i=0; i<100;i++){
    double middle=(l+r)/2.0;
    if(C(middle))
      l=middle;
    else
      r=middle;
  }
  return r;
}


int main(){
  cin>>N;
  cin>>K;
  for (int i = 0; i < N; ++i)
    {
      scanf("%lf",&L[i]);
    }
  double res=solve();
  printf("%.2f\n", floor(res*100)/100);
}


/*
4 2540
8.02
7.43
4.57
5.39


4 2542
8.02
7.43
4.57
5.39
*/
