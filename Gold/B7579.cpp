//앱

#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

typedef pair<int, int> pii;



int N, M, total_cost = 0;
vector<pii> v(101);
vector<vector<int>> dp(101, vector<int>(10001, 0));


int main(){

  cin >> N >> M;
  for(int i = 1; i <= N; ++i){
    cin >> v[i].first;
  }
  for(int i = 1 ; i <= N; ++i){
    cin >> v[i].second;
    total_cost += v[i].second;
  }


  for(int i = 1; i <= N; ++i){
    for(int j = 0; j <= total_cost; ++j){
      int cost = v[i].second;
      if(j - cost >= 0) dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost]+v[i].first);
      else dp[i][j] = dp[i-1][j];
      
    }
  }

  for(int i = 0; i <= total_cost; ++i){
    if(dp[N][i] >= M){
      cout << i;
      break;
    }
  }

}
