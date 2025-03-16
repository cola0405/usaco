import sys
sys.stdin = open('poker.in', 'r')
sys.stdout = open('poker.out', 'w')

n = int(input())
a = [int(input()) for _ in range(n)]
ans = a[0]
for i in range(1,n):
    if a[i] > a[i-1]:
         ans += a[i] - a[i-1]
print(ans)
