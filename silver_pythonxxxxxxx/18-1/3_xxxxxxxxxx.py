from collections import defaultdict, deque
import sys
sys.stdin = open('mootube.in', 'r')
sys.stdout = open('mootube.out', 'w')

n, q = map(int, input().split())
g = defaultdict(dict)
for _ in range(n-1):  # n-1 不会成环
    v1, v2, r = map(int, input().split())
    g[v1][v2] = r
    g[v2][v1] = r

for _ in range(q):
    k, v = map(int, input().split())
    res = 0
    q = deque([v])
    available = [1]*(n+1)
    while q:
        top = q.popleft()
        available[top] = 0
        for node in g[top]:
            if available[node] and g[top][node] >= k:
                q.append(node)
                res += 1
                available[top] = 0
    print(res)
