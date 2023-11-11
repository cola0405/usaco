# 贪心，过70%
import sys
sys.stdin = open("snowboots.in", "r")
sys.stdout = open("snowboots.out", "w")

n,b = map(int, input().split())
f = list(map(int, input().split()))
boots = [list(map(int, input().split())) for _ in range(b)]

bi = 0
cur = 0
abandon = 0
while cur<n-1:
    si,di = boots[bi]
    for i in range(cur+1, min(cur+1+di, len(f)))[::-1]:
        if f[i] <= si:
            cur = i
            break
    else:
        bi += 1
        while boots[bi][0] < f[cur]:
            bi += 1
print(bi)
