//스타트와 링크

#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>

using namespace std;

int N, _min = 20000;
int arr[20][20] = {0};
vector<bool> visited(20, false);

void Input(){
  cin >> N;
  for(int i = 0; i < N; ++i){
    for(int j = 0; j < N; ++j){
      cin >> arr[i][j];
    }
  }
}

void dfs(int n){

  if(count(visited.begin(), visited.begin()+N, true) == N/2){

    int _sum1 = 0;
    int _sum2 = 0;
    for(int i = 0; i < N; ++i){
      if(visited[i]){
        for(int j = 0; j < N; ++j){
          if(visited[j]) _sum1 += arr[i][j];
        }
      }
      else{
        for(int j = 0; j < N; ++j){
          if(!visited[j]) _sum2 += arr[i][j];
        }
      }
    }
    _min = min(abs(_sum1 - _sum2), _min);
    return;
  }
  if(n == N) return;

  for(int i = n; i < N; ++i){
    visited[i] = true;
    dfs(i+1);
    visited[i] = false;
  }
}


int main(){

  Input();
  dfs(0);
  cout << _min;
  return 0;
}