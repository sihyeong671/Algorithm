#include<iostream>
#include<queue>
using namespace std;
priority_queue<int, vector<int>, greater<int>> pq;
int N;
int main(){
  ios_base :: sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  cin >> N;
  for(int i = 0; i < N; ++i){
    int tmp;
    cin >> tmp;
    switch (tmp){
      case 0:
        if(pq.size()){
          cout << pq.top() << '\n';
          pq.pop();
        }
        else{
          cout << 0 << '\n';
        }
        break;

      default:
        pq.push(tmp);
        break;
    }
  }
}