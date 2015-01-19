/*
 * File: Combinations.cpp
 * ----------------------
 * Name: [TODO: enter name here]
 * Section: [TODO: enter section leader here]
 * This file is the starter project for the recursive combinations problem.
 * [TODO: rewrite the documentation]
 */

#include <iostream>
//#include "console.h"
#include "simpio.h"
using namespace std;
int TIME = 0;
int array[100][100];
int combinations(int n,int k);

int main() {
  int n = getInteger("Input the number n:");
  int k = getInteger("Input the number k:");
  int result = combinations(n,k);
  cout<<result<<"Total time: "<<TIME<<endl;
  return 0;
}

int combinations(int n, int k){
  if(n<k){TIME++; return 0;}
  if(n==0||n==1||k==0) {
    TIME++; 
    return 1;}
  else {
    TIME++;
    if(array[n][k]!=0) return array[n][k];
    array[n-1][k-1]=combinations(n-1,k-1);
    array[n-1][k]=combinations(n-1,k);
    return array[n-1][k-1]+array[n-1][k];
  }
}
