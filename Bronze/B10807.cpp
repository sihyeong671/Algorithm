#include <iostream>
using namespace std;

// 미리 배열의 길이를 정해둠

int arr[100] = {0};

int main(){
  int N, cnt = 0, v;
  cin >> N;
  for(int i = 0; i < N; i ++){
    cin >> arr[i];
  }
  cin >> v;
  for(int i = 0; i < N; i ++){
    if(arr[i] == v){
      cnt += 1;
    }
  }
  cout << cnt;

  return 0;
}