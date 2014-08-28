/*************************************************************
 * File: pqueue-linkedlist.cpp
 *
 * Implementation file for the LinkedListPriorityQueue
 * class.
 */
#include<iostream>
#include "pqueue-linkedlist.h"
#include "error.h"

LinkedListPriorityQueue::LinkedListPriorityQueue() {
	// TODO: Fill this in!
  startLinkp=new linkedList;
  startLinkp=NULL;
}

LinkedListPriorityQueue::~LinkedListPriorityQueue() {
  cout<<1<<endl;
 linkedList* nextp=new linkedList;
 cout<<1<<endl;
  while(startLinkp!=NULL){
    nextp=startLinkp->nextLinkp;
    delete  startLinkp;
    startLinkp=nextp;
  }
}

int LinkedListPriorityQueue::size() {
  int size=0;
  linkedList* p=new linkedList;
  p=startLinkp;
  if(p==NULL) return 0;
  while(p!=NULL){
    p=p->nextLinkp;
    size++;
  }
  return size;
}

bool LinkedListPriorityQueue::isEmpty() {
  return (startLinkp==NULL);
}

void LinkedListPriorityQueue::enqueue(string value) {
  linkedList *newP=new linkedList;
  linkedList *currentP=new linkedList;
  linkedList *preP=new linkedList;
  currentP=startLinkp;
  newP->str=value;
  newP->nextLinkp=NULL;
  // empty priority queue case
  if(currentP==NULL) {
    startLinkp=newP;
  }
  // insert in the head
  else if(currentP->str>=value){
    newP->nextLinkp=currentP;
    startLinkp=newP;
  }
  else{
    while(currentP->str<value){
      preP=currentP;
      currentP=currentP->nextLinkp;
      if(currentP==NULL) break;
    }
    // insert in the end
    if(currentP==NULL){
      preP->nextLinkp=newP;
    }
    // insert in the middle
    else{
      newP->nextLinkp=preP->nextLinkp;
      preP->nextLinkp=newP;
    }
  }
}



string LinkedListPriorityQueue::peek() {
  if(startLinkp==NULL) error("No more");
  else{
  string str=startLinkp->str;
  return str;
  }
}

string LinkedListPriorityQueue::dequeueMin() {
  if(startLinkp==NULL) error("No more");
  else{
  string str=startLinkp->str;
  startLinkp=startLinkp->nextLinkp;
  return str;
  }
}

