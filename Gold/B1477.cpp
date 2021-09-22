//휴게소 세우기
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int N, M, L;
vector<int> v, l;
int s = 0, e, m;
int main(){

  cin >> N >> M >> L;
  for(int i = 0; i < N; ++i){
    int tmp;
    cin >> tmp;
    v.push_back(tmp);
  }
  l.push_back(v[1]-0);
  for(int i = 1; i < v.size(); ++i){
    l.push_back(v[i] - v[i-1]);
  }
  l.push_back(L-v.back());

  e = L;
  while(s<=e){
    m = (s+e)/2;
    int sum_ = 0;
    for(int i = 0; i < l.size(); ++i){
      int n = 2;
      while(true){
        if(ceil((float)l[i]/n) >= m){
          sum_+= n;
          break;
        }
        n++;
      }
    }
    if(sum_ <= M) e = m - 1;
    else s = m + 1;
  }
  cout << m;
  return 0;
}