// //스도쿠

#include<iostream>
#include<vector>
using namespace std;

typedef pair<int, int> pii;
int arr[9][9];
vector<pii> cord; // 0인 좌표
bool check = false;


bool Check(pii c){
  int area_r = 3*(c.first / 3);
  int area_c = 3*(c.second / 3);

  for(int i = 0; i < 9; ++i){
    if(arr[c.first][i] == arr[c.first][c.second] && i != c.second)
      return false;
    if(arr[i][c.second] == arr[c.first][c.second] && i != c.first)
      return false;
  }

  for(int i = area_r; i < area_r + 3; ++i){
    for(int j = area_c; j < area_c + 3; ++j){
      if(arr[c.first][c.second] == arr[i][j] && (i != c.first && j != c.second))
        return false;
    }
  }
  return true;
}

void Solve(int n){
  if(n == cord.size()){
    for(int i = 0; i < 9; ++i){
      for(int j = 0; j < 9; ++j){
        cout << arr[i][j] << ' ';
      }
      cout << '\n';
    }
    check = true;
    return;
  }

  for(int i = 1; i < 10; ++i){
    arr[cord[n].first][cord[n].second] = i;
    if(Check(cord[n])){
      Solve(n+1);
    }
    if(check) return;
  }
  arr[cord[n].first][cord[n].second] = 0;
  return;
}

int main(){
  for(int i = 0; i < 9; ++i){
    for(int j = 0; j < 9; ++j){
      cin >> arr[i][j];
      if(arr[i][j]==0){
        cord.push_back(make_pair(i, j));
      }
    }
  }
  Solve(0);
  return 0;
}