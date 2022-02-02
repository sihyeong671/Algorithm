#include <iostream>
using namespace std;
typedef long long ll;
const ll P = 1000000007;

ll div2(ll a, ll b){
  if(b == 0) return 1;

  ll tmp = div2(a, b/2);
  if(b%2){ // 홀수
    return (((tmp*tmp)%P)*a)%P;
  }
  else{ // 짝수
    return (tmp*tmp)%P;
  }

}

int main(){
  int N, K;
  cin >> N >> K;
  
  ll t_1 = 1;
  ll t_2 = 1;

  for(int i = K + 1; i <= N; ++i){ // 분자
    t_1 = (t_1*i)%P;
  }
  for(int i = 1; i <= N-K; ++i){ // 분모
    t_2 = (t_2*i)%P;
  }
  cout << (t_1 * div2(t_2, P-2)) % P;
}