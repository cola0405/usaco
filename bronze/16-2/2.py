# 读题
# 枚举
# 草稿纸

import sys
sys.stdin = open('cbarn.in', 'r')
sys.stdout = open('cbarn.out', 'w')

n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

ans = 2e10
for i in range(n):
    distance = 0
    doors = 1
    for j in range(i+1, n+i):
        distance += nums[j%n]*doors
        doors += 1
    ans = min(ans, distance)

print(ans)