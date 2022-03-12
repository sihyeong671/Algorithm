//양팔저울

#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

void put(int w, int n);
int num, check_num, w;
bool check;
vector<int> v(31, 0);
vector<vector<bool>> dp(31, vector<bool>(40001, false));

int main(){

  cin >> num;
  for(int i = 0; i < num; ++i){
    cin >> v[i];
  }

  cin >> check_num;
  for(int i = 0; i < check_num; ++i){
    cin >> w;
    check = false;
    put(0, 0);
    if(dp[num][w]) cout << "Y ";
    else cout << "N ";
  }

  return 0;
}

void put(int w, int n){
  if(n > num|| dp[n][w]) return;
  dp[n][w] = true;

  put(w, n+1);
  put(w+v[n], n+1);
  put(abs(w-v[n]), n+1);

}

