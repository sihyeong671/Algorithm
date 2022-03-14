// 이분 그래프

#include<iostream>
#include<vector>

using namespace std;

int K, V, E;
bool state;
void dfs(int past, int current, vector<bool> &list, vector<vector<int>> &graph);

int main(){
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> K;

  for(int i = 0; i < K; ++i){
    cin >> V >> E;

    int u, v;
    vector<vector<int>> graph(V+1);
    vector<bool> check(V+1, false);
    state = false;
    for(int j = 1; j <= E; ++j){
      cin >> u >> v;
      graph[u].push_back(v);
      graph[v].push_back(u);
    }
    
    for(int j = 1; j <= V; ++j){
      if(!check[j]) dfs(0, j, check, graph);
    }

    if(state) cout << "NO\n";
    else cout << "YES\n";
  }
}

void dfs(int past, int current, vector<bool> &list, vector<vector<int>> &graph){
  if(state) return;

  if(list[current]){
    state = true;
    return;
  }

  list[current] = true;
  cout << "graph : " << graph[current].size() << endl;
  for(auto n : graph[current]){
    if(n == past) continue;
    dfs(current, n, list, graph);
  }
}