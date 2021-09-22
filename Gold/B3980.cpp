//선발명단
#include<iostream>
using namespace std;
int T, ans;
int arr[11][11] = {0,};
bool visited[11] = {false,}; 

void dfs(int d, int s){
  if (d == 11){
    ans = max(ans, s); 
    return;
  } 

  for(int j = 0; j < 11; ++j){
    if(!visited[j] && arr[d][j] != 0){
      visited[j] = true;
      dfs(d+1, s+arr[d][j]);
      visited[j] = false;
    }
  }
}

int main(){
  cin >> T;
  for(int k = 0; k < T; ++k){
    ans = 0;
    for(auto &n : visited)
      n = false;
    for(int i = 0; i < 11; ++i){
      for(int j = 0; j < 11; ++j){
        cin >> arr[i][j];
      }
    }
    dfs(0, 0);
    cout << ans << '\n';
  }
  return 0;
}