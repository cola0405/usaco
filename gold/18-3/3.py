'''
python没办法全过

01背包问题
这道题直接dp求t/w的最大值不可行，因为t/w之间没有直接的关系
转而我们要让t一定的时候，w尽可能小
进而我们可以有dp[i] 表示talent 为i时，weight的最小值

然后再把dp数组扫一遍，找到最大的ratio
'''

import sys
sys.stdout = open('talent.out', 'w')
sys.stdin = open('talent.in', 'r')

n, W = map(int, input().split())
cows = [tuple(map(int, input().split())) for _ in range(n)]

max_talent = sum(t for w, t in cows)
dp = [float('inf')] * (max_talent + 1)
dp[0] = 0

for weight, talent in cows:
    for i in range(max_talent, talent - 1, -1):
        if dp[i - talent] + weight < dp[i]:
            dp[i] = dp[i - talent] + weight

max_ratio = 0.0
for t in range(1, max_talent + 1):
    if dp[t] >= W:
        ratio = t / dp[t]
        if ratio > max_ratio:
            max_ratio = ratio

print(int(max_ratio * 1000))