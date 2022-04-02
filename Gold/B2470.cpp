// 두 용액

#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

typedef pair<int, int> pii;

int N;
pii ans;

int main(){
  cin >> N;
  
  vector<int> v(N);
  for(int i = 0; i < N; ++i){
    cin >> v[i];
  }

  sort(v.begin(), v.end());

  int p1 = 0, p2 = N-1;
  int acidity = v[p1] + v[p2];

  ans = {v[p1], v[p2]};
  while(p2 > p1){

    int c_acidity = v[p1] + v[p2]; 
    pii tmp = {v[p1], v[p2]};

    if(c_acidity > 0){ // 산도가 0보다 큰 경우
      --p2;
    }
    else if(c_acidity < 0){ // 산도 0보다 작은 경우
      ++p1;
    }
    else{
      ans = tmp;
      break;
    }

    if(abs(acidity) > abs(c_acidity)){
      ans = tmp;
      acidity = c_acidity;
    }
  }

  cout << ans.first << ' ' << ans.second;

}