/*************************************************************
 * File: pqueue-heap.cpp
 *
 * Implementation file for the HeapPriorityQueue
 * class.
 */
 
#include "pqueue-heap.h"
#include "error.h"
#include <iostream>
using namespace std;

HeapPriorityQueue::HeapPriorityQueue() {
  MAXIMA=2;
  stringHeap = new string[MAXIMA];
  stringHeap[0]="DUMP!";
  size1 = 0;
}

HeapPriorityQueue::~HeapPriorityQueue() {
  delete[] stringHeap;
}

int HeapPriorityQueue::size() {
	return size1;
}

bool HeapPriorityQueue::isEmpty() {
	return size1==0;
}

void HeapPriorityQueue::enqueue(string value) {
  enlargeHeap();
  if(size1==0) {
    size1=1;
    stringHeap[1]=value;
  }
  else{
    size1++;
    stringHeap[size1]=value;
    updateHeap(size1);
  }
}

string HeapPriorityQueue::peek() {
  if(size1==0) error("no");
  else{
	return stringHeap[1];
  }
}

string HeapPriorityQueue::dequeueMin() {
  if(size1==0) error("no");
  string tmp=stringHeap[1];
  swap(1, size1);
  size1--;
  if(size1>1) updateHead();
  return tmp;
}

void HeapPriorityQueue::updateHead(){
  int Index=1;
  while(2*Index+1<=size()){
    if(stringHeap[Index*2]<=stringHeap[Index*2+1]&&stringHeap[Index*2]<stringHeap[Index]){
      swap(Index*2, Index);
      Index*=2;
    }
     else{
       if(stringHeap[Index*2]>=stringHeap[Index*2+1]&&stringHeap[Index*2+1]<stringHeap[Index])
	 {
	   swap(Index*2+1, Index);
	   Index=Index*2+1;
	 }
       else break;
     }
  }
  if(Index*2<=size()){
    if(stringHeap[Index]>stringHeap[Index*2])
      swap(Index, Index*2);
  }
}


void HeapPriorityQueue::enlargeHeap(){
  if(size1==MAXIMA-1){
    MAXIMA*=2;
   string* newString=new string[MAXIMA];
    for(int i=0; i<=size1; i++)
      newString[i]=stringHeap[i];
    delete[] stringHeap;
    stringHeap=newString;
  }
}

void HeapPriorityQueue::swap(int pos1, int pos2){
  string tmp = stringHeap[pos1];
  stringHeap[pos1]=stringHeap[pos2];
  stringHeap[pos2]=tmp;
}

void HeapPriorityQueue::updateHeap(int newPos){
  while(newPos>1){
    int parIndex=newPos/2;
    if(stringHeap[newPos]<stringHeap[parIndex]){
      swap(newPos, parIndex);
      newPos=parIndex;
    }
    else
      break;
  }
}
    
