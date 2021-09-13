// IBM빼기 1
#include <iostream>
#include <string>
using namespace std;

int n;
string com;
int main(){
  cin >> n;
  for(int i = 0; i < n; i++){
    cin >> com;
    cout << "String #" << i+1 << '\n';
    for(int j = 0; j < com.length(); j++){
      char temp = com[j];
      temp = (temp + 1);
      if(temp > 90) temp = 65;
      cout << temp;
    }
    cout << "\n\n";
  }
}