# 枚举

import sys
sys.stdin = open('pails.in', 'r')
sys.stdout = open('pails.out', 'w')

x, y, m = map(int, input().split())
ans = 0
for i in range(1000):
    sum_x = i*x
    if sum_x > m:
        break
    for j in range(1000):
        sum_y = j*y
        if sum_y > m or sum_x + sum_y > m:
            break

        ans = max(ans, sum_x+sum_y)

print(ans)