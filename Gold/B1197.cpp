// 최소 스패닝 트리
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int V, E;
int tree[10001];

struct Edge{
  int u,v,c;
  Edge(int u, int v, int c): u(u), v(v), c(c){}
  bool operator <(Edge &e){return c < e.c;}
};

int find(int n){
  if(tree[n] == -1) return n;
  return tree[n] = find(tree[n]); // 경로 압축
}

void _union(int x, int y){
  x = find(x);
  y = find(y);
  if(x != y) tree[y] = x;
}

int main(){
  cin >> V >> E;
  for(int i = 1; i <= V; ++i){
    tree[i] = i;
  }
  vector<Edge> v;
  int u_, v_, c_;
  for(int i = 0; i < E; ++i){
    cin >> u_ >> v_ >> c_;
    v.push_back(Edge(u_, v_, c_));
  }
  sort(v.begin(), v.end());
  int sum_ = 0;
  for(int i = 0; i < v.size(); ++i){
    if(find(v[i].u) != find(v[i].v)){
      _union(v[i].u, v[i].v);
      sum_ += v[i].c;
    }
  }

  cout << sum_;
}