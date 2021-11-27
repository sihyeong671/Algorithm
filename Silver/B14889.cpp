//스타트와 링크

#include<iostream>

using namespace std;

int N;
int arr[20][20] = {0};
bool visited[20] = {false};




int main(){
  cin >> N;
  for(int i = 0; i < N; ++i){
    for(int j = 0; j < N; ++j){
      cin >> arr[i][j];
    }
  }


  return 0;
}