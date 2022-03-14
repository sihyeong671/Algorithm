// 이분 그래프

#include<iostream>
#include<vector>

using namespace std;

int K, V, E;

int main(){
  cin >> K;

  for(int i = 0; i < K; ++i){
    cin >> V >> E;
    int u, v;
    vector<vector<int>> graph(V);
    vector<bool> check(V, false);
    for(int j = 0; j < E; ++j){
      cin >> u >> v;
      graph[u].push_back(v);
      graph[v].push_back(u);
    }

    
  }
  
}