n = int(input())
cows = list(map(int, input().split()))
stalls = list(map(int, input().split()))

cows.sort()
stalls.sort()

ans = 1
j = 0
for i in range(n):
    while j<n and cows[j]<=stalls[i]:
        j += 1
    ans *= (j-i)

print(ans)
