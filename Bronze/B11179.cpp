#include <iostream>
#include <vector>
#include <cmath>
using namespace std;
int N, ans = 0;
vector <int> list;
int main(){
  cin >> N;
  while(N != 0){
    list.push_back(N % 2);
    N /= 2;
  }
  int idx = 0;
  while(!list.empty()){
    ans += (list.back()*pow(2, idx));
    list.pop_back();
    idx ++;
  }
  cout << ans;
}

// #include <iostream>
// using namespace std;

// int main() {
// 	ios::sync_with_stdio(0);
// 	cin.tie(0);

// 	int N; cin >> N;
// 	int ans = 0;
// 	while (N > 0) {
// 		ans <<= 1;
// 		if (N & 1) ans++;
// 		N >>= 1;
// 	}
// 	cout << ans;
// }