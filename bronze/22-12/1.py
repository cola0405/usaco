n = int(input())
c = list(map(int, input().split()))

c.sort()

ans = (0,0)
for i in range(n):
    fee = c[i]
    value = fee * (n - i)
    if value > ans[0]:
        ans = (value, fee)

print(ans[0], ans[1])