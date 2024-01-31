n = int(input())
cows = list(map(int, input().split()))
stalls = list(map(int, input().split()))

cows.sort()
stalls.sort()

ans = 1
j = 0
for i in range(n):
    while j<n and cows[j]<=stalls[i]:
        j += 1      # j之前的牛都是可以入当前stall[i]的
    ans *= j-i      # i为已经入的牛, j-i就是还剩下的牛

print(ans)
