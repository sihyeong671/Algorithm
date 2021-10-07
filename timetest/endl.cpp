//endl vs '\n'

// endl은 버퍼를 비우고 \n은 비우지 않는다
// Flush : 버퍼 비우는 행위

#include<iostream>
#include<ctime>
#include<windows.h>
#define MAX 100000
using namespace std;


void PrintEndl(){
  for(int i = 0 ; i < MAX; ++i){
    cout << endl;
  }
}

void Printn(){
  for(int i = 0 ; i < MAX; ++i){
    cout << '\n';
  }
}

double TimeCheck(void (*fptr)()){
  clock_t start, end;
  double result;

  start = clock();

  fptr();

  end = clock();

  result = (double)(end - start);
  return result;
}


int main(){
  
  // cout << TimeCheck(Printn) << " ms";

  return 0;
}