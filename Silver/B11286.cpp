// 절댓값 힙

#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>

using namespace std;

int N, x;
vector<int> ans;
priority_queue<int, vector<int>, less<int>> pq_n;
priority_queue<int, vector<int>, greater<int>> pq_p;

int main(){

  cin >> N;

  for(int i = 0; i < N; ++i){
    cin >> x;
    if(x == 0){
      if(pq_n.empty() && pq_p.empty()){
        // cout << "0";
        ans.push_back(0);
      } 
      else if(pq_n.empty()){
        // cout << pq_p.top();
        ans.push_back(pq_p.top());
        pq_p.pop();
      } 
      else if(pq_p.empty()){
        // cout << pq_n.top();
        ans.push_back(pq_n.top());
        pq_n.pop();
      }
      else{
        if(abs(pq_n.top()) <= pq_p.top()){
          // cout << pq_n.top();
          ans.push_back(pq_n.top());
          pq_n.pop();
        }
        else{
          // cout << pq_p.top();
          ans.push_back(pq_p.top());
          pq_p.pop();
        }
      }
    }
    else{
      if(x < 0) pq_n.push(x);
      else pq_p.push(x);
    }
  }
  for(auto n: ans){
    cout << n << endl;
  }

  return 0;
}