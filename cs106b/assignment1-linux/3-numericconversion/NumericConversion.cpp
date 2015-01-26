/*
 * File: NumericConversion.cpp
 * ---------------------------
 * Name: [TODO: enter name here]
 * Section: [TODO: enter section leader here]
 * This file is the starter project for the numeric-conversion problem
 * in which you implement the functions intToString and stringToInt.
 * [TODO: rewrite the documentation]
 */

#include <iostream>
#include <string>
#include <assert.h>
//#include "console.h"
using namespace std;

/* Function prototypes */

string intToString(int n);
int stringToInt(string str);

/* Main program */

int main() {
   // [TODO: fill in the code]
  assert(intToString(1729)=="1729");
  assert(intToString(-1729)=="-1729");
  assert(stringToInt("123")==123);
  assert(stringToInt("-123")==-123);
  return 0;
}

string intToString(int n){
  if(n<0) return "-"+intToString(-n);
  if(n<10) return string()+char(n+'0');
  else return intToString(n/10)+intToString(n%10);
}

int stringToInt(string str){
  if(str[0]=='-') return -stringToInt(str.substr(1, str.length()-1));
  if(str.length()==1) return int(str[0])-int('0');
  else {
    string part1 = str.substr(0, str.length()-1);
    string part2 = str.substr(str.length()-1,1);
    int partOne = stringToInt(part1);
    int partTwo = stringToInt(part2);
    return 10*partOne+partTwo;
}
}
