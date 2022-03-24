// 이분 그래프

#include<iostream>
#include<vector>

using namespace std;

int K, V, E;
bool state;
void dfs(int n, vector<int> &list, vector<vector<int>> &graph);

int main(){

  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  cin >> K;


  for(int i = 0; i < K; ++i){
    
    cin >> V >> E;
    vector<vector<int>> graph(V+1);
    vector<int> num(V+1, 0);
    int u, v;
    for(int j = 1; j <= E; ++j){
      cin >> u >> v;
      graph[u].push_back(v);
      graph[v].push_back(u);
    }
    state = false;
    for(int j = 1; j <= V; ++j){
      if(num[j] == 0) {
        num[j] = 1;
        dfs(j, num, graph);
      }
    }

    if(state) cout << "NO\n";
    else cout << "YES\n";

  }
}

void dfs(int n, vector<int> &list, vector<vector<int>> &graph){
  
  if(state) return;
  for(auto e : graph[n]){
    if(list[e] == list[n]){ // 같은 영역에 있는 경우
      state = true;
      return; 
    }
    else if(list[e] == 0){ // 아직 모르는 경우
      list[e] = list[n] * -1; 
      dfs(e, list, graph);
    } 
  }
}