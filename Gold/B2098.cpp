// 외판원 순회 (TSP)

#include<iostream>
#include<vector>

using namespace std;

int TSP(int current, int visited, vector<vector<int>> &W, vector<vector<int>> &D);
int N, ans;
const int INF = 1e9;

int main(){

  cin >> N;
  vector<vector<int>> W(N, vector<int>(N));
  vector<vector<int>> D(N, vector<int>(1<<N, 0));

  for(int i = 0; i < N; ++i){
    for(int j = 0; j < N; ++j){
      cin >> W[i][j];
    }
  }

  cout << TSP(0, 1, W, D);

}

int TSP(int current, int visited, vector<vector<int>> &W, vector<vector<int>> &D){

  int dist = D[current][visited];

  if(dist != 0) return dist; // 이미 최솟값 구한 경우

  if(visited == (1<<N)-1){ // 모든 도시 다 방문 했을 경우
    if(W[current][0] == 0) return INF; // 다시 시작점으로 돌아올 수 없는 경우
    else return W[current][0]; // 순회 가능한 경우
  }

  dist = INF;
  for(int i = 0; i < N; ++i){
    if(W[current][i] == 0 || (visited & (1 << i))) continue; // 길없거나, 재방문인 경우
    dist = min(dist, W[current][i]+TSP(i, (visited|1<<i), W, D));
  }

  D[current][visited] = dist;
  return dist;
}