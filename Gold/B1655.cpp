// 가운데를 말해요

#include<iostream>
#include<queue>
#include<vector>
#include<algorithm>

using namespace std;

priority_queue<int, vector<int>, greater<int>> pq_h;
priority_queue<int> pq_l;
int N, x;

int main(){
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  cin >> N;
  for(int i = 0; i < N; ++i){
    cin >> x;
    if(pq_l.empty()) pq_l.push(x);
    else if(x > pq_l.top()){
      pq_h.push(x);
    }
    else{
      pq_l.push(x);
    }
    // unsigned 끼리 빼면 unsigned 나옴 리턴이 음수면 에러
    if(pq_l.size() >= pq_h.size() + 2){
      pq_h.push(pq_l.top());
      pq_l.pop();
    }
    else if(pq_h.size() >= pq_l.size() + 1){
      pq_l.push(pq_h.top());
      pq_h.pop();
    }
    cout << pq_l.top() << '\n';
  }
}