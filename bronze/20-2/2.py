# 贪心策略是：尽可能多连续

import sys
sys.stdin = open('breedflip.in', 'r')
sys.stdout = open('breedflip.out', 'w')

n = int(input())
A = input()
B = input()

ans = 0
i = 0
while i<n:
    flag = 0
    while i<n and B[i] != A[i]:
        flag = 1
        i += 1
    if flag:
        ans += 1
    i += 1
print(ans)
