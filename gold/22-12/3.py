'''
逆序并查集 + 拓扑排序

题目大意：
有 n个节点的无向图，块内互通的几头牛可以组成一个团体
团体有一个指标 = 团体内各节点的最小度 * 团体的节点数，题目要求这个指标的最大值
Ps：题目的测试用例中 {1,2,3,4} 团体的最小度为 3

思路：
因为 n的值大，我们不可能枚举所有子集
不难发现指标与度的关系比较密切，而且可能需要剔除并查集内的某些点
剔除哪些呢？很明显，度小的
到这就不难想到我们的删点处理了，然后我们进行逆向加点 + 并查集求解即可
接下来就应该解决下一个问题了 —— 如何确认删点的顺序呢？
注意！不是直接按照初始状态的度排序就行，因为删点之后，某些相关点的度会受到影响
所以，这里我们前半段先试用拓扑排序找到度数最小的删除序列

之后，我们从度数大的点开始加点，过程中维护块内最小度和块内节点数，然后更新 ans即可
Ps：块内最小度只可能出现在新加入进来的点（这点很重要！）
'''
from collections import defaultdict
import heapq

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

n,m = map(int, input().split())
g = defaultdict(list)
degree = [0]*(n+1)
pq = []
for _ in range(m):
    u,v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
    degree[u] += 1
    degree[v] += 1

# 正向拓扑排序确认节点删除顺序（每次找到度最小的节点开始删，过程中更新各节点度的情况）
for x in range(1,n+1):
    heapq.heappush(pq, (degree[x], x))
vis = [0]*(n+1)         # 记录节点是否被删除过
order = []              # 节点删除顺序
while pq:
    d, u = heapq.heappop(pq)
    if vis[u]: continue
    vis[u] = 1
    order.append(u)
    for v in g[u]:
        if vis[v]: continue
        degree[v] -= 1
        heapq.heappush(pq, (degree[v], v))

root = list(range(n+1))          # 并查集数组
node_cnt = [1]*(n+1)             # 统计各个块内节点的数量
d_cnt = [0]*(n+1)                # 统计各个节点的度
flag = [0]*(n+1)                 # 记录节点是否已被添加过
ans = 0
for u in order[::-1]:            # 先加度数大的点
    flag[u] = 1
    for v in g[u]:               # 虽然是两层循环，但是每条边只会访问 2次，时间复杂度仍为 O(m)
        if flag[v]:
            d_cnt[u] += 1
            d_cnt[v] += 1
            if find(u) != find(v):
                node_cnt[find(u)] += node_cnt[find(v)]
                root[find(v)] = find(u)
            ans = max(ans, min(d_cnt[u], d_cnt[v]) * node_cnt[find(u)])
print(ans)
