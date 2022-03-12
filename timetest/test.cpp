#include<iostream>
#include<vector>
using namespace std;

int main(){
	vector<vector<int>> v;
	v.reserve(vector<int>(10));
	v[3][3] = 3;

	cout << v[3][3];
	
}