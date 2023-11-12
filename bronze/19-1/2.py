# 最右边一对有问题的数字


import sys
sys.stdin = open("sleepy.in", "r")
sys.stdout = open("sleepy.out", "w")

n = int(input())
cows = list(map(int, input().split()))

ans = 0
for i in range(1, n)[::-1]:
    if cows[i] < cows[i-1]:
        ans = i
        break
print(ans)



