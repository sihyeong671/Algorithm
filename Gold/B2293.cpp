// 동전1

#include<iostream>
#include<vector>

using namespace std;


int n, k, coin;
vector<int> coins(100);
vector<int> dp(10001, 0);

int main(){
  cin >> n >> k;
  for(int i = 0; i < n; ++i){
    cin >> coins[i];
  }

  dp[0] = 1;
  for(int i = 0; i < n; ++i){
    for(int j = coins[i]; j <= k; ++j){
      dp[j] += dp[j - coins[i]];

    }
  }

  cout << dp[k];
}

