# 说白了拿一个长度为k的窗口直接滑就行。。。
# 前缀和帮助统计区间内坏信号灯的数量，找最小值
# 区间问题 - 前缀和


import sys
sys.stdin = open("maxcross.in", "r")
sys.stdout = open("maxcross.out", "w")

n,k,b = map(int, input().split())

broken = [0]*(n+1)
for i in range(b):
    broken[int(input())] = 1

p = [0]*(n+1)
for i in range(1,n+1):
    p[i] = p[i-1]
    if broken[i] == 1:
        p[i] += 1

ans = float('inf')
for i in range(1,n-k+2):  # 范围拿草稿纸写一下证好了
    broken_count = p[i+k-1] - p[i-1]
    ans = min(broken_count, ans)

print(ans)
