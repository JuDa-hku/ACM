#include<iostream>
#include<cstdio>
#include<algorithm>
#include<queue>
#define INF 10000000
#define MAX_N 1000
#define MAX_M 1000
int N=4, L=25, A[4]={10,14,20,21}, B[4]={10,5,2,4}, P=10;
int res=0;
using namespace std;

bool solve(){
  priority_queue<int> pque;
  while(true){
    L=L-P;
    if(L<=0){
      cout<<res<<endl;
      return true;
    }
    for(int i=0; i<N; i++){
      if(A[i]>0){
      A[i]-=P;
      if(A[i]<=0)
	pque.push(B[i]);
      }
    }
    if(!pque.empty()) {
      P=pque.top();
      res++;
    }
    if(pque.empty()) return false;
    pque.pop();
}
}
int main(){
  if(solve())
    cout<<"True";
}
