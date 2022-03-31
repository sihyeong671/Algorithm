// KCM Travel

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

typedef pair<int, pair<int, int>> piii;


// pq top 원소는 가장 뒤에 있음
struct compare{
  bool operator()(piii a, piii b){
    return a.second.second > b.second.second;
  }
};

int dijkstra(vector<vector<piii>> &graph);
const int INF = 1e9;
int T, N, M, K, u, v, c, d;

int main(){

  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> T;
  for(int i = 0; i < T; ++i){
    cin >> N >> M >> K;
    vector<vector<piii>> graph(N+1);
    for(int j = 1; j <= K; ++j){
      cin >> u >> v >> c >> d;
      graph[u].push_back({v, {c, d}});
    }
    int ans = dijkstra(graph);

    if(ans == INF) cout << "Poor KCM\n";
    else cout << ans << '\n';
  }
}

int dijkstra(vector<vector<piii>> &graph){
  vector<vector<int>> dist(N+1, vector<int>(M+1, INF));
  priority_queue<piii, vector<piii>, compare> pq;

  dist[1][1] = 0;
  pq.push({1, {0, 0}});

  while(!pq.empty()){
    int c_idx = pq.top().first;
    int cost = pq.top().second.first;
    int time = pq.top().second.second;
    pq.pop();

    if(dist[c_idx][cost] < time) continue;

    for(auto &e : graph[c_idx]){
      int n_idx = e.first;
      int n_cost = cost + e.second.first;
      int n_time = time + e.second.second;
      if(n_cost <= M && dist[n_idx][n_cost] > n_time){
        for(int i = n_cost; i <= M; ++i){
          if(dist[n_idx][i] > n_time)  dist[n_idx][i] = n_time;
        }
        pq.push({n_idx, {n_cost, n_time}});
      }
    }
  }
  int ans = INF;
  for(auto e: dist[N]){
    ans = min(ans, e);
  }
  return ans;
}