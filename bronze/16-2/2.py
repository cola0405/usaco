# 读题
# 枚举
# 草稿纸

import sys
sys.stdin = open('cbarn.in', 'r')
sys.stdout = open('cbarn.out', 'w')

n = int(input())
rooms = [int(input()) for _ in range(n)]
total = sum(rooms)

ans = float('inf')
for i in range(n):  # 模拟各个房间开始
    d = 0
    cows = total
    for j in range(i, i+n):
        cows -= rooms[j%n]   # 处理环形问题
        d += cows
    ans = min(ans, d)

print(ans)