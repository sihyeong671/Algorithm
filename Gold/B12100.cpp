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


  if(n == 5){
    for(int r = 0; r < N; ++r){
      for(int c = 0; c < N; ++c){
        ans = max(ans, board[r][c]);
        cout << board[r][c] << ' ';
      }
      cout << endl;
    }
    cout << endl;
    return;
  }

  bool move_l = false, move_r = false, move_u = false, move_d = false;

  // 좌
  vector<vector<int>> copy_board_l(board);

  for(int r = 0; r < N; ++r){
    int pre = copy_board_l[r][0];
    vector<int> tmp;
    for(int c = 1; c < N; ++c){
      if(copy_board_l[r][c] != 0){
        if(pre == copy_board_l[r][c]){
          move_l = true;
          tmp.push_back(pre<<1);
        }
        else{
          tmp.push_back(copy_board_l[r][c]);
        }
        pre = 0;
      }
    }
    if(tmp.size() == 0){
      tmp.push_back(copy_board_l[r][0]);
    }
    
    for(int i = 0; i < N; ++i){
      if(i >= tmp.size()){
        copy_board_l[r][i] = 0;
        continue;
      }
      copy_board_l[r][i] = tmp[i];
    }
  }

  dfs(n+1, copy_board_l);

  // 우
  vector<vector<int>> copy_board_r(board);

  for(int r = 0; r < N; ++r){
    int pre = copy_board_r[r][N-1];
    vector<int> tmp;
    for(int c = N-2; c >= 0; --c){
      if(copy_board_r[r][c] != 0){
        if(pre == copy_board_r[r][c]){
          move_r = true;
          tmp.push_back(pre<<1);
        }
        else{
          tmp.push_back(copy_board_r[r][c]);
        }
        pre = 0;
      }
    }

    if(tmp.size() == 0){
      tmp.push_back(copy_board_l[r][N-1]);
    }

    for(int i = 0; i < N; ++i){
      if(i >= tmp.size()){
        copy_board_r[r][N-i-1] = 0;
        continue;
      }
      copy_board_r[r][N-i-1] = tmp[i];
    }
  }

  dfs(n+1, copy_board_r);
  
  // 상
  vector<vector<int>> copy_board_u(board);
  for(int c = 0; c < N; ++c){
    int pre = copy_board_u[0][c];
    vector<int> tmp;
    for(int r = 1; r < N; ++r){
      if(board[r][c] != 0){
        if(pre == copy_board_u[r][c]){
          move_u = true;
          tmp.push_back(pre<<1);
        }
        else{
          tmp.push_back(copy_board_u[r][c]);
        }
        pre = 0;
      }
    }
    
    if(tmp.size() == 0){
      tmp.push_back(copy_board_l[0][c]);
    }

    for(int i = 0; i < N; ++i){
      if(i >= tmp.size()){
        copy_board_u[i][c] = 0;
        continue;
      }
      copy_board_u[i][c] = tmp[i];
    }
  }

  dfs(n+1, copy_board_u);

  // 하
  vector<vector<int>> copy_board_d(board);
  for(int c = 0; c < N; ++c){
    int pre = copy_board_d[0][c];
    vector<int> tmp;
    for(int r = N-1; r >= 0; --r){
      if(copy_board_d[r][c] != 0){
        if(pre == copy_board_d[r][c]){
          move_u = true;
          tmp.push_back(pre<<1);
        }
        else{
          tmp.push_back(copy_board_d[r][c]);
        }
        pre = 0;
      }
    }

    if(tmp.size() == 0){
      tmp.push_back(copy_board_l[N-1][c]);
    }

    for(int i = 0; i < N; ++i){
      if(i < tmp.size() - 1){
        copy_board_d[N-i-1][c] = 0;
        continue;
      }
      copy_board_d[N-i-1][c] = tmp[i];
    }
  }

  dfs(n+1, copy_board_d);
  
} 