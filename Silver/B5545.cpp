// 최고의 피자
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int N; // 토핑 종류
int A, B, C; // 도우의 가격, 토핑의 가격, 도우의 열량
vector<int> v;
int main(){
  cin >> N;
  cin >> A >> B;
  cin >> C;

  for(int i = 0; i < N; i++){
    int temp;
    cin >> temp;
    v.push_back(temp);
  }

  sort(v.begin(), v.end(), greater<int>());

  int cal = C;
  int price = A;
  int max_ = cal / price;
  for(int i = 0; i < N; i++){
    cal += v[i];
    price += B;
    max_ = max(max_, cal / price);
  }
  cout << max_;
}