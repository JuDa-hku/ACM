/**********************************************
 * File: pqueue-vector.h
 *
 * A priority queue class backed by an unsorted
 * vector.
 */
#ifndef PQueue_Vector_Included
#define PQueue_Vector_Included

#include <string>
#include "vector.h"
using namespace std;

/* A class representing a priority queue backed by an
 * unsorted Vector.
 */
class VectorPriorityQueue {
public:
  VectorPriorityQueue();
  ~VectorPriorityQueue();
  int size();
  bool isEmpty();

  void enqueue(string value);
	
  string peek();
	
	/* Returns and removes the lexicographically first string in the
	 * priority queue.
	 */
  string dequeueMin();

 private:
  Vector<string> vpq;
};

#endif
