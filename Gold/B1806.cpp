// 부분합

#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;
typedef long long ll;
int N, S;
ll _sum = 0;
int length = 1e5;
bool check = false;
int main(){

  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N >> S;
  vector<int> v(N);
  for(int i = 0; i < N; ++i){
    cin >> v[i];
  }
  
  int p1 = 0, p2 = 0;
  while(true){
    if(_sum < S){
      _sum += v[p2++];
    }
    else{
      check = true;
      length = min((p2-p1), length);
      _sum -= v[p1++];
    }

    if(p1 == N || (p2 == N && _sum < S)) break;

  }
  if(check) cout << length;
  else cout << "0";
}