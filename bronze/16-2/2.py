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
for i in range(n):
    d = 0
    cows = total
    for j in range(i, i+n):
        cows -= rooms[j%n]
        d += cows
    ans = min(ans, d)

print(ans)