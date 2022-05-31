// 가르침

#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>

using namespace std;

int N, K, _max=0;
vector<bool> used(26, false);
vector<string> str_arr(50);
void dfs(int n, int alpha);
int check(string str);

int main(){
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  
  cin >> N >> K;

  used[0] = true; // a
  used[13] = true; // n
  used[19] = true; // t
  used[8] = true; // i
  used[2] = true; // c

  for(int i = 0; i < N; ++i){
    cin >> str_arr[i];
  }

  if(K < 5){
    cout << 0;
    return 0;
  }

  dfs(K-5, 0);

  cout << _max;
}

void dfs(int n, int alpha){

  if(n == 0){
    int cnt = 0;
    for(int i = 0; i < N; ++i){
      cnt += check(str_arr[i]);
    }
    _max = max(_max, cnt);
    return;
  }

  for(int i = alpha; i < 26; ++i){
    if(!used[i]){
      used[i] = true;
      dfs(n-1, i);
      used[i] = false;
    }
  }
}

int check(string str){

  if(str.length() == 8){
    return 1;
  }

  for(int i = 4; i < str.length() - 4; ++i){
    int idx = str.at(i) - 97;
    if(!used[idx]){
      return 0;
    }
  }
  return 1;
}
