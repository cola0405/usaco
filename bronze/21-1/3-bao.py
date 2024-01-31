# 过5个

import itertools
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = tuple(itertools.permutations(a))

count = 0
for cn in c:
    flag = True
    for i in range(n):
        if cn[i]>b[i]:
            flag = False
    if flag:
        count += 1

print(count)
