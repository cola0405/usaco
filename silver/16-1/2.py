# 区间和

import sys
sys.stdin = open('div7.in', 'r')
sys.stdout = open('div7.out', 'w')

n = int(input())

p = [0]
for i in range(n):
    id = int(input())
    p.append(p[-1]+id)

ans = 0
for i in range(0, n):
    for j in range(i+1,n+1):
        s = p[j] - p[i]
        if s%7 == 0:
            ans = max(j-i, ans)
print(ans)