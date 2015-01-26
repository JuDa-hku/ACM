/*
 * File: ConsecutiveHeads.cpp
 * --------------------------
 * Name: [TODO: enter name here]
 * Section: [TODO: enter section leader here]
 * This file is the starter project for the coin-flipping problem.
 * [TODO: rewrite the documentation]
 */

#include <iostream>
#include <string>
//#include "console.h"
#include "random.h"
using namespace std;

int main() {
   // [TODO: fill in the code]
  int Coin,sum ;
  sum = 0;
  int tag = 0;
  while(tag<3){
    Coin = randomInteger(0,1);
    if(Coin == 1){
      cout<<"Heads"<<endl;
      tag++;
      sum++;
    }
    else{
      cout<<"Tails"<<endl;
      tag = 0;
      sum++;
    }
  }
  cout<<"It took "<<sum<<" flips to get 3 consecutive heads"<<endl;
  return 0;
}
