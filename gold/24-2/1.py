'''
c++
dijastra 跑多源最短路

题目大意：有 n个节点，前 c个节点是汽车出发点，汽车可以选择任一出发点出发，最远行驶距离为 r
对于目标节点，如果至少有 k个出发点可达，那么他就是 well-connected
题目要求总共有哪些节点是 well-connected

思路：把出发点都放入优先队列中跑多源的 dijastra
每个节点在被访问时，记录其是从哪个出发点过来的，并且同时对距离做判断，如果已经超出可达范围 r，那就不再搜索
然后这道题还考察一个优化，因为 k的值很小，所以我们可以进行一个剪枝
如果某个节点 x已经有 k个可达充电站，那就没必要再去考虑更多的可达充电站 ****
如此一来可以把时间复杂度降低到 O(kmlogn)

'''

from collections import defaultdict
import heapq
n,m,c,r,k = map(int,input().split())
g = defaultdict(lambda: defaultdict(int))
for i in range(m):
    u,v,l = map(int,input().split())
    g[u][v] = l
    g[v][u] = l

pq = []
s = [set() for i in range(n+1)]     # 记录有多少个充电站可达
# 初始化优先队列时，把充电站都放入优先队列 (多源最短路，不能设置 vis，每个节点都可能被多次访问的)
for cs in range(1,c+1):                  # 前 c个是充电站
    heapq.heappush(pq, (0, cs, cs))      # (当前最短距离, 当前节点，出发的充电站)

while pq:
    dis, x, cs = heapq.heappop(pq)
    if cs in s[x] or len(s[x]) == k or dis > r: continue      # 这个剪枝可以把时间复杂度降低到 O(kmlogn)
    s[x].add(cs)
    for nxt in g[x]:
        if len(s[nxt]) < k:
            heapq.heappush(pq, (dis+g[x][nxt], nxt, cs))

ans = []
for i in range(c+1,n+1):
    if len(s[i]) >= k:
        ans.append(i)
print(len(ans))
for i in ans: print(i)
