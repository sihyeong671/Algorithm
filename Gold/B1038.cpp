// 감소하는 수

#include <iostream>
#include <string>

using namespace std;
typedef long long ll;

int check(ll n);
int N;
int cnt = -1;
bool flag = false;

int main(){

  cin >> N;

  ll num = 0;
  while(num <= 9876543210){
    cnt += check(num);
    if(cnt == N){
      flag = true;
      break;
    }
    num++;
  }

  if(flag) cout << num;
  else cout << -1;
}


int check(ll n){

  if(n < 10){
    return 1;
  }

  int pre, current;

  pre = n%10;
  n /= 10;
  while(n != 0){
    current = n % 10;
    n /= 10;
    if(current <= pre){
      return 0;
    }
    pre = current;
  }
  return 1;

}