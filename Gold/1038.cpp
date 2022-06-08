// 감소하는 수
#include <iostream>
#include <vector>

typedef long long ll;
using namespace std;

int N;

int cnt = 0;
ll num = 1;

int main(){

  cin >> N;

  if(N == 0){
    cout << 0;
    return 0;
  }

  while(num < 9876543210){
    bool flag = true;
    ll tmp = num;
    int pre;
    int cur = tmp % 10;
    tmp /= 10;
    while(tmp != 0){
      pre = cur;
      cur = tmp % 10;
      if(pre >= cur){
        flag = false;
        break;
      }
      tmp /= 10;
    }

    if(flag) cnt++;
    
    if(cnt == N){
      cout << num;
      return 0;
    }
    num++;
  }

  cout << -1;
}