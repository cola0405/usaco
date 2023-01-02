import sys
sys.stdin = open("hoofball.in","r")
sys.stdout = open("hoofball.out","w")

n = int(input())
cows = list(map(int, input().split()))
cows.append(0)
cows.sort()

nex = [0]*105
cnt = [0]*105

nex[1] = 2
cnt[2] = 1
nex[n] = n-1
cnt[n-1] = 1
for i in range(2,n):
    if cows[i]-cows[i-1] <= cows[i+1]-cows[i]:
        cnt[i-1] += 1
        nex[i] = i-1
    else:
        cnt[i+1] += 1
        nex[i] = i+1

ans = 0
for i in range(1,n+1):
    if cnt[i]==0:
        ans += 1
    if i<n and cnt[i]==1 and cnt[i+1]==1 and nex[i] == i+1 and nex[i+1]==i:
        ans += 1

print(ans)
