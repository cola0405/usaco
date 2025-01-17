# dijastra（必须经过某些节点）

'''
yummy值的解释：如果不去吃东西，pasture到 N 的最短路为 d1
绕路去吃草堆然后到 N的最短路为 d2
如果 d2 + yummy值 <= d1
那牛就认为划算，值得绕路，就输出 1 否则输出 0

从 N节点开始跑 dijastra可以轻易确定各草堆到 N节点的最短路
但比较棘手的点是草堆数量多，我们没办法枚举确定各个 pasture分别走哪个草堆合适

解决的办法 —— 新建特殊节点(N+1)
把所有草堆和 (N+1)节点连起来（Ps：权值不是设置成 0，要特殊处理，具体的之后解释）
然后我们从 (N+1)出发跑 dijastra可以确定各 pasture到任意草堆的最短路
这里可能有疑惑？
我们如何保证加上后半段 —— 草堆到 N的路径后，整条路径是最优的呢？

这就需要回去看新建边的权值设置了 —— 草堆到 N的距离 - yummy值
在这个前提下，从 (N+1)跑 dijastra 其实是各个 pasture到 N的最短距离

如果理解起来困难的话可以先抛开题目对于 yummy值的限制
把问题转变为 —— 牛必须经过指定的特殊草堆，然后求牛到 N节点的最短路
我们可以跑两次 dijastra来解决这个问题
第一次 dijastra先把各特殊草堆到 N节点的距离明确
然后，新建 (N+1)节点，连接各特殊草堆将权值设置为到各特殊草堆到 N的最短距离
然后从 (N+1)节点跑 dijastra，从而求得牛必须经过某些节点再到 N的最短路（因为已经把后半段的距离考虑进去了）
'''

from collections import defaultdict
import heapq
import sys

def dijastra(node):
    dis = [float('inf')]*(n+2)
    dis[node] = 0
    vis = [0]*(n+2)
    pq = [(0, node)]
    while pq:
        t, node = heapq.heappop(pq)
        vis[node] = 1
        for nxt, t1 in g[node]:
            if not vis[nxt] and t+t1 < dis[nxt]:
                dis[nxt] = t+t1
                heapq.heappush(pq, (t+t1, nxt))
    return dis

sys.stdin = open('dining.in', 'r')
sys.stdout = open('dining.out', 'w')

n,m,k = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    a,b,t = map(int, input().split())
    g[a].append((b,t))
    g[b].append((a,t))

yummy = defaultdict(int)
for _ in range(k):
    pi,y = map(int, input().split())
    yummy[pi] = y
dis1 = dijastra(n)      # N到各个pasture的最短距离 (包括特殊草堆)

# 新建一个节点 (n+1)连接所有草堆, 同时特殊处理一下这些新建边的权值
# 然后跑一遍 dijastra求得各个 pasture经过草堆到 barn的最短距离
for pi in yummy:
    g[n+1].append((pi,dis1[pi]-yummy[pi]))      # 边的权值是：草堆到N的距离 - yummy值
    g[pi].append((n+1,dis1[pi]-yummy[pi]))      # 在这个前提下跑 dijastra 即是各个 pasture到 N的最短距离
dis2 = dijastra(n+1)    # N+1到各个pasture的最短距离（各个pasture经过草堆到N的最短距离 —— 源于前面对于N+1的特殊处理）

for i in range(1,n):
    if dis2[i] <= dis1[i]: print(1)
    else: print(0)