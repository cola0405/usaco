# Python 过不了

import sys

def find(x):
    while x != root[x]:
        root[x] = root[root[x]]     # 每次 find 的时候，都会至少压缩一层路径
        x = root[x]
    return x

sys.stdin = open('fencedin.in', 'r')
sys.stdout = open('fencedin.out', 'w')

A,B,n,m = map(int, input().split())
ver = [int(input()) for _ in range(n)]
hor = [int(input()) for _ in range(m)]
ver.sort()
hor.sort()

root = list(range((n+1)*(m+1)))
q = []   # (边长, 区域 1编号, 区域 2编号)
# 处理竖线 —— 连接左右格子
last = 0
for j in range(m):
    q.append((hor[j]-last, j, 0))
    last = hor[j]
q.append((B-last, m, 0))

# 处理横线 —— 连接上下格子
last = 0
for i in range(n):
    q.append((ver[i]-last, i, 1))
    last = ver[i]
q.append((A-last, n, 1))
q.sort()

ans = 0
for k in range(len(q)):
    d, i, t = q[k]
    if t == 0 and n > 0:
        for j in range(n):
            if find(i*(n+1) + j) != find(i*(n+1)+j + 1):
                root[find(i*(n+1) + j)] = find(i*(n+1) + j + 1)
                ans += d
    elif t == 1 and m > 0:
        for j in range(m):
            if find(j*(n+1) + i) != find((j+1)*(n+1) + i):
                root[find(j*(n+1) + i)] = find((j+1)*(n+1) + i)
                ans += d
print(ans)
