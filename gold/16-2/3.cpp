// kruskal + 数据压缩

/*
题目大意：nxm 个线段把矩形区域分成 (n+1)*(m+1) 份
我们可以移除线段使得相邻两区域连通，问若要使得所有区域连通，移除线段的最少代价是多少

这道题其实是一个二维网格的最小生成树问题
难的地方在于如何把二维网格构建成树的结构
如果给每一格子都编号作为一个节点，那么这道题内存、时间都会爆掉，需要进行优化
这份代码就是后面几个测试用例过不了

优化策略：详见3_1.cpp

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

    vector<int> ver(n);
    for (int i = 0; i < n; ++i) {
        cin >> ver[i];
    }
    vector<int> hor(m);
    for (int i = 0; i < m; ++i) {
        cin >> hor[i];
    }
    // 对垂直和水平的围栏长度进行排序
    sort(ver.begin(), ver.end());
    sort(hor.begin(), hor.end());

    vector<int> root((n + 2) * (m + 2));
    for (int i = 0; i < (n + 2) * (m + 2); ++i) {
        root[i] = i;
    }
    // 存储边的优先队列，存储三元组 (边长, 区域 1 编号, 区域 2 编号)
    vector<vector<int>> q;
    // 处理水平边
    for (int i = 0; i < n; ++i) {
        int last = 0;
        for (int j = 0; j < m; ++j) {
            q.push_back({hor[j] - last, j * (n + 1) + i, (j * (n + 1) + i) + 1});
            last = hor[j];
        }
        q.push_back({B - last, m * (n + 1) + i, (m * (n + 1) + i) + 1});
    }
    // 处理垂直边
    for (int j = 0; j < m; ++j) {
        int last = 0;
        for (int i = 0; i < n; ++i) {
            q.push_back({ver[i] - last, j * (n + 1) + i, (j + 1) * (n + 1) + i});
            last = ver[i];
        }
        q.push_back({A - last, j * (n + 1) + n, (j + 1) * (n + 1) + n});
    }
    sort(q.begin(), q.end());
    ll ans = 0;
    for(int k=0; k < q.size(); ++k){
        vector<int> edge = q[k];
        int d = edge[0];
        int i = edge[1];
        int j = edge[2];
        if (find(root, i) != find(root, j)) {
            root[find(root, i)] = find(root, j);
            ans += d;
        }
    }
    cout << ans << endl;
    return 0;
}