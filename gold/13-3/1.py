'''
区间 dp —— 基于[i+1][j-1]的 dp

题目大意：
有 N头牛在一条线上，牛每分钟会造成 1点损失
FJ 从 0点出发处理这些牛，每分钟移动一个单位，问损失最小是多少

dp[i][j][0/1] 表示处理完第 i 到 第 j 头牛，FJ位于左端/右端的最小损失
具体转移方程看下面代码

这道题的初始状态相对比较复杂一点，需要额外插入初始 0点，然后处理完初始点的最小代价是 0
'''

def cost(a, b):     # 表示 FJ从 a到 b过程中的损失总和
    return abs(pos[a]-pos[b]) * (n-(j-i))   # 距离（时间）* 还未处理的牛的数量

import sys
sys.stdin = open('cowrun.in', 'r')
sys.stdout = open('cowrun.out', 'w')

n = int(input())
pos = sorted([0] + [int(input()) for _ in range(n)])
n += 1
dp = [[[float('inf')]*2 for j in range(n)] for i in range(n)]
# 初始状态
FJ = pos.index(0)
dp[FJ][FJ][0] = 0
dp[FJ][FJ][1] = 0

for i in range(n)[::-1]:    # 需要倒序dp， 因为涉及到 [i+1]
    for j in range(i+1,n):
        # 注意cost的参数是不同的，一个是从 i+1 到 i，另一个是从 i 到 j
        # 这里区间 dp转移状态会比较有意思，会出现 [i+1]到 [i] 的转移，不理解的话可以参考 Leetcode 516.最长回文子序列
        dp[i][j][0] = min(dp[i+1][j][0] + cost(i+1,i), dp[i+1][j][1] + cost(i,j))
        dp[i][j][1] = min(dp[i][j-1][0] + cost(i,j), dp[i][j-1][1] + cost(j-1, j))
print(min(dp[0][n-1][0], dp[0][n-1][1]))

