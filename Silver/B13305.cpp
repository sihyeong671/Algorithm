//주유소
#include<iostream>
#include<vector>
#define For(i, a, b) for(int i = a; i < b; i++)
using namespace std;

int N, l;
long long d;
vector<int> oil;
vector<long long> dist;
int main(){
  cin >> N;
  For(i, 0, N-1){
    cin >> d;
    dist.push_back(d);
  }
  For(i, 0, N){
    cin >> l;
    oil.push_back(l);
  }
  
  int idx = 0, temp = oil[0];
  long long int total_oil=oil[0]*dist[0];
  For(i, 1, N-1){
    if(oil[i] < temp){
      idx = i;
      total_oil += (oil[idx]*dist[i]);
      temp = oil[i];
    }
    else{
      total_oil += oil[idx]*dist[i];
    }
  }
  cout << total_oil;
}