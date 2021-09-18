//차이를 최대로
#include<iostream>
#include<algorithm>
using namespace std;
int N, tmp, max_ = 0;
int arr[8] = {0,};
int lst[8] = {0,};
bool visited[8] ={false,};

void dfs(int d){
  if(d == N){
    int sum_ = 0;
    for(int i = 0; i < N-1; i++){
      sum_ += abs(lst[i]-lst[i+1]);
    }
    max_ = max(sum_, max_);
  }

  for(int i = 0; i < N; i++){
    if(!visited[i]){
      visited[i] = true;
      lst[d] = arr[i]; 
      dfs(d+1);
      visited[i] = false;
    }
  }
}

int main(){
  cin >> N;
  for(int i = 0; i < N; i++){
    cin >> tmp;
    arr[i] = tmp;
  }
  dfs(0);
  cout << max_;
}