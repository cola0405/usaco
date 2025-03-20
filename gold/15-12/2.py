'''
完全背包问题
反复dp
因为各操作之间不互相影响，所以可以分开进行dp

'''

import sys
sys.stdin = open('feast.in', 'r')
sys.stdout = open('feast.out', 'w')

t,a,b = map(int, input().split())
dp = [False] * (t + 1)
dp[0] = True

# 第一次吃冰淇淋和糖果
for i in range(a, t + 1):
    dp[i] = dp[i] or dp[i - a]
for i in range(b, t + 1):
    dp[i] = dp[i] or dp[i - b]

# 喝水
for i in range(1, t + 1):
    dp[i // 2] = dp[i // 2] or dp[i]        # 不能从*2去处理问题，因为题目说的减半允许向下取整，不一定是整除2的关系

# 第二次吃冰淇淋和糖果
for i in range(a, t + 1):
    dp[i] = dp[i] or dp[i - a]
for i in range(b, t + 1):
    dp[i] = dp[i] or dp[i - b]

# 找到最大满足条件的 t
while t:
    if dp[t]:
        print(t)
        break
    t -= 1
    
