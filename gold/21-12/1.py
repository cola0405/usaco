t,n,k = map(int,input().split())
x = [0]*(n+1)
w = [0]*(n+1)
for i in range(1,n+1):
    a,b = map(int,input().split())
    x[i] = a
    w[i] = b

dp = [[0]*2 for _ in range(n+1)]        # dp[i][0/1] 表示到第 i个点，有未匹配的点 ——[1]，都已匹配 ——[0]，最小未配对的重量总和
l = 1
for i in range(1, n+1):
    while l > x and x[i] - x[l] > k:  # mark
        l += 1
    j = i&1                    # 到第 i个点，总共有 i个点，如果 i是奇数，则当前 dp肯定是选择存在未匹配点的[1]，否则[0]
    k = j^1
    dp[i][j] = dp[l][k] + w[i]    # 到第 i位总共有奇数个点时，当前 dp位选择不匹配，
    if x[i] - x[i-1] <= k:
        dp[i][1] = min(dp[i][1], dp[i-1][0])
    if i+1 <= n and x[i+1] - x[i] <= k:
        dp[i][1] = min(dp[i][1], dp[i-1][1])

