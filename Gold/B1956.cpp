// 운동

#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

typedef pair<int, int> pii;

const int INF = 1e9;
int V, E, a, b, c;

int main(){
  cin >> V >> E;
  vector<vector<int>> dist(V+1, vector<int>(V+1, INF));

  for(int i = 1; i <= V; ++i){
    dist[i][i] = 0;
  }

  for(int i = 0; i < E; ++i){
    cin >> a >> b >> c;
    dist[a][b] = c; 
  }

  for(int i = 1;i <= V; ++i){
    for(int j = 1; j <= V; ++j){
      for(int k = 1; k <= V; ++k){
        dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k]);
      }
    }
  }

  int ans = INF;
  for(int i = 1; i <= V; ++i){
    for(int j = 1; j <= V; ++j){
      if(i==j) continue;
      ans = min(ans, dist[i][j]+dist[j][i]);
    }
  }

  if(ans == INF) cout << "-1";
  else cout << ans;
}