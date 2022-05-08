#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int N;
const int INF = 1e6;


int main(){
  cin >> N;

  vector<int> dp(N+1, INF);
  vector<int> before(N+1, 0); // 역추적

  dp[N] = 0;
  int idx = N-1;
  while(idx >= 1){

    if(dp[idx] > dp[idx+1] + 1){
      dp[idx] = dp[idx+1] + 1;
      before[idx] = idx + 1;
    }
    if(idx*2 <= N && dp[idx] > dp[idx*2] + 1){
      dp[idx] = dp[idx*2] + 1;
      before[idx] = idx*2;
    }
    if(idx*3 <= N && dp[idx] > dp[idx*3] + 1){
      dp[idx] = dp[idx*3] + 1;
      before[idx] = idx*3;
    }
    --idx;
  }


  cout << dp[1] << '\n';
  int tmp = 1;
  vector<int> ans;
  while(tmp != 0){
    ans.push_back(tmp);
    tmp = before[tmp];
  }
  for(int i = ans.size() - 1; i >= 0; --i){
    cout << ans[i] << ' ';
  }
}