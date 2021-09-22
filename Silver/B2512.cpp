//예산
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int N, M;
int sum_, max_ = 0;
int p_s, p_e, mid;
vector<int> money;

int main(){
  cin >> N;
  for(int i = 0; i < N; ++i){
    int tmp;
    cin >> tmp;
    money.push_back(tmp);
    max_ = max(max_, tmp);
  }
  cin >> M;

  p_s = 0;
  p_e = max_;
  
  while(p_s <= p_e){
    sum_ = 0;
    mid = (p_s+p_e)/2;

    for(int i = 0; i < N; ++i){
      sum_ += min(money[i], mid);  
    }

    if(sum_ > M) p_e = mid-1;
    else{
      p_s = mid+1;
    } 
  }

  cout << p_e; 

  return 0;
}

