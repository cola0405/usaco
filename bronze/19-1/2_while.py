# 最右边一对有问题的数字


import sys
sys.stdin = open("sleepy.in", "r")
sys.stdout = open("sleepy.out", "w")

n = int(input())
cows = list(map(int, input().split()))

ans = 0
i = len(cows)-1
while i > 0:
    if cows[i] < cows[i-1]:
        ans = i
        break
    i -= 1

print(ans)


