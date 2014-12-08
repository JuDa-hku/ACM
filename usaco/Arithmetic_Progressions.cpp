/*
ID: judanju1
PROG: ariprog
LANG: C++    
*/
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#define MaxM 125001
using namespace std;
int N, M;
bool bisquares[MaxM];
struct solution{
  int first;
  int diff;
};
bool comp(solution a, solution b){
  if(a.diff<b.diff) return true;
  if(a.diff==b.diff) return a.first<b.first;
  else return false;
}

void inittable(){
  for(int i=0; i<=M; i++)
    for(int j=0; j<=M; j++)
      bisquares[i*i+j*j]=true;
}

bool check(int first, int diff){
  for(int i=0; i<N; i++){
    if((first+i*diff)>2*M*M||!bisquares[first+i*diff])
      return false;
  }
  return true;
}

int main() {
  vector<solution> solutions;
  ofstream fout ("ariprog.out");
  ifstream fin ("ariprog.in");
  fin >> N >> M;
  inittable();
  for(int first=0; first<=2*M*M; first++)
    for(int diff=1; diff<=2*M*M; diff++){
      if(first+(N-1)*diff>2*M*M) break;
      if(check(first, diff)){
	solution tmp;
	tmp.first=first;
	tmp.diff=diff;
	solutions.push_back(tmp);
      }
    }
  if(solutions.size()==0) fout<<"NONE"<<endl;
  else{
    sort(solutions.begin(), solutions.end(), comp);
    for(int i=0; i<solutions.size(); i++)
      fout<<solutions[i].first<<" "<<solutions[i].diff<<endl;
}
    return 0;
}
