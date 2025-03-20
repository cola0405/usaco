'''
C++

path dp

题目大意：所有牛有自己的编号，从第一个H牛出发，求访问完所有奶牛，且最后停在最后一个H奶牛的最小距离。
对于一个某个位置的H牛，有2种转移方式：
1. 从上一个H奶牛转移过来
2. 从某个G奶牛转移过来
dp[i][j][k]: 访问了i个H奶牛和j个G奶牛，当前停留在类型k奶牛的最小总距离

'''

import sys
sys.stdin = open('checklist.in', 'r')
sys.stdout = open('checklist.out', 'w')

H,G = map(int, input().split())
h = [list(map(int, input().split())) for _ in range(H)]
g = [list(map(int, input().split())) for _ in range(G)]
n = H+G
# dp[i][j][0] 表示已经走了i个H类，j个G类，且当前当前停在H类的最小距离 （dp[i][j][1] 则是停在G类）
dp = [[[float('inf')]*2 for j in range(G+1)] for i in range(H+1)]
# 初始状态
dp[0][0][0] = 0
dp[1][0][0] = 0
for i in range(1, H+1):
    for j in range(G+1):
        if i-2 >= 0:    # 从 i-1 到 i
            dp[i][j][0] = dp[i-1][j][0] + (h[i-1][0]-h[i-2][0])**2 + (h[i-1][1]-h[i-2][1])**2
        # 从 G类到 i
        dp[i][j][0] = min(dp[i][j][0], dp[i-1][j][1] + (h[i-1][0]-g[j-1][0])**2 + (h[i-1][1]-g[j-1][1])**2)

        # 从 j-1 到 j
        if j-2 >= 0:
            dp[i][j][1] = dp[i][j-1][1] + (g[j-1][0]-g[j-2][0])**2 + (g[j-1][1]-g[j-2][1])**2
        # 从 H类到 j
        dp[i][j][1] = min(dp[i][j][1], dp[i][j-1][0] + (g[j-1][0]-h[i-1][0])**2 + (g[j-1][1]-h[i-1][1])**2)

print(dp[H][G][0])