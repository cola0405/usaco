import sys
sys.stdin = open('paint.in', 'r')
sys.stdout = open('paint.out', 'w')

a, b = map(int, input().split())
c, d = map(int, input().split())

f = [0]*101


for i in range(a,b):
    f[i] += 1
for i in range(c,d):
    f[i] += 1

ans = 0
for i in range(100):
    if f[i] >= 1:
        ans += 1

print(ans)