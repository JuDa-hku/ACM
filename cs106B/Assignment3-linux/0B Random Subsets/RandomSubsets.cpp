/*
 * File: RandomSubsets.cpp
 * ----------------------
 * Name: [TODO: enter name here]
 * Section: [TODO: enter section leader here]
 * This file is the starter project for the Random Subsets problem
 * on Assignment #3.
 * [TODO: extend the documentation]
 */

#include <iostream>
#include "set.h"
#include "random.h"
//#include "console.h"
using namespace std;

/* Given a set of integers, returns a uniformly-random subset of that
 * set.
 */
Set<int> randomSubsetOf(Set<int>& s);
Set<int> initSet();

int main() {
  Set<int> s=initSet();
  Set<int> resultSet = randomSubsetOf(s);
  foreach(int element in resultSet)
    cout<<element<<endl;
  return 0;
}

Set<int> initSet(){
  Set<int> s;
  cout<<"Input intger to form the set and end with number 123456789";
  int i=0;
  while(i!=123456789){
    cin>>i;
    s.add(i);
  }
  return s;
}

Set<int> randomSubsetOf(Set<int>& s){
  bool tag=bool(randomInteger(0,1));
  if(s.isEmpty()){
    Set<int> emptySet;
    return emptySet;
  }
  if(tag){
    int element=s.first();
    s.remove(element);
    Set<int>    result=randomSubsetOf(s);
    result.add(element);
    return result;
  }
  if(!tag){
    int element=s.first();
    s.remove(element);
    return randomSubsetOf(s);
  }
}
