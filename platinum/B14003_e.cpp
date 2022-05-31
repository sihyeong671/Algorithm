#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;
typedef pair<int, int> pii;
int N;
int lowerbound(vector<pii>& lst, int val);

int main(){
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N;

  vector<int> before(N);
  vector<int> v(N);
  vector<pii> ans;
  for(auto &e: v){
    cin >> e;
  }

  ans.push_back({0, v[0]});
  before[0] = -1;
  for(int i = 1; i < N ;++i){
    if(v[i] > ans.back().second){
      before[i] = ans.back().first;
      ans.push_back({i, v[i]});
    }
    else{
      int idx = lowerbound(ans, v[i]);
      if(idx == 0){
        before[i] = -1;
        ans[idx] = {i, v[i]};
      }
      else{
        before[i] = ans[idx-1].first;
        ans[idx] = {i, v[i]};
      }
    }
  }

  int p = ans.back().first;  
  vector<int> tmp;
  while(p != -1){
    tmp.push_back(v[p]);
    p = before[p];
  }
  cout << ans.size() << endl;
  for(int i = tmp.size() - 1; i >= 0; i--){
    cout << tmp[i] << ' ';
  }

}

int lowerbound(vector<pii> &lst, int val){
  int p1 = 0, p2 = lst.size()-1;
  while(p1 <= p2){
    int mid = (p2 + p1) / 2;
    if(lst[mid].second < val){
      p1 = mid + 1;
    }
    else{
      p2 = mid - 1;
    }
  }
  return p1;
}