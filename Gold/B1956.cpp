// 운동

#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>


using namespace std;

typedef pair<int, int> pii;

int V, E, a, b, c;

int main(){
  cin >> V >> E;
  vector<vector<pii>> graph(V+1);

  for(int i = 0; i < E; ++i){
    cin >> a >> b >> c;
    graph[a].push_back({b, c});
  }
}