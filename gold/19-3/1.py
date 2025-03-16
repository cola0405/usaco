# python 没办法全过

import sys
from collections import defaultdict
sys.stdin = open('snakes.in', 'r')
sys.stdout = open('snakes.out', 'w')

n,k = map(int, input().split())
a = list(map(int, input().split()))
s = set(a)
dp = [[defaultdict(lambda: float('inf')) for j in range(k+1)] for i in range(n+1)]
min_val = [[float('inf') for j in range(k+1)] for i in range(n+1)]      # min_val[i][j] = min(dp[i+1][j])
min_val[0][0] = 0
for ai in s:
    if ai >= a[0]:
        dp[0][0][ai] = ai - a[0]

for i in range(1,n):
    for j in range(k+1):
        if j > i+1: continue
        for v in s:     # 可能大小的网一定在 ai之中
            if v >= a[i]:
                # 不变
                dp[i][j][v] = min(dp[i][j][v], dp[i-1][j][v] + (v - a[i]))
                # 变为 v
                if j > 0:
                    dp[i][j][v] = min(dp[i][j][v], min_val[i-1][j-1] + (v - a[i]))
                min_val[i][j] = min(min_val[i][j], dp[i][j][v])
print(min(min_val[n-1]))