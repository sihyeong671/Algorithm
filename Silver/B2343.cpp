//기타 레슨
#include <iostream>
#include <vector>
#include<array>
using namespace std;

typedef long long ll;

//타입 맞춰줘야 함
ll N, M;
ll s=0, e=0, m;

int main(){
  cin >> N >> M;
  vector<ll> v(N);
  for(int i = 0; i < N; ++i){
    cin >> v[i];
    e += v[i];
    s = max(s, v[i]);
  }

  while(s <= e){
    m = (s+e)/2;
    int cnt = 0;
    ll tmp = 0;
    for(int i = 0; i < N; ++i){
      tmp += v[i];
      if(tmp > m){
        tmp = v[i];
        cnt++;
      }
    }
    if(tmp != 0) cnt++;

    if(cnt <= M) e = m-1; 
    else s = m+1;
  }
  cout << s;
}