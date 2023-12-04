# 不依赖于交集操作

from collections import defaultdict
import sys
sys.stdin = open('badmilk.in', 'r')
sys.stdout = open('badmilk.out', 'w')
N, M, D, S = map(int, input().split())

record = [tuple(map(int, input().split())) for _ in range(D)]

sick = dict()
for _ in range(S):
    p,t = map(int, input().split())
    sick[p] = t

count = defaultdict(set)
for p,m,t in record:
    if p in sick and t < sick[p]:   # 统计生病前喝过的牛奶
        count[m].add(p)

ans = 0
for milk in count:
    if len(count[milk]) == S:  # 生病的人都喝过的milk
        s = set()
        for p,m,t in record:
            if m == milk:
                s.add(p)
        ans = max(ans, len(s))

print(ans)