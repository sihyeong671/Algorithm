// 이장님 초대
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
int N, t;
vector<int> tree;
int main(){
  cin >> N;
  for(int i = 0; i < N; i++){
    cin >> t;
    tree.push_back(t); 
  }
  sort(tree.begin(), tree.end(), greater<>());

  int temp, ans = 0;
  for(int i = 0; i < tree.size(); i++){
    temp = tree[i] + (i+2);
    ans = max(ans, temp);
  }
  cout << ans;
}