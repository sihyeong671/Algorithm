//모든 순열
#include<iostream>
using namespace std;

int N;
int arr[8] = {0,};
bool visited[8] = {false,};

void dfs(int d){
  if(d == N){
    for(int i = 0; i < N; i++){
      cout << arr[i] << ' ';
    }
    cout << '\n';
    return;
  }

  for(int i = 0; i < N; i++){
    if(!visited[i]){
      visited[i] = true;
      arr[d] = i+1;
      dfs(d+1);
      visited[i] = false;
    }
  }
  
}

int main(){
  cin >> N;
  dfs(0);
  
}