'''
Python 没办法全过

区间 dp
dp[i][j] 表示 [i,j] 的最少操作次数
经典枚举中间 k的做法 —— 这个在这里也能合并，因为枚举 k会把所有可能的连续区间都考虑到
'''

n = int(input())
a = list(map(int, input().split()))
dp = [[float('inf')]*n for _ in range(n)]

for i in range(n)[::-1]:
    dp[i][i] = 1
    for j in range(i+1, n):
        if a[i] == a[j]:            # j会枚举所有的区间，故两端一样的时候，直接转移，不用特意去找
            dp[i][j] = min(dp[i+1][j], dp[i][j-1])
        else:
            for k in range(i, n-1):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j])

print(dp[0][-1])