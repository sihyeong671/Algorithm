//ROT13
#include<iostream>
#include<string>
using namespace std;

string words;

int main(){
  getline(cin, words);
  for(int i = 0; i < words.length(); i++){
    char temp = words[i];

    if(temp>=65 && temp<=90){
      temp += 13;
      if (temp > 90) temp -= 26;
      cout << temp;
    }
    else if(temp>=97 && temp<=122){
      if(temp > 114) temp -= 26;
      temp += 13;
      if (temp > 122) temp -= 26;
      cout << temp;   
    }
    else cout << words[i];
  }

}