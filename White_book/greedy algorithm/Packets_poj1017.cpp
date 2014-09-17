#include<iostream>
#include<cstdio>
#include<algorithm>
#include<string>
#include<queue> // for bfs
#define MAX_N 10
using namespace std;
int size[MAX_N];
int ans;
void solve(){
  ans=size[6]+size[5]+size[4];
  size[1]=size[1]-11*size[5];
  //  cout<<size[1]<<endl;
  // from box 5*5 to box 1*1
  int numfrom4to2=0;
  for(; numfrom4to2<size[4]*5; numfrom4to2++){
    if(numfrom4to2==size[2])
      break;
  }
  size[2]-=numfrom4to2;
  //  cout<<size[2]<<endl;
  // the max box 2*2 from 4*4
  if(size[2]==0)
    size[1]-=4*(size[4]*5-numfrom4to2);
  //  cout<<size[1]<<endl;
  // box 2*2 has been all used and put 1*1
  ans+=size[3]/4;
  // box 3*3 needed
  size[3]%=4;
  //  cout<<size[3]<<endl;
  // has non zero box 3*3
  if(size[3]){
    ans++;
    int numfrom3to2=1;
    int maxfrom3to2=7-2*size[3];
    for(;numfrom3to2<maxfrom3to2; numfrom3to2++)
      if(numfrom3to2==size[2])
	break;
    size[2]-=numfrom3to2;
    size[1]-=(8-size[3]);
    if(numfrom3to2<size[2])
      size[1]-=4*(maxfrom3to2-numfrom3to2);
    //  cout<<size[1]<<endl;
  }

  if(size[2]<0)
    size[2]=0;
  if(size[1]<0)
    size[1]=0;
  size[1]+=(4*size[2]);
  if(size[1]>0&&size[1]%36!=0)
    ans++;
  ans+=size[1]/36;
}


int main(){
  while(true){
    scanf("%d %d %d %d %d %d", &size[1], &size[2], &size[3], &size[4], &size[5], &size[6]);
    if(size[1]==0&&size[2]==0&&size[3]==0&&size[4]==0&&size[5]==0&&size[6]==0)
      break;
    solve();
    cout<<ans<<endl;
    ans=0;
}
}



/*
0 0 4 0 0 1 
7 5 1 0 0 0 
65 65 513 1 8 8
1 0 0 0 0 0
0 1 0 0 0 0
0 0 1 0 0 0
0 0 0 1 0 0
0 0 0 0 1 0
0 0 0 0 0 1
0 0 0 0 0 0 
*/







