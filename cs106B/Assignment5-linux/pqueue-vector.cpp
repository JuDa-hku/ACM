/*************************************************************
 * File: pqueue-vector.cpp
 *
 * Implementation file for the VectorPriorityQueue
 * class.
 */
 
#include "pqueue-vector.h"
#include "error.h"

VectorPriorityQueue::VectorPriorityQueue() {
}

VectorPriorityQueue::~VectorPriorityQueue() {
}

int VectorPriorityQueue::size() {
  return vpq.size();
}

bool VectorPriorityQueue::isEmpty() {
  return (vpq.size()==0);
}

void VectorPriorityQueue::enqueue(string value) {
  vpq.add(value);
}

string VectorPriorityQueue::peek() {
  string min;
  if(vpq.isEmpty()) 
    error("The queue is empty");
  else {
    min=vpq[0];
    for(int i=0; i<vpq.size(); i++){
      if(vpq[i]<min)
	min=vpq[i];
    }
  return min;
  }
}

string VectorPriorityQueue::dequeueMin() {
  string min;
  int j=0;
  if(vpq.isEmpty())
    error("The queue is empty");
  else{
    for(int i=0;i<vpq.size();i++){
      if(vpq[i]<vpq[j])
	j=i;
    }
    min=vpq[j];
    vpq.remove(j);
    return min;
  }
}

