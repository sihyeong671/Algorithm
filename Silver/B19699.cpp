//소-난다!
#include<iostream>
#include<algorithm>
#include<vector>
#include<cmath>
#define For(n, a, b) for(int n = a; n < b; n++)
using namespace std;

int N, M;
int arr[9] = {0,};
bool visited[9] = {false,};
int num = 9001;
int primeNum[9001];
vector<int> prime, ans, lst;

bool IsPrime(int n){ // 숫자 커질 경우 이분탐색
  For(i, 0, prime.size()){
    if(n == prime[i]) return true;
  }
  return false;
}

void dfs(int d, int l){
  if(d == M){
    
    int sum_ = 0;
    For(i, 0, d){
      sum_ += lst[i];
    }
    if(IsPrime(sum_)) ans.push_back(sum_);
    return;
  }
  For(i, l, N){
    if(!visited[i]){
      lst.push_back(arr[i]);
      visited[i] = true;
      dfs(d+1, i);
      lst.pop_back();
      visited[i] = false;
    }
    
  }
}

int main(){
  cin >> N >> M;

  For(i, 2, num){
    primeNum[i] = i;
  }
  For(i, 2, sqrt(num)+1){
    if(primeNum[i] == 0) continue;
    For(j, i*i, num){
      if(primeNum[j]%i == 0) primeNum[j] = 0;
    }
  }
  For(i, 2, num){
    if(primeNum[i] != 0)  prime.push_back(i);
  }

  For(i, 0, N){
    cin >> arr[i];
  }

  dfs(0, 0);

  sort(ans.begin(), ans.end());
  ans.erase(unique(ans.begin(), ans.end()), ans.end());
  if(ans.size() == 0) cout << -1;
  else{
    For(i, 0, ans.size()){
      cout << ans[i] << ' ';
    }
  }
}