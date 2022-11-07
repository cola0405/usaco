n, l = map(int, input().split())
cites = list(map(int, input().split()))

cites.sort()
i = 0
diff = []
while i < n:
    num = n-i
    while i+1 < n and cites[i] == cites[i+1]:
        diff.append(cites[i] - num)
        i += 1
    diff.append(cites[i] - num + l)
    i += 1

ans = 0
i = n-1
while i >= 0:
    if diff[i] <= 0 and diff[i] > diff[ans]:
        ans = i
    i -= 1

print(cites[ans]+l)
# <=0 then max


