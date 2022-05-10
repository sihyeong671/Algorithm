#include <iostream>
#include <vector>

using namespace std;

int N, S;

int find_S(int n, int _sum, vector<int> &arr);

int main(){
  cin >> N >> S;

  vector<int> num_arr(N);

  for(auto &num : num_arr){
    cin >> num;
  }

  if(S == 0) cout << find_S(0, 0, num_arr) -1;
  else cout << find_S(0, 0, num_arr);
}

int find_S(int n, int _sum, vector<int> &arr){
  
  if(n == N){
    if(_sum == S) return 1;
    else return 0;
  }

  // 포함 하는 경우 + 포함 하지 않는 경우
  return (find_S(n+1, _sum+arr[n], arr) + find_S(n+1, _sum, arr));
  
}