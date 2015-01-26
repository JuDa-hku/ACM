/*
 * File: RandomWriter.cpp
 * ----------------------
 * Name: [TODO: enter name here]
 * Section: [TODO: enter section leader here]
 * This file is the starter project for the random writer problem
 * on Assignment #2.
 * [TODO: extend the documentation]
 */

#include <fstream>
#include <iostream>
#include <string>
//#include "console.h"
#include "map.h"
#include "simpio.h"
#include "random.h"
#include "strlib.h"
#include "vector.h"
using namespace std;
string getFileName();
void scanFile(int order, string fileName);
string initKey();
void outPutFile(int order);
Map<string, Vector<char> > Ordermap;
Vector<string> Keys;

int main() {
  string fileName=getFileName();
  int order= getInteger("Input the order:");
  scanFile(order, fileName);
  outPutFile(order);
  return 0;
}

string getFileName(){
  while(true){
    string fileName = getLine("Input the file name: ");
    fstream infile;
    infile.open(fileName.c_str());
    if(infile.is_open()){
      infile.close();
      return fileName;
    }
    else
      cout<<"Input the name again.";
  }
}

void scanFile(int order, string fileName){
  fstream infile;
  infile.open(fileName.c_str());
  char ch;
  string str="";
  while(infile.get(ch)){
    str=str+ch;
    if(str.length()==order+1){
      string key = str.substr(0, order);
      Keys.add(key);
      Ordermap[key].add(str[order]);
      str = str.substr(1, order);
    }
  }
}

string initKey(){
  string freKey;
  int lengthest=0;
  foreach(string key in Keys){
    int len = Ordermap[key].size();
    if(len>lengthest){
      freKey=key;
      lengthest=len;
    }
  }
  return freKey;
}

void outPutFile(int order){
  string keyString = initKey();
  cout<<keyString;
  for(int i=0; i<2000; i++){
    Vector<char> chVec = Ordermap[keyString];
    int seed = randomInteger(0, chVec.size()-1);
    char ch = chVec[seed];
    if(ch=='\0') break;
    cout<<ch;
    keyString = keyString.substr(1, order-1)+ch;
  }
  cout<<endl;
}





