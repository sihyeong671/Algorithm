#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;
typedef long long ll;

ll N, k;

int main(){
  cin >> N >> k;
  ll start = 1;
  ll end = N*N;
  while(start <= end){
    ll mid = (start + end)/ 2;
    ll num = 0;
    for(int i = 1; i <= N; ++i){
      ll tmp;
      num += min(mid/i, N);
    }
    if(num < k){
      start = mid + 1;
    }
    else{
      end = mid - 1;
    }
  }
  cout << start;
  return 0;
}