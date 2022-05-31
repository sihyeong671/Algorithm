// 감소하는 수

#include<iostream>
#include<string>

using namespace std;

int N;

int main(){
  cin >> N;
  int n = 0;
  int num = 0;
  while(n <= N && num <= 1000000){
    if(n < 10){
      n++;
      num++;
      continue;
    }
    int length = to_string(num).size();
    int pre;
    for(int i = 0; i < length; i++){
       
    }
  }
}