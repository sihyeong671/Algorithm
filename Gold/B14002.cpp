#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N;

int main(){

  cin >> N;

  vector<int> v(N);
  vector<int> dp(N, 1);
  vector<int> before(N, 0);

  for(auto &e: v){
    cin >> e;
  }

  int idx=0, _max=1;
  for(int i = 0; i < N; ++i){
    for(int j = 0; j < i; ++j){
      if(v[j] < v[i] && dp[i] < dp[j] + 1){
        dp[i] = dp[j] + 1;
        before[i] = j;
        if(_max < dp[i]){
          _max = dp[i];
          idx = i;
        }
      }
    }
  }

  cout << _max << '\n';
  vector<int> tmp;
  for(int i = 0; i < _max; ++i){
    tmp.push_back(v[idx]);
    idx = before[idx];
  }
  for(int i = tmp.size()-1; i >= 0; --i){
    cout << tmp[i] << ' ';
  }
}