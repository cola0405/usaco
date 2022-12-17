n = int(input())
c = list(map(int, input().split()))

c.sort()
already = set()

ans = (0,0)
for i in range(n):
    fee = c[i]
    if fee in already:
        continue
    already.add(fee)
    value = fee * (n - i)
    if value > ans[0]:
        ans = (value, fee)


print(ans[0], ans[1])
