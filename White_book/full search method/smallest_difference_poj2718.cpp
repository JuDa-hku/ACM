#include<iostream>
#include<cstdio>
#include<algorithm>
#include<string>
#define INF 10000000
#define MAX_N 1000
#define MAX_M 1000
using namespace std;
int num[11];
bool used[11];
int per[11];
int best=INF;

void smallest(int pos, int n){
  if(pos==n){ //this case perm has the array
    int    m=n/2;
    int part1=0, part2=0;
    if(per[0]!=0&&per[m]!=0&&per[0]>per[m]){
      for(int i=0; i<m; i++){
	part1=per[i]+10*part1;
      }
      for(int i=m; i<n; i++)
	part2=per[i]+10*part2;
      best=min(best, abs(part1-part2));
    }
  }
  for(int i=0; i<n; i++){
    if(!used[i]){
      per[pos]=num[i];
      used[i]=true;
      smallest(pos+1, n);
      used[i]=false;
    }
  }
  return ;
}

void permutation2(int n){
  for(int i=0; i<n; i++)
    per[i]=num[i];
  do{
    int    m=n/2;
    int part1=0, part2=0;
        if(per[0]==0&&n==2)
          best=per[1]-per[0];
	else if(per[0]!=0&&per[m]!=0){
	  for(int i=0; i<m; i++){
	    part1=per[i]+10*part1;
	  }
	  for(int i=m; i<n; i++){
	    part2=per[i]+10*part2;
	  }
	  best=min(best, abs(part1-part2));
	}
  }while(next_permutation(per, per+n));
  return ;
}

  
  
  
int main(){
    int n;
    cin >> n;
    cin.ignore();
    while (n--)
    {
        string all;
	best=INF;
        getline(cin, all);
        all.erase(remove(all.begin(), all.end(), ' '), all.end());
	int m=all.size();
	for(int i=0; i<m; i++){
	  num[i]=all[i]-'0';
	//	smallest(0, m);
	}
	permutation2(m);
	cout<<best<<endl;
    }
}

//at first I forgot the special case that n=1; which make the subarray begin with 0.
