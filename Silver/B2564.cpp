//경비원
#include <iostream>
#include <vector>
using namespace std;

typedef struct cord{
  int w;
  int h;
} CORD;

int W, H, N, ans=0;
int main(){
  cin >> W >> H;
  cin >> N;
  vector<CORD> v(N+1);
  for(auto &n : v){
    int tmp_s, tmp_d;
    cin >> tmp_s >> tmp_d;
    switch(tmp_s){
      case 1:
        n.w = tmp_d;
        n.h = H;
        break;
      case 2:
        n.w = tmp_d;
        n.h = 0;
        break;
      case 3:
        n.w = 0;
        n.h = H-tmp_d;
        break;
      case 4:
        n.w = W;
        n.h = H-tmp_d;
        break; 
    }
  }
  CORD pos = v.back();
  for(int i = 0; i < v.size()-1; ++i){
    if(abs(pos.w - v[i].w) == W){
      ans += min(W+v[i].h+pos.h, W+H-v[i].h+H-pos.h);
    }
    else if(abs(pos.h - v[i].h) == H){
      ans += min(H+v[i].w+pos.w,H+W-v[i].w+W-pos.w);
    }
    else{
      ans += (abs(pos.w - v[i].w) + abs(pos.h-v[i].h));
    }
  }
  cout << ans;
}