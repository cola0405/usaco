# union-find set（连通块的数量） + 逆序加点

'''
题目大意：每次删除一个节点，让我们判断每次删除之后图是否保持全连接状态
关于连通性的题目，考虑到并查集
但是节点删除，对于并查集的更新并不容易，所以对问题进行转化：
题目讲到的按顺序删除节点，其实可以看做是逆序加节点 —— 那测试用例看下就懂了
那问题就变成了 —— 每次添加一个节点，判断连通块的数量是否为 1
'''

from collections import defaultdict
import sys

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

sys.stdin = open('closing.in', 'r')
sys.stdout = open('closing.out', 'w')

n,m = map(int,input().split())
g = defaultdict(list)
for _ in range(m):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

root = [i for i in range(n+1)]
order = [int(input()) for _ in range(n)][::-1]   # 逆序插入
valid = [0] * (n+1)
ans = []
cnt = 0
for i in range(n):
    x = order[i]
    valid[x] = 1
    cnt += 1
    for nxt in g[x]:
        if valid[nxt] and root[find(nxt)] != find(x):
            root[find(nxt)] = find(x)
            cnt -= 1            # 记录块的数量，每次发生合并操作时，块的数量 -1
    if cnt == 1: ans.append('YES')
    else: ans.append('NO')
ans[0] = 'YES'
for x in ans[::-1]: print(x)