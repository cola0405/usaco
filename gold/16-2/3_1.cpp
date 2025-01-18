// kruskal + 数据压缩

/*
题目大意：nxm 个线段把矩形区域分成 (n+1)*(m+1) 份
我们可以移除线段使得相邻两区域连通，问若要使得所有区域连通，移除线段的最少代价是多少

这道题其实是一个二维网格的最小生成树问题
难的地方在于如何把二维网格构建成树的结构
如果给每一格子都编号作为一个节点，那么这道题内存、时间都会爆掉，需要进行优化

优化策略：kruskal 其实就是找当前的最短边
二维网格有其特殊性，一横过去或一竖下去，都是长度相等的边
故我们可以不用把每条边都进行存储，可以压缩成一份进行存储

Ps：虽然若干线段可以压缩在一起，但是并不意味着移除线段时，是直接把一横(或一竖)所有的线段都移除
里面的每一对相邻区域我们还是要用并查集进行额外的连通性判断

*/

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <fstream>
using namespace std;
typedef long long ll;


// 查找根节点
int find(vector<int>& root, int x) {
    if(x != root[x]) root[x] = find(root, root[x]);
    return root[x];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    freopen("fencedin.in", "r", stdin);
    freopen("fencedin.out", "w", stdout);

    int A, B, n, m;
    cin >> A >> B >> n >> m;
    vector<int> ver(n), hor(m);
    for (int i = 0; i < n; ++i) cin >> ver[i];
    for (int i = 0; i < m; ++i) cin >> hor[i];
    sort(ver.begin(), ver.end());
    sort(hor.begin(), hor.end());

    vector<int> root((n+1) * (m+1));
    for (int i=0; i<(n+2) * (m+1); ++i) root[i] = i;
    
    vector<vector<int>> q;          // (边长, 行/列, 类型)，1 —— 竖边，0 —— 横边

    // 处理竖边 —— 连接左右的格子
    int last = 0;
    for (int j=0; j<m; ++j) {
        q.push_back({hor[j] - last, j, 1});
        last = hor[j];
    }
    q.push_back({B - last, m, 1});  // 最后一节需要特殊处理一下

    // 处理横边 —— 连接上下格子
    last = 0;
    for (int i=0; i<n; ++i) {
        q.push_back({ver[i] - last, i, 0});
        last = ver[i];
    }
    q.push_back({A - last, n, 0});
    sort(q.begin(), q.end());

    ll ans = 0;
    for(int k=0; k<q.size(); ++k){
        int d=q[k][0], i=q[k][1], type=q[k][2];
        if(type==1 && n>0){                      // 连接左右
            for(int j = 0; j < n; ++j){  // 这里不能只笼统判断前两个，每对都得判断一下并查集的关系
                if(find(root, i*(n+1) + j) != find(root, i*(n+1)+j + 1)){
                    root[find(root, i*(n+1) + j)] = find(root, i*(n+1)+j + 1);
                    ans += d;
                }
            }
        }
        else if(m>0){                          // 连接上下
            for(int j=0; j<m; ++j){
                if(find(root, i + j*(n+1)) != find(root, i + (j+1)*(n+1))){
                    root[find(root, i + j*(n+1))] = find(root, i + (j+1)*(n+1));
                    ans += d;
                }
            }
        }
    }
    cout << ans << endl;
    return 0;
}