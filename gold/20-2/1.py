'''
topological sort

题目大意：
有 N个挤奶会，给出一些限制情况，b至少是在 a发生后的 x天
问每个挤奶会最早什么时候能进行

'''

import sys
from collections import defaultdict,deque

sys.stdin = open('timeline.in', 'r')
sys.stdout = open('timeline.out', 'w')

n,m,c = map(int,input().split())
S = [0] + list(map(int, input().split()))
ab = defaultdict(list)
pre = [0]*(n+1)     # 统计前置 session数量
for _ in range(c):
    a,b,x = map(int,input().split())
    ab[a].append((b,x))     # b需要在 a之后 x天
    pre[b] += 1

q = []
for i in range(1,n+1):
    if pre[i] == 0: q.append(i)

while q:
    a = q.pop()
    for b,x in ab[a]:
        pre[b] -= 1
        S[b] = max(S[b], S[a]+x)        # 这里就是在取满足所有限制条件的最早时间
        if pre[b] == 0: q.append(b)     # 前置要求为 0时加入队列

for t in S[1:]: print(t)



