#include<iostream>
#include<ctime>

using namespace std;

int main(){
  // ios::sync_with_stdio(false);
  // cin.tie(NULL);
  // cout.tie(NULL);
  clock_t start, end;
  double result;
  const int N = 100000;
  start = clock();
  for(int i = 0; i < N; ++i){
    cout << "hi" << '\n';
  }
  end = clock();
  result = (double)(end - start);
  cout << result;
}