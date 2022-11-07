#
import itertools
n = int(input())
a = [int(i) for i in input().split(" ")]
b = [int(i) for i in input().split(" ")]

c = tuple(itertools.permutations(a,n))

count = 0

for cn in c:
    flag = True
    for i in range(n):
        if cn[i]>b[i]:
            flag = False
    if flag:
        count += 1

print(count)
