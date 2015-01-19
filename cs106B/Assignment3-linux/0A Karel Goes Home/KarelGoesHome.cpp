/*
 * File: KarelGoesHome.cpp
 * ----------------------
 * Name: [TODO: enter name here]
 * Section: [TODO: enter section leader here]
 * This file is the starter project for the Karel Goes Home
 * warmup problem for Assignment 3
 * [TODO: extend the documentation]
 */

#include <iostream>
#include <simpio.h>
//#include "console.h"
using namespace std;

/* Given a street number and avenue number, which are 1-indexed,
 * returns the number of paths Karel can take back home that only
 * moves left or down.
 */
int choice;
int numPathsHome(int street, int avenue);

int main() {
  int street = getInteger("Input the street number: ");
  int avenue = getInteger("Input the avenue number: ");
  int num = numPathsHome(street , avenue);
  cout<<num<<endl;
  return 0;
}


int numPathsHome(int street, int avenue){
  if(street==1&&avenue==1){
    cout<<"Home now. Haha!!"<<endl;
    return 0;
  }
  if(street==1&&avenue>1){
    return 1;
  }
  if(street>1&&avenue==1){
    return 1;
  }
  else{
    return numPathsHome(street-1, avenue)+numPathsHome(street, avenue-1);
  }
}
    
