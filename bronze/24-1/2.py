n,start = map(int, input().split())

typ = [0]*(n+1)
value = [0]*(n+1)
count = [0]*(n+1)
for i in range(1,n+1):
    t, v = map(int, input().split())
    typ[i] = t
    value[i] = v

cur = start
power = 1
ans = 0
d = 1
zero_count = 0
while 1 <= cur <= n:
    if typ[cur] == 1:
        if power >= value[cur]:
            typ[cur] = 2
            ans += 1
        cur += power*d
    elif typ[cur] == 2:
        cur += power*d
    else:
        count[cur] += 1
        if count[cur] > 100:
            break
        d *= -1
        power += value[cur]
        cur += power*d

print(ans)

