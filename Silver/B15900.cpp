// 나무탈출

#include <iostream>
#include <vector>
#define For(i,a,b) for(int i = int(a); i < int(b); i++)
using namespace std;

vector<int> tree[500001];
bool visited[500001];
int cnt = 0;
int N;

void dfs(int node, int depth){
  if(node != 1 && tree[node].size() == 1){
    cnt += depth;
    return;
  }

  For(i, 0, tree[node].size()){
    if(!visited[tree[node][i]]){
      visited[node] = true;
      dfs(tree[node][i], depth+1);
      visited[node] = false;
    }
  }
}

int main(){
  ios_base::sync_with_stdio(false);
  cin >> N;
  int a, b;
  For(i, 0, N-1){
    cin >> a >> b;
    tree[a].push_back(b);
    tree[b].push_back(a);
  }

  visited[1] = true;
  dfs(1, 0);
  if(cnt % 2 == 0) cout << "No";
  else cout << "Yes";
  
}