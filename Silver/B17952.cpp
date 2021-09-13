// 과제는 끝나지 않아!
#include <iostream>
#include <vector>
using namespace std;
int N;
int W, A, T;
int ans=0;
int main(){
  vector<pair<int, int>> st;

  cin >> N;
  for(int i = 0;i < N; i++){
    cin >> W;
    if (W == 1){
      cin >> A >> T;
      st.push_back(make_pair(A, T));
    }
    if(!st.empty()){
      st.back().second -= 1;
      if (st.back().second == 0){
        ans += st.back().first;
        st.pop_back();
      }
    }
  }
  cout << ans;
}