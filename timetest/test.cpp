#include<iostream>
#include<vector>
using namespace std;

void test(int n, vector<vector<int>> v);

int main(){
	vector<vector<int>> v(10, vector<int>(10, 0));
	cout << "main : " << &v << endl;
	for(int i = 0; i < 10; ++i){
		cout << &v[i] << ' ';
	}
	cout << '\n';
	vector<vector<int>> v_copy(v);
	// v_copy = v;
	cout << &v_copy << endl;
	for(int i = 0; i < 10; ++i){
		cout << &v_copy[i] << ' ';
	}
	cout << '\n';
	// test(0, v);
}

void test(int n, vector<vector<int>> v){
	if(n == 2){
		return;
	}
	cout << "test " << n << ": " << &v << endl;
	for(int i = 0; i < 10; ++i){
		cout << &v[i] << ' ';
	}
	cout << '\n';
	test(n+1, v);
}