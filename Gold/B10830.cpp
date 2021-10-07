//행렬 제곱

#include<iostream>
#include<vector>
using namespace std;
int N;
long long B;
typedef vector<vector<long long>> matrix;
matrix m, m_, res(5, vector<long long>(5, 0));

matrix multiple(matrix m1, matrix m2){
  matrix new_m(5, vector<long long>(5,0));
  for(int r = 0; r < N; ++r){
    for(int c = 0; c < N; ++c){
      long long sum_ = 0;
      for(int k = 0; k < N; ++k){
        sum_ += m1[r][k]*m2[k][c];
      }
      new_m[r][c] = sum_%1000;
    }
  }
  return new_m;
}

void recursive(long long n){
  if(n==2){
    m = multiple(m, m);
    return;
  }
  else if(n==3){
    m = multiple(multiple(m, m), m_);
    return;
  }

  if(n%2 == 0){
    recursive(n/2);
    m = multiple(m, m);
  }
  else{
    recursive(n/2);
    m = multiple(multiple(m, m), m_);
  }
}

int main(){
  cin >> N >> B;
  for(int i = 0; i < N; ++i){
    vector<long long> tmp(N);
    for(int j = 0; j < N; ++j){
      cin >> tmp[j];
      tmp[j] %= 1000;
    }
    res[i][i] = 1;
    m.push_back(tmp);
    m_.push_back(tmp);
  }

  // recursive(B);

  while(B){
    if(B%2 == 1){
      res = multiple(res, m);
    }
    m = multiple(m, m);
    B /= 2;
  }

  for(int r = 0; r < N; ++r){
    for(int c = 0; c < N; ++c){
      cout << res[r][c] << ' ';
    }
    cout << '\n';
  }
  return 0;
}