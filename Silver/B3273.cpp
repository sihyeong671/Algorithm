// 두 수의 합

#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int n, x;
int ans = 0;
int main(){
  
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  cin >> n;
  vector<int> v(n);
  int tmp;
  for(auto &e : v){
    cin >> tmp;
    e = tmp;
  }
  cin >> x;
  sort(v.begin(), v.end());

  int p1 = 0;
  int p2 = n-1;

  while(p2 > p1){
    if(v[p1]+v[p2] == x){
      ++ans;
      ++p1; // or --p2
    } 
    else if (v[p1]+v[p2] < x) ++p1;
    else if (v[p1]+v[p2] > x) --p2;
  }

  cout << ans;

}