//꿀 따기

#include<iostream>
#include<array>
#include<algorithm>
using namespace std;
int N;
array<int, 100001> v;
array<int, 100001> v_1;
array<int, 100002> v_2;

int main(){
  cin >> N;
  for(int i = 1; i <= N; ++i){
    cin >> v[i];
    v_1[i] = v_1[i-1] + v[i];
  }
  for(int i = N; i > 0; --i){
    v_2[i] = v_2[i+1] + v[i];
  }
  int ans = 0;

  for(int i = 2; i < N; ++i){
    ans = max(ans, v_1[N] - v_1[1] + v_1[N] - v_1[i] - v[i]);
    ans = max(ans, v_2[1] - v_2[N] + v_2[1] - v_2[i] - v[i]);
    ans = max(ans, v_1[i] - v_1[1] + v_2[i] - v_2[N]);
  }

  cout << ans;
  return 0;
}