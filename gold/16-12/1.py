# kruskal + union-find set

import heapq
import sys
sys.stdin = open('moocast.in', 'r')
sys.stdout = open('moocast.out', 'w')

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
edges = []
root = list(range(n))
for i in range(n):
    for j in range(i+1, n):
        x1, y1 = points[i]
        x2, y2 = points[j]
        dist = (x1-x2)**2 + (y1-y2)**2
        heapq.heappush(edges, (dist, i, j))

ans = 0
while edges:
    dist, i, j = heapq.heappop(edges)
    if root[find(i)] != find(j):        # 并查集判断是否成环
        root[find(i)] = find(j)
        ans = max(ans, dist)
print(ans)



