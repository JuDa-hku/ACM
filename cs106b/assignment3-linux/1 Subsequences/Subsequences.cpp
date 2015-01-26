/*
 * File: Subsequences.cpp
 * ----------------------
 * Name: [TODO: enter name here]
 * Section: [TODO: enter section leader here]
 * This file is the starter project for the Subsequences problem
 * on Assignment #3.
 * [TODO: extend the documentation]
 */

#include <iostream>
#include <string>
//#include "console.h"
using namespace std;

/* Given two strings, returns whether the second string is a
 * subsequence of the first string.
 */
bool isSubsequence(string text, string subsequence);

int main() {
  bool tag=isSubsequence("leasta", "steal");
  if(tag) cout<<"dfag"<<endl;
  return 0;
}


bool isSubsequence(string text, string subsequence){
  cout<<text.length()<<" "<<text<<" "<<subsequence<<endl;
  if(subsequence.length()==0)
    return true;
  if(subsequence.length()==1){
    int pos=text.find(subsequence[0]);
    cout<<pos<<endl;
    return pos!=-1;
  }
  if(text.length()==1){
    cout<<"here"<<endl;
    return false;
  }
  int pos=text.find(subsequence[0]);
  if(pos!=-1){
    cout<<pos<<endl;
    return isSubsequence(text.substr(pos+1), subsequence.substr(1));
  }
}
    
