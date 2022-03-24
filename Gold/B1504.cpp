//특정한 최단 경로

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

typedef struct{
  int v;
  int cost;
  bool v1_find;
  bool v2_find;
}info;

struct compare{
  bool operator()(info &a, info &b){
    return a.cost > b.cost;
  }
};

int N, E, v1, v2;

int main(){

  cin >> N >> E;

  vector<vector<int>> graph(N+1, vector<int>(N+1, -1));
  priority_queue<info, vector<info>, compare> q;
  int a, b ,c;

  for(int i = 0; i < N; ++i){
    cin >> a >> b >> c;
    graph[a][b] = c;
    graph[b][a] = c;
  }
  
  cin >> v1 >> v2;


  return 0;
}