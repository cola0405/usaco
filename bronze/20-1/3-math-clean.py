import math
import sys
sys.stdin = open('race.in', 'r')
sys.stdout = open('race.out', 'w')

k, n = map(int, input().split())
p = 1
while p*(p+1) < k*2:
    p += 1

for i in range(n):
    x = int(input())
    if x >= p:
        print(p)
        continue
    h = int(math.sqrt((2*k+x**2-x)/2))
    meters = (2*h**2-x**2+x)/2
    if meters == k:
        print(2*h - x)
    elif k - meters <= h:
        print(2*h - x + 1)
    else:
        print(2*h - x + 2)
