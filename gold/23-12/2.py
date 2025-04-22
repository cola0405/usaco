'''
拓扑排序 + dp

题目大意：
DAG 求从各个节点出发的最长路径（要求：当有多条最长路径时，选择 label序列字典序最小的）

思路：
最长路径可以在反向图中进行拓扑排序一层一层求得（额外用一个 depth数组记录即可，就是对应的最长路径长度）
比较麻烦的是去找到字典序最小的路径，这里的字典序不是按照节点来排，而是按照边的 label
我们不可能去记下每条最长路径，那怎么办呢？

能否利用 dp帮忙记录？
节点 i面临了多条路，该选哪条呢？
如果有其中一条路径开头的边权小，那么就直接选它
如果都一样就接着看下一条边......
关键点就在这！我们是否可以记录下之后的情况，或者是否有什么指标可以衡量后续的情况呢？
算法给每条边都创建了一个量叫做 rank（综合了边权、label字典序的一个量）
如果路径开头的边权有更小的就选更小的边，如果没有那就选择 rank更高 (小)的边

以下我们讨论 rank的合理性：
我们在反图中进行拓扑排序的过程中分层维护 rank
对于某一层的所有节点，我们对他们进行排序，依据：(边权，后续路径的 rank)
对于同层的边，边权小的路径的 rank自然高，如果边权一致，那就取决于后续的 rank（即后一条边的rank）
rank这个量是不断累计的，所以可代表后续路径的情况

综上：大概思路就是在拓扑排序的过程中逐层对路径进行 dp和 rank排名
dp 用于记录后续路径的 label_sum，以求得总的 label_sum
rank 用于选取合适的路径
'''


from collections import defaultdict, deque
import heapq

n,m = map(int,input().split())
g = defaultdict(list)
r = defaultdict(list)       # 反图
in_degree = [0]*(n+1)      # 入度（对反向图而言）
for i in range(m):
    u,v,l = map(int,input().split())
    g[u].append((v,l))
    r[v].append((u,l))
    in_degree[u] += 1

rank = [0]*(n+1)        # 每个节点的排名（排名综合考虑边权和字典序），rank越小表示路径越优
depth = [0]*(n+1)       # 各个点的深度（后面需要逐层处理这些节点）
q = deque()             # 拓扑排序队列，只保存节点即可
pq = []                 # 优先队列，在多条路径中选取最优的路径

for i in range(1,n+1):
    if in_degree[i] == 0:       # 从反图入度为 0的点开始进行拓扑排序（Ps：图可能分为多个块）
        q.append(i)
        depth[i] = 0

cur_depth = 0
cnt = 0                                 # rank 计数器每次 +1
label_sum = [0]*(n+1)                   # 求某个节点最长路径的 label_sum
min_label = [float('inf')]*(n+1)        # 记录节点 i邻接边的最小 label值
min_rank = [float('inf')]*(n+1)         # 记录节点 i当前可达的最小 rank值
while q:
    u = q.popleft()
    if depth[u] == cur_depth+1:         # 到下一层了，开始 pq并且统计上一层节点的 rank
        cur_depth += 1
        while pq:
            x = heapq.heappop(pq)[2]
            rank[x] = cnt
            cnt += 1

    if depth[u] == cur_depth:       # 之前层的状态已经都更新完了，那新一层的节点就都可以开始统计了
        for v, l in g[u]:
            if depth[v] != depth[u]-1: continue     # 拓扑排序 + 层数可以确保
            if l < min_label[u]:
                min_label[u] = l
                label_sum[u] = label_sum[v]+l       # 状态转移
                min_rank[u] = rank[v]               # 更换路径的话，min_rank也需要更新
            elif l == min_label[u] and rank[v] < min_rank[u]:       # 边权相等的情况下，我们选后续字典序小的（rank小的）
                min_rank[u] = rank[v]
                label_sum[u] = label_sum[v]+l

    for v, l in r[u]:                               # 维护拓扑排序
        in_degree[v] -= 1
        if in_degree[v] == 0:
            q.append(v)
            depth[v] = depth[u]+1
        if depth[v] == cur_depth+1:
            heapq.heappush(pq, (l, rank[u], v))     # 收集下一层的节点 —— （正向 v到 u的 label值，v后续节点的 rank[u]，当前节点）

for i in range(1,n+1):
    print(depth[i], label_sum[i])