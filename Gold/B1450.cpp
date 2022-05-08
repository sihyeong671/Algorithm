// 냅색문제

#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

typedef long long ll;

int N, C;
ll ans = 0;
vector<int> v1, v2;
void dfs(int s, int e, int sum_, vector<int> &list, vector<int> &v);

int main(){
  
  cin >> N >> C;
  vector<int> items(N);
  for(int i = 0; i < N; ++i){
    cin >> items[i];
  }
  
  dfs(0, N/2, 0, items, v1);
  dfs(N/2+1, N-1, 0, items, v2);
  sort(v2.begin(), v2.end());

  for(int i = 0; i < v1.size(); ++i){
    ans += upper_bound(v2.begin(), v2.end(), C-v1[i]) - v2.begin();
    //
  }
  
  cout << ans;
}

void dfs(int s, int e, int sum_, vector<int> &items, vector<int> &v){
  if(sum_ > C) return;
  if(s > e){
    v.push_back(sum_);
    return;
  } 

  dfs(s+1, e, sum_, items, v);
  dfs(s+1, e, sum_+items[s], items, v);

}
