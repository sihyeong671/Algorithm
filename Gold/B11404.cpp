// 플로이드

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
const int INF = 1e9;
int n, m;

int main(){
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> n;
  cin >> m;
  vector<vector<int>> dist(n+1, vector<int>(n+1, INF));
  for(int i = 1; i <= n; ++i){
    dist[i][i] = 0;
  }
  int a, b, c;
  for(int i = 0; i < m; ++i){
    cin >> a >> b >> c;
    if(c < dist[a][b]) dist[a][b] = c;
  }
  

  for(int i = 1; i <= n; ++i){
    for(int j = 1; j <= n; ++j){
      for(int k = 1; k <= n; ++k){
        dist[j][k] = min(dist[j][k], dist[j][i]+dist[i][k]);
      }
    }
  }

  for(int i = 1; i <= n; ++i){
    for(int j = 1; j <= n; ++j){
      if(dist[i][j] == INF) cout << "0 ";
      else cout << dist[i][j] << " ";
    }
    cout << '\n';
  }
}