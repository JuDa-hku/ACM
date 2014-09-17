/* for given numbers, a_1, a_2,....a_n, judge whether we can pick up some numbers, the sum of which are k.
 */
#include<iostream>
#include<cstdio>
#define MAX_N 100
//input 
using namespace std;
int a[MAX_N];
int n, k;
bool dfs(int i, int sum){
if(i==n) return sum==k;
if(dfs(i+1, sum)) return true;
if(dfs(i+1, sum-a[i])) {
cout<<a[i]<<endl;
return true;
}
return false;
}
void solve(){
  if(dfs(0,10)) printf("Yes\n");
  else printf("No\n");
}
int main(){
  cout<<"Input number of integer: "<<endl;
  cin>>n;
  for(int i=0; i<n; i++)
    cin>>a[i];
  solve();
  return 0;
}
