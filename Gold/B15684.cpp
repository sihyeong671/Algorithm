#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef pair<int, int> pii;
int N, M, H;
int ans = 4;

void dfs(int n, vector<vector<int>> &v, pii pos);
bool check(int n, vector<vector<int>> &v);

int main(){

  cin >> N >> M >> H;
  
  vector<vector<int>> v(H, vector<int>(N, 0));

  int a, b;
  for(int i = 0; i < M; i++){
    cin >> a >> b;
    v[a-1][b-1] = 1;
  }

  if(!check(0, v)){
    for(int i = 0; i < H; i++){
      for(int j = 0; j < N-1; j++){
        if(v[i][j] == 0){
          if((v[i][j-1] == 0 && v[i][j+1] == 0) ||
                  (j == N-2 && v[i][j-1] == 1) ||
                  (j == 0 && v[i][j+1] == 1)){
            v[i][j] = 1;
            dfs(1, v, {i, j});
            v[i][j] = 0;
          }
        }
      }
    }
  }

  if(ans >= 4) cout << -1;
  else cout << ans;
}

void dfs(int n, vector<vector<int>> &v, pii pos){

  if(n >= ans) return;

  if(check(n, v)) return;

  for(int i = pos.first; i < H; i++){
    for(int j = pos.second; j < N-1; j++){
      if(v[i][j] == 0){
        if((j >= 1 && v[i][j-1] != 1) && (j <= N-1 && v[i][j+1] != 1)){
          v[i][j] = 1;
          dfs(n+1, v, {i, j});
          v[i][j] = 0;
        }
      }
    }
  }
}

bool check(int n, vector<vector<int>> &v){
  cout << "check\n";
  bool check = true;
  for(int i = 0; i < N; i++){
    int idx = i;
    for(int j = 0; j < H; j++){

      // 우
      if(idx == 0 && v[j][idx] == 1){
        idx++;
      }
      else if(1 <= idx && idx < N-1 && v[j][idx] == 1){
        idx++;
      }
      // 좌
      else if(idx == N-1 && v[j][idx-1] == 1){
        idx--;
      }
      else if(1 <= idx && idx < N-1 && v[j][idx-1] == 1){
        idx--;
      }
    }

    if(idx != i){
      check = false;
    }
  }

  if(check) ans = min(ans, n);
  return check;
}