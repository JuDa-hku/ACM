/******************************************************************************
 * File: Trailblazer.cpp
 *
 * Implementation of the graph algorithms that comprise the Trailblazer
 * assignment.
 */

#include "Trailblazer.h"
#include "TrailblazerGraphics.h"
#include "TrailblazerTypes.h"
#include "TrailblazerPQueue.h"
#include "random.h"
using namespace std;

/* Function: shortestPath
 * 
 * Finds the shortest path between the locations given by start and end in the
 * specified world.	 The cost of moving from one edge to the next is specified
 * by the given cost function.	The resulting path is then returned as a
 * Vector<Loc> containing the locations to visit in the order in which they
 * would be visited.	If no path is found, this function should report an
 * error.
 *
 * In Part Two of this assignment, you will need to add an additional parameter
 * to this function that represents the heuristic to use while performing the
 * search.  Make sure to update both this implementation prototype and the
 * function prototype in Trailblazer.h.
 */
Vector<Loc>
shortestPath(Loc start,
						 Loc end,
						 Grid<double>& world,
	     double costFn(Loc from, Loc to, Grid<double>& world), double heuristic(Loc start, Loc end, Grid<double>& world)) {
  Loc tmp=end;
  end=start;
  start=tmp;
  TrailblazerPQueue<Loc> TPQ;
  Set<Loc> greySet;
  Set<Loc> yellowSet;
  Set<Loc> greenSet;
  Map<Loc, double> disMap;
  Map<Loc, Loc> parentMap;
  for(int i=0; i<world.numRows(); i++)
    for(int j=0; j<world.numCols(); j++){
      Loc loc=makeLoc(i, j);
      colorCell(world, loc, GRAY);
      greySet.add(loc);
  }
  disMap[start]=0;
  colorCell(world, start, YELLOW);
  yellowSet.add(start);
  greySet.remove(start);
  double h=heuristic(start, end, world);
  TPQ.enqueue(start, h);
  while(!TPQ.isEmpty()){
    Loc curr=TPQ.dequeueMin();
    greenSet.add(curr);
    colorCell(world, curr, GREEN);
    if(curr==end)
      break;
    for(int i=-1; i<=1; i++)
      for(int j=-1; j<=1; j++){
	if(0<=curr.row+i<world.numRows()&&
	   0<=curr.col+j<world.numCols()){
	  Loc neigh=makeLoc(curr.row+i, curr.col+j);
	  if(greySet.contains(neigh)){
	    colorCell(world, neigh, YELLOW);
	    yellowSet.add(neigh);
	    greySet.remove(neigh);
	    parentMap[neigh]=curr;
	    disMap[neigh]=disMap[curr]+costFn(curr, neigh, world);
	    double h=heuristic(neigh, end, world);
	    TPQ.enqueue(neigh, disMap[neigh]+h);
	  }
	  if(yellowSet.contains(neigh)){
double newdist=disMap[curr]+costFn(curr, neigh, world);
 if(newdist<disMap[neigh]){
   parentMap[neigh]=curr;
   disMap[neigh]=newdist;
   double h=heuristic(neigh, end, world);
   TPQ.decreaseKey(neigh, newdist+h);
 }
	  }
	}
      }
  }
  Vector<Loc> shortestPath;
  cout<<end.row<<" "<<end.col<<endl;
  for(Loc i=end;i!=start; i=parentMap[i])
    shortestPath.add(i);
  shortestPath.add(start);
  cout<<shortestPath[1].row<<" "<<shortestPath[1].col<<endl;
  return shortestPath;
}


Vector<Loc>
shortestPathOri(Loc start,
						 Loc end,
						 Grid<double>& world,
						 double costFn(Loc from, Loc to, Grid<double>& world)) {
  Loc tmp=end;
  end=start;
  start=tmp;
  TrailblazerPQueue<Loc> TPQ;
  Set<Loc> greySet;
  Set<Loc> yellowSet;
  Set<Loc> greenSet;
  Map<Loc, double> disMap;
  Map<Loc, Loc> parentMap;
  for(int i=0; i<world.numRows(); i++)
    for(int j=0; j<world.numCols(); j++){
      Loc loc=makeLoc(i, j);
      colorCell(world, loc, GRAY);
      greySet.add(loc);
  }
  disMap[start]=0;
  colorCell(world, start, YELLOW);
  yellowSet.add(start);
  greySet.remove(start);
  TPQ.enqueue(start, disMap[start]);
  while(!TPQ.isEmpty()){
    Loc curr=TPQ.dequeueMin();
    greenSet.add(curr);
    colorCell(world, curr, GREEN);
    if(curr==end)
      break;
    for(int i=-1; i<=1; i++)
      for(int j=-1; j<=1; j++){
	if(0<=curr.row+i<world.numRows()&&
	   0<=curr.col+j<world.numCols()){
	  Loc neigh=makeLoc(curr.row+i, curr.col+j);
	  if(greySet.contains(neigh)){
	    colorCell(world, neigh, YELLOW);
	    yellowSet.add(neigh);
	    greySet.remove(neigh);
	    parentMap[neigh]=curr;
	    disMap[neigh]=disMap[curr]+costFn(curr, neigh, world);
	    TPQ.enqueue(neigh, disMap[neigh]);
	  }
	  if(yellowSet.contains(neigh)){
double newdist=disMap[curr]+costFn(curr, neigh, world);
 if(newdist<disMap[neigh]){
   parentMap[neigh]=curr;
   disMap[neigh]=newdist;
   TPQ.decreaseKey(neigh, newdist);
 }
	  }
	}
      }
  }
  Vector<Loc> shortestPath;
  cout<<end.row<<" "<<end.col<<endl;
  for(Loc i=end;i!=start; i=parentMap[i])
    shortestPath.add(i);
  shortestPath.add(start);
  cout<<shortestPath[1].row<<" "<<shortestPath[1].col<<endl;
  return shortestPath;
}

Set<Edge> createMaze(int numRows, int numCols) {
  Set<Edge> result;
  Set<Edge> edgeSet;
  Vector<Set<Loc> > clusters;
  for(int i=0; i<numRows; i++)
    for(int j=0; j<numCols; j++){
          Loc curr=makeLoc(i, j);
           Set<Loc> currSet;
           currSet.add(curr);
           clusters.add(currSet);
      if(i+1<numRows){
      	Loc locDown=makeLoc(i+1, j);
      	Edge edgeDown=makeEdge(curr, locDown);
	cout<<locDown.row<<endl;
      	edgeSet.add(edgeDown);
      }
      if(j+1<numCols){
      	Loc locRight=makeLoc(i,j+1);
      	Edge edgeRight=makeEdge(curr, locRight);
      	edgeSet.add(edgeRight);
      }
    }
  TrailblazerPQueue<Edge> mazePQ;
  foreach(Edge edge in edgeSet)
    mazePQ.enqueue(edge, randomInteger(0, 10));
  cout<< mazePQ.isEmpty()<<endl;
  while(clusters.size()>1){
  cout<< mazePQ.isEmpty()<<endl;
    Edge e=mazePQ.dequeueMin();
    cout<<1<<endl;
    Loc eLoc1=e.start;
    Loc eLoc2=e.end;
    int index1, index2;
    for(int i=0;i<clusters.size();i++){
      if(clusters[i].contains(eLoc1))
	index1=i;
      if(clusters[i].contains(eLoc2))
	index2=i;
    }
    if(index1!=index2){
      clusters[index1]+=clusters[index2];
      clusters.remove(index2);
      result.add(e);
    }
  }
return result;
//  return result;
}
