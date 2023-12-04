# 优化重复遍历record
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

people = defaultdict(set)  # 统计每个牛奶的饮用者
count = defaultdict(set)
for p,m,t in record:
    people[m].add(p)
    if p in sick and t < sick[p]:  # 统计生病前喝过的牛奶
        count[m].add(p)

ans = 0
for milk in count:
    if len(count[milk]) == S:  # sick都喝过的milk
        ans = max(ans, len(people[milk]))

print(ans)