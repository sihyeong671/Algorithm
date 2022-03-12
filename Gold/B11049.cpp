// 행렬 곱셈 순서

#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

const int INF = pow(2, 31) - 1;
typedef pair<int, int> pii;

int matrix_dot(int s, int m, int e);
int N, r, c;
vector<pii> v;


int main(){
  cin >> N;
  int x, y;
  for(int i = 0; i < N; ++i){
    cin >> x >> y;
    v.push_back(make_pair(x, y));
  }

  vector<vector<int>> dp(N+1, vector<int>(N+1, 0));

  for(int i = 1; i <= N; ++i){
    for(int j = 1; j <= N - i; ++j){
      dp[j][j+i] = INF;
      for(int k = 0; k < i; ++k){
        dp[j][j+i] = min(dp[j][j+i], dp[j][j+k]+dp[j+k+1][j+i]+matrix_dot(j, j+k, i+j));
      }
    }
  }

  cout << dp[1][N];
  

  return 0;
}

int matrix_dot(int s, int m, int e){
  return (v[s-1].first * v[m-1].second * v[e-1].second);
}