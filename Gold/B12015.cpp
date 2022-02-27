// 가장 긴 증가하는 부분 수열2

#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(){

  int N, tmp;
  vector<int> v, ans;

  cin >> N;
  for(int i = 0; i < N; ++i){
    cin >> tmp;
    v.push_back(tmp);
  }

  ans.push_back(v[0]);
  for(int i = 1; i < N; ++i){
    if(v[i] > ans.back()){
      ans.push_back(v[i]);
    }
    else{
      vector<int>::iterator low = lower_bound(ans.begin(), ans.end(), v[i]);
      *low = v[i];
    }
  }

  cout << ans.size();
}