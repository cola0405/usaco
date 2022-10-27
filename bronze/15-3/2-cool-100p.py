# 100%
# 利用for循环去构建奇偶搭配

import sys
sys.stdin = open('geteven.in', 'r')
sys.stdout = open('geteven.out', 'w')

n = int(input())
variables = 'BESIOMG'
d = {}
for i in variables:
    d[i] = [0,0,0]

for i in range(n):
    line = input().split()
    k = line[0]
    v = int(line[1])
    if v%2 == 0:
        d[k][2] += 1
    else:
        d[k][1] += 1

ans = 0
for b in range(1,3):
    for e in range(1,3):
        for s in range(1,3):
            for i in range(1,3):
                for o in range(1,3):
                    for m in range(1,3):
                        for g in range(1,3):
                            res = (b+e+s+s+i+e)*(g+o+e+s)*(m+o+o)
                            if res%2 == 0:
                                ans += d['B'][b]*d['E'][e]*d['S'][s]*d['I'][i]*d['O'][o]*d['M'][m]*d['G'][g]

print(ans)