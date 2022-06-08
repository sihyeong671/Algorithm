// 감소하는 수

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;
typedef long long ll;

void dfs(ll num, int d);
bool check(ll num);
int N;
vector<bool> nums(10, false);
vector<ll> v;


int main(){
  cin >> N;

  dfs(0, 0);
  sort(v.begin(), v.end(), less<>());

  for(auto e : v){
    cout << e << ' ';
  }

  // if(N+2 > v.size()) cout << -1;
  // else cout << v[N];
}

void dfs(ll num, int d){
  
  if(d == 10){
    return;
  }

  if(num < 10){
    v.push_back(num);
  }

  for(int i = 0; i < 10; ++i){
    if(!nums[i]){
      nums[i] = true;
      int tmp = num*10 + i;
      if(check(tmp)){
        dfs(tmp, d+1);
      }
      nums[i] = false;
    }
  }
}

bool check(ll num){
  
  if(num < 10) return true;

  ll pre = num % 10;
  num /= 10;

  while(num != 0){
    ll current = num%10;
    if(pre >= current) return false;
    pre = current;
    num /= 10;
  }

  return true;
}