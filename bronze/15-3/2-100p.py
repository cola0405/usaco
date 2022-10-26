# 利用奇偶的加法、乘法的规律

import sys
sys.stdin = open('geteven.in', 'r')
sys.stdout = open('geteven.out', 'w')

n = int(input())
d = {'B':[], 'E':[], 'S':[], 'I':[],'O':[],'M':[], 'G':[]}


for i in range(n):
    line = input().split()
    k = line[0]
    v = int(line[1])
    d[k].append(v)

m_even = 0
b_even = 0
i_even = 0
m_odd = 0
b_odd = 0
i_odd = 0

for i in d['M']:
    if i%2 == 0:
        m_even += 1
    else:
        m_odd += 1

for i in d['B']:
    if i%2 == 0:
        b_even += 1
    else:
        b_odd += 1

for i in d['I']:
    if i%2 == 0:
        i_even += 1
    else:
        i_odd += 1

p2_even = b_odd*i_odd + b_even*i_even
p2_odd = b_odd*i_even + b_even*i_odd

for_even = p2_odd*m_odd+p2_odd*m_even+p2_even*m_odd+p2_even*m_even
for_odd = p2_odd*m_even+p2_even*m_odd+p2_even*m_even

ans = 0
for e in d['E']:
    for s in d['S']:
        for o in d['O']:
            for g in d['G']:
                part = g+o+e+s
                if part % 2 == 0:
                    ans += for_even
                else:
                    ans += for_odd

print(ans)