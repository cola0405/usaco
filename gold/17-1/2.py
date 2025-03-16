# c++ 代码才可行
import sys
sys.stdin = open('hps.in', 'r')
sys.stdout = open('hps.out', 'w')

n,k = map(int, input().split())
g = [input() for _ in range(n)]
g.insert(0, '')
gesture = ['P', 'H', 'S']
score = {('P', 'S'): 0, ('P', 'H'): 1, ('H', 'S'): 1, ('H', 'P'): 0,
            ('S', 'P'): 1, ('S', 'H'): 0, ('P', 'P'): 0, ('H', 'H'): 0, ('S', 'S'): 0}
dp = [[[0]*3 for j in range(k+1)] for i in range(n+1)]

for i in range(3):
    dp[1][0][i] = score[(gesture[i], g[1])]

for i in range(2, n+1):
    for j in range(k+1):
        if j > i: continue
        for v in range(3):
            # 不变
            dp[i][j][v] = dp[i-1][j][v] + score[(gesture[v], g[i])]
            # 变
            if j-1 >= 0:
                dp[i][j][v] = max(max(dp[i-1][j-1][(v+1)%3], dp[i-1][j-1][(v+2)%3]) + score[(gesture[v], g[i])], dp[i][j][v])
ans = 0
for i in range(k+1):
    ans = max(ans, max(dp[n][i]))
print(ans)