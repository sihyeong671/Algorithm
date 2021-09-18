//예산
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int N, M, sum_ = 0;
vector<int> money;
int main(){
  cin >> N;
  for(int i = 0; i < N; ++i){
    int tmp;
    cin >> tmp;
    money.push_back(tmp);
  }
  cin >> M;
  sort(money.begin(), money.end());
  for(auto &n : money){
    sum_ += n;
  }
  if(sum_ < M){
    cout << money.back();
    return 0;
  }  

  for(int i = 0; i < money.size(); ++i){
    if(M/(money.size()-i) < money[i]){
      cout << M/(money.size()-i);
      break;
    }
    M -= money[i];
  }
}

