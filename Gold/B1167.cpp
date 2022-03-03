#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

struct node
{
    int num;
    vector<pair<int,int>> child;
};

int n, ans=0;
node d[100001];

int f(int n, int parent)
{
    int max=0 , sec=0;
    for(auto k : d[n].child)
    {
        if(k.first==parent)continue;

        int temp;
        temp= k.second + f(k.first, n);
        if(temp > max)
        {
            sec=max;
            max=temp;
        }
        else if(temp > sec) sec=temp;

    }
    if(ans<sec+max) ans=sec+max;
    return max;
}
int main()
{
    int sp=1;
    cin >> n;
    for(int i=0; i<n; i++)
    {
        int num,count=0;
        cin >> num;
        for(;;)
        {
            int a, b;
            cin >> a;
            if(a==-1)
            {
                break;
            }
            count++;
            cin >> b;
            d[num].child.push_back(make_pair(a,b));
        }
        if(count>=2) sp=num;
    }
    f(sp,0);
    cout << ans;
    return 0;
}