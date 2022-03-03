#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

const int INF = 100000000;
int T, K, c;
int main(){
  cin >> T;
  for(int i = 0; i < T; ++i){
    cin >> K;
    vector<vector<int>> dp(K+1, vector<int>(K+1, 0));
    vector<int> sum_(K+1, 0);
    for(int j = 1; j <= K; ++j){
      int tmp;
      cin >> tmp;
      sum_[j] = sum_[j-1] + tmp;
    }

    for(int j = 1; j <= K; ++j){
      for(int k = 1; k <= K - j; ++k){
        dp[k][k+j] = INF;
        for(int w = 0; w < j; ++w){
          dp[k][k+j] = min(dp[k][k+j], dp[k][k+w] + dp[k+w+1][k+j] + sum_[k+j] - sum_[k-1]);
        }
      }
    }
    cout << dp[1][K] << endl;
  }
}
