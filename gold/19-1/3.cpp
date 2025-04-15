// dijastra(添加一条边) + dfs

/*
题目大意：
有n个节点，每个节点有c头牛，这些牛会选择到节点1的最短路跑去
允许我们在任意节点和节点1之间添加一条捷径，问捷径最多能节约多少时间（Ps：1是终点）
注意事项:
1.如果最短路不止一种选择，要选择字典序最小的路径
2.牛不会绕路去走捷径，意思就是在添加捷径之前牛走的最短路是已经确定了的，牛只会走最短路上顺路可以走的捷径
3.Python的 dfs 会超递归层数

解题步骤：
1.先跑一遍 dijastra 把最短路径确认下来
2.沿着最短路径进行 dfs 统计各个节点会有多少头牛经过
3.每个捷径能够节约的时间 = 经过该节点的牛数 * (该节点到节点1的最短时间 - 走捷径所需时间T)
*/

#include <iostream>
#include <unordered_map>
#include <vector>
#include <queue>
#include <climits>
using namespace std;
typedef long long ll;


// 表示图的边
struct Edge {
    ll destination;
    ll weight;
};


// dfs 统计最短路中各个节点有多少牛经过（从终点开始dfs）
ll dfs(unordered_map<ll, vector<ll>>& dja_g, vector<ll>& passing_cow, vector<bool>& vis, ll x) {
    if (vis[x]) return passing_cow[x];
    vis[x] = true;
    for (auto& nxt : dja_g[x]) {
        if (!vis[nxt]) passing_cow[x] += dfs(dja_g, passing_cow, vis, nxt);
    }
    return passing_cow[x];
}


int main() {
    freopen("shortcut.in", "r", stdin);
    freopen("shortcut.out", "w", stdout);

    ll N, M, T;
    cin >> N >> M >> T;

    vector<ll> c(N + 1);
    for (ll i = 1; i <= N; ++i) {cin >> c[i];}

    unordered_map<ll, vector<Edge>> g;
    for (ll i = 0; i < M; ++i) {
        ll a, b, t;
        cin >> a >> b >> t;
        g[a].push_back({b, t});
        g[b].push_back({a, t});
    }

    vector<ll> min_time(N+1, LONG_MAX);
    vector<bool> vis(N+1, false);
    min_time[1] = 0;
    unordered_map<ll, vector<ll>> dja_g;
    priority_queue<pair<ll, pair<ll, ll>>> q;
    q.push({0, {-1, 1}});

    while (!q.empty()) {
        pair<ll, pair<ll, ll>> cur = q.top();
        q.pop();
        ll d = -cur.first;                  // 距离
        ll node = -cur.second.first;        
        ll last = -cur.second.second;

        if (vis[node]) continue;
        vis[node] = true;
        dja_g[last].push_back(node);        // 保存了从 1 到各个节点的最短路，而不仅是 1 到 N 的那条路

        for (const Edge& edge : g[node]) {
            ll nxt = edge.destination;
            ll t = edge.weight;
            if (!vis[nxt] && d+t <= min_time[nxt]) {        // 注意，题目有说多条路径所需时间相同的情况下，取字典序最小的路径，所以这题要取到等号
                min_time[nxt] = d+t;
                q.push({-min_time[nxt], {-nxt, -node}});    // 默认从大到小，要取最短时间且要保证选取最短路的字典序最小
            }
        }
    }

    vector<ll> passing_cow = c;
    vis.assign(N+1, false);
    dfs(dja_g, passing_cow, vis, 1);

    ll max_reduce = 0;
    for (ll i = 2; i <= N; ++i) {
        if (T < min_time[i]) {
            max_reduce = max(max_reduce, passing_cow[i] * (min_time[i] - T));
        }
    }

    cout << max_reduce << endl;
    return 0;
}