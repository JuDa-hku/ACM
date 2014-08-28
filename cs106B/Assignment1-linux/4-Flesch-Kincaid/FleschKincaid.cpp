/*******************************************************************
 * File: FleschKincaid.cpp
 *
 * A program that approximates the Flesch-Kincaid grade level of a
 * piece of text.
 */

#include <iostream>
#include <fstream>
#include<assert.h>
#include "tokenscanner.h"
#include "simpio.h"
using namespace std;
int numberOfWord=0, numberOfSen=0, numberOfSyll=0;
void count(string file);
int countSyll(string str);
bool isVowel(char ch);

int main() {
  string fileName;
  while(true){
  fileName=getLine("Input the file name:");
  fstream myfile;
  myfile.open(fileName.c_str());
  if(myfile.is_open()){ 
    myfile.close();
    break;
  }
  }
  assert(isVowel('a'));
  count(fileName);
  cout<<numberOfWord<<endl;
  cout<<numberOfSen<<endl;
  cout<<numberOfSyll<<endl;
  return 0;
}

void count(string file){
  fstream myfile;
  myfile.open(file.c_str());
  TokenScanner scanner(myfile);
  scanner.ignoreWhitespace();
  scanner.addWordCharacters("':");
   while(scanner.hasMoreTokens()){
     string str=scanner.nextToken();
     char ch=str[0];
     if(isalpha(ch))
       {
       numberOfWord++;
       numberOfSyll+=countSyll(str);
       }
     if(ch=='.'||ch=='!'||ch=='?')
       numberOfSen++;
   }
  myfile.close();
}

bool isVowel(char ch){
  switch(ch){
  case 'a': return true;
  case 'e': return true;
  case 'o': return true;
  case 'u': return true;
  case 'i': return true;
  case 'y': return true;
  }
  return false;
  }

int countSyll(string str){
  int result=0;
  bool tag=true;
  for(int i=0; i<=str.length()-1; i++){
    if(tag&&isVowel(str[i])){
      result++;
      tag=false;
    }
    else tag=true;
  }
  if(result==0) result++;
  return result;
}
    
