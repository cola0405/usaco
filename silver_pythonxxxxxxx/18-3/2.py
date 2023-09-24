# 大的往前排

import sys
sys.stdin = open("lemonade.in", "r")
sys.stdout = open("lemonade.out", "w")

n = int(input())
w = list(map(int, input().split()))

w.sort(reverse=True)

amount = 0
for i in range(n):
    if w[i] >= amount:
        amount += 1
    else:
        break

print(amount)
