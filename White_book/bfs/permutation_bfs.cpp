#include<iostream>
#include<algorithm>
#include<cstdio>
#define INF 10000000
#define MAX_N 1000
using namespace std;
bool used[MAX_N];
int perm[MAX_N];
//to get n! permutation
void permutation1(int pos, int n){

  if(pos==n){
    for (int i = 0; i<n; i++)
      cout<<perm[i];
    cout<<endl;
 }


  for(int i = 0; i < n; i++){
    if(!used[i]){
      perm[pos]=i;
      used[i]=true;
      permutation1(pos+1, n);
      used[i]=false;
    }
  }

}

void solve(){
}
int main(){
  int n=3;
  permutation1(0, 3);
}
