//토마토

#include<iostream>
#include<queue>
#include<algorithm>
using namespace std;
typedef struct queue_data
{
  int r, c, day;
} qd;

int N, M, max_day;

int arr[1000][1000];
bool visited[1000][1000];
queue<qd> q;

int main(){
  ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
  
  cin >> M >> N;

  int nr[] = {-1, 1, 0, 0};
  int nc[] = {0, 0, -1, 1};

  qd tmp;
  for(int i = 0; i < N; ++i){
    for(int j = 0; j < M; ++j){
      cin >> arr[i][j];
      if(arr[i][j] == 1)  {
        tmp = {i, j, 0};
        q.push(tmp);
        visited[i][j] = true;
      }
    }
  }
  

  
  while(!q.empty()){
    int r = q.front().r;
    int c = q.front().c;
    int d = q.front().day;
    q.pop();
    for(int w = 0; w < 4; ++w){
      int dr = r + nr[w];
      int dc = c + nc[w];

      if(0 <= dr && dr < N && 0 <= dc && dc < M && arr[dr][dc] == 0 && !visited[dr][dc]){
        q.push({dr, dc, d+1});
        visited[dr][dc] = true;
        max_day = max(max_day, d + 1);
      }
    }
  }

  for(int i = 0; i < N; ++i){
    for(int j = 0; j < M; ++j){
      if(arr[i][j] == 0 && !visited[i][j]){
        cout << -1;
        return 0;
      }
    }
  }

  cout << max_day;
}