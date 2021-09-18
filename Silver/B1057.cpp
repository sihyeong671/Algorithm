//토너먼트
#include<iostream>
#include<cmath>
using namespace std;

int N, a ,b , r = 0;
int main(){
  cin >> N >> a >> b;
  while(true){
    if(pow(2, r) >= N) break;
    r++;
  }
  int s; // 기준
  while(true){
    s = pow(2, r);
    if((a <= s && b > s)||(a > s && b <= s)){
      cout << r+1;
      break;
    }
    else if(a <= s && b <= s) r--;
    else if(a > s && b > s){
      a -= s;
      b -= s;
      r --;
    }
  }
}