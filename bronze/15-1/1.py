import sys
sys.stdin = open('cowroute.in', 'r')
sys.stdout = open('cowroute.out', 'w')

A,B,N = map(int, input().split())
ans = float('inf')
for _ in range(N):
    cost, city_num = map(int, input().split())
    cities = list(map(int, input().split()))

    if (A in cities and B in cities)\
            and (cities.index(A) < cities.index(B)):
        ans = min(cost,ans)

if ans == float('inf'):
    print(-1)
else:
    print(ans)


