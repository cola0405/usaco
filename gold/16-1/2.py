'''
path dp
这个问题要求 Farmer John 和 Bessie 在各自沿着路径移动时，
每一步选择是否前进，使得他们在到达终点时的总能量消耗（各时间步距离平方之和）最小

dp[i][j] 表示 FJ执行完 i个指令，Bessie执行完 j个指令后的最少能量消耗
那每次有 3种移动方式：
1. FJ动
2. Bessie动
3. 两个人都动

'''

import sys
sys.stdin = open('radio.in', 'r')
sys.stdout = open('radio.out', 'w')

n,m = map(int,input().split())
fx,fy = map(int,input().split())
bx,by = map(int,input().split())
s1 = ' ' + input()
s2 = ' ' + input()

d = {'N':(0,1), 'S':(0,-1), 'E':(1,0), 'W':(-1,0)}
f_pos = [(fx,fy)]   # f_pos[i]表示 FJ执行完第 i个指令后的位置
for i in range(1, n+1):
    f_pos.append((f_pos[-1][0] + d[s1[i]][0], f_pos[-1][1] + d[s1[i]][1]))
b_pos = [(bx,by)]   # b_pos[i]表示 Bessie执行完第 i个指令后的位置
for i in range(1, m+1):
    b_pos.append((b_pos[-1][0] + d[s2[i]][0], b_pos[-1][1] + d[s2[i]][1]))

dp = [[float('inf')]*(m+1) for _ in range(n+1)]     # dp[i][j] 表示 FJ执行完第 i步，Bessie 执行完第 j步 最小的能量消耗
# 初始状态
dp[0][0] = 0
for i in range(1, n+1):
    dp[i][0] = dp[i-1][0] + (f_pos[i][0] - b_pos[0][0])**2 + (f_pos[i][1] - b_pos[0][1])**2
for j in range(1, m+1):
    dp[0][j] = dp[0][j-1] + (f_pos[0][0] - b_pos[j][0])**2 + (f_pos[0][1] - b_pos[j][1])**2

for i in range(1,n+1):
    for j in range(1, m+1):
        dis = (f_pos[i][0] - b_pos[j][0])**2 + (f_pos[i][1] - b_pos[j][1])**2
        dp[i][j] = min(dp[i][j], min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + dis)
print(dp[n][m])