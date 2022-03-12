// 내리막 길

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int dfs(int r, int c);
int M, N;

vector<int> tr = {-1, 1, 0, 0};
vector<int> tc = {0, 0, -1, 1};
vector<vector<int>> map(500, vector<int>(500));
vector<vector<int>> dp(500, vector<int>(500, -1));

int main(){
  cin >> M >> N;
  for(int i = 0; i < M; ++i){
    for(int j = 0; j < N; ++j){
      cin >> map[i][j];
    }
  }

  cout << dfs(M-1, N-1);
}

int dfs(int r, int c){
  if(dp[r][c] != -1) return dp[r][c];
  if(r == 0 && c == 0) return 1;
  dp[r][c] = 0;
  for(int i = 0; i < 4; ++i){
    int nr = r+tr[i];
    int nc = c+tc[i];
    if(0 <= nr && nr < M && 0 <= nc && nc < N && map[nr][nc] > map[r][c]){
      dp[r][c] += dfs(nr, nc);
    }
  }
  return dp[r][c];
}