#include<iostream>
#include<cstdio>
#include<algorithm>
#define INF 10000000
#define MAX_N 1000
#define MAX_M 1000
using namespace std;
int d;
int x=10,y=10;
void extgcd(int a, int b, int& x, int& y){
  if(b!=0){
    extgcd(b, a%b, y, x);
    y-=(a/b)*x;
  }
  else{
    x=1;
    y=0;
  }
}

int main(){
  extgcd(10,7,x,y);
  cout<<x<<' '<<y<<endl;
}
