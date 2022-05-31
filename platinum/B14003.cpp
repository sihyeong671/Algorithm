// 가장 긴 증가하는 부분 수열 5

#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;
int N;

int main(){

  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N;

  vector<int> indexLIS(N);
  vector<int> v(N);
  vector<int> ans;

  for(auto &e: v){
    cin >> e;
  }
  
  indexLIS[0] = 0;
  ans.push_back(v[0]);
  for(int i = 1; i < N ; ++i){
    if(v[i] > ans.back()){
      indexLIS[i] = ans.size();
      ans.push_back(v[i]);
    }
    else{
      int idx = lower_bound(ans.begin(), ans.end(), v[i]) - ans.begin();
      indexLIS[i] = idx;
      ans[idx] = v[i];
    }
  }
  int p = ans.size() - 1;  
  vector<int> tmp;
  for(int i = N-1; i >= 0; --i){
    if(p < 0) break;
    if(indexLIS[i] == p){
      tmp.push_back(v[i]);
      p--;
    }
  }
  cout << ans.size() << '\n';
  for(int i = tmp.size() - 1; i >= 0; i--){
    cout << tmp[i] << ' ';
  }
}
