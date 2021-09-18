//양치기 꿍
#include<iostream>
#include<queue>
#include<string>
#define MAX 250
using namespace std;
int R, C, Total_Sheep=0, Total_Wolf=0;
char arr[MAX][MAX];
bool visited[MAX][MAX];

int dr[] = {-1, 1, 0, 0};
int dc[] = {0, 0, -1, 1};

void Input(){
  cin >> R >> C;
  for(int i=0; i<R; i++){
    string s;
    cin >> s;
    for(int j=0; j<C; j++){
      arr[i][j] = s[j];
    }
  }
}

void BFS(){
  for(int r=0; r<R; r++){
    for(int c=0; c<C; c++){
      if (arr[r][c] == '#' || visited[r][c]) continue;

      int sheep = 0, wolf = 0;
      queue<pair<int, int>> q;
      q.push({r, c});
      visited[r][c] = true;

      if(arr[r][c] == 'v') wolf += 1;
      else if (arr[r][c] == 'k') sheep += 1;

      while(!q.empty()){
        int _r = q.front().first;
        int _c = q.front().second;
        q.pop();

        for(int i=0; i<4; i++){
          int nr = _r + dr[i];
          int nc = _c + dc[i];

          if(0<=nr && nr<R && 0<=nc && nc<C && arr[nr][nc] != '#' && !visited[nr][nc]){
            if(arr[nr][nc] == 'v') wolf += 1;
            else if (arr[nr][nc] == 'k') sheep += 1;
            visited[nr][nc] = true;
            q.push({nr, nc});
          }
        }
      }
      if (sheep > wolf) Total_Sheep += sheep;
      else Total_Wolf += wolf;
    }
  }
  cout << Total_Sheep << ' ' << Total_Wolf;
}

int main(){
  ios_base::sync_with_stdio(0);
  Input();
  BFS();
}