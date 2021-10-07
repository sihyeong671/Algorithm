// 두 용액

#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int N;
int main(){
  cin >> N;
  vector<long long> liquid(N);
  for(int i = 0; i < N; ++i){
    cin >> liquid[i];
  }
  sort(liquid.begin(), liquid.end());
  int p_1 = 0, p_2 = N-1;
  int sum_;
  while(p_1 < p_2){
    sum_ = p_1 + p_2;
    if(sum_ > 0) p_2 -= 1; 
    else if (sum_ < 0) p_1 += 1;
    else break;
  }
  if(p_1 > p_2){
    int tmp;
    tmp = p_2;
    p_2 = p_1;
    p_1 = tmp;
  }
  cout << liquid[p_1] << ' ' << liquid[p_2];
  return 0;
}