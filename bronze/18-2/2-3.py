import sys
sys.stdin = open("hoofball.in","r")
sys.stdout = open("hoofball.out","w")
n = int(input())
cows = list(map(int, input().split()))

cows.sort()
pass_flags = [0]*n

PASS = 1
for i in range(1, n-1):
    if cows[i] - cows[i-1] < cows[i+1] - cows[i]:
        pass_flags[i-1] = PASS
    else:
        pass_flags[i+1] = PASS


ans = 0
NO_PASS = 0
for i in range(n):
    if pass_flags[i] == NO_PASS:
        ans += 1
    print(cows[i], pass_flags[i])
print(ans)

