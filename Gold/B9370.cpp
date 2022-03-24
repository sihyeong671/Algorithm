// 미확인 도착지

#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>

using namespace std;

typedef pair<int, int> pii; // next_node, cost

const int INF = 1e9;
int T, n, m, t;
int s, g, h;
int a, b, d;
int tmp;
vector<int> ans;

void solve();
vector<int> dijkstra(int s, vector<vector<pii>> &graph);



int main(){
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> T;

  for(int i = 0; i < T; ++i){
    solve();
  }
}

void solve(){
  cin >> n >> m >> t;
  cin >> s >> g >> h;
  vector<vector<pii>> graph(n+1); // {index, cost}
  
  for(int j = 0; j < m; ++j){
    cin >> a >> b >> d;
    if((a == g && b == h) || (a == h && b == g)) tmp = d;
    graph[a].push_back({b, d});
    graph[b].push_back({a, d});
  }
  // int destination;
  // for(int j = 0; j < t; ++j){
  //   cin >> destination;
  //   vector<int> start_s = dijkstra(s, graph);
  //   vector<int> start_d = dijkstra(destination, graph);
  //   int short_p = start_s[destination];
  //   int estimate_1 = start_s[g] + start_d[h] + tmp;
  //   int estimate_2 = start_s[h] + start_d[g] + tmp;
  //   if(short_p == min(estimate_1, estimate_2)){
  //     ans.push_back(destination);
  //   }
  // }
  vector<int> destinations(t);
  for(int j = 0; j < t; ++j){ 
    cin >> destinations[j];
  }

  vector<int> start_s = dijkstra(s, graph);
  vector<int> start_g = dijkstra(g, graph);
  vector<int> start_h = dijkstra(h, graph);

  for(auto dest: destinations){
    if(start_s[dest] == min(start_s[g]+start_h[dest] + tmp, start_s[h]+start_g[dest]+tmp)){
      ans.push_back(dest);
    }
  }

  sort(ans.begin(), ans.end(), less<>());
  for(auto answer : ans){
    cout << answer << ' ';
  }
  cout << '\n';
  ans.clear();
}

vector<int> dijkstra(int s, vector<vector<pii>> &graph){
  priority_queue<pii, vector<pii>, greater<pii>> pq; //{cost, index}
  vector<int> dist(n+1, INF);
  dist[s] = 0;
  pq.push({0, s});
  while(!pq.empty()){
    int c_idx = pq.top().second;
    int cost = pq.top().first;
    pq.pop();

    if(dist[c_idx] < cost) continue;

    for(auto next : graph[c_idx]){
      int n_idx = next.first;
      int n_cost = cost + next.second;

      if(dist[n_idx] > n_cost){
        dist[n_idx] = n_cost;
        pq.push({n_cost, n_idx});
      }
    }
  }
  return dist;
}