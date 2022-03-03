#include <iostream>
#include <array>

using namespace std;


typedef long long ll;
typedef array<array<ll, 2>,2> matrix;

const ll mod = 1000000007;
ll N;

matrix multiple(matrix &m_1, matrix &m_2){

  matrix temp;
  for(int r = 0; r < 2; ++r){
    for(int c = 0; c < 2; ++c){
      ll tmp = 0;
      for(int i = 0; i < 2; ++i){
        tmp += m_1[r][i]*m_2[i][c];
      }
      temp[r][c] = tmp%mod;
    }
  }
  
  return temp;
}


int main(){
  cin >> N;
  N -= 2;
  matrix mt = {{{1,1},{1,0}}};
  matrix ans = {{{1,1},{1,0}}};

  while(N > 0){
    if(N%2==1){ // 홀수
      ans = multiple(mt, ans);
    }
    mt = multiple(mt, mt);
    N /= 2;
  }
  cout << ans[0][0];
}
