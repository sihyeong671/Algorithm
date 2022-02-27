#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int N, C;
vector<int> v; // 공유기 배열

int main(){
  cin >> N >> C;
  int tmp;
  for(int i = 0; i < N; ++i){
    cin >> tmp;
    v.push_back(tmp);
  }
  sort(v.begin(), v.end(), less<int>());

  int left = 1;
  int right = v.back();

  int dist = 0;

  while(left <= right){
    int mid = (left + right) / 2;
    int current_router = 1;
    int pre_i = 0;

    for(int i = 1; i < N; ++i){
      if(v[i] - v[pre_i] >= mid){
        pre_i = i;
        current_router++;
      }
    }

    if(current_router >= C) {
      dist = max(dist, mid);
      left = mid + 1;
    }
    else  right = mid - 1;

  }
  cout<< dist;
}