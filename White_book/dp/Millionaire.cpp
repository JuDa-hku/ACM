/*
You have been invited to the popular TV show "Would you like to be a millionaire?". Of course you would!
The rules of the show are simple:

    Before the game starts, the host spins a wheel of fortune to determine P, the probability of winning each bet.
    You start out with some money: X dollars.
    There are M rounds of betting. In each round, you can bet any part of your current money, including none of it or all of it. The amount is not limited to whole dollars or whole cents.

    If you win the bet, your total amount of money increases by the amount you bet. Otherwise, your amount of money decreases by the amount you bet.
    After all the rounds of betting are done, you get to keep your winnings (this time the amount is rounded down to whole dollars) only if you have accumulated $1000000 or more. Otherwise you get nothing.

Given M, P and X, determine your probability of winning at least $1000000 if you play optimally (i.e. you play so that you maximize your chances of becoming a millionaire).
*/

#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#define INF 10000000
#define MAX_N 1000
#define MAX_M 15
using namespace std;
int M, X;
double P;
double dp[2][(1<<MAX_M)-1];

void solve(){
  int n=1<<M;
  double *prv=dp[0], *nxt=dp[1];
  memset(prv, 0, sizeof(double)*(n+1));
  prv[n]=1.0;

  for(int r=0; r<=M; r++){
    for(int i=0; i<=n; i++){
      double t=0.0;
      int jub=min(i, n-i);
      for(int j=0; j<=jub; j++)
	t=max(t, P*prv[i+j]+(1-P)*prv[i-j]);
      nxt[i]=t;
    }
    swap(prv, nxt);
}

  int i=X*n/1000000;
  cout<<prv[i]<<endl;
}

int main(){
  M=3;
  P=0.75;
  X=600000;
  solve();
}
