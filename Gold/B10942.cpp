// 팰린드롬?

#include <iostream>
#include <vector>

using namespace std;

int dfs(int s, int e);
int N, S, E, M;
vector<int> v(2001);
vector<vector<int>> dp(2001, vector<int>(2001, 2));

int main(){

  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N;

  for(int i = 1; i <= N; ++i){
    cin >> v[i];
  }

  cin >> M;

  for(int i = 0; i < M; ++i){
    cin >> S >> E;
    cout << dfs(S, E) << '\n';
  }

  return 0;
}

int dfs(int s, int e){
  if(s == e) return 1;

  if(dp[s][e] == 2){
    if(v[s] == v[e]){
      if(s+1 == e){
        dp[s][e] = 1;
        return 1;
      }
      int tmp = dfs(s+1, e-1);
      dp[s][e] = tmp; 
      return tmp;
    }
    else{
      dp[s][e] = 0;
      return 0;
    }
  }
  else if(dp[s][e] == 1){
    return 1;
  }
  else return 0;
}