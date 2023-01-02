import sys
sys.stdin = open("hoofball.in","r")
sys.stdout = open("hoofball.out","w")

n = int(input())
cows = list(map(int, input().split()))
cows.sort()

way1 = 1
i = 0
nearest = 2000
while i+1<len(cows):
    gap = cows[i+1] - cows[i]
    if gap > nearest:
        way1 += 1
    nearest = gap
    i += 1

way2 = 1
i = len(cows)-1
nearest = 2000
while i-1>=0:
    gap = cows[i] - cows[i-1]
    if gap >= nearest:
        way2 += 1
    nearest = gap
    i -= 1

ans = min(way1,way2)
print(ans)
