#include <iostream>
using namespace std;

int main(){
  int arr[5][4];

  int sum, max_ = 0;
  // max_는 0으로 초기화됨, sum은 그렇지 않다
  int num = 0;
  for(int i = 0; i < 5; i++){
    for(int j = 0; j < 4; j++){
      cin >> arr[i][j];
    }
  }
  for(int i = 0; i < 5; i++){
    sum = 0;
    for(int j = 0; j < 4 ; j++){
      sum += arr[i][j];
    }
    if(sum > max_){
      num = i + 1;
      max_ = sum;
    }
  }
  cout << num << ' ' << max_;
  return 0;
}