// 타임머신

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

const ll INF = 1e9; 
int N, M, A, B, C;
bool flag = false;


int main(){
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N >> M;
  vector<vector<pii>> graph(N+1);
  vector<ll> dist(N+1, INF); // 최악의 경우 음의 값 생각해야 돼서 long long 타입

  for(int i = 0; i < M; ++i){
    cin >> A >> B >> C;
    graph[A].push_back({B, C});
  }

  dist[1] = 0;
  for(int i = 1; i <= N; ++i){
    for(int j = 1; j <= N; ++j){
      for(auto &e: graph[j]){
        int next = e.first;
        int cost = e.second;
        if(dist[j] != INF && dist[next] > dist[j] + cost){ // long long + int 하면 int 자동으로 형 확장
          dist[next] = dist[j] + cost;
          if(i == N) flag = true; // 최악이라도 N-1일 때 최선의 경우 탐색하는데 한번 더 탐색하면 음의 간선 사이클 있는 경우다
        }
      }
    }
  }

  if(flag){
    cout << "-1";
  }
  else{
    for(int i = 2; i <= N; ++i){
      if(dist[i] == INF) cout << "-1\n";
      else cout << dist[i] << '\n';
    }
  }
}
