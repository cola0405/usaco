/*
path dp

题目大意：所有牛有自己的编号，从第一个H牛出发，求访问完所有奶牛，且最后停在最后一个H奶牛的最小距离。
对于一个某个位置的H牛，有2种转移方式：
1. 从上一个H奶牛转移过来
2. 从某个G奶牛转移过来
dp[i][j][k]: 访问了i个H奶牛和j个G奶牛，当前停留在类型k奶牛的最小总距离
*/

#include <iostream>
#include <fstream>
#include <vector>
#include <climits>
#include <algorithm>
typedef long long ll;

using namespace std;
// 计算两点间距离的平方
ll dist(const pair<int,int>& a, const pair<int,int>& b) {
    return 1LL * (a.first - b.first) * (a.first - b.first) + 
           1LL * (a.second - b.second) * (a.second - b.second);
};

int main() {
    freopen("checklist.in", "r", stdin);
    freopen("checklist.out", "w", stdout);

    int H, G;
    cin >> H >> G;

    vector<pair<int, int>> h(H+1);
    vector<pair<int, int>> g(G+1);

    for (int i = 1; i <= H; ++i) {
        cin >> h[i].first >> h[i].second;
    }
    for (int i = 1; i <= G; ++i) {
        cin >> g[i].first >> g[i].second;
    }

    // 预处理所有可能的距离
    vector<vector<ll>> hh(H+1, vector<ll>(H+1));
    vector<vector<ll>> gg(G+1, vector<ll>(G+1));
    vector<vector<ll>> hg(H+1, vector<ll>(G+1));

    for(int i = 1; i <= H; i++)
        for(int j = 1; j <= H; j++)
            hh[i][j] = dist(h[i], h[j]);
    
    for(int i = 1; i <= G; i++)
        for(int j = 1; j <= G; j++)
            gg[i][j] = dist(g[i], g[j]);
    
    for(int i = 1; i <= H; i++)
        for(int j = 1; j <= G; j++)
            hg[i][j] = dist(h[i], g[j]);

    int n = H + G;
    // dp[i][j][k]: 访问了i个H奶牛和j个G奶牛，当前停留在类型k奶牛的最小总距离
    // k=0表示当前在H奶牛，k=1表示当前在G奶牛
    vector<vector<vector<ll>>> dp(H + 1, vector<vector<ll>>(G + 1, vector<ll>(2, INT_MAX)));

    // 初始状态
    dp[0][0][0] = 0;
    dp[1][0][0] = 0;

    for (int i = 1; i <= H; ++i) {
        for (int j = 0; j <= G; ++j) {
            // 当前在H奶牛，有两种可能的转移：
            // 1. 从上一个H奶牛转移过来
            if (i-1 >= 1) dp[i][j][0] = dp[i-1][j][0] + hh[i][i-1];
            // 2. 从当前位置的G奶牛转移过来
            if (j >= 1) dp[i][j][0] = min(dp[i][j][0], dp[i-1][j][1] + hg[i][j]);

            // 当前在G奶牛，同样有两种可能的转移：
            // 1. 从上一个G奶牛转移过来
            if (j-1 >= 1) dp[i][j][1] = dp[i][j-1][1] + gg[j][j-1];
            // 2. 从当前位置的H奶牛转移过来
            if (j >= 1) dp[i][j][1] = min(dp[i][j][1], dp[i][j-1][0] + hg[i][j]);
        }
    }

    // 输出访问完所有奶牛，且最后停在H奶牛的最小距离
    cout << dp[H][G][0] << endl;
    return 0;
}