'''
2序列匹配问题

题目大意：给定两个序列 A 和 B要求找出最多的匹配对 (i,j)
限制 1：线条之间不相交
限制 2：匹配的两点之间的 |a-b| <= 4

不难想到 dp[i][j] 表示 a走到 i，b走到 j 的最多匹配数
对于 a[i] 我们不确定它会和 b中的那一个匹配，那就需要都枚举一遍
然后第二个问题，状态如何转移？
1.连线时，为了避免相交，我们只能从dp[i-1][j-1]来
2.不连线时，有两种状态 max(dp[i-1][j], dp[i][j-1])
'''

import sys
sys.stdin = open('nocross.in', 'r')
sys.stdout = open('nocross.out', 'w')

n = int(input())
a = [' '] + [int(input()) for _ in range(n)]
b = [' '] + [int(input()) for _ in range(n)]

dp = [[0]*(n+1) for _ in range(n+1)]        # dp[i][j] 表示 a走到 i，b走到 j 的最多匹配数

for i in range(1,n+1):
    for j in range(1,n+1):      # 对于 a[i], 我们会把 b中所有的 b[j] 都考虑一遍，然后不断维护 dp数组
        if abs(a[i] - b[j]) <= 4:
            dp[i][j] = dp[i-1][j-1] + 1     # 每次只会从 [i-1][j-1] 处转移过来，避免了线条相交
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])      # 不画线

print(dp[n][n])