/*
 * File: WordLadder.cpp
 * --------------------
 * Name: [TODO: enter name here]
 * Section: [TODO: enter section leader here]
 * This file is the starter project for the word ladder problem
 * on Assignment #2.
 * [TODO: extend the documentation]
 */

#include <iostream>
#include<assert.h>
//#include "console.h"
#include "lexicon.h"
#include "queue.h"
#include "simpio.h"
#include "vector.h"
using namespace std;
bool judgeOne(string, string);
Lexicon onlyOneDif(string);
bool findLadder();

typedef Vector<string> vs;
Vector<string> result;
Lexicon english("EnglishWords.dat");

int main() {
  assert(judgeOne("abc","dbc"));
  Lexicon result1=onlyOneDif("come");
  foreach(string word in result1)
    cout<<word<<endl;
  bool tag=findLadder();
    if(tag){
      foreach(string word in result)
      cout<<word<<endl;
    }
}


bool judgeOne(string str1, string str2){
  int tag=0;
  if(str1.length()!=str2.length()) return false;
  for(int i=0;i<str1.length();i++){
    if(str1[i]!=str2[i]) tag++;
  }
  if(tag==1)
    return true;
}

Lexicon onlyOneDif(string str){
  Lexicon result;
  foreach (string word in english){
    if(judgeOne(str, word))
      result.add(word);
  }
  return result;
}
    


bool findLadder(){
  Queue<vs> queue;
  Lexicon wordUsed;
  Vector<string> ladder, firstLadder;
  string start=getLine("Input the start string: ");
  ladder.add(start);
  wordUsed.add(start);
  string end=getLine("Input the end string: ");
  queue.enqueue(ladder);
  while(queue.size()!=0){
    firstLadder = queue.dequeue();
    string endWord = firstLadder[firstLadder.size()-1];
    wordUsed.add(endWord);
    if(endWord==end){
      result = firstLadder;
      return true;
    }
    Lexicon oneDifLex=onlyOneDif(endWord);
    foreach(string word in oneDifLex){
      if(!wordUsed.contains(word)){
      Vector<string> firstLadderCopy = firstLadder;
      firstLadderCopy.add(word);
      queue.enqueue(firstLadderCopy);
      wordUsed.add(word);
    }
  }
}
}




