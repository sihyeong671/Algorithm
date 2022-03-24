//특정한 최단 경로

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

typedef pair<int, int> pii;
int N, E, v1, v2;
const int INF = 1e9;

vector<int> dijkstra(vector<vector<int>> &graph, int s);

int main(){

  cin >> N >> E;

  vector<vector<int>> graph(N+1, vector<int>(N+1, 0));

  int a, b ,c;
  for(int i = 0; i < E; ++i){
    cin >> a >> b >> c;
    graph[a][b] = c;
    graph[b][a] = c;
  }
  cin >> v1 >> v2;

  // 1 -> v1, 1 -> v2
  vector<int> dist_1 = dijkstra(graph, 1);
  // v1 -> N, v1 -> v2 == v2 -> v1
  vector<int> dist_2 = dijkstra(graph, v1);
  // v2 -> N
  vector<int> dist_3 = dijkstra(graph, v2);

  int ans = min((dist_1[v1]+dist_2[v2]+dist_3[N]),(dist_1[v2]+dist_3[v1]+dist_2[N]));
  if(ans >= INF || ans < 0) cout << -1; // INF가 21억을 넘어가는 경우 음수가 되기 때문에 0보다 작다는 조건 추가
  else cout << ans;
   
  return 0;
}


vector<int> dijkstra(vector<vector<int>> &graph, int s){
  vector<int> dist(N+1, INF);
  priority_queue<pii, vector<pii>, greater<pii>> pq; // {cost, index}
  pq.push({0, s}); // C++ 11이상부터 가능

  dist[s] = 0;
  while(!pq.empty()){
    int current_idx = pq.top().second;
    int cost = pq.top().first;
    pq.pop();

    if(cost > dist[current_idx]) continue;

    for(int i = 1; i <= N; ++i){ // next_idx == i
      if(graph[current_idx][i] == 0) continue;
      int next_cost = cost + graph[current_idx][i];

      if(dist[i] > next_cost){
        dist[i] = next_cost;
        pq.push({next_cost, i});
      }
    }
  }
  return dist;
}