# union-find set (no recursion) + 各个连通块的大小 + sort optimization

'''
常规 bfs肯定超时
像这种连续传递的其实也可以用并查集来做
块的准入标准设置为相关性 >= k
那块内节点的数量就是在 k限制下可以被推荐的视频数量（这道题的合并还需要维护各个块的大小）

如果是每个询问都进行合并的话，还是会超时
所以这里我们可以借助排序做进一步的优化
从大到小处理 k —— 已经合并的节点肯定已经符合相关性的限制了
对边也从大到小排序 —— while 循环从左到右处理即可，不需要每次遍历所有边

Ps：python里面递归层数限制大概是1000 如果是递归形式的并查集的话有一个数据点会报错
故这里需要用到非递归的并查集
'''

import sys
from collections import defaultdict

def find(x):
    while x != root[x]:
        root[x] = root[root[x]]     # 每次 find 的时候，都会至少压缩一层路径
        x = root[x]
    return x

sys.stdin = open('mootube.in', 'r')
sys.stdout = open('mootube.out', 'w')

N,Q = map(int,input().split())
edges = [tuple(map(int, input().split())) for _ in range(N-1)]
q = [tuple(map(int, input().split())) + (i,) for i in range(Q)]
edges.sort(key=lambda x: x[2], reverse=True)
q.sort(reverse=True)

i = 0
root = list(range(N+1))
cnt = defaultdict(lambda: 1)        # 初始化每个块的大小为 1
ans = [0]*Q
for k,v,inx in q:
    while i < len(edges):
        x1,x2,r = edges[i]
        if r >= k:
            if root[find(x1)] != find(x2):
                cnt[find(x2)] += cnt[find(x1)]      # 先统计数量再做合并操作
                root[find(x1)] = find(x2)
            i += 1
        else: break
    ans[inx] = cnt[find(v)]-1       # 减去自身

for x in ans: print(x)



