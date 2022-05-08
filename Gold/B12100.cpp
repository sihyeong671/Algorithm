#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, ans = 0;
void dfs(int n, vector<vector<int>> board);

int main(){
  
  cin >> N;
  vector<vector<int>> board(N, vector<int>(N));
  for(int i = 0; i < N; ++i){
    for(int j = 0; j < N; ++j){
      cin >> board[i][j];
    }
  }
  dfs(0, board);
  cout << ans;
}

void dfs(int n, vector<vector<int>> board){

  if(n == N){
    for(int r = 0; r < N; ++r){
      for(int c = 0; c < N; ++c){
        ans = max(ans, board[r][c]);
      }
    }
    return;
  }

  bool move_l = false, move_r = false, move_u = false, move_d = false;

  // 좌
  for(int r = 0; r < N; ++r){
    int pre = board[r][0];
    vector<int> tmp;
    for(int c = 1; c < N; ++c){
      if(board[r][c] != 0){
        if(pre == board[r][c]){
          move_l = true;
          tmp.push_back(pre<<1);
        }
        else{
          tmp.push_back(pre);
        }
        pre = board[r][c];

        if(c == N-1) tmp.push_back(pre); // 마지막 값 넣기
      }
    }

    for(int i = 0; i < N; ++i){
      if(i >= tmp.size()){
        board[r][i] = 0;
        continue;
      }
      board[r][i] = tmp[i];
    }
  }

  if(move_l) dfs(n+1, board);
  

  // 상하 합칠게 있는지 검사
  for(int c = 0; c < N; ++c){
    int pre = board[0][c];
    for(int r = 1; r < N; ++r){
      if(board[r][c] != 0){
        if(pre == board[r][c]){
          move_ud = true;
        }
        pre = board[r][c];
      }
    }
  }

  if(move_ud){
    // 상

    // 하
  }
  
}