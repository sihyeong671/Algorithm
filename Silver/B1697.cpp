//숨바꼭질

#include<iostream>
#include<vector>
#include<queue>

using namespace std;

typedef pair<int, int> pii;

int N, K, time=0;
queue<pii> q;
vector<bool> v(100001, false);

int main(){
  cin >> N >> K;

  q.push(make_pair(N, 0));
  while(!q.empty()){
    
    pii pos = q.front();
    v[pos.first] = true;
    q.pop();
    if(pos.first == K){
      cout << pos.second;
      break;
    }

    if(pos.first+1 <= 100000 && !v[pos.first+1]) q.push(make_pair(pos.first+1, pos.second+1));
    if(pos.first-1 >= 0 && !v[pos.first-1]) q.push(make_pair(pos.first-1, pos.second+1));
    if(2*pos.first <= 100000 && !v[2*pos.first]) q.push(make_pair(2*pos.first, pos.second+1));
  }

}