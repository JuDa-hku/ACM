/*************************************************************
 * File: pqueue-doublylinkedlist.cpp
 *
 * Implementation file for the DoublyLinkedListPriorityQueue
 * class.
 */
 
#include "pqueue-doublylinkedlist.h"
#include "error.h"
#include <iostream>
using namespace std;
DoublyLinkedListPriorityQueue::DoublyLinkedListPriorityQueue() {
  startP=NULL;
}

DoublyLinkedListPriorityQueue::~DoublyLinkedListPriorityQueue() {
  while(startP!=NULL){
    dbl* tmp=startP->next;
    delete startP;
    startP=tmp;
  }
}

int DoublyLinkedListPriorityQueue::size() {
  int size=0;
  for(dbl* tmp=startP; tmp!=NULL; tmp=tmp->next)
    size++;
  return size;
}

bool DoublyLinkedListPriorityQueue::isEmpty() {
  return (startP==NULL);
}

void DoublyLinkedListPriorityQueue::enqueue(string value) {
  dbl* addEle=new dbl;
  addEle->str=value;
  addEle->next=startP;
  addEle->pre=NULL;
  if(startP!=NULL) startP->pre=addEle;
  startP=addEle;
}

string DoublyLinkedListPriorityQueue::peek() {
  if(startP==NULL) error("NO");
  else{
    string str=startP->str;	
    for(dbl* tmp=startP; tmp!=NULL; tmp=tmp->next){
      if(tmp->str<str)
	str=tmp->str;
    }
    return str;
  }
}
string DoublyLinkedListPriorityQueue::dequeueMin() {
  if(startP==NULL) error("NO");
  else{
    dbl* remove=startP;
    string str=startP->str;	
    for(dbl* tmp=startP; tmp!=NULL; tmp=tmp->next){
      if(tmp->str<str){
	str=tmp->str;
	remove=tmp;
    }
  }
    if(remove==startP){
      startP=remove->next;
      delete remove;
}
    else{
      if(remove->next==NULL){
	remove->pre->next=NULL;
      delete remove;
      }
    else{
      remove->pre->next=remove->next;
      remove->next->pre=remove->pre;
      delete remove;
    }
    }
    return str;
  }
}


