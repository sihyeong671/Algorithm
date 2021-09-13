// 캠핑
#include <iostream>
using namespace std;
int L, P, V;
int max_day, idx = 1;
int main(){
  int temp, ans;
  while(true){
    cin >> L >> P >> V;
    if(L == 0 && P == 0 && V == 0){
      break;
    }
    if((V % P) > L){
      temp = L;
    }
    else{
      temp = (V%P);
    }
    ans = (V / P) * L + temp;

    cout << "Case " << idx << ": " <<  ans << endl;
    idx ++;
  }
}